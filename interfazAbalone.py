import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
from tkinter import StringVar

import pandas as pd 
from pandas import DataFrame
import matplotlib.pyplot as plot
from scipy import stats
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root= tk.Tk()
root.title("Abalone")
root.geometry("700x700")

archivo='abalone.csv'
df=pd.read_csv(archivo)
df.columns=["Sex","Longitud","Diametro","Altura","Peso entero","Peso cascara","Peso viseras","Peso caparazón","Numero de anillos"] 
copia = df.copy()
seleccion = IntVar()
variable1= ""
variable2= ""
textvariable = ""


def mostrarList2():
    listbox2.pack()

def ocultarList2():
    listbox2.pack_forget()
    

def click():
    if (seleccion.get()==4 ):
        mostrarList2()
             
    else:
        ocultarList2()
       

def graficarCon():
    if(seleccion.get()==1):
        
        win1= tk.Tk()
        win1.title("histograma")
        win1.geometry("750x500")
        
        media=np.mean(df[variable1])
        mediana=np.median(df[variable1])
        moda=stats.mode(df[variable1])
        simetria = pd.DataFrame.skew(df[variable1])
        kurtosis = pd.DataFrame.kurtosis(df[variable1])
        

        figure1 = plot.Figure(figsize=(5,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.hist(x=df[variable1])
        scatter1 = FigureCanvasTkAgg(figure1, win1) 
        scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        labelda = tk.Label(win1,text =  media, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=0)
        labelda1 = tk.Label(win1,text =  mediana, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=20)
        labelda2 = tk.Label(win1,text =  moda, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=40)
        labelda3 = tk.Label(win1,text =  simetria, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=60)
        labelda4 = tk.Label(win1,text =  kurtosis, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=80)
        
        win1.mainloop()
        win1.destroy
        

    elif(seleccion.get()==2):
        win4= tk.Tk()
        win4.title("normalizacion")
        win4.geometry("750x500")
        
        media1=np.mean(df[variable1])
        mediana1=np.median(df[variable1])
        moda1=stats.mode(df[variable1])
        simetria1 = pd.DataFrame.skew(df[variable1])
        kurtosis1 = pd.DataFrame.kurtosis(df[variable1])
        
        fig = plot.Figure(figsize=(5,5), dpi=100)
        ax = fig.add_subplot(111)
        res= stats.probplot(df[variable1],dist=stats.norm, plot=ax)
        scatter = FigureCanvasTkAgg(fig, win4) 
        scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        labelda = tk.Label(win4,text =  media1, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=0)
        labelda1 = tk.Label(win4,text =  mediana1, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=20)
        labelda2 = tk.Label(win4,text =  moda1, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=40)
        labelda3 = tk.Label(win4,text =  simetria1, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=60)
        labelda4 = tk.Label(win4,text =  kurtosis1, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=80)

        win4.mainloop()
        win4.destroy
        
        
    elif(seleccion.get()==3):
        win2= tk.Tk()
        win2.title("boxplot")
        win2.geometry("750x500")
        
        
        figure2 = plot.Figure(figsize=(5,5), dpi=100)
        ax2 = figure2.add_subplot(111)
        ax2.boxplot(df[variable1])
        scatter2 = FigureCanvasTkAgg(figure2, win2) 
        scatter2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        media2=np.mean(df[variable1])
        mediana2=np.median(df[variable1])
        moda2=stats.mode(df[variable1])
        simetria2 = pd.DataFrame.skew(df[variable1])
        kurtosis2 = pd.DataFrame.kurtosis(df[variable1])

        labelda = tk.Label(win2,text =  media2, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=0)
        labelda1 = tk.Label(win2,text =  mediana2, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=20)
        labelda2 = tk.Label(win2,text =  moda2, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=40)
        labelda3 = tk.Label(win2,text =  simetria2, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=60)
        labelda4 = tk.Label(win2,text =  kurtosis2, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=80)
        
        win2.mainloop()
        win2.destroy
        
        
    elif(seleccion.get()==4):
        win3= tk.Tk()
        win3.title("dispercion")
        win3.geometry("750x500")
        
        figure3 = plot.Figure(figsize=(5,5), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.scatter((df[variable1]),(df[variable2]))
        scatter3 = FigureCanvasTkAgg(figure3, win3) 
        scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        media3=np.mean(df[variable1])
        mediana3=np.median(df[variable1])
        moda3=stats.mode(df[variable1])
        simetria3 = pd.DataFrame.skew(df[variable1])
        kurtosis3 = pd.DataFrame.kurtosis(df[variable1])

        labelda10 = tk.Label(win3,text =  media3, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=0)
        labelda11 = tk.Label(win3,text =  mediana3, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=20)
        labelda12 = tk.Label(win3,text =  moda3, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=40)
        labelda13 = tk.Label(win3,text =  simetria3, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=60)
        labelda14 = tk.Label(win3,text =  kurtosis3, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=80)
        
        win3.mainloop()
        win3.destroy
        
def graficarSin():
    if(seleccion.get()==1):
        
        Q1= df[variable1].quantile(0.25)
        Q3= df[variable1].quantile(0.75)
        IQR = Q3-Q1
        limiteInferior = Q1 - 1.5 *IQR
        limiteSuperior = Q3 + 1.5 *IQR

        ubicacionSin = (df[variable1]>= limiteInferior) & (df[variable1]<= limiteSuperior)
        Sinatipicos = df[ubicacionSin]
        win1= tk.Tk()
        win1.title("histograma")
        win1.geometry("750x500")
     
        figure1 = plot.Figure(figsize=(5,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.hist(x=Sinatipicos[variable1])
        scatter1 = FigureCanvasTkAgg(figure1, win1) 
        scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        media4=np.mean(df[variable1])
        mediana4=np.median(df[variable1])
        moda4=stats.mode(df[variable1])
        simetria4 = pd.DataFrame.skew(df[variable1])
        kurtosis4 = pd.DataFrame.kurtosis(df[variable1])

        labelda10 = tk.Label(win1,text =  media4, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=0)
        labelda11 = tk.Label(win1,text =  mediana4, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=20)
        labelda12 = tk.Label(win1,text =  moda4, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=40)
        labelda13 = tk.Label(win1,text =  simetria4, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=60)
        labelda14 = tk.Label(win1,text =  kurtosis4, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=80)
      
        win1.mainloop()
        win1.destroy   
        

    elif(seleccion.get()==2):
        Q1= df[variable1].quantile(0.25)
        Q3= df[variable1].quantile(0.75)
        IQR = Q3-Q1
        limiteInferior = Q1 - 1.5 *IQR
        limiteSuperior = Q3 + 1.5 *IQR

        ubicacionSin = (df[variable1]>= limiteInferior) & (df[variable1]<= limiteSuperior)
        Sinatipicos = df[ubicacionSin]
        
        
        win4= tk.Tk()
        win4.title("normalizacion")
        win4.geometry("750x500")
        
        fig = plot.Figure(figsize=(5,5), dpi=100)
        ax = fig.add_subplot(111)
        res= stats.probplot(Sinatipicos[variable1],dist=stats.norm, plot=ax)
        scatter = FigureCanvasTkAgg(fig, win4) 
        scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        media5=np.mean(df[variable1])
        mediana5=np.median(df[variable1])
        moda5=stats.mode(df[variable1])
        simetria5 = pd.DataFrame.skew(df[variable1])
        kurtosis5 = pd.DataFrame.kurtosis(df[variable1])

        labelda10 = tk.Label(win4,text =  media5, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=0)
        labelda11 = tk.Label(win4,text =  mediana5, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=20)
        labelda12 = tk.Label(win4,text =  moda5, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=40)
        labelda13 = tk.Label(win4,text =  simetria5, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=60)
        labelda14 = tk.Label(win4,text =  kurtosis5, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=80)
        
        win4.mainloop()
        win4.destroy
        
        
    elif(seleccion.get()==3):
        Q1= df[variable1].quantile(0.25)
        Q3= df[variable1].quantile(0.75)
        IQR = Q3-Q1
        limiteInferior = Q1 - 1.5 *IQR
        limiteSuperior = Q3 + 1.5 *IQR

        ubicacionSin = (df[variable1]>= limiteInferior) & (df[variable1]<= limiteSuperior)
        Sinatipicos = df[ubicacionSin]
        
        win2= tk.Tk()
        win2.title("boxplot")
        win2.geometry("750x500")
        
        figure2 = plot.Figure(figsize=(5,5), dpi=100)
        ax2 = figure2.add_subplot(111)
        ax2.boxplot(Sinatipicos[variable1])
        scatter2 = FigureCanvasTkAgg(figure2, win2) 
        scatter2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        media6=np.mean(df[variable1])
        mediana6=np.median(df[variable1])
        moda6=stats.mode(df[variable1])
        simetria6 = pd.DataFrame.skew(df[variable1])
        kurtosis6 = pd.DataFrame.kurtosis(df[variable1])

        labelda10 = tk.Label(win2,text =  media6, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=0)
        labelda11 = tk.Label(win2,text =  mediana6, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=20)
        labelda12 = tk.Label(win2,text =  moda6, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=40)
        labelda13 = tk.Label(win2,text =  simetria6, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=60)
        labelda14 = tk.Label(win2,text =  kurtosis6, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=80)
        
        win2.mainloop()
        win2.destroy
        
        
    elif(seleccion.get()==4):
        Q1= df[variable1].quantile(0.25)
        Q3= df[variable1].quantile(0.75)
        IQR = Q3-Q1
        limiteInferior = Q1 - 1.5 *IQR
        limiteSuperior = Q3 + 1.5 *IQR

        ubicacionSin = (df[variable1]>= limiteInferior) & (df[variable1]<= limiteSuperior)
        Sinatipicos = df[ubicacionSin]
        
        win3= tk.Tk()
        win3.title("dispercion")
        win3.geometry("750x500")
        
        figure3 = plot.Figure(figsize=(5,5), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.scatter((Sinatipicos[variable1]),(Sinatipicos[variable2]))
        scatter3 = FigureCanvasTkAgg(figure3, win3) 
        scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        media7=np.mean(df[variable1])
        mediana7=np.median(df[variable1])
        moda7=stats.mode(df[variable1])
        simetria7 = pd.DataFrame.skew(df[variable1])
        kurtosis7 = pd.DataFrame.kurtosis(df[variable1])

        labelda10 = tk.Label(win3,text =  media7, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=0)
        labelda11 = tk.Label(win3,text =  mediana7, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=20)
        labelda12 = tk.Label(win3,text =  moda7, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=40)
        labelda13 = tk.Label(win3,text =  simetria7, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=60)
        labelda14 = tk.Label(win3,text =  kurtosis7, 
                         bg= '#20b4d8',
                         fg ='#2088d8', 
                         height = 1, width=20, font=("Serif",12)).place(x=500, y=80)
        
        win3.mainloop()
        win3.destroy


label = tk.Label(root,text = 'Datos de Abalones', 
                 bg= '#20b4d8',
                 fg ='#2088d8', 
                 height = 1, width=20, font=("Serif",16))

label_n2 = tk.Label(root,text = 'Tipo de grafico', 
                 bg= '#20b4d8',
                 fg ='#2088d8', 
                 height = 1, width=20, font=("Serif",16)).place(x=10, y=50)

label_n3 = tk.Label(root,text = 'Variables de entrada', 
                 bg= '#20b4d8',
                 fg ='#2088d8', 
                 height = 1, width=20, font=("Serif",16)).place(x=10, y=225)

label.pack()

Radiobutton = tk.Radiobutton(root, text='Histograma',value=1, variable=seleccion, command=click).place(x=10, y=85)
Radiobutton_n2= tk.Radiobutton(root, text='Normalización',value=2, variable=seleccion , command=click).place(x=10, y=120)
Radiobutton_n3= tk.Radiobutton(root, text='Boxplot',value=3, variable=seleccion, command=click).place(x=10, y=155)
Radiobutton_n4= tk.Radiobutton(root,text='Disperción',value=4, variable=seleccion, command=click).place(x=10, y=190)



listaDevariables = tk.StringVar()
listbox1 = ttk.Combobox(root,textvariable=listaDevariables,height=6)
listbox1.place(x=10, y=260)
listbox1["values"] = ["Sex","Longitud","Diametro","Altura","Peso entero","Peso cascara","Peso viseras","Peso caparazón","Numero de anillos"]
listbox1["state"] = "readonly"


listaDevariables2 = tk.StringVar()
listbox2 = ttk.Combobox(root,textvariable=listaDevariables2,height=6)
listbox2.place(x=10, y=295)
listbox2["values"] = ["Sex","Longitud","Diametro","Altura","Peso entero","Peso cascara","Peso viseras","Peso caparazón","Numero de anillos"]
listbox2["state"] = "readonly"


Button = tk.Button(root,text = 'Graficar con atipicos',height = 2, width=20, font=("Serif",12), bg= '#20dbd3', fg ='#d8efd4', command=graficarCon).place(x=400, y=85)
Button_n2 = tk.Button(root,text = 'Graficar sin atipicos',height = 2, width=20, font=("Serif",12), bg= '#20dbd3', fg ='#d8efd4', command=graficarSin).place(x=400, y=155)



def VariableSeleccionada1(event):
    global  variable1
    variable1=listbox1.get()
    print(variable1)


def VariableSeleccionada2(event):
    global variable2
    variable2 = listbox2.get()
    print(variable2)

listbox1.bind("<<ComboboxSelected>>",VariableSeleccionada1)
listbox2.bind("<<ComboboxSelected>>",VariableSeleccionada2)

root.mainloop()
root.destroy


    