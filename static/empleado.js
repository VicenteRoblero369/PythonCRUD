
document.addEventListener("DOMContentLoaded", function () {
    fetch('/empleados-json')  
        .then(response => response.json())
        .then(data => {
            const tablaBody = document.getElementById("tablaEmpleados");
            tablaBody.innerHTML = "";
           data.forEach(emp => {
                // Convertimos true/false a Activo/Inactivo
                let estatus = emp.Estatus ? "Activo" : "Inactivo"; // Usando operador ternario para simplificar
                let estatusClase = emp.Estatus ? "text-bg-success" : "text-bg-danger"; // Definir clase según estado


                let fila = `<tr>
                    <td>${emp.Id}</td>
                    <td>${emp.Nombres}</td>
                    <td>${emp.Apellidos}</td>
                    <td>${emp.Correo}</td>
                    <td class="badge rounded-pill ${estatusClase}">${estatus}</td>
                    <td><button onclick="eliminarEmpleado(${emp.Id})" class="btn btn-danger">Eliminar</button></td>
                    <td><button onclick="editarEmpleado(${emp.Id})" class="btn btn-warning">Editar</button></td>
                </tr>`;
                tablaBody.innerHTML += fila;
            });
        })
        .catch(error => console.error("Error al obtener empleados:", error));
});
