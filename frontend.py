from tkinter import * #Importa todos os símbolos (funções, classes, etc.)
#do módulo tkinter para serem usados no programa.

class Gui ():##Classe q chama a Interface Gráfica 'Gui'
    x_pad = 5   #Atributos de classe, como as margens x_pad e y_pad, 
    y_pad = 3   #largura da entrada width_entry, e uma instância da janela (window)
    width_entry = 30  #criada usando o Tk().                                  
    window = Tk()
    window.wm_title("PYSQL versão 1.0")
        
    #variáveis de controle,ref a entrada(Entry) rastrea e manipula os 
    # dados inseridos pelo user.
    
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()
    #'Label' rótulo para exibir
    lblnome = Label (window, text="Nome")
    lblsobrenome = Label (window, text="Sobrenome")
    lblemail = Label (window, text="Email")
    lblcpf = Label (window, text="CPF")
    #'Entry' campo entrada p user digitar
    entNome = Entry (window, textvariable=txtNome, width=width_entry)
    entSobrenome =Entry (window, textvariable=txtSobrenome, width=width_entry)
    entEmail = Entry (window, textvariable=txtEmail, width=width_entry)
    entCPF = Entry (window, textvariable=txtCPF, width=width_entry)
    #Caixa de lista para exibir informações sobre os clientes
    listClientes = Listbox (window, width=100)
    # Barra de rolagem associada à caixa de lista para rolar entre os itens.
    scrollClientes = Scrollbar (window)
    # Botão para visualizar todos os clientes.
    btnViewAll = Button (window, text="Ver todos")
    #Botão para buscar informações de um cliente específico.
    btnBuscar =Button (window, text="Buscar")
    # Botão para inserir um novo cliente.
    btnInserir = Button (window, text="Inserir")
    #Botão para atualizar as informações de um cliente.
    btnUpdate = Button (window, text="Atualizar Selecionados")
    #Botão para excluir um cliente.
    btnDel = Button (window, text="Deletar selecionados")
    #Botão para fechar a aplicação.
    btnClose = Button (window, text="Fechar")
    
    #Agora vamos associar os objetos criados ao Grid da Janela
    #posiciona os widgets na interface.
    lblnome.grid (row=0, column=0) #linhas/colunas das label
    lblsobrenome.grid (row=1, column=0)
    lblemail.grid (row=2, column=0)
    lblcpf.grid (row=3, column=0)
    #posição das entradas(Entry) no grid, cada entrada 
    #está associada a um campo específico. padx e pady 
    #espaçamento horizontal e vertical.  
    entNome.grid (row=0, column=1, padx=50, pady=50)
    entSobrenome.grid (row=1, column=1)
    entEmail.grid (row=2, column=1)
    entCPF.grid (row=3, column=1)
    #Aqui, está sendo configurada a posição e o número de linhas ocupadas pela 
    # lista (ListBox) no grid. 'rowspan' define quantas linhas a ListBox deve 
    # ocupar verticalmente.   
    listClientes.grid (row=0, column=2, rowspan=10)
    #Semelhante à lista, esta linha configura a posição e o número de linhas 
    # ocupadas pela barra de rolagem vertical associada à ListBox.
    scrollClientes.grid (row=0, column=6, rowspan=10)
    #posição dos botões no grid, cada um ocupando duas colunas. 'columnspan'
    # indica quantas colunas o widget deve se estender.    
    btnViewAll.grid (row=4, column=0, columnspan=2)
    btnBuscar.grid (row=5, column=0, columnspan=2)
    btnInserir.grid (row=6, column=0, columnspan=2)
    btnUpdate.grid (row=7, column=0, columnspan=2)
    btnDel.grid (row=8, column=0, columnspan=2)
    btnClose.grid (row=9, column=0, columnspan=2) 
                

    #União do Scrollbar com a Listbox, barra de rolagem,
    #com caixa listagem
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    # aparência da interface,Utiliza o método winfo_children() para obter uma
    # lista dos widgets filhos da janela principal.
    #Inicia um loop for para iterar sobre cada widget filho.
    for child in window.winfo_children ():
    #Usa __class__.__name__ para obter o nome da classe do widget filho.
    #Armazena esse nome na variável widget_class.
        widget_class = child.__class__.__name__
    #Se o widget filho for um botão, configura a grade (grid) do botão com 
    # espaçamento interno (padx e pady) e define a opção sticky como 'WE' 
    # (o botão se estende nas direções horizontal - West e East).
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
    #Se o widget filho for uma lista, configura a grade da lista com espaçamento 
    # interno zero (padx=0, pady=0) e define a opção sticky como 'NS' (a lista se
    # estende nas direções vertical - North e South).            
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
    #Se o widget filho for uma barra de rolagem, configura a grade da barra de 
    # rolagem com espaçamento interno zero (padx=0, pady=0) e define a opção 
    # sticky como 'NS' (a barra de rolagem se estende nas direções 
    # vertical - North e South).           
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
    #Para qualquer outro widget que não seja botão, lista ou barra de rolagem, 
    # configura a grade com espaçamento interno (padx e pady) e define a opção 
    # sticky como 'N' (o widget não se estende em nenhuma direção).
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
            

            
    #inicia o loop principal da interface gráfica.           
    def mainloop(self):
        self.window.mainloop()  
        
    def run(self):
        self.window.mainloop()
        
    #Cria uma instância da classe Gui e inicia o loop principal da interface gráfica.            
if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()       
          
            
        
 