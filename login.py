from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# cores
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# criando janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# dividindo janela
frameCima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frameCima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frameBaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando frame cima
l_nome = Label(frameCima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frameCima, text='', width=275, anchor=NW, font=('Ivy 25'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

# função para verificar senha
credenciais = ['Vitor', '123456789']

def verificaSenha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo, Admin.')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta, ' + credenciais[0])

        # apagar o que tiver no frame baixo e cima
        for widget in frameBaixo.winfo_children():
            widget.destroy()
        for widget in frameCima.winfo_children():
            widget.destroy()

        novaJanela()
    else:
        messagebox.showwarning('Erro', 'Verifique as credenciais!')

# função após verificação
def novaJanela():
    # configurando frame cima
    l_nome = Label(frameCima, text='Usuário: ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frameCima, text='', width=275, anchor=NW, font=('Ivy 25'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    # configurando frame baixo
    l_nome = Label(frameBaixo, text='Seja bem vindo, ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)

# configurando frame baixo
l_nome = Label(frameBaixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frameBaixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_pass = Label(frameBaixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frameBaixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_confirmar = Button(frameBaixo, command=verificaSenha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)

janela.mainloop()