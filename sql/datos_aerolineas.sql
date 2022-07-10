CREATE TABLE aerolineas (
	id INTEGER PRIMARY KEY,
	nombre VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO aerolineas VALUES
    (1, 'Volaris'),
    (2, 'Aeromar'),
    (3, 'Interjet'),
    (4, 'Aeromexico');

CREATE TABLE aeropuertos (
	id INTEGER PRIMARY KEY,
	nombre VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO aeropuertos VALUES
    (1, 'Beniro Juarez'),
    (2, 'Guanajuato'),
    (3, 'La paz'),
    (4, 'Oaxaca');
 
CREATE TABLE movimientos (
	id INTEGER PRIMARY KEY,
	descripcion VARCHAR(50) UNIQUE NOT NULL
);


INSERT INTO movimientos  VALUES
    (1, 'Salida'),
    (2, 'Llegada');
    

CREATE TABLE vuelos (
	id_aerolinea INTEGER,
	id_aeropuerto INTEGER,
	id_movimiento INTEGER,
	fecha DATE
);

INSERT INTO vuelos  VALUES
    (1, 1, 1, '2021-05-02'),
    (2, 1, 1, '2021-05-02'),
    (3, 2, 2, '2021-05-02'),
    (4, 3, 2, '2021-05-02'),
    (1, 3, 2, '2021-05-02'),
    (2, 1, 1, '2021-05-02'),
    (2, 3, 1, '2021-05-04'),
    (3, 4, 1, '2021-05-04'),
    (3, 4, 1, '2021-05-04');