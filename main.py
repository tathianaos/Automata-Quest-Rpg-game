from PySide2.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore
from ui_main import Ui_MainWindow
import sys



sigma, states, transitions, lista = [], [], [], []
states_symbols = set()  
current_room = "EH"


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Automata Quest Game")
		
         #paginas
        inv =[]
        self.pb_instruct.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_instr))
        self.pb_back.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_home))
        self.pb_start.clicked.connect(lambda: self.pages.setCurrentWidget(self.Hall))
        
        def start():    
            file = 'config.in'  # le o nome no arquivo de configuração
            with open(file, "r") as f:
                tag = '#'  # tag recebe valores: "Sigma", "States", ou "Transitions"
                while ls := f.readline():  #atribuimos a linha atual do arquivo a ls e verificamos se não é nula
                    ls = ls.rstrip('\n').split()  # remove '\n' do final da string e separa as palavras com espaços
                    # entre eles
                    if ls[0] == '#':  # se o primeiro elemento da linha for #, é vazio e nao conta
                        continue
                    if ls[0] == 'Sigma:':  # se o primeiro elemento da linha for Sigma:, arualizamos o valor da tag
                        tag = ls[0]
                    elif ls[0] == 'States:':  # ................................ States:, ..........................
                        tag = ls[0]
                    elif ls[0] == 'Transitions:':  #.............................Transitions:, .....................
                        tag = ls[0]
                    elif tag == 'Sigma:':  # se a tag atualfor Sigma, significa que lemos o alfabeto até acharmos a palavra
                        # 'End'; 'End' significa que a parte Sigma está concluida
                        if ls != ['End']:
                            sigm(ls)
                    elif tag == 'States:':  # se tag atual for States, quer dizer q lemos elementos de mais de um estado
                        # ate obtermos a palavra 'End'
                        if ls != ['End']:
                            stat(ls)
                    elif tag == 'Transitions:':  # se tag atual for Transitions, quer dizer q lemos elementos de varios estadpos
                        # transições ate termos a palavra 'End'
                        if ls != ['End']:
                            trans(ls)
            #  depois de obter os dados do arquivo de configuração, verificamos se constitui um afd
            return validacao()

        


        # Funcao pra ler um transicao
        def trans(linha):
            global transitions
            if linha[3] == '-':  # so são aceitas transiçoes que tenham um hifen entre si, do contraio nao sao aceitas pelo programa
                #adicionamos in transitions uma 2-upla consistindo de 2 elementos do tipo 3-upla
                transitions.append(
                    (
                        (linha[0].rstrip(','), linha[1].rstrip(','), linha[2]),  # analisa 1 transicao
                        (linha[4].rstrip(','), linha[5].rstrip(','), linha[6])  # analisa 2 transicao
                    )
                )


                # Funcao pra ler um elemento do alfabeto
        def sigm(linha):
            global sigma
            sigma.append(linha[0])  # pegamos aopenas o primeiro elemento da lista poi um item do alfabeto consiste em uma palavra



        # Funcao pra ler um elemento do alfabeto
        def sigm(linha):
            global sigma
            sigma.append(linha[0])  # pegamos apenas o primeiro elemento da lista poi um item do alfabeto consiste em uma palavra



        # Funcao para ler um elemento do conjunto de estados
        def stat(linha):
            global states
            try:
                states.append((linha[0].rstrip(','), linha[1]))  # se o estado estier marcado como s de inicial ou F de final, adicionamos uma dupla consistindo o nome do estado s ou f
            except IndexError:
                states.append((linha[0].rstrip(','), -1))  # se o estado estiver marcado como s de inicial ou F de final, escrevemos -1 para indicar que nao e estado inicial nem final



        def go(palavra):
            global current_room
            # definimos o estado inicial como q1
            if palavra not in states_symbols:
                # se o elemento nao estiver no alfabeto, ele nao corresponde ao AFD
                input_wrong()
                return False
            for t in transitions:  # passamos por cada transição
                if t[0][0] == current_room and palavra == t[0][1]:  # verifica se o estado da transição é o nosso estado atual, e se o elemento a1 é igual a letra em que estamos na palavra lida
                    # Na transição (q1, a1, s1) → (q2, a2, a3) verificamos se ha s1 na lista
                    if t[0][2] != "epsilon":
                        if t[0][2] not in lista:
                            print("Você não possui o item necessário para entrar.")
                            return False

                    # Na transição (q1, a1, s1) → (q2, a2, a3) excluimos a2 da lista, se existir.
                    if t[1][1] != "epsilon":
                        try:
                            lista.remove(t[1][1])
                        except ValueError:
                            print(f"O elemento {t[1][1]} nao pode ser excluido porque não existe.")

                    if t[1][2] != "epsilon" and t[1][2] not in lista:
                        lista.append(t[1][2]) 
                    current_room = t[1][0] 
                    break
            else:
                print("Você não pode entrar nesta sala.")


        def input_wrong():
            print("erro, entrada invalida.")


        def validacao():
            global sigma, states, transitions, states_symbols
            s_counter = 0  
            for s in states:
                states_symbols.add(s[0])
                if s[1] == 'S':  
                    s_counter += 1
            if s_counter > 1:  
                wrong()
                print("counter")
                return False

            
            for t in transitions:
                if t[0][0] not in states_symbols or t[1][0] not in states_symbols:  
                    wrong()
                    return False
                if t[0][1] not in sigma and t[0][2] not in sigma and t[1][1] not in sigma and t[1][2] not in sigma:
                    
                    wrong()
                    return False
            print("Automato esá correto")
            return True


        def wrong():
            print("Automato esta errado")


        if not start():
            print("Arquivo de configuração não encontrado")
            exit(0)

       


        info = {
            "EH": "A entrada do castelo das ilusões, tem segurança, preciso de um convite para voltar aqui",
            "DR": "Uma grande mesa com um farto banquete sobre ela",
            "K": "Uma cozinha repleta de ingredientes diferenciados",
            "A": "Uma camara cheia de armas e armaduras antigos",
            "T": "Uma sala repleta dos mais variados tesouros",
            "L": "Uma sala repleta de livros, anotações e Artefatos",
            "P": "A despensa do castelo, parecem estar faltando alguns utensilios.",
            "TR": "O trono do Rei. Nenhum sinal dele ou sua coroa.",
            "WS": "Uma sala com varios rtefatos misticos e livros sobre magia, o feiticeiro costuma ficar por aqui.",
            "SE": "A passagem secreta que leva à saida do castelo"
        }

        #objetos nas salas
        objeto_sala = {
            "EH": ["chave"],
            "DR": ["convite", "chapeu"],
            "K": ["colher"],
            "A": ["espada", "coroa"],
            "T": ["moeda_antiga"],
            "L": ["livro_magia"],
            "P": [],
            "TR": [],
            "WS": ["varinha"],
            "SE": []
        }
            
        



        def exibir_mensagem():
            

            if( current_room != "SE"):
            #print("\n[sala] pode ser:  Hall de entrada = EH; Sala de jantar = DR; Cozinha = K; Armaria = A; Sala do tesouro = T, Biblioteca = L, Despensa = P; Sala do trono = TR; Sala do feiticeiro = WS; Saida secreta = SE")
            #print("\n[item] pode ser: chave = chave; convite = convite; chapeu de cozinha = chapeu; colher = colher; espada = espada; coroa = coroa; moeda antiga = moeda; livro de feitiços = livro_magia; varinha = varinha\n")
                dado_lido = janela.lineEdit.text()
                dado_lido = dado_lido.split()
                if dado_lido[0] == "inventario":
                    print(lista)
                elif dado_lido[0] == "ir":
                    go(dado_lido[1])
                    
                elif dado_lido[0] == "ver":
                    print(f"Sala atual:\n{current_room}: {info[current_room]}")
                    print(f"Objeto na sala atual: {objeto_sala[current_room]}")
                    print("Salas adjacentes:")
                    for t in transitions:
                        if t[0][0] == current_room:  
                            print(f"{t[0][1]}: {info[t[0][1]]}")  
                    print()
                elif dado_lido[0] == "pegar":
                    if dado_lido[1] in objeto_sala[current_room]:
                        if dado_lido[1] not in lista:
                            lista.append(dado_lido[1])
                            objeto_sala[current_room].remove(dado_lido[1])  
                        else:
                            print("você ja possui este item.")
                    else:
                        print("O objeto nao esta nesta sala.")
                elif dado_lido[0] == "largar":
                    if dado_lido[1] in lista:
                        lista.remove(dado_lido[1])
                        objeto_sala[current_room].append(dado_lido[1])
                elif dado_lido[0] == "sair":
                    exit(0)
                if current_room == "SE":
                    print("Parabens! Voce saiu do castelo das ilusoes")
                    #break
            print(dado_lido)
            janela.lineEdit.setText("")

        if current_room == "EH":
            self.pages.setCurrentWidget(self.dining_room)

        elif current_room == "DR":
            self.pages.setCurrentWidget(self.dining_room)

        app =QtWidgets.QApplication([])
        janela=uic.loadUi("rpg.ui")
        janela.pushButton.clicked.connect(exibir_mensagem)

        janela.show()
        app.exec()
    
        #appIcons = QIcon()

       

       
        
        #sala jantar
        #self.pb_k.clicked.connect(lambda: self.pages.setCurrentWidget(self.dining_room))
        
        

        #self.pb_k.clicked.connect(lambda: self.pages.setCurrentWidget(self.kitchen))

#sala de armas
        #self.pb_a.clicked.connect(lambda: self.pages.setCurrentWidget(self.saladearmas))
        #self.pb_start.clicked.connect(lambda: self.pages.setCurrentWidget(self.Hall))
        
        #self.pb_lib.clicked.connect(lambda: self.pages.setCurrentWidget(self.biblioteca))
        #self.pb_se.clicked.connect(lambda: self.pages.setCurrentWidget(self.page))
        #self.pb_sm.clicked.connect(lambda: self.pages.setCurrentWidget(self.page))
        #self.pb_sm_2.clicked.connect(lambda: self.pages.setCurrentWidget(self.page))

        #self.pb_tes.clicked.connect(lambda: self.pages.setCurrentWidget(self.treasure_room))
        #self.pb_tes_2.clicked.connect(lambda: self.pages.setCurrentWidget(self.treasure_room))
        #self.pb_h.clicked.connect(lambda: self.pages.setCurrentWidget(self.Hall))
        #self.pb_hall.clicked.connect(lambda: self.pages.setCurrentWidget(self.Hall))
        
        



if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()














    ############################################################################################################




###############################################################################################################

