# Pruebas Testing (Automatizacion)
En este proyecto se veran las disintas formas de automatizar
los campos de ingreso de datos de un formulario de una pagina web con el software de selenium,
como ejemplo se utilizo la pagina de Udemy Academy en su modulo
de inicio de sesion.
## Requisitos
Para la ejecucion de los codigos que veran, se uso el controlador 
de Chrome. Los controladores permiten que al ejecutar
el codigo con la instancia de los objetos de selenium
se pueda ejecutar un navegador y en el poder acceder a la url
de la pagina con el formulario a automatizar.
Por lo tanto se requiere la descarga de Selenium y 
el controlador (Driver) que en este caso sera chrome.

- Comando de instalacion de selenium
```
pip install selenium
```
- Para la instalacion del controlador de Chrome, [ingrese aqui](https://chromedriver.storage.googleapis.com/index.html?path=103.0.5060.53/)

Luego de la descarga del controlador, se creara una carpeta en el mismo proyecto
llamada "Drivers" y se almacenara ahi el controlador de chrome
para que sea mas facil su instanciación.

Tambien se requiere de la instalacion de Chropath para el uso 
del software de Xpath, se puede acceder a ella en la tienda
de extensiones de google(es gratis)

## Descripcion de Archivos

Como se dijo previamente, cada archivo tiene una forma
de automatizar los campos de forma distinta, aqui se dara una
breve descripcion de como lo hace cada uno.

|Archivo | Descripcion
|--------|------------
|[Id](Id.py) | Completa los campos de texto, buscando en las etiquetas de los campos de la pagina web su atributo de id=""
|[class](class.py) | Completa los campos de texto, buscando en las etiquetas de los campos de la pagina web su atributo de class=""
|[name](Id.py) | Completa los campos de texto, buscando en las etiquetas de los campos de la pagina web su atributo de name=""
|[link](link.py) | Busca en el archivo una palabra o caracter que referencie un link, luego de encontrarlo, le da click y al ingresar a la nueva ventana se usan los otros modos de completar un campo de texto si en el formulario hay campos a diligenciar
|[xpath](tag_css.py) | En este archivo usaremos la extension de Chropath que nos suministrara informacion de las rutas de las etiquetas de la pagina web ademas de las rutas referenciadas con atributos, alli se manejaran las rutas relativas y las rutas absolutas. Las rutas relativas son cortas pero se usan cuando no se tiene la certeza de que se vayan a modificar las etiquetas de posicion, en cambio las rutas absolutas son aquellas que se sabe que no van a cambiar y la ruta de su posicion siempre sera la misma 
|[tag_css](tag_css.py) | En este archivo se usara como parametro de busqueda de los campos el CSS_SELECTOR para la busqueda y llenado de campos, se usa la referencia del atributo id
|[tag_css](tag_css.py) | En este archivo se usara como parametro de busqueda de los campos el CSS_SELECTOR para la busqueda y llenado de campos, se usa la referencia del atributo class
