
function eliminarEmpleado(id) {
    fetch(`/eliminar-empleado/${id}`, { method: 'DELETE' })
        .then(response => response.json())
        .then(data => {
            alert(data.mensaje);
            location.reload(); // Recarga la tabla después de eliminar
        })
        .catch(error => console.error("Error al eliminar empleado:", error));
        }
        console.log("delete.js cargado correctamente.");