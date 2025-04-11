import sqlite3
import pandas as pd

conn = sqlite3.connect("base_datos_2.db")
cursor = conn.cursor()


#TABLA CATEGORÍAS
cursor.execute("""
CREATE TABLE categorias (
    categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    codigo_categoria TEXT UNIQUE NOT NULL
);
""")
cursor.execute("INSERT INTO categorias (nombre, codigo_categoria) VALUES ('Mecánica', 'CAT001')")

print("Categorías:")
for fila in cursor.execute("SELECT * FROM categorias"):
    print(fila)


#TABLA PROVEEDORES
cursor.execute("""
CREATE TABLE proveedores (
    proveedor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT,
    ciudad TEXT,
    provincia TEXT,
    codigo_proveedor TEXT UNIQUE NOT NULL
);
""")

cursor.execute("INSERT INTO proveedores (nombre, direccion, ciudad, provincia, codigo_proveedor) VALUES ('Recambios López')")

#TABLA PIEZAS
cursor.execute("""
CREATE TABLE piezas (
    pieza_id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_pieza TEXT UNIQUE NOT NULL,
    nombre TEXT NOT NULL,
    color TEXT,
    precio REAL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id) 
);
""")

#TABLA PEDIDOS
cursor.execute("""
CREATE TABLE pedidos(
    suministro_id INTEGER PRIMARY KEY AUTOINCREMENT,
    proveedor_id INTEGER NOT NULL,
    pieza_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores(proveedor_id),
    FOREIGN KEY (pieza_id) REFERENCES piezas(pieza_id)
);
""")
conn.commit()
conn.close()

