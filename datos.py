from sqlalchemy import create_engine, select, String, Integer, Float
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)

# =====================================
# TODO ORM 1 - CONFIGURAR LA CONEXION
# =====================================

# Crear el engine para conectar con
# una base SQLite llamada zapateria.db

engine = create_engine("sqlite:///zapateria.db", echo=True)

# =====================================
# TODO ORM 2 - CREAR LA CLASE BASE
# =====================================

# Crear la clase Base utilizando
# DeclarativeBase.
class Base(DeclarativeBase):
    pass

# =====================================
# TODO ORM 3 - CREAR EL MODELO ZAPATO
# =====================================

# Construir la clase Zapato.
# Tabla: zapatos
# Atributos:
# - id: entero, clave primaria
# - modelo: texto
# - talla: entero
# - precio: real
#
# Utilizar Mapped y mapped_column.

class Zapato(Base):

    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    modelo: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    
    talla: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    precio: Mapped[float] = mapped_column(
        Float, nullable=False
    )

# =====================================
# TODO ORM 4 - CREAR LA TABLA
# =====================================

def inicializar_bd():
    # Crear las tablas del modelo
    # utilizando el engine.
    Base.metadata.create_all(engine)

# =====================================
# TODO ORM 5 - REGISTRAR ZAPATO
# =====================================
    # Crear un objeto Zapato.
    # Abrir una sesion.
    # Agregar el objeto.
    # Confirmar la transaccion.
    # Retornar True si se registro.

def crear_zapato(modelo, talla, precio):

    try:
        with Session(engine) as session:
            zapato = Zapato(
                modelo=modelo, talla=talla, precio=precio
            )
            session.add(zapato)
            session.commit()
        return True

    except Exception:
        return False

# =====================================
# TODO ORM 6 - LISTAR ZAPATOS
# =====================================
    # Consultar todos los objetos
    # Zapato utilizando SQLAlchemy.
    #
    # Retornar una lista de objetos.

def listar_zapatos():

    with Session(engine) as session:
        consulta = select(Zapato)
        zapatos = session.scalars(consulta).all()
        return zapatos

# =====================================
# TODO ORM 7 - BUSCAR POR ID
# =====================================
# Buscar un Zapato por su ID.
    #
    # Retornar el objeto encontrado
    # o None si no existe.

def buscar_zapato(id_zapato):

    with Session(engine) as session:
        zapato = session.get(Zapato, id_zapato)
        return zapato

# =====================================
# TODO ORM 8 - ACTUALIZAR PRECIO
# =====================================

    # Buscar el zapato por ID.
    # Modificar el atributo precio.
    # Confirmar el cambio.
    #
    # Retornar True si se actualizo.
    # Retornar False si no existe.
   
def actualizar_precio(id_zapato, nuevo_precio):

    with Session(engine) as session:
        zapato = session.get(Zapato, id_zapato)
        if zapato is None:
            return False
        zapato.precio = nuevo_precio
        session.commit()
        return True

# =====================================
# TODO ORM 9 - ELIMINAR ZAPATO
# =====================================
# Buscar el zapato por ID.
    # Eliminar el objeto con el ORM.
    # Confirmar la transaccion.
    #
    # Retornar True si se elimino.
    # Retornar False si no existe.

def eliminar_zapato(id_zapato):
    with Session(engine) as session:
        zapato = session.get(Zapato, id_zapato)
        if zapato is None:
            return False
        session.delete(zapato)
        session.commit()
        return True