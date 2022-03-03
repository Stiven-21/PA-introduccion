from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")

@app.get("/contacto/<contactoID>/edit")
def editarContactos(contactoID):
    return render_template("contactos/editar.html", id = contactoID)

@app.get("/contacto/edad/<int:edad>")
def edad(edad):
    return render_template("contactos/edad.html", edad = edad)

app.run(debug=True)