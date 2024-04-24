
# Huffman

Este script de python es una simple interfaz grafica (GUI) para una aplicacion usando el algoritmo de Huffman. El algoritmo de Huffman es usado para comprimir data.




## Dependencias

El script usa los modulos tkinter y filedialog de las librerias standar de Python para crear la GUI y manejar los archivos.



## Funciones

- leer_archivo(archivo): Esta funcion abre un archivo en modo lectura, lee el contenido y pasa el contenido a la funcion contar_caracteres.

- contar_caracteres(contenido): Esta funcion recibe un string de contenido, cuenta cada caracter y guarda el conteo en diccionarios. También convierte en minusculas todos los caracteres para evitar que se cuenten doble. Solo cuenta letras y espacios.

- ventana_main(): Esta funcion crea la ventana principal de la GUI. Conntiene filedialog para poder seleccionar el archivo y un boton para para ejecutar la operacion. 2 de los botonoes no hacen nada en el script.

## GUI Layout

- El primer frame contiene solo un lable y una textbox que sirven para saber sobre que archivo se esta trabajando y el path de donde viene este.

- El segundo frame contiene los botones: 'Examinar', 'Comprimir' y 'Descomprimir'. El boton 'Examinar' abre el filedialog y muestra el path en la textbox. Los otros dos botones no hacen nada de momento.

## Ejecución 

El script se ejecuta con la linea de comando 'python huffman_frontend.py'. Se ejecuta la GUI y espera por una interaccion de un usuario.

## Nota
Este script es solo el frontend todavía no se implementa el algoritmo de Huffman, se espera que se conecte con el backend que es el que ejecutara las partes de comprensión y descompresión.
