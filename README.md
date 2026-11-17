# Sistema de Inventario de Zapatos — SQLAlchemy ORM

## 1. Información del proyecto

| Información | Descripción |
| Estudiante | [CHELSSEA LANS MERCADO] |
| Asignatura | [DESARROLLO DE APLICACIONES CON ACCESO A DATOS] |
| Docente | [EDUARDO PIMIENTA] |
| Fecha | [17/11/2026] |
| Lenguaje de programación | Python |
| ORM utilizado | SQLAlchemy |
| Base de datos | SQLite |

## 2. Descripción del proyecto

**¿En qué consiste el programa?**

El Sistema de Inventario de Zapatos es una aplicación desarrollada en Python que permite administrar un inventario de calzado mediante una base de datos SQLite y el ORM SQLAlchemy. El programa permite almacenar información de cada zapato, incluyendo su id, modelo, talla y precio. y su propósito es facilitar la gestión de los productos de una zapatería mediante un menú interactivo que permite realizar operaciones de creación, consulta, actualización y eliminación de registros, conocidas como operaciones CRUD.

**¿Qué funcionalidades tiene?**

Describe brevemente las operaciones que permite realizar el sistema:

- Registrar zapatos.
- Consultar el inventario.
- Buscar zapatos por ID.
- Actualizar precios.
- Eliminar zapatos.

## 3. Estructura del proyecto

Presenta la estructura de archivos de tu aplicación.

tienda_zapatos/
│
├── main.py
├── datos.py
├── requirements.txt
├── README.md
├── zapateria.db
└── evidencias/
    ├── registro.png
    ├── listado.png
    ├── busqueda.png
    ├── actualizacion.png
    ├── eliminacion.png
    └── persistencia.png

**Explicación de los archivos:**

| Archivo | ¿Cuál es su responsabilidad? |
| `main.py` | [Contiene el menú principal, recibe los datos ingresados por el usuario, valida la información y llama a las funciones del módulo datos.py] |
| `datos.py` | [Contiene la configuración de SQLAlchemy, la clase Base, el modelo Zapato y las funciones encargadas de realizar las operaciones CRUD.] |
| `requirements.txt` | [Contiene lo necesario para ejecutar el proyecto, SQLAlchemy. ] |
| `zapateria.db` | [Es la base de datos SQLite donde se almacenan los registros de los zapatos.] |

## 4. Instalación y ejecución

**Paso 1. Requisitos**

Contar con un editor de código, como Visual Studio Code.
Tener Python instalado.
Tener acceso a una terminal o consola de comandos.
Contar con conexión a Internet para instalar las dependencias.
Disponer de los archivos del proyecto.

**Paso 2. Instalación de dependencias**

```bash
python -m pip install -r requirements.txt
```

**Paso 3. Ejecución**

```bash
python main.py
```

**Paso 4. Resultado esperado**

Cuando el programa se ejecuta correctamente, aparece un menú interactivo en la terminal con seis opciones:

===== TIENDA DE ZAPATOS =====
1. Registrar zapato
2. Listar zapatos
3. Buscar zapato por ID
4. Actualizar precio
5. Eliminar zapato
6. Salir
Seleccione una opción:

El usuario puede seleccionar cualquiera de las opciones ingresando el número correspondiente. Según la opción seleccionada, el sistema realiza la operación solicitada y muestra un mensaje indicando el resultado.

---

# 5. Documentación técnica — Preguntas obligatorias

Responde las siguientes preguntas utilizando tu implementación. Cuando sea necesario, incluye fragmentos de tu código para explicar el funcionamiento.

### Pregunta 1. Modelo y tabla

¿Qué clase de Python representa la tabla de la base de datos? Explica cómo SQLAlchemy identifica el nombre de la tabla y sus columnas.

**Respuesta:**

La clase de Python que representa la tabla de la base de datos es Zapato. Esta clase utiliza el sistema ORM de SQLAlchemy para relacionar los objetos de Python con los registros almacenados en SQLite. La clase hereda de Base, que es una clase declarativa creada mediante DeclarativeBase. SQLAlchemy identifica el nombre de la tabla mediante el atributo __tablename__ = "zapatos", que tiene el valor "zapatos". Las columnas se definen utilizando Mapped y mapped_column, indicando el tipo de dato y las características de cada campo.

**Fragmento de código relacionado:**

class Base(DeclarativeBase):
    pass
class Zapato(Base):
    __tablename__ = "zapatos" = "zapatos"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True,autoincrement=True
    )
    modelo: Mapped[str] = mapped_column(
        String(100),nullable=False
    )
    talla: Mapped[int] = mapped_column(
        Integer,nullable=False
    )
    precio: Mapped[float] = mapped_column(
        Float,nullable=False
    )

### Pregunta 2. Creación de la base de datos

¿Qué ocurre cuando ejecutas el programa por primera vez? Explica cómo se crea la base de datos `zapateria.db` y la tabla `zapatos`.

**Respuesta:**

Cuando se ejecuta el programa por primera vez, Python importa el módulo datos.py y se configura la conexión con SQLite mediante create_engine(). Luego, desde la función main() se llama a datos.inicializar_bd(), esta función utiliza Base.metadata.create_all(engine) para crear las tablas correspondientes a los modelos registrados en SQLAlchemy.

Si la base de datos y la tabla todavía no existen, SQLite las crea automáticamente. El archivo generado se llama zapateria.db y contiene la tabla zapatos,si se vuelve a ejecutar el programa, SQLAlchemy comprueba la existencia de las tablas y evita crearlas nuevamente si ya existen.

**Fragmento de código relacionado:**

engine = create_engine(
    "sqlite:///zapateria.db", echo=True
)
def inicializar_bd():
    Base.metadata.create_all(engine)

En el archivo main.py:
def main():
    datos.inicializar_bd()


### Pregunta 3. Registro de zapatos

Cuando seleccionas la opción de registrar un zapato, ¿qué recorrido siguen los datos desde el menú hasta quedar almacenados en SQLite? Identifica las funciones utilizadas.

**Respuesta:**

Cuando el usuario selecciona la opción 1 del menú, el programa solicita los datos del zapato: modelo, talla y precio.
El archivo main.py recibe la información mediante input(). Después convierte la talla a un número entero y el precio a un número decimal,el programa verifica que el modelo no esté vacío y que la talla y el precio sean mayores que cero, si los datos son válidos, se llama a la función datos.crear_zapato(modelo, talla, precio), que se encuentra en el archivo datos.py dentro de esta función se crea un objeto de la clase Zapato, se abre una sesión de SQLAlchemy, se agrega el objeto mediante session.add() y finalmente se confirma la transacción con session.commit().


**Fragmento de código relacionado:**
En main.py:

if opcion == "1":
    modelo = input("Modelo: ").strip()
    talla = int(input("Talla: "))
    precio = float(input("Precio: "))
    if not modelo or talla <= 0 or precio <= 0:
        print("Datos no válidos.")
        continue
    if datos.crear_zapato(modelo, talla, precio):
        print("Zapato registrado correctamente.")
    else:
        print("No se pudo registrar.")

En datos.py:

def crear_zapato(modelo, talla, precio):
    try:
        with Session(engine) as session:
            zapato = Zapato(
                modelo=modelo,
                talla=talla,
                precio=precio
            )
            session.add(zapato)
            session.commit()
        return True
    except Exception:
        return False


### Pregunta 4. Sesiones y transacciones

¿Para qué se utiliza una sesión de SQLAlchemy? ¿Qué ocurriría si agregas o modificas un objeto, pero no confirmas la transacción con `commit()`?

**Respuesta:**

Una sesión de SQLAlchemy se utiliza para gestionar la comunicación entre los objetos de Python y la base de datos. A través de ella se pueden agregar, consultar, modificar y eliminar registros. se utiliza Session(engine) para abrir una sesión que permite realizar las operaciones sobre la tabla zapatos.

El método commit() es el que confirma los cambios realizados durante una transacción y permite que se guarden permanentemente en la base de datos.Si se agrega o modifica un objeto, pero no se ejecuta commit(), los cambios pendientes no quedan confirmados. Al cerrar la sesión sin confirmar, la transacción pendiente se revierte.

**Fragmento de código relacionado:**
with Session(engine) as session:
    zapato = Zapato(
        modelo=modelo,
        talla=talla,
        precio=precio
    )
    session.add(zapato)
    session.commit()

### Pregunta 5. Búsqueda por ID

¿Cómo funciona la búsqueda de zapatos por ID? Explica qué devuelve tu función cuando encuentra el registro y qué devuelve cuando no existe.

**Respuesta:**

La búsqueda de zapatos por ID se realiza mediante la función buscar_zapato(id_zapato) del archivo datos.py, esta función abre una sesión de SQLAlchemy y utiliza el método session.get() para buscar un registro de la clase Zapato utilizando su clave primaria, si el zapato existe, devuelve el objeto correspondiente con sus atributos: ID, modelo, talla y precio, si el registro no existe, devuelve None.


**Fragmento de código relacionado:**

En datos.py:

def buscar_zapato(id_zapato):
    with Session(engine) as session:
        zapato = session.get(Zapato, id_zapato)
        return zapato

En main.py:

elif opcion == "3":
    id_zapato = int(input("ID del zapato: "))
    zapato = datos.buscar_zapato(id_zapato)
    if zapato is None:
        print("Zapato no encontrado.")
    else:
        mostrar_zapato(zapato)

### Pregunta 6. Actualización de precios

¿Cómo se actualiza el precio de un zapato mediante el ORM? Explica cómo se obtiene el objeto, cómo se modifica su atributo y cómo se guarda el cambio.

**Respuesta:**

La actualización del precio comienza cuando el usuario selecciona la opción 4 del menú e ingresa el ID del zapato y el nuevo precio, el programa comprueba que el precio sea mayor que cero y llama a la función actualizar_precio() del archivo datos.py. Esta función abre una sesión y utiliza session.get() para localizar el zapato mediante su ID, si el registro existe, se modifica directamente el atributo precio del objeto. SQLAlchemy detecta el cambio y, al ejecutar session.commit(), guarda la actualización en la base de datos, si el zapato no existe, la función devuelve False.

**Fragmento de código relacionado:**

def actualizar_precio(id_zapato, nuevo_precio):
    with Session(engine) as session:
        zapato = session.get(Zapato, id_zapato)
        if zapato is None:
            return False
        zapato.precio = nuevo_precio
        session.commit()
        return True

### Pregunta 7. Eliminación de registros

¿Qué ocurre cuando eliminas un zapato? Explica cómo compruebas que el registro ya no existe en la base de datos.

**Respuesta:**

Cuando el usuario selecciona la opción 5, el programa solicita el ID del zapato que desea eliminar, después llama a la función eliminar_zapato() del archivo datos.py y esta función abre una sesión y busca el registro utilizando session.get() entonces si encuentra el zapato, utiliza session.delete() para marcar el objeto para su eliminación y luego ejecuta session.commit() para confirmar el cambio. Si el zapato no existe, devuelve False y no realiza ninguna eliminación.

**Fragmento de código relacionado:**

def eliminar_zapato(id_zapato):
    with Session(engine) as session:
        zapato = session.get(Zapato, id_zapato)
        if zapato is None:
            return False
        session.delete(zapato)
        session.commit()
        return True

### Pregunta 8. Persistencia de datos

¿Qué sucede con los zapatos registrados cuando cierras y vuelves a ejecutar el programa? Explica por qué permanecen almacenados.

**Respuesta:**

Cuando se cierra el programa, los zapatos registrados permanecen almacenados en la base de datos porque SQLite utiliza un archivo físico llamado zapateria.db para guardar la información.Los datos no dependen de que el programa esté abierto, ya que cada operación de registro o actualización se confirma mediante session.commit(), Cuando se vuelve a ejecutar el programa, SQLAlchemy establece nuevamente la conexión con el mismo archivo y permite consultar los registros que fueron almacenados anteriormente.

---

## 6. Pruebas de funcionamiento y evidencias

Debes ejecutar el programa y demostrar el funcionamiento de cada una de las operaciones.

### Prueba 1. Registrar zapatos

- **Acción realizada:** registrar dos zapatos.
- **Datos utilizados:** Nike, 38, 150000,, puma,37,160000.
- **Resultado obtenido:** El programa registra ambos zapatos y mostrar el mensaje Zapato registrado correctamente.

**Evidencia:**

![Registro de zapatos](evidencias/registro.png)

### Prueba 2. Listar inventario

- **Acción realizada:** consultar todos los zapatos.
- **Resultado obtenido:** El programa muestra todos los zapatos registrados, incluyendo su ID, modelo, talla y precio.

**Evidencia:**

![Listado de zapatos](evidencias/listado.png)

### Prueba 3. Buscar por ID

- **ID utilizado:** [1].
- **Resultado obtenido:** El sistema encuentra el registro y muestra toda su información.

**Evidencia:**

![Búsqueda de zapatos](evidencias/busqueda.png)

### Prueba 4. Actualizar precio

- **Zapato seleccionado:** [2].
- **Precio anterior:** [160000].
- **Precio nuevo:** [140000].
- **Resultado obtenido:** El programa muestra “Precio actualizado”. Al listar nuevamente el inventario, aparece el nuevo precio.

**Evidencia:**

![Actualización de precio](evidencias/actualizacion.png)

### Prueba 5. Eliminar zapato

- **ID eliminado:** [1].
- **Resultado obtenido:** El programa muestra “Zapato eliminado”. Al consultar nuevamente el inventario, el zapato eliminado ya no aparece.

**Evidencia:**

![Eliminación de zapato](evidencias/eliminacion.png)

### Prueba 6. Comprobar persistencia

- **Acción realizada:** cerrar y ejecutar nuevamente el programa.
- **Resultado obtenido:** Los registros que no fueron eliminados continuan almacenados y aparecen al seleccionar la opción 2.

**Evidencia:**

![Persistencia de datos](evidencias/persistencia.png)

### Pruebas con registros inexistentes

Ejecuta las operaciones de buscar, actualizar y eliminar utilizando un ID que no exista.

| Operación | ¿Qué sucedió? |
|---|---|
| Buscar ID inexistente | El programa muestra “Zapato no encontrado”. |
| Actualizar ID inexistente | El programa muestra “Zapato no encontrado”. |
| Eliminar ID inexistente | El programa muestra “Zapato no encontrado”. |

## 7. Conclusiones

Responde brevemente:

1. ¿Qué aprendiste al implementar las operaciones CRUD utilizando SQLAlchemy?
Aprendí a utilizar SQLAlchemy como herramienta ORM para gestionar una base de datos desde Python. Comprendí cómo crear modelos, configurar conexiones, utilizar sesiones y realizar operaciones CRUD. También aprendí la importancia de confirmar las transacciones para que los cambios queden almacenados correctamente.

2. ¿Qué diferencia identificaste entre trabajar con objetos Python y escribir sentencias SQL directamente?
La principal diferencia es que utilizando SQLAlchemy ORM se pueden administrar los registros mediante objetos y atributos de Python, sin tener que escribir manualmente todas las sentencias SQL. Esto permite organizar mejor el código, facilitar su mantenimiento y trabajar de una manera más relacionada con la programación orientada a objetos.

3. ¿Cuál fue la principal dificultad durante el desarrollo y cómo la solucionaste?
Una de las principales dificultades fue comprender cómo se relacionan los modelos de Python con las tablas de SQLite y cómo utilizar correctamente las sesiones para guardar los cambios. Esta dificultad se solucionó implementando paso a paso las funciones del ORM, utilizando métodos como add(), get(), delete() y commit(), y comprobando el funcionamiento de cada operación.


## Indicaciones de documentación

- Responde las ocho preguntas con tus propias palabras.
- Relaciona tus explicaciones con el código que implementaste.
- Incluye fragmentos de código únicamente cuando ayuden a explicar tu respuesta.
- Todas las evidencias deben corresponder a ejecuciones reales del programa.
- Guarda las capturas dentro de la carpeta `evidencias/` utilizando los nombres indicados o actualiza las rutas del README.
- Verifica que las imágenes se visualicen correctamente en GitHub.
- Elimina los textos entre corchetes y reemplázalos con tus respuestas antes de entregar.
- La documentación debe permitir que otra persona comprenda cómo instalar, ejecutar y utilizar tu aplicación.