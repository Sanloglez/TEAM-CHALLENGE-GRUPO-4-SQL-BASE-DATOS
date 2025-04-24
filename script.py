import sqlite3
import pandas as pd

conn = sqlite3.connect("base_datos_2.db")
cursor = conn.cursor()


#TABLA CATEGORÍAS
cursor.execute("""
CREATE TABLE categorias (
    codigo_categoria VARCHAR PRIMARY KEY,
    nombre TEXT NOT NULL
);
""")
cursor.execute("INSERT INTO categorias (codigo_categoria,nombre) VALUES ('CAT001','Mecánica')")

print("Categorías:")
for fila in cursor.execute("SELECT * FROM categorias"):
    print(fila)


#TABLA PROVEEDORES
cursor.execute("""
CREATE TABLE proveedores (
    codigo_proveedor VARCHAR PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT,
    ciudad TEXT,
    provincia TEXT
);
""")

cursor.execute("INSERT INTO proveedores (codigo_proveedor,nombre, direccion, ciudad, provincia) VALUES ('PROV01','Recambios López', 'General Castaños', 'Algeciras', 'Cádiz')")

#TABLA PIEZAS
cursor.execute("""
CREATE TABLE piezas (
    codigo_pieza VARCHAR PRIMARY KEY,
    nombre TEXT NOT NULL,
    color TEXT,
    precio REAL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id) 
);
""")

cursor.execute("INSERT INTO piezas (codigo_pieza, nombre, color, precio) VALUES ('RU01', 'Rueda', 'gris', '80.00')")

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

cursor.execute("INSERT INTO pedidos(proveedor_id, pieza_id, cantidad, fecha) VALUES ('RU01', 'Rueda', 'gris', '80.00')")

conn.commit()
conn.close()

