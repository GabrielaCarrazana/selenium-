# language: es
@fotos #para ejecutarlo es el comando behave --tags=@fotos  features -f behave_html_formatter:HTMLFormatter -o reports/report.html
Característica: PANTALLA DE wiki
Escenario:Abrir wikipedia y extraer todas las fotos y hacerle capturas de pantalla al elemento 
    Dado Que tengo un navegador abierto
    Cuando Entro al sitio "https://es.wikipedia.org/wiki/Salamanca"
    Y Identificar los elementos con xpath: "//img"
    Entonces Hacer captura de elementos
  
    