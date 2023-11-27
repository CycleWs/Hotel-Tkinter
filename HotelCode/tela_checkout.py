import tkinter as tk
from tkinter import *
from database import *
from tkinter import messagebox

database = RoomDB()

class tela_de_checkout:
    def checkout():
        def apagar_hospede():
            def verify_cpf(cpf,cpf_existente):
                for i in range(len(cpf_existente)):
                    if(cpf == cpf_existente[i][0]):
                        return False
                return True
            
            all_cpfs = database.select_all_cpf()
            cpf = cpf_entry.get()
            if(verify_cpf(cpf,all_cpfs)):
                messagebox.showerror(title="Error", message="CPF inexistente!")
                return
            else:
               database.delete_room(cpf)       
            
            checkout_tela.destroy()
            
            
        checkout_tela = tk.Tk()
        checkout_tela.geometry("300x300")
        checkout_tela.minsize(300, 300)
        checkout_tela.maxsize(300, 300)
        checkout_tela.title("Tela inicial")
        rotuloDoTitulocheckout_tela = Label(checkout_tela,text="Checkout",bg="dark blue",fg="white", width=180, height=6)
        rotuloDoTitulocheckout_tela.pack() 
        
        cpf_entry = Entry(checkout_tela, width=11, font=("calibri", 15))
        cpf_entry.pack()
        cpf_entry.place(x=95, y=100)
        deletar_hospede = Button(checkout_tela,text="Checkout", bg="dark blue",fg="white", width=8, height=2,command=lambda: apagar_hospede())
        deletar_hospede.pack()
        deletar_hospede.place(x=120,y=150)
        
        checkout_tela.mainloop()