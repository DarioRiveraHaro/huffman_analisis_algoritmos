import tkinter as tk
from tkinter import filedialog

# Abre un archivo seleccionado bajo el nombre 'archivo' en modo leer.
def leer_archivo(archivo):
    with open(archivo, 'r') as archivo:
        contenido = archivo.read()
        contar_carcteres(contenido) # Pasa como argumento el contenido del archivo.

# Cuenta cada caracter y los guarda en diccionarios.
def contar_carcteres(contenido):
    dic = {}
    for caracter in contenido: # Recorre caracter por caracter
        caracter = caracter.lower() # Convierte todos los caracteres en minusculas para no contar doble
        if caracter.isalpha() or caracter.isspace():  
            if caracter in dic: # Checa si el caracter en el que esta es uno que ya se guardo en un diccionario y le suma uno
                dic[caracter] += 1
            else:
                dic[caracter] = 1 # Si no hay ningun caracter se crea el diccionario y se le agrega uno
    print(dic)

# Frontend
def ventana_main():
    root = tk.Tk()
    root.geometry('300x100')
    
    # Cuando se llama esta funcion abre el file manager para poder selecionar el archivo
    def abrir_filemanager():
        archivo = filedialog.askopenfilename()
        archivo_entry.delete(0, tk.END)
        archivo_entry.insert(0, archivo)
        leer_archivo(archivo) # Pasa como argumento el archivo seleccionado 

    main_frame = tk.Frame(master=root) # Frame que contiene todo lo que hay en la ventana 
    main_frame.pack(padx=8, pady=8)

    archivo_frame = tk.Frame(master=main_frame) # Frame que contiene el lable y la caja de texto sobre el archivo
    archivo_frame.pack(padx=8, pady=8)

    archivo_lbl = tk.Label(master=archivo_frame, text='Archivo: ')
    archivo_lbl.grid(column=0, row=0)

    archivo_entry = tk.Entry(master=archivo_frame, width=35)
    archivo_entry.grid(column=1, row=0)

    botones_frame = tk.Frame(master=main_frame) # Frame que contiene todos los botones
    botones_frame.pack(padx=8, pady=8)

    examinar = tk.Button(master=botones_frame, text='Examinar', command=abrir_filemanager)
    examinar.grid(padx=8, pady=4, column=0, row=0)

    comprimir = tk.Button(master=botones_frame, text='Comprimir')
    comprimir.grid(padx=8, pady=4, column=1, row=0)

    descomprimir = tk.Button(master=botones_frame, text='Descomprimir')
    descomprimir.grid(padx=8, pady=4, column=2, row=0)

    root.mainloop()

if __name__ == '__main__':
    ventana_main()