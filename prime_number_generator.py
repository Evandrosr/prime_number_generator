import tkinter
import math
'''Cria a interface gráfica'''
app = tkinter.Tk()
app.title('Prime Number Generator')
app.geometry('300x70')

primos = [2,3]
def eh_primo(number):
    '''Retorna True caso number seja primo senão False.'''
    if number < 2:
        return False
    for i in primos:
        if number%i == 0:
            return False
        if i > math.sqrt(number):
            primos.append(number)
            return True
    primos.append(number)
    return True


def gerar():
    '''Retorna um gerador de números primos.
    '''
    yield 2
    yield 3
    number = 3
    while True:
        number += 2
        if eh_primo(number):
            yield number

'''inicializa gerador de números primos.'''
primo = gerar()


def gera_primo():
    '''Exibe numero primo e agenda próximo em .5 segundos.'''
    valor.set(next(primo))
    schedule.set(label.after(500,gera_primo))

def iniciar():
    '''Inicia números aleatórios.'''
    if not  schedule.get():
        gera_primo()



def parar():
    '''Para o gerador mas não reinicia o gerador.'''
    label.after_cancel(schedule.get())
    schedule.set('')

def desligar_app():
    '''Para o gerador e desliga o aplicativo.'''
    label.after_cancel(schedule.get())
    app.destroy()


def reset():
    '''Reinicia o gerador de números aleatórios.'''
    global primo
    primo = gerar()
    valor.set(2)

'''Anota o ultimo agendamento de geração de número'''
schedule = tkinter.StringVar()
schedule.set('')
'''Valor a ser exibido em tela'''
valor = tkinter.IntVar()
valor.set(2)
'''Rótulo com valor primo'''
label = tkinter.Label(app, textvariable=valor, font='36')
label.pack(padx=10,pady=10)
'''Botão para iniciar o gerador de números primos'''
botao_inicia = tkinter.Button(app, text='Iniciar', command=iniciar)
botao_inicia.pack(side='left')
'''Botão para parar ao gerador de números primos '''
botao_desliga = tkinter.Button(app, text='Parar', command=parar)
botao_desliga.pack(side='left')
'''Botão para reiniciar o gerador de números primos '''
botao_reset = tkinter.Button(app, text='Reiniciar', command=reset)
botao_reset.pack(side='left')

app.protocol("WM_DELETE_WINDOW", desligar_app)
app.mainloop()
