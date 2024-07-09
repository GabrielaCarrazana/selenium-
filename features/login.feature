# language: es
@login  #para ejecutarlo es el comando behave --tags=@login  features -f behave_html_formatter:HTMLFormatter -o reports/report.html
Característica: Pantalla de login

Antecedentes: ##lo que es comun para todos
    Dado Que tengo un navegador abierto
    Cuando Entro al sitio "https://katalon-demo-cura.herokuapp.com/"




Escenario: Hacer login datos correctos
    Cuando Hago click en el boton con id "btn-make-appointment"
    Y Escribo "John Doe" en el campo con id "txt-username"
    Y Escribo "ThisIsNotAPassword" en el campo con id "txt-password"
    Y Hago una captura de pantalla con nombre "antes de login"
    Y Hago click en el boton con id "btn-login"
    Y Hago una captura de pantalla con nombre "despues de login"
    Entonces Deberia encontrar en la pagina el elemento con Xpath "//h2[normalize-space()='Make Appointment']" que contenga el texto "Make Appointment"


Escenario: Hacer login datos incorrectos
    Cuando Hago click en el boton con id "btn-make-appointment"
    Y Escribo "nada" en el campo con id "txt-username"
    Y Escribo "nada" en el campo con id "txt-password"
    Y Hago una captura de pantalla con nombre "antes de login"
    Y Hago click en el boton con id "btn-login"
    Y Hago una captura de pantalla con nombre "despues de login"
    Entonces Deberia encontrar en la pagina el elemento con Xpath "//p[@class='lead text-danger']"

Escenario: abrir y hacer captura
    Cuando Hago una captura de pantalla con nombre "al abrir" 



    