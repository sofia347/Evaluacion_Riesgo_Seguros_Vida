from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos de clientes
clientes = [
    {"nombre": "Mayabi", "edad": 22, "salud": "saludable", "historial_familiar": "false", "estilo_vida": "activo", "ocupacion": "oficina", "historial_seguro": "bueno"},
    {"nombre": "Carlos", "edad": 30, "salud": "diabetes", "historial_familiar": "true", "estilo_vida": "fumador", "ocupacion": "piloto", "historial_seguro": "reclamos_frecuentes"},
    {"nombre": "Ana", "edad": 51, "salud": "saludable", "historial_familiar": "false", "estilo_vida": "activo", "ocupacion": "oficina", "historial_seguro": "bueno"}
]

# Factores de riesgo
factores_negativos = ["fumador", "alcoholico", "piloto", "bombero", "minero"]
factores_positivos = ["saludable", "bueno", "false"]

def evaluar_riesgo(cliente):
    puntaje = cliente["edad"]
    if cliente["estilo_vida"] in factores_negativos:
        puntaje += 4
    if cliente["ocupacion"] in factores_negativos:
        puntaje += 4
    if cliente["salud"] not in factores_positivos:
        puntaje += 4
    if cliente["historial_familiar"] != "false":
        puntaje += 4
    if cliente["historial_seguro"] != "bueno":
        puntaje += 4
    
    if puntaje <= 29:
        return "Bajo Riesgo"
    elif 30 <= puntaje <= 50:
        return "Moderado Riesgo"
    else:
        return "Alto Riesgo"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nuevo_cliente = {
            "nombre": request.form["nombre"],
            "edad": int(request.form["edad"]),
            "salud": request.form["salud"],
            "historial_familiar": request.form["historial_familiar"],
            "estilo_vida": request.form["estilo_vida"],
            "ocupacion": request.form["ocupacion"],
            "historial_seguro": request.form["historial_seguro"]
        }
        nuevo_cliente["riesgo"] = evaluar_riesgo(nuevo_cliente)
        clientes.append(nuevo_cliente)
        return redirect(url_for('index'))
    
    for cliente in clientes:
        cliente["riesgo"] = evaluar_riesgo(cliente)
    return render_template('index.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
