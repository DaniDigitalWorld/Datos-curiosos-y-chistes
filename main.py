from flask import Flask
import random

app = Flask(__name__)

# =========================
# DATOS CURIOSOS
# =========================

datos = [
    {
        "texto": "Los pulpos tienen tres corazones y cuando nadan, dos de ellos dejan de latir temporalmente.",
        "imagen": "pulpo.jpg"
    },

    {
        "texto": "En Venus, un día dura más que un año. Venus tarda unos 243 días terrestres en girar sobre sí mismo, pero solo unos 225 días en dar una vuelta alrededor del Sol.",
        "imagen": "venus.jpg"
    },

    {
        "texto": "Los gatos pueden producir más de 100 sonidos diferentes.",
        "imagen": "gato.jpg"
    },

    {
        "texto": "Los tiburones existen desde antes que los árboles. Los primeros tiburones aparecieron hace más de 400 millones de años.",
        "imagen": "tiburon.jpg"
    },

    {
        "texto": "Una nube puede pesar cientos de toneladas, aunque desde el suelo parezca ligera y esponjosa.",
        "imagen": "nube.jpg"
    },

    {
        "texto": "Los plátanos son bayas según la clasificación botánica, pero las fresas técnicamente no lo son.",
        "imagen": "platano.jpg"
    },

    {
        "texto": "Los cuervos pueden recordar rostros humanos y aprender a reconocer a personas específicas. Además, pueden transmitir información sobre personas peligrosas a otros cuervos, incluso a generaciones futuras.",
        "imagen": "cuervo.jpg"
    },

    {
        "texto": "La miel puede durar muchísimo tiempo sin echarse a perder si se conserva correctamente.",
        "imagen": "miel.jpg"
    },

    {
        "texto": "Los astronautas pueden crecer algunos centímetros temporalmente en el espacio porque la columna vertebral se estira.",
        "imagen": "astronauta.jpg"
    },

    {
        "texto": "Las mariposas pueden saborear usando sensores ubicados en sus patas.",
        "imagen": "mariposa.jpg"
    },

    {
        "texto": "El corazón de una ballena azul puede llegar a pesar más de 150 kilogramos.",
        "imagen": "ballena.jpg"
    },

    {
        "texto": "Los koalas tienen huellas dactilares tan parecidas a las humanas que pueden resultar difíciles de distinguir a simple vista.",
        "imagen": "koala.jpg"
    },

    {
        "texto": "Algunas especies de bambú pueden crecer casi un metro en un solo día en condiciones ideales.",
        "imagen": "bambu.jpg"
    },

    {
        "texto": "Los ojos de los avestruces son más grandes que su cerebro.",
        "imagen": "avestruz.jpg"
    },

    {
        "texto": "Los tardígrados son animales microscópicos capaces de sobrevivir a condiciones extremas.",
        "imagen": "tardigrado.jpg"
    }
]


# =========================
# CHISTES
# =========================

chistes = [
    {
        "texto": "¿Qué le dice un pez a otro pez? ¡Nada, nada!",
        "imagen": "pez.jpg"
    },

    {
        "texto": "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
        "imagen": "cebra.jpg"
    },

    {
        "texto": "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "imagen": "abeja.jpg"
    },

    {
        "texto": "¿Cómo se despiden los químicos? Ácido un placer.",
        "imagen": "quimica.jpg"
    },

    {
        "texto": "¿Qué le dijo un techo a otro techo? Techo de menos.",
        "imagen": "techo.jpg"
    },

    {
        "texto": "Mamá, en la escuela me dicen distraído. Niño, tú vives en la casa de enfrente.",
        "imagen": "distraido.jpg"
    },

    {
        "texto": "¿Qué hace un gato programador? ¡Miau-thon!",
        "imagen": "gato_chiste.jpg"
    }
]


# =========================
# PÁGINA PRINCIPAL
# =========================

@app.route("/")
def inicio():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Datos y Chistes</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>

        <div class="contenedor">

            <h1> 🌐 Datos curiosos y chistes 😊</h1>

            <p class="descripcion">
                ¡Bienvenido! Aquí puedes descubrir cosas increíbles
                y reírte un rato.
            </p>

            <div class="botones">

                <a href="/random_fact" class="boton">
                    🤯 Dato curioso
                </a>

                <a href="/chiste" class="boton">
                    😂 Chiste
                </a>

            </div>

        </div>

    </body>
    </html>
    '''


# =========================
# DATOS CURIOSOS
# =========================

@app.route("/random_fact")
def dato_random():

    dato_elegido = random.choice(datos)

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dato curioso</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>

        <div class="contenedor">

            <div class="tarjeta">

                <h1>🤯 ¿Sabías que...?</h1>

                <img src="/static/img/{dato_elegido["imagen"]}" class="imagen">

                <p class="texto">
                    {dato_elegido["texto"]}
                </p>

                <a href="/random_fact" class="boton">
                    🔎 Otro dato
                </a>

                <a href="/" class="volver">
                    🏠 Página principal
                </a>

            </div>

        </div>

    </body>
    </html>
    '''


# =========================
# CHISTES
# =========================

@app.route("/chiste")
def chiste():

    chiste_elegido = random.choice(chistes)

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chiste</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>

        <div class="contenedor">

            <div class="tarjeta">

                <h1>😂 Chiste</h1>

                <img src="/static/img/{chiste_elegido["imagen"]}" class="imagen">

                <p class="texto">
                    {chiste_elegido["texto"]}
                </p>

                <a href="/chiste" class="boton">
                    😂 Otro chiste
                </a>

                <a href="/" class="volver">
                    🏠 Página principal
                </a>

            </div>

        </div>

    </body>
    </html>
    '''


# =========================
# INICIAR FLASK
# =========================

app.run(debug=True, port=5001)