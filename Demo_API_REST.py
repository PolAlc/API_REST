from flask import Flask

#La supervariable __name__ tomará por nombre al nombre del archivo py
app = Flask(__name__)

#Flask permite crear rutas y qué ocurre cuando se accede a esas rutas. En esta primera, se está indicando qué hacer cuando accede a la raíz de la ruta ("/"):
@app.route("/")

#Luego qué ocurre al acceder a esa ruta, se define con una función
def home():
    return("Hola mundo desde la home de Flask :D")

#Se configura con qué puerto se conectará al servidor web de flask (en este caso se usó el 3000 al azar - generalmente está libre):
#app.run( port = 3000 )

#Al agregar host = "0.0.0.0", estoy habilitando el uso del router. Esto ya lo habilita a ser usado en una intranet de mi casa. Cuando se corre con esta opción, muestra: http://miip:3000/, que es el ip de mi conexión a internet, con lo cual si ejecuto esto en el navegador de mi teléfono, si éste está en la misma red, se conecta.
app.run( port = 3000, host = "0.0.0.0" )


