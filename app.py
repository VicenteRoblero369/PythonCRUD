from flask import Flask, jsonify, request, render_template, redirect, url_for
app = Flask(__name__, static_url_path='/static')
import database
import json

app = Flask(__name__)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        Nombres = request.form['Nombres']
        Apellidos = request.form['Apellidos']
        FechaNacimiento = request.form['FechaNacimiento']
        NumeroIdentificacion = request.form['NumeroIdentificacion']
        Direccion = request.form['Direccion']
        Telefono = request.form['Telefono']
        Correo = request.form['Correo']
        FechaIngreso = request.form['FechaIngreso']
        CargoPuesto = request.form['CargoPuesto']
        Departamento = request.form['Departamento']
        Salario = request.form['Salario']
        TipoContrato = request.form['TipoContrato']
        Estatus = request.form['Estatus']

        conexion = database.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO empleado (Nombres, Apellidos, FechaNacimiento, NumeroIdentificacion, Direccion, Telefono, Correo, FechaIngreso, CargoPuesto, Departamento, Salario, TipoContrato, Estatus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (Nombres, Apellidos, FechaNacimiento, NumeroIdentificacion, Direccion, Telefono, Correo, FechaIngreso, CargoPuesto, Departamento, Salario, TipoContrato, Estatus ))
        conexion.commit()
        conexion.close()

        return render_template("empleados.html")

    return render_template('registro.html')
#mandar a trael mi lista de empleados con json
@app.route('/empleados-json')
def obtener_empleados():
    try:
        conexion = database.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT Id, Nombres, Apellidos, Correo, Estatus FROM empleado")
        
        empleados = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        conexion.close()

        return jsonify(empleados)  # Retorna lista de empleados en JSON

    except Exception as e:
        print(f"Error al obtener empleados: {e}")
        return jsonify([])

@app.route('/empleados', endpoint='empleados')
def empleados_html():
    return render_template('empleados.html')  # Carga la página HTML

#eliminar datos de la tabla 
@app.route('/eliminar-empleado/<int:id>', methods=['DELETE'])
def eliminar_empleado(id):
    try:
        conexion = database.conectar_bd()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM empleado WHERE Id = ?", (id,))
        conexion.commit()
        conexion.close()

        return jsonify({"mensaje": "Empleado eliminado"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    #editar empleado
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conexion = database.conectar_bd()
    cursor = conexion.cursor()
    if request.method == 'POST':
        nombres = request.form['Nombres']
        apellidos = request.form['Apellidos']
        correo = request.form['Correo']
        estatus = request.form['Estatus']

        cursor.execute("""
            UPDATE empleado 
            SET Nombres=?, Apellidos=?, Correo=?, Estatus=? 
            WHERE Id=?
        """, (nombres, apellidos, correo, estatus, id))

        conexion.commit()
        conexion.close()
        return redirect(url_for('empleados'))  # Redirige a la lista de empleados

    cursor.execute("SELECT * FROM empleado WHERE Id=?", (id,))
    empleado = cursor.fetchone()
    conexion.close()

    return render_template('update.html', empleado=empleado)

if __name__ == "__main__":
    app.run(debug=True)
