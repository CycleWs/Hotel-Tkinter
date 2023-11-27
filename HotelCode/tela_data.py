import tkinter as tk
import tela_quartos
from tkinter import *
from database import *
from tkcalendar import DateEntry
from datetime import datetime 
database = RoomDB()

class telasDeData:
    def primeiraTela(): 
        def saveDates():
            with open('dates.txt', 'a') as f:
                checkin1 = checkin_date.get_date()
                checkout1 = checkout_date.get_date()
                if(checkin1 > checkout1):
                    return
                else:
                    f.write("{}:{}".format(checkin1,checkout1))
                    f.close()
                    telaUm.destroy()
                    database.insert_room(NONE,NONE,NONE,NONE,NONE,0)
                    tela_quartos.telasDeQuartos.segundaTela()
                
        telaUm = tk.Tk()
        telaUm.geometry("300x300")
        telaUm.minsize(300, 300)
        telaUm.maxsize(300, 300)
        telaUm.title("Check-In e Check-Out")
        rotuloDoTituloTelaUm = Label(telaUm, bg="dark blue", width=180, height=6)
        rotuloDoTituloTelaUm.pack()

        tituloTelaUm1 = Label(telaUm, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        tituloTelaUm1.pack()
        tituloTelaUm1.place(x=70, y=30)

        tituloTelaUm2 = Label(telaUm, text="Datas:", font=("Datas", 18))
        tituloTelaUm2.pack()

        LabelTelaUm1 = tk.Label(telaUm, text="Data Check-in:")
        LabelTelaUm1.pack()
        LabelTelaUm1.place(x=100,y=130)

        checkin_date = DateEntry(telaUm, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1),
                                  maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)
        checkin_date.pack(padx=10, pady=10)
        checkin_date.place(x=100,y=150)

        LabelTelaUm2 = tk.Label(telaUm, text="Data Check-out:")
        LabelTelaUm2.pack()
        LabelTelaUm2.place(x=100,y=180)

        checkout_date = DateEntry(telaUm, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1),
                                   maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)
        checkout_date.pack(padx=10, pady=10)
        checkout_date.place(x=100,y=200)

        continuar = Button(telaUm,text="Salvar Datas", bg="dark blue",fg="white", width=8, height=2,command=saveDates)
        continuar.pack()
        continuar.place(x=120,y=250)