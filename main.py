# importando tkinter
from tkinter import *
from tkinter import ttk
from turtle import right

# cores
cor1 = "#19191a" #preta
cor2 = "#feffff" #branca
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)


# criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# variável todosValores
todosValores = ''

# criando label
valor_texto = StringVar()

# criando funcao
def entrarValores(event):

    global todosValores

    todosValores = todosValores + str(event)
    
    #passando valor para tela
    valor_texto.set(todosValores)

# função para calcular
def calcular():
    global todosValores
    resultado = eval(todosValores)
    valor_texto.set(str(resultado))
    todosValores = str(resultado)

# função limpar tela
def limparTela():
    global todosValores
    todosValores = ""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# criando botões
b_1 = Button(frame_corpo, command=limparTela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda:entrarValores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda:entrarValores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command=lambda:entrarValores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command=lambda:entrarValores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command=lambda:entrarValores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command=lambda:entrarValores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, command=lambda:entrarValores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command=lambda:entrarValores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command=lambda:entrarValores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command=lambda:entrarValores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command=lambda:entrarValores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command=lambda:entrarValores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command=lambda:entrarValores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command=lambda:entrarValores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command=lambda:entrarValores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command=lambda:entrarValores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()