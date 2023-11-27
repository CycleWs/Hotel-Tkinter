from tkinter import *
import tkinter as tk
from database import *
import tela_resumo
import os
from tkinter import messagebox
import datetime

database = RoomDB()
telaDois = None
Quarto = None

class telasDeQuartos:
    def segundaTela():
        global telaDois
        teladois = tk.Tk()
        telaDois = teladois
        telaDois.geometry("1024x768")
        telaDois.minsize(1024, 768)
        telaDois.maxsize(1920, 1080)
        telaDois.title("Tela de reservas")
        rotuloDoTitulo = Label(telaDois, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()

        titulo1 = Label(telaDois, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        titulo1.pack()
        titulo1.place(x=430,y=30)

        titulo2 = Label(telaDois, text="Quartos:", font=("Quartos", 18))
        titulo2.pack()

        telasDeQuartos.BtnBox("5A", 200, 150)
        telasDeQuartos.BtnBox("5B", 400, 150)
        telasDeQuartos.BtnBox("5C", 600, 150)
        telasDeQuartos.BtnBox("5D", 800, 150)
        telasDeQuartos.BtnBox("4A", 200, 275)
        telasDeQuartos.BtnBox("4B", 400, 275)
        telasDeQuartos.BtnBox("4C", 600, 275)
        telasDeQuartos.BtnBox("4D", 800, 275)
        telasDeQuartos.BtnBox("3A", 200, 400)
        telasDeQuartos.BtnBox("3B", 400, 400)
        telasDeQuartos.BtnBox("3C", 600, 400)
        telasDeQuartos.BtnBox("3D", 800, 400)
        telasDeQuartos.BtnBox("2A", 200, 525)
        telasDeQuartos.BtnBox("2B", 400, 525)
        telasDeQuartos.BtnBox("2C", 600, 525)
        telasDeQuartos.BtnBox("2D", 800, 525)
        telasDeQuartos.BtnBox("1A", 200, 650)
        telasDeQuartos.BtnBox("1B", 400, 650)
        telasDeQuartos.BtnBox("1C", 600, 650)
        telasDeQuartos.BtnBox("1D", 800, 650)
        

        def on_closing():
            print("Window was closed")
            os.remove("dates.txt")
            database.delete_room("none")
            telaDois.destroy()
            
        telaDois.protocol("WM_DELETE_WINDOW",on_closing)

    def checkOccupiedColor(quarto):
        with open('dates.txt', 'r') as f:
            for linha in f.readlines():
                checkin = linha.strip("\n").strip(":")[0:10]
                checkout = linha.strip("\n").strip(":")[11:21]

                if database.select_occupied_for_dates(quarto, checkin, checkout):
                    return "red"
        
        return "green"
        
    def BtnBox(quarto, x, y):
        cor = telasDeQuartos.checkOccupiedColor(quarto)
        if cor == "red":
            btnBox = Button(telaDois, text=quarto, font=(quarto, 25), bg=cor, fg="white", width=5, height=2)
        else:
            btnBox = Button(telaDois, text=quarto, font=(quarto, 25), bg=cor, fg="white", width=5, height=2, command=lambda:Cadastro.cadastro(quarto))
        btnBox.pack()
        btnBox.place(x=x, y=y)


class Cadastro:
    
    
    def cadastro(quarto):
        Quarto = quarto
        def save_data():
            def verify_cpf(cpf,cpf_existente):
                for i in range(len(cpf_existente) - 1):
                    if(cpf == cpf_existente[i][0]):
                        return False
                return True
            valid_cpfs = [10,11,12,21,22,23,32,33,34,43,44,45,54,55,56,65,66,67,76,77,78,89,88]
            nome = nameEntry.get()
            cpf = cpfEntry.get()
            all_cpfs = database.select_all_cpf()
            number = 0
            index = 0
            if(not(verify_cpf(cpf,all_cpfs))):
                messagebox.showerror(title="Error", message="CPF já existente!")
                return
            if(nome == ''):
                messagebox.showerror(title="Error", message="Nome inválido!")
                return
            
            while(index < len(cpf)):
                number += int(cpf[index])
                index += 1
                
            if((number not in valid_cpfs) or (len(cpf) != 11)):
                messagebox.showerror(title="Error", message="CPF inválido!")
                return
            
            with open('dates.txt', 'r') as f:
                for linha in f.readlines():
                    checkin = linha.strip("\n").strip(":")[0:10]
                    checkout = linha.strip("\n").strip(":")[11:21]
            f.close()
            database.update_name(nome, "none")
            database.update_checkin(checkin, "none")
            database.update_checkout(checkout, "none")
            database.update_CPF(cpf, "none")
            database.update_number(Quarto, cpf)
            database.update_occupied(1, cpf)
            telaTres.destroy()
            telaDois.destroy()
            tela_resumo.TelaDeResumo.quartaTela(cpf,quarto)
            os.remove("dates.txt")
            
        telaTres = tk.Tk()
        telaTres.geometry("525x450")
        telaTres.minsize(525, 450)
        telaTres.maxsize(525, 450)
        telaTres.title("Wyden Hotel")
        Font_tuple = ("Writer", 20, "bold")

        rotuloDoTitulo = Label(telaTres, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()
            
        nameLabelRoom = Label(telaTres, text="quarto: "+quarto ,bg="dark blue" ,fg="white")
        nameLabelRoom.pack()
        nameLabelRoom.configure(font=Font_tuple)
        nameLabelRoom.place(x=10, y=30)

        nameLabel = Label(telaTres, text="Nome do hóspede:",font=("Nome do hóspede", 15))
        nameLabel.pack()
        nameLabel.place(x=30, y=100)

        nameEntry = Entry(telaTres, width=22, font=("calibri", 15))
        nameEntry.pack()
        nameEntry.place(x=30, y=140)

        cpfLabel = Label(telaTres, text="CPF do hóspede:",font=("CPF do hóspede:", 15))
        cpfLabel.pack()
        cpfLabel.place(x=30, y=180)
        cpfEntry = Entry(telaTres, width=22, font=("calibri", 15))
        cpfEntry.pack()
        cpfEntry.place(x=30, y=220)
        salvarDados = Button(telaTres, text="Resumo", bg="black", fg="white", width=8, height=2, command=save_data)
        salvarDados.pack()
        salvarDados.place(x=380, y=190)