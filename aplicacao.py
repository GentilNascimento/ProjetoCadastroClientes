from tkinter import *#Importa todos os símbolos (funções, classes, etc.) 
#do módulo tkinter para serem usados no programa.
from frontend import Gui#Importa a classe Gui do módulo frontend
import Backend as core #Importa o módulo Backend e o apelida como core.

app = None  #Esta variável será usada para armazenar uma instância da classe Gui.
selected = None #Essa variável será usada para armazenar a linha selecionada na 
#lista de clientes.

#'def view'obtém todas as linhas da tabela "clientes" usando a função view do 
# módulo core e exibe essas linhas na lista de clientes na interface gráfica 
# (app.listClientes).
def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)
  
#'def search',busca os registros na tabela "clientes" com base nos valores fornecidos 
# nos campos de busca na interface gráfica (app.txtNome, app.txtSobrenome, app.txtEmail,
# app.txtCPF). Em seguida, exibe os resultados na lista de clientes.      
def search_command():
    app.listClientes.delete(0, END)
    
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(),
                       app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)
 
#'def insert',insere um novo registro na tabela "clientes" com base nos valores 
# fornecidos nos campos de entrada na interface gráfica. Após a inserção, 
# chama view_command para atualizar a lista de clientes.       
def insert_command():
    
    core.insert(app.txtNome.get(), app.txtSobrenome.get(),
                app.txtEmail.get(), app.txtCPF.get())
    view_command()

#'def update',atualiza o registro selecionado na tabela "clientes" com base nos
# valores fornecidos nos campos de entrada na interface gráfica. Após a atualização, 
# chama view_command para refletir as alterações na lista de clientes.    
def update_command():
    
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(),
                app.txtEmail.get(), app.txtCPF.get())
    view_command()

#'def del', exclui o registro selecionado da tabela "clientes". Após a exclusão, 
# chama view_command para atualizar a lista de clientes.    
def del_command():
    item_id = selected[0]
    core.delete(item_id)
    view_command()

#'def getSelectedRow', que é chamada quando uma linha é selecionada na lista de 
# clientes. Atualiza a variável selected com os valores da linha selecionada e 
# preenche os campos de entrada (app.entNome, app.entSobrenome, app.entEmail, 
 #app.entCPF) com os valores do registro selecionado.   
def getSelectedRow(event):
    global selected 
    index = app.listClientes.curselection() 
    if index:
        selected = app.listClientes.get(index)
        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])
        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])
        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])
        
#Verifica se o script está sendo executado como o programa principal (não sendo importado como um módulo). Se verdadeiro, cria uma instância da classe Gui e configura os comandos dos botões na interface gráfica para as funções definidas acima.
#A chamada app.mainloop() inicia o loop principal da interface gráfica.
if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
    
    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.mainloop()
    
    
 