import sqlite3

# Crear conexión y cursor
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Crear tablas con SQL corregido
cursor.executescript("""
CREATE TABLE Proveedores (
    proveedor_id INTEGER PRIMARY KEY,
    nombre TEXT,
    direccion TEXT,
    ciudad TEXT,
    provincia TEXT
);

CREATE TABLE Categorias (
    categoria_id INTEGER PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE Piezas (
    pieza_id INTEGER PRIMARY KEY,
    nombre TEXT,
    color TEXT,
    precio REAL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(categoria_id)
);

CREATE TABLE Pedidos (
    suministro_id INTEGER PRIMARY KEY,
    proveedor_id INTEGER,
    pieza_id INTEGER,
    cantidad INTEGER,
    fecha DATE,
    FOREIGN KEY (proveedor_id) REFERENCES Proveedores(proveedor_id),
    FOREIGN KEY (pieza_id) REFERENCES Piezas(pieza_id)
);
""")

conn.commit()

# Insertar datos en Proveedores
cursor.execute("INSERT INTO Proveedores VALUES (1, 'Proveedor A', 'Calle Falsa 123', 'CDMX', 'CDMX')")

# Insertar datos en Categorias
cursor.execute("INSERT INTO Categorias VALUES (1, 'Electrónica')")

# Insertar datos en Piezas
cursor.execute("INSERT INTO Piezas VALUES (101, 'Resistor', 'Marrón', 0.15, 1)")

# Insertar datos en Pedidos
cursor.execute("INSERT INTO Pedidos VALUES (1001, 1, 101, 500, '2025-04-10')")

conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Proveedores")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Piezas")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Pedidos")
print(cursor.fetchall())