# Tarea 10: Módulo de Gestión de Ordenadores

## Descripción

Este módulo de Odoo ha sido creado para la asignatura de Sistemas de Gestión Empresarial. Su función es llevar un inventario de los ordenadores de la empresa, saber qué componentes tienen dentro, cuánto cuestan en total y qué empleado los está utilizando.

## Estructura del Módulo

El módulo cuenta con dos modelos principales:

1.  **Componente (`sge.componente`):** Guarda la información de las piezas (RAM, Discos, etc.) con su precio individual.
2.  **Ordenador (`sge.ordenador`):** Es el modelo principal que agrupa todo.

## Explicación Técnica y Código

A continuación explico cómo he resuelto los puntos clave de la práctica:

### 1\. Las Relaciones (Base de datos)

Para conectar los datos he usado dos tipos de campos relacionales en el modelo `Ordenador`:

  * **Relación con el Usuario (`Many2one`):**
    Un ordenador solo puede tener un dueño a la vez, pero un usuario puede tener varios ordenadores. Se enlaza con el modelo nativo de usuarios (`res.users`).

    ```python
    user_id = fields.Many2one("res.user", string="Usuario asignado")
    ```

  * **Relación con Componentes (`Many2many`):**
    Un ordenador tiene muchas piezas, y ese tipo de pieza (ej. un modelo de disco duro) puede estar en muchos ordenadores a la vez.

    ```python
    component_ids = fields.Many2many("sge.componente", string="Lista de piezas")
    ```

### 2\. Restricción de Fecha (`@api.constrains`)

He creado una función para impedir que se pongan fechas futuras en el campo "Última modificación". Si el usuario se equivoca, salta un error (ValidationError).

```python
@api.constrains('ultima_mod')
def _comprobar_fecha(self):
    for record in self:
        # Si la fecha puesta es mayor a la de hoy, lanza error
        if record.ultima_mod > fields.Date.today():
            raise ValidationError("La fecha no puede ser futura")
```

### 3\. Precio Autocalculado (`@api.depends`)

El precio total del ordenador no se escribe a mano. Se calcula sumando el precio de todos los componentes que le añadamos.

  * Uso `@api.depends` para que se recalcule solo cuando cambien los componentes.
  * Uso un bucle `sum` para sumar todos los precios.

```python
precio_total = fields.Monetary(string="Precio Total", compute="_compute_total")

@api.depends("component_ids.price")
def _compute_total(self):
    for record in self:
        # Suma el campo 'price' de cada componente en la lista
        record.precio_total = sum(comp.price for comp in record.component_ids)
```

### 4\. BONUS: Etiquetas (Tags)

Para los Sistemas Operativos he usado el widget `many2many_tags`. Esto permite seleccionar "Windows", "Linux", etc., y que aparezcan como etiquetas de colores en la ficha del ordenador, haciendo que se vea más moderno y visual.
