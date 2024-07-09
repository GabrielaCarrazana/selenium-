# Selenium 
Organizacion que fabrica 3 herramientas: 
Selenium web driver
selenium IDE -> No vale ,Extension de navegador sisponible parea chrome y firefox para grabar y reproducir pruebas, mejor el katalon Recorder que hace lo mismo y cn mejor feedback
Selenium Grid:Montar una granja de servidores para ejecutar pruebas en paalelo en diferentes navegadores, dispositivos y sistemas operativos


Herramienta para automatizaciones en entornos web
vamos a usar unitest + Selenium para conseguir automatizar pruebas dentro de un navegador web sobre el frontal de una aplicacion

# Vocabulario en testing
error Errores que se cometen en desarrollo que introducen un defecto en un producto que se puede manifestar en un fallo, el sistema no se comporta como deberia, una vez que se detecta el fallo se procede a subsanar el defecto 
Para subsanar el defecto primero se debe identificar ese defecto (Depurar)
defecto 
fallo 
 
 # Para que sirven las pruebas: 
 -Para verificar si un programa cumple con sus requisitos.
 -Para encontrar fallos.
 -Recopilar la mayor cantidad de informaci'on sobre un fallo para poder identificar mas rapido el defecto que lo produce.
 -Conocer mas acerca del producto.
 -Encontrar la mayor cantidad posible de defectos antes de la puesta en produccion del programa


 ----TDD:Desarrollo dirigido por Test Test Firts + refactorizxacion en cada iteracion 
 refactorizacion: Tercnica de ingenieria de software que tiene como objetivo alterar su comportam,iento sin cambiar su funcionalidad y reducir los tiempos de desarrollo y facil;itar su mantenimiento:
 Se comienza por definir pruebas unitarias
------BDD Se comienza por definir pruebas de sistemas
------ATDD Se com,ienza por definir pruebas de aceptacion

# Metodologias Agiles
Forma de gestionar un proyecto qeu remplaza a otras formas mas tradicionales que se venian usando 
distincion : El producto se entrewga de forma incremental al cliente, para conseguir un rapido feedback por parte del cliente para poder adaptar el producto a sus necesidades
Sprint 1 dia 30 de comenzar un proyecto hago instalacion del sw en produccion ---Instalacion quizas solo con un 5% ( Hay que probar ese 5%) de la funcionalidad pero que sea 100% funcional, al sprint 2  una segunda entrega donse anyado otro 20% (volver a probar el 5% antiguo y el 20% nuevo ) y luego en los siguientes Sprints otro 30% ( probar el 5% el 20% y el 30 recien entregado ) y asi.....

---Han traido problemas nuevos: HAY NERCESIDAD DE HACER MAS PRUEBAS DE SW (EN CADA ENTREGA )
soluciones: 1 No hacer pruebas -> No es solucion
Solucion 2 : Automatizar las pruebas para no repetir el  trabajo 

> El software funcionando es la medida escencial de progreso 
La medida principal de como va el proyecto es el software funcionando, El indicador que se debe usar el software funcionando
Quien dice que un software funciona: el resultado de las pruebas.
La pruebas son el indicador de progreso de un software 

# Tipos de prubas: Se clasifican en base a diferentes criterios 
- En base al objeto de prueba: funcionales-> Unitarias, integracion, sistema, aceptacion
                               no funcionales -> Estres, disponibilidad, rendimiento, carga, us,ha
En base a procedimiento: Estaticas -> No hay que poner el sistema en funcionamiento, nos sirve para identificar defectos
                         Dinamicas-> Hay que depurar el sistema, ponerlo en funcionamiento, identifica fallos

Pruebas Unitarias : Se centra en una caracteristica de un componente aislado de un sistema
integracion : Se centra een la comunicacion entre dos componentes ejemplo->Sistema de frenado mas ruedas y ya habiedo realizado pruebas unitarias al sistema de frenado mas a las ruedas.
Sistema : Se centra en el comportamiento del sistema en su conjunto
Prubas de aceptacion: son un subconjunto de las de sistema

Con selenium webdriver se pueden hacer todo tipo de pruebas: Dinamicas, funcionales, de sistemas y de aceptacion  !!!No puedo hacer ni Unitarias ni de integracion.
Estas se hacen con Cypres, Karka, webdriver.io
Al trabajar con selenium se puede automatizar una prueba, se construyen scripts y vamos a elegir un lenguaje de programacion guay para montar script: Python 

### Tipos de softwares: 
Sistema Operativo
Driver
Libreria
Aplicacion
Demonio:
----Servicio 
Script ***----Un programa que ejecuta una secuencia de tareas... hasta qeua acaba

objetivos del curso : Scripts con python de pruebas funcionales y de sistemas:
Conociemientos: -Python basico
                -Selenium.
                -HTML.(Basico).
                -CSS.
                -XPATH.

# SELENIUM WEBDRIVER: Está basado en u standar de W3C llamado webdriver: define como construir programas que controlen acciones dentro de un navegador web.
se creará un script de python con libreria de selenium -> Web driver -> Navegador web
 ^
 Se trabaja a este nivel
 Cada version de cada navegador tiene su propio webdriver: Chrome: un webdriver diferente de moxilla 
 Webdriver | Webdriver
 chrome    | ChromeDriver
 Firefox   | GueckoDrver
 Edge      | EdgeDriver
 Safari    | SafariDriver
 La configuracion de estas herramientas es un latazo ya que hay que mantenerlas actualizadas. 
 # Metodologia
 Todos los scrpts que s montaran en python para selenium, tendran la misma estructura: 
                                                                                    1. Configurar webdriver
                                                                                    2. arrancar webdriver en el navegador
                                                                                    3.Automatizar tareas denrtro del navegador....>>>>SELENIUM WEBDRIVER 
                                                                                    4. Ejecutar una pruebas.... ->ENTONCES ...<<<UNITTEST
                                                                                    5 Cerrar el navegador
## Ejemplo practico:
Probar formulario de login del formulario de entrada de : https://katalon-demo-cura.herokuapp.com 
Prueba:
A la hora de definir cada prueba hay qeu definir
COMNTEXTO en el que se realiza la prueba............................. GIVEN.. DADO EL CONTEXTO
ACCION  que quiero probar............................................ WHEN... DEFINO UNA ACCION
PRUEBAS que garantizan que se ejecuta la prueba correctamente.........THEN....ENTONCES DEBO TENER UN RESULTADO ESPERADO 

A la hora de definir una prueba hay que tener en cuenta los principios first del desarrollo de software 
F. fast.............Ejecutable en un tiempo razonable.
I. independent......No debe depender de otras pruebas.
R. Repeteable.......Se debe poder repetir.
S. Self-validating..Debe poder determinar si misma si ha pasado o no todas las condiciones necesarias para dada por buena.
T. Timely...........oportuna, debo tener la prueba en el momento adecuado, no definir pruebas unitarias si ya el sistema esta montado.

Unitaria -> Integracion -> sistema
No hay necesidad de si las pruebas de sistema pasan todas, hacer las pruebas unitarias, sin embargo con las pruebas unitarias pasadas es necesario hacer las de integracio y las de sistemas.

PRUEBAS DE CAJA NEGRA : NO CONOZCO CODIGO FUENTE DEL SISTEMA
        1.1 uSUARIO CORRECTO, CONTRASENYA INCORRECTA
        1.2 USUARIO INCORRECTO, CONTRASE;A CORRECTA
        1.3 USUARIO CORRECTO Y CONTRASENYA MAYUSCULA
        1.4 FORMULARIO EN BLANCO.
        1.5 iNTENTAR ACCEDER CON USUARIO Y CONTRASENYA INCORRECTA (VAALIDAR FORM DE ACCESO)
        1.6 USUARIO EN BLANCO Y CONTRASENYA CORRECTA
        1.7 USUARIO CORRECTO CONTRASENYA EN BLANCO 
PRUEBAS DE CAJA BLANCA: cONOZCO EL CODIGO FUENTE DEL SISTEMA:
        El desarrollador que conoce como funciona el sw sabe que no puede entrar con los campos vacios 

PRUEBA 2 ACCEDER CON USUARIO Y CONTRASENYA CORRECTA
        Dado: Conozco usuario y contrasenya registradas en el sistema 
        ..Y un navegador con mi appa abierta 
        ..Y haber pulsado en el boton de reservar cita 
        Cuando: Introduzco Usuario( campo usuario) ....***IDENTIFICAR ESOS COMPONENTES EN LA WEB
        ..E contrasenya ( Campo contrasenya)...........*** 
        ..Y boton de login............................**** Problema en el futuro, si cambia la web
        Entonces : debo llegar al formulario de reserva de cita
        ..........................................................................................***Necesitar XPATH


PRUEBA 3 SEGURIDAD: INYECTAR CODIGO FUENTE EN EL FORM
##### IMPORTANTE !!!!! Hay que hacer las pruebas sobre todos los navegadores y sobre por lo menos las ultimas 5 versiones de los navegadores y para todos los sistemas operativos por lo que se usa un grid de selenium
En el dia a dia, tiro a 2 navegadores y a veces me monto un grid de selenium en mi maquina o un servidor de la empresa y cuando voy a instalar en produccion tiro la pruebaa  lo bruto a ver que no hay ningun problema.    
Montar un grid de selenium con 3 navegadores  puede tardar unos 30 segundos 

## identificacion de elementos con selenium html
selenium busca elementos en el DOM de la pagina web que no es su coigo fuente sino lo que el navegador ha cargado de esa pagina web
 la fija es tener un identificador 
 navegador.find_element(BY.ATRIBUTO, VALOR)
 ****EL PROBLEMA ES QUE SIEMPRE VOY A ENCONTRAR ELEMENTOS DONDE LOS DESARROLLAADORES NO HAN PUESTO id:
 QUE HACER ??: 
 -Intentar dentro de las posibilidades que desarrollo ponga IDs unicos a los elementos que necesito.
 lo guay es tener definidos los test antes que el desarrollador haya hecho el codigo (test first) y enviarle el fichero de test al desarrollador, y que este trabaje hasta que la prueba pase, esto ser'ia la mejor forma de trabajar y la tendencia hoy en dia en la industria.
 navegador.find_element(BY.ATRIBUTO, VALOR)

 -Opcion 2 leer opcion 1 e insistir por in ID

 tambien se puede buscar por el XPATH este sirvepara buscar cualquier elemento dentro del html siguiendo la siguiente sintaxis:
 //-> Busca desde donde estoy hacia abajo
 /-> Busca el elemento dentro donde estoy 
* -> Buscar cualquiuer elemento
. ->Donde estoy
tipo -> Elemento de un detereminado tipo ejemplo

HTML--------------------------------------0
    HEAD-----------------------------------1
     TITLE-----------------------------------2
     LINK-----------------------------------3
    BODY-----------------------------------4
     DIV-----------------------------------5
      H1-----------------------------------6
      P-----------------------------------7
      DIV---------------------------------8
      P-----------------------------------9
     DIV-----------------------------------10
      P-----------------------------------11
      P-----------------------------------12
      H2 class ="Titulo"-----------------------------------13
      P-----------------------------------14
      DIV-----------------------------------15
       P-----------------------------------16

/HTML/BODY/DIV/H1 -------7
/HTML/BODY//H1----------7
/DIV/P ---------> 7,9,11,12,14,16
//he[@class = titulo] ----------> 13
//*[@id="btn-make-appointment"]
//a[@id='btn-make-appointment'] 
Los corchetes se leen como tal que osea donde estoy que se cumpla una condicion entre corchetes
para ver las funciones posibles en el xpath hay que buscar xpath functions en google
text()-> extrae el texto de un elemento 
//TITLE/text()  extrae el texto de title
//div/p[contains(texto(),"texto a buscar")]   Busca por los parrafos que estan encapsulados en div, cual contiene un texto en especifico

## Cucumber Herramienta alternativa a unittest dispopnible para m,uchos lenguajes de programacion
al trabajar con cucmber vamos a escribir los ficheros en un lenguaje llamado gerkin(traduccion = pepinillo) las pruebas se definen en gerking para subirlas a cucumber, son un conjunto de restricciones que aplicamos a un lenguaje natural. Se puede elegir ingles, espanyol, catalan ...etc