from tkinter import *
import tkinter as tk
from database import *
database = RoomDB()

class TelaDeResumo:
    def quartaTela(cpf,quarto):
        telaQuatro = tk.Tk()
        telaQuatro.geometry("400x400")
        telaQuatro.minsize(300, 300)
        telaQuatro.maxsize(600, 600)
        telaQuatro.title("Resumo")

        rotuloDoTitulo = Label(telaQuatro, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()

        titulo1 = Label(telaQuatro, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        titulo1.pack()
        titulo1.place(x=70,y=30)

        nomep = Label(telaQuatro, text="Nome: "+str(database.select_name(cpf)[0]), font=9)
        nomep.pack()
        nomep.place(x=50,y=100)

        cpfp = Label(telaQuatro, text="CPF: "+str(database.select_CPF(quarto)[0]), font=9)
        cpfp.pack()
        cpfp.place(x=50,y=130)

        quarto = Label(telaQuatro, text="Quarto: "+str(database.select_number(cpf)[0]), font=9)
        quarto.pack()
        quarto.place(x=50, y=160)

        datacheckin = Label(telaQuatro, text="Data de checkin: "+str(database.select_checkin(cpf)[0]), font=9)
        datacheckin.pack()
        datacheckin.place(x=50,y=190)

        datacheckout = Label(telaQuatro, text="Data de checkin: "+str(database.select_checkout(cpf)[0]), font=9)
        datacheckout.pack()
        datacheckout.place(x=50,y=220)

        terminar = Button(telaQuatro, text="Resumo", bg="black", fg="white", width=8, height=2,command=lambda: (UltimaTela.ultimaTela(), telaQuatro.destroy()))
        terminar.pack()
        terminar.place(x=120, y=250)

class UltimaTela:
    def ultimaTela():
        terminar = tk.Tk()
        terminar.geometry("300x300")
        terminar.minsize(300, 300)
        terminar.maxsize(300, 300)
        terminar.title("Resumo")          

        rotuloDoTitulo = Label(terminar, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()

        titulo1 = Label(terminar, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        titulo1.pack()
        titulo1.place(x=70,y=30)

        mensagemFinal = Label(terminar, text="Aproveite a estadia!",font=9)
        mensagemFinal.pack()
        mensagemFinal.place(x=80, y=150)

        acabou = Button(terminar, text="Finalizar", bg="black", fg="white", width=8, height=2, command=terminar.destroy)
        acabou.pack()
        acabou.place(x=120, y=200) 