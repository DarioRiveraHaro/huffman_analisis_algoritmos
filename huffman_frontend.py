import tkinter as tk
from tkinter import filedialog

def leer_archivo(archivo):
    dic = {}
    with open(archivo, 'r') as archivo:
        contenido = archivo.read()
        for caracter in contenido:
            caracter = caracter.lower()
            if caracter.isalpha() or caracter.isspace():  
                if caracter in dic:
                    dic[caracter] += 1
                else:
                    dic[caracter] = 1
    print(dic)
        
def ventana_main():
    root = tk.Tk()
    root.geometry('300x100')
    
    def abrir_filemanager():
        archivo = filedialog.askopenfilename()
        archivo_txt.delete(0, tk.END)
        archivo_txt.insert(0, archivo)
        leer_archivo(archivo)

    main_frame = tk.Frame(master=root)
    main_frame.pack(padx=8, pady=8)

    archivo_frame = tk.Frame(master=main_frame)
    archivo_frame.pack(padx=8, pady=8)

    archivo_lbl = tk.Label(master=archivo_frame, text='Archivo: ')
    archivo_lbl.grid(column=0, row=0)

    archivo_txt = tk.Entry(master=archivo_frame, width=35)
    archivo_txt.grid(column=1, row=0)

    botones_frame = tk.Frame(master=main_frame)
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