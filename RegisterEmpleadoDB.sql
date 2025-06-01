CREATE TABLE empleado (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombres NVARCHAR(50),
	Apellidos NVARCHAR(50),
	FechaNacimiento NVARCHAR(50),
	NumeroIdentificacion NVARCHAR(50),
	Direccion NVARCHAR(100),
	Telefono NVARCHAR(50),
    Correo NVARCHAR(100),
	FechaIngreso DATE,
	CargoPuesto NVARCHAR(100),
	Departamento NVARCHAR(100),
	Salario DECIMAL,
	TipoContrato NVARCHAR(100),
	Estatus NVARCHAR (MAX)
);
use Empleado
ALTER TABLE empleado
ALTER COLUMN Estatus BIT;