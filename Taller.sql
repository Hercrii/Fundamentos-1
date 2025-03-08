DROP TABLE IF EXISTS Detalles_Pedido;
DROP TABLE IF EXISTS Pedidos;
DROP TABLE IF EXISTS Productos;
DROP TABLE IF EXISTS Clientes;


CREATE TABLE Clientes (
    ClienteID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    Correo TEXT UNIQUE,
    Telefono TEXT
);


CREATE TABLE Productos (
    ProductoID INTEGER PRIMARY KEY AUTOINCREMENT,
    NombreProducto TEXT,
    Precio REAL,
    Stock INTEGER
);


CREATE TABLE Pedidos (
    PedidoID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClienteID INTEGER,
    Fecha TEXT,
    Total REAL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);


CREATE TABLE Detalles_Pedido (
    DetalleID INTEGER PRIMARY KEY AUTOINCREMENT,
    PedidoID INTEGER,
    ProductoID INTEGER,
    Cantidad INTEGER,
    Subtotal REAL,
    FOREIGN KEY (PedidoID) REFERENCES Pedidos(PedidoID),
    FOREIGN KEY (ProductoID) REFERENCES Productos(ProductoID)
);


-- Insertar Clientes
INSERT INTO Clientes (Nombre, Correo, Telefono) VALUES 
('Juan Pérez', 'juan.perez@email.com', '123456789'),
('María Gómez', 'maria.gomez@email.com', '987654321');

-- Insertar Productos
INSERT INTO Productos (NombreProducto, Precio, Stock) VALUES 
('Laptop', 800.00, 10),
('Mouse', 25.00, 50),
('Teclado', 45.00, 30);


INSERT INTO Pedidos (ClienteID, Fecha, Total) VALUES 
(1, '2025-03-08', 895.00);


INSERT INTO Detalles_Pedido (PedidoID, ProductoID, Cantidad, Subtotal) VALUES 
(1, 1, 1, 800.00),  -- 1 Laptop a 800.00
(1, 2, 2, 50.00),   -- 2 Mouse a 25.00 cada uno
(1, 3, 1, 45.00);   -- 1 Teclado a 45.00


SELECT * FROM Clientes;


SELECT Pedidos.PedidoID, Clientes.Nombre, Pedidos.Fecha, Pedidos.Total
FROM Pedidos
JOIN Clientes ON Pedidos.ClienteID = Clientes.ClienteID;

SELECT Pedidos.PedidoID, Productos.NombreProducto, Detalles_Pedido.Cantidad, Detalles_Pedido.Subtotal
FROM Detalles_Pedido
JOIN Productos ON Detalles_Pedido.ProductoID = Productos.ProductoID
JOIN Pedidos ON Detalles_Pedido.PedidoID = Pedidos.PedidoID;
