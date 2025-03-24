def eh_19(l,n):
     return "A" <= l <= "S" and 1 <= n <= 19

def eh_13(l,n):
     return "A" <= l <= "M" and 1 <= n <= 13 #Cada uma destas tres funções verifica que
                                             # os parametros de uma interseção são adequados
                                             # dependendo das dimensões do territorio

def eh_9(l,n):
     return "A" <= l <= "I" and 1 <= n <= 9

def cria_intersecao(l, n):
    '''Dado dois parametros, verifica se estes podem formar uma interseção do goban e
        se for assim, criam a interseção'''
    if isinstance(l, str) and isinstance(n, int) and \
        (eh_19(l, n) or eh_13(l, n) or eh_9(l, n)):
        return (l, n)  # Retorna o tuplo com os valores já verificados
    else:
        raise ValueError("cria_intersecao: argumentos invalidos")
    
def obtem_col(inter):
      '''Obtem a letra correspondente à coluna à qual a interseção
          pertence '''
      return inter[0] #Obtem o a letra (coluna)

def obtem_lin(inter):
      '''Obtem o numero correspondente à linha da interseção'''
      return inter[1] #Obtem o numero (linha)

def eh_intersecao(inter):
      '''Verifica se um dado parametro é uma interseção do territorio'''
      return isinstance(inter, tuple) and\
                len(inter) == 2 and\
                isinstance(inter[0], str) and isinstance(inter[1], int) and\
                (eh_19(inter[0], inter[1]) or eh_13(inter[0], inter[1]) or eh_9(inter[0], inter[1])) #Verifica se é um tuplo, depois se tem dois elementos e 
                                                               #verifica cada elemento. Esta ordem de operações evita erros.

def intersecoes_iguais(inter1, inter2):
      '''Dados dois parametros, verifica se ambos são inerseçoes e se são iguais'''
      return eh_intersecao(inter1) and eh_intersecao(inter2) and inter2 == inter1 
                  #Esta função so retorna o valor True caso sejam todos os predicados verdadeiros, ou seja, 
                  # são duas interseçóes iguais

def intersecao_para_str(inter):
      '''Transforma uma interseção num argumento em forma de string'''
      return obtem_col(inter) + str(obtem_lin(inter)) #Considera-se o parametro inter como uma interseçao valida

def str_para_intersecao(arg):
      '''Transforma uma string que representa uma interseçao, a
          uma interseção em forma de tuplo'''
      return (arg[0], ) + (int(arg[1:]) ,) #Considera-se arg como um parametro valido

def filtra_adjacente(tup):
     '''Dada uma lista de possiveis interseções adjacentes,
         remove aquelas que não são posiveis'''
     lista = list(tup) #Transforma numa lista de forma a que seja possível
     for i in lista:      #altera-la
          if not eh_intersecao(i): 
               lista.remove(i) #Se não é valida, é removida
     return tuple(lista) #Retorna um tuplo

def sort_linhas(lista):
    '''Esta função ordena uma lista de interseções dum goban'''
    i = 0 #Assumimos a primeira interseção como a minima
    while i != len(lista):
        for b in range(i+1, len(lista)):
            anterior = lista[i]
            seguinte = lista[b]
            if obtem_lin(seguinte) < obtem_lin(anterior) or (obtem_col(seguinte) < obtem_col(anterior) and obtem_lin(seguinte) == obtem_lin(anterior)): #se encontrar uma interseção menor, troca-as
                lista[b], lista[i] = lista[i], lista[b] #Caso seja de uma linha menor, troca. Caso sejam da mesma linha, mas uma coluna menor, troca.
        i += 1 #Já foi encontrada uma interseção como a minima definitiva
    return lista

def ordena_intersecoes(tup):
      '''Esta função ordena um tuplo com interseções de acordo com a ordem de leitura do go'''
      lista = list(tup) #Transforma o tuplo de forma a ser possível a mudança
      return tuple(sort_linhas(lista))

def obtem_intersecoes_adjacentes(inter, l):
     '''Retorna um tuplo com as interseções adjacentes a uma dada, em
         ordem de leitura do tabuleiro go'''
     letra_ord = ord(obtem_col(inter))
     num = obtem_lin(inter) #Estas duas variaveis funcionam para obter as letras e numeros deinterseões adjacentes 
     adjacentes = ((chr(letra_ord+1), num), ) + ((chr(letra_ord-1), num), ) + ((chr(letra_ord), num +1), ) + ((chr(letra_ord), num -1), )
     filtrado = filtra_adjacente(adjacentes) #Filtra o tuplo "adjacentes" deixando só interseções validas
     return ordena_intersecoes(filtrado) #Retorna só as interseções validas
     
class pedra:
     '''Esta classe permite a representação no codigo do objeto, neste caso, a pedra'''
     def __init__(self, cor):
          self.cor = cor #A unica carateristica que associamos à pedra é a sua cor

def cria_pedra_preta():
     '''Cria uma pedra preta'''
     return pedra("X") #Associa a string "X" à classe, de forma a identifica-la como uma pedra preta

def cria_pedra_branca():
     '''Cria uma pedra branca'''
     return pedra("O") #Neste caso, associa a classe a uma pedra branca

def cria_pedra_neutra():
     '''Cria uma pedra neutra'''
     return pedra(".") 
     #Com estes valores do tipo string, é muito mais facil a transformação de pedra para str

def eh_pedra(arg):
     '''Reconhece se um argumento dado é uma pedra ou não'''
     if isinstance(arg, pedra):
          return True            #Utilizamos a classe como se fosse um novo tipo de dados
     if isinstance(arg, str) and arg in (".", "X", "O"): #Caso a pedra a ser avaliada seja a representação
          return True                                    #da mesma num goban da forma listas
     return False

def eh_pedra_branca(arg):
     '''Reconhce se um argumento dado é uma pedra branca'''
     return arg.cor == "O"

def eh_pedra_preta(arg):
     '''Reconhece se um argumento dado é uma pedra preta'''
     return arg.cor == "X"

def pedras_iguais(p1, p2):
     '''Verifica se duas pedras pertencem ao mesmo jogador'''
     return p1.cor == p2.cor #São iguais se as suas cores são iguais

def pedra_para_str(p):
     '''Retorna o valor 'X' para as pedras pretas,
         'O' para as brancas e '.' para as consideradas neutras'''
     return p.cor #Retorna só a cor associada à pedra

def eh_pedra_jogador(p):
     '''Verifica se uma pedra é preta ou branca, isto é, pertence
         a um dos jogadores'''
     return not p.cor == "."

def cria_goban_vazio(n):
    '''Retorna um tuplo de tuplos, que representam as linha horizontais de um goban'''
    if not isinstance(n, int) or\
        n not in (9,13,19): #Caso o argumento não corresponda a um numero valido
        raise ValueError ("cria_goban_vazio: argumento invalido")
    return [["." for _ in range(n)] for _ in range(n)] #Criado com list comprehensions

def transforma_tuplos(ib,ip):
     '''Transforma tudo argumento em tuplos'''
     if not isinstance(ip, tuple):
          ip = (ip, )
     if not isinstance(ib, tuple):
          ib = (ib, )
     return ib, ip

def corresponde_intersecoes_goban(n, ib, ip):
     '''Verifica se as interseções correspondem às dimensões do goban e que as mudanças sejam possiveis'''
     if isinstance(n, int) and n in (9, 13, 19): #Caso as dimensões estejam certas 
        ib, ip = transforma_tuplos(ib, ip) #Transforma interseções unicas em tuplos, permitindo iteração
        if all(isinstance(b, str) for b in ib):
           ib = tuple([str_para_intersecao(c) for c in ib])
        if all(isinstance(d, str) for d in ip):  #Caso as interseções estejam representadas em forma string
           ip = tuple([str_para_intersecao(e) for e in ip])
        for i in ib + ip:
                avaliado = ()
                if not eh_intersecao(i) or\
                   i in avaliado or\
                   not "A" <= obtem_col(i) <= chr(n+64) or\
                   not  1 <= obtem_lin(i) <= n: #Verifica que as interseções pertencem ao goban de n dimensões,
                      return False               # mas também verifica que não existam interseções repetidas
                avaliado = avaliado + (i, )
        return True
     else:
          return False
     
def cria_goban(n, ib, ip):
    '''Cria um goban com as duas interseções identificadas ocupadas por pedras brancas e
        pretas respetivamente'''
    if corresponde_intersecoes_goban(n, ib, ip):
            ib, ip = transforma_tuplos(ib, ip) #Transforma interseções unicas em tuplos, permitindo iteração
            if all(isinstance(b, str) for b in ib):
               ib = tuple([str_para_intersecao(c) for c in ib])
            if all(isinstance(d, str) for d in ip):  #Caso as interseções estejam representadas em forma string
               ip = tuple([str_para_intersecao(e) for e in ip])
            goban = cria_goban_vazio(n)                    
            b, p = cria_pedra_branca(), cria_pedra_preta()
            for intersecao in ib:
                goban[obtem_lin(intersecao)-1][ord(obtem_col(intersecao))-65] = b.cor #Muda a interseção em cada sublista
            for intersecao in ip:
                 goban[obtem_lin(intersecao)-1][ord(obtem_col(intersecao))-65] = p.cor
            return goban
    else:
         raise ValueError("cria_goban: argumentos invalidos")
    
def cria_copia_goban(g):
      '''Cria uma copia de um dado goban'''
      if isinstance(g, list):
        return [cria_copia_goban(i) for i in g] #Recursivamente cria uma copia
      else:
        return g #Quando é uma interseção retorna a interseção

def obtem_ultima_intersecao(g):
    '''Devolve a interseção que corresponde ao canto superior direito'''
    return (chr(len(g)+64), len(g)) #Funciona assumindo que o parametro dado é um goban
                                    # 9x9, 13x13 ou 19x19

def obtem_pedra(g, i):
    '''Retorna a cor da pedra que se encontra na interseção fornecida'''
    linha = obtem_lin(i) - 1
    coluna = ord(obtem_col(i)) - 65
    cor = g[linha][coluna] #retira a string nessa interseção.
    return pedra(cor) #Deve retornar a pedra associada à pedra nesta interseção

def vizinhanca(g, i, avaliado):
    '''Recursivamente, retorna um tuplo contendo todos os elementos de uma cadeia'''
    final2 = ()
    p = obtem_pedra(g, i) #Cor da pedra
    adjacentes = obtem_intersecoes_adjacentes(i, 0)
    for b in adjacentes:
        if "A" <= obtem_col(b) <= chr(len(g) + 64) and 1 <= obtem_lin(b) <= len(g): #Se a interseção corresponde ao territorio
            if p.cor == obtem_pedra(g, b).cor and b not in avaliado:#Se é igual e nao foi avaliada, é adicionada
                avaliado.add(b)
                final2 = final2 + (b, ) + vizinhanca(g, b, avaliado)
    return final2

def obtem_cadeia(g, i):
    '''Retorna a cadeia de pedras da interseção dada. Caso
        não tenha uma pedra, retorna os espaços livres'''
    avaliado = set()
    final = ()
    avaliado.add(i)
    final = final + (i, )
    resto = vizinhanca(g, i, avaliado)
    final = final + resto
    return ordena_intersecoes(final)

def coloca_pedra(g, i, c):
    '''Coloca uma pedra da cor definida na interseção dada'''
    g[obtem_lin(i)-1][ord(obtem_col(i))-65] = c.cor #o parametro c pode só admitir valores "b" e "p"
    return g

def remove_pedra(g, i):
    '''Remove a pedra colocada na interseção dada'''
    g[obtem_lin(i)-1][ord(obtem_col(i))-65] = "." #Torna a pedra de cor numa pedra nula
    return g

def remove_cadeia(g, tup):
    '''Remove as pedras das interseções pertencentes ao tuplo dado'''
    for i in tup:
         remove_pedra(g, i)
    return g
     
def eh_goban(g):
    '''Verifica se um argumento universal dado é um goban'''
    if isinstance(g, list) and\
        (len(g) == 9 or len(g) == 13 or\
        len(g) == 19): #Se é uma lista adequada, como foi definido um goban anteriormente
          for i in g:
            if not isinstance(i, list) or\
               len(i) != len(g): #False caso não seja uma lista de listas ou exista
                 return False    # uma com dimensão diferente
            for b in i:
                 if not eh_pedra(b):
                      return False   #Se um elemento de uma sublista não é uma pedra, retorna falso
          return True  
    return False

def eh_intersecao_valida(g, i):
    '''Verifica se uma interseção dada pertence ao goban dado'''
    return eh_intersecao(i) and\
            "A" <= obtem_col(i) <= chr(len(g)+64) or\
             1 <= obtem_lin(i) <= len(g)        

def gobans_iguais(g1, g2):
     '''Verifica se dois gobans fornecidos são iguais'''
     return eh_goban(g1) and eh_goban(g2) and\
             g1 == g2

def goban_para_str(g):
     '''Transforma o goban numa linha de carateres que representa uma 
         construção bidimensional do goban'''
     tudo = ""
     corpo = ""
     n = 1
     linha_topo = ""
     while n < len(g):
          linha_topo += chr(n + 64) + " " #Adiciona letras à linha do topo até ser do comprimento certo
          n += 1
     linha_topo += chr(n+64)
     for i in range(len(g)):
          linha_corpo = str(i+1).rjust(2)#Do topo para que encaixe com os numeros de dois digitos
          for b in g[i]:
             linha_corpo = linha_corpo + " " + b
          linha_corpo = linha_corpo + " " + str(i+1).rjust(2) + "\n" #Cosntroi cada linha horizontal
          corpo = linha_corpo + corpo                                #E cria uma nova linha para a seguinte
     tudo = "   " + linha_topo + "\n" + corpo + "   " + linha_topo
     return tudo
     
def obtem_territorios(g):
     '''Retorna um tuplo de tuplos, cada subtuplo contendo as interseções
         de cada territorio'''
     avaliados = set()
     territorios = ()
     for i in range(len(g)): #Por cada linha
          for b in range(len(g[0])): #Cada interseção em cada linha
               intersecao = (chr( b + 65), i + 1) #Transforma o valor numa interseção em forma de tuplo
               if intersecao not in avaliados and obtem_pedra(g, intersecao).cor == ".":
                    cadeia = obtem_cadeia(g, intersecao) #Obtem cada grupo de interseções vazias
                    avaliados.update(cadeia)             #que estão aisladas
                    territorios = territorios + (cadeia, )
     return territorios
                         
def filtra_diferentes(g, i):
     '''Esta função obtem as interseções adjacentes a uma dada e
        filtra as adjacentes em base aos criterios da função na qual é chamada'''
     final = ()
     visto = set()
     if obtem_pedra(g, i).cor == ".":
        adjacentes = obtem_intersecoes_adjacentes(i, 0)
        for b in adjacentes:
            if "A" <= obtem_col(b) <= chr(len(g)+64) and\
                  1 <= obtem_lin(b) <= len(g):
                    if b not in visto and obtem_pedra(g, b).cor != ".":
                            final = final + (b, )
                            visto.update(b)
     if obtem_pedra(g, i).cor == "X" or obtem_pedra(g, i).cor == "O":
        adjacentes = obtem_intersecoes_adjacentes(i, 0)
        for b in adjacentes:
                if "A" <= obtem_col(b) <= chr(len(g)+64) and\
                  1 <= obtem_lin(b) <= len(g):
                    if b not in visto and obtem_pedra(g, b).cor == ".":
                        final = final + (b, )
                        visto.update(b)
     return final

def obtem_adjacentes_diferentes(g, t):
     '''Obtem um tuplo ordenado das adjacentes a cada uma do tuplo t, dependendo
          se a interseção está vazia ou tem uma pedra'''
     if type(t[0]) == str:
          t = (t, )#Caso t seja uma unica interseção, permite a iteração
     final = set()
     for i in t:
          final.update(filtra_diferentes(g, i)) #Filtra as adjacentes de cada interseção 
     return ordena_intersecoes(final)             #em t
               
def jogada(g, i ,p):
     '''Coloca uma pedra no tabuleiro e, caso esta jogada elimine todas
         as pedras, efetua a eliminação'''
     avaliado = set() #Evita a avaliação de interseções já visitadas 
     coloca_pedra(g, i, p)
     adjacentes = obtem_intersecoes_adjacentes(i, 0)
     for b in adjacentes:
          if "A" <= obtem_col(b) <= chr(len(g)+64) and\
               1 <= obtem_lin(b) <= len(g) and\
               eh_pedra_jogador(obtem_pedra(g,b)) and\
               obtem_pedra(g, b).cor != p.cor and\
               b not in avaliado: #Caso a interseção tenha uma pedra e esta seja diferente à colocada
                    cadeia = obtem_cadeia(g, b) #Obtem a possivel cadeia dessa pedra
                    liberdades = obtem_adjacentes_diferentes(g, cadeia)
                    if len(liberdades) == 0: #Se não tem liberdades, é removida a cadeia
                         remove_cadeia(g, cadeia)
                    avaliado.update(cadeia)
          avaliado.update(b)
     return g

def obtem_pedras_jogadores(g):
    '''Retorna um tuplo contendo dois inteiros, que representam o
        numero de pedras brancas e pretas no goban, respetivamente'''
    brancas = sum(i.count("O") for i in g) #Por cada linha, contamos as brancas
    pretas = sum(i.count("X") for i in g) #Igual para as pretas
    return (brancas, pretas)

def calcula_pontos(g):
     '''Retorna um tuplo contendo os pontos do jogador branco e do jogador preto
          respetivamente'''
     pretas = obtem_pedras_jogadores(g)[1] 
     brancas = obtem_pedras_jogadores(g)[0] #Começa por calcular o numero de pedras de cada um
     territorios = obtem_territorios(g)
     if len(territorios) >= 2:
          for cada in territorios: #itera cada territorio
               fronteira = obtem_adjacentes_diferentes(g, cada) #E obtem a sua fronteira
               referencia = fronteira[0]
               if all(obtem_pedra(g, x).cor == obtem_pedra(g, referencia).cor for x in fronteira):
                    if obtem_pedra(g, referencia).cor == "X": #Se são todas iguais na fornteira, adiciona as 
                         pretas += len(cada)                  #interseções seja às brancas ou às pretas
                    if obtem_pedra(g, referencia).cor == "O":
                         brancas += len(cada)
     if len(territorios) == 1 and\
          brancas == 0 or pretas == 0:
             if brancas > 0:
                  brancas += len(territorios[0])
             if pretas > 0:
                  pretas += len(territorios[0])
     return (brancas, pretas)

def eh_suicidio(g, i, p):
     '''Verifica se uma jogada é um suicidio'''
     suicidio = False #Assume que não é suicidio
     copia = cria_copia_goban(g)
     jogada(copia, i, p) #Altera a copia do goban
     cadeia = obtem_cadeia(copia, i)
     liberdades = obtem_adjacentes_diferentes(copia, cadeia)
     if liberdades == (): #Se a pedra não tem liberdades e todas as adjacentes são diferentes
          suicidio = True                #(a sua cadeia é ela própria), então é suicidio
     del copia
     return suicidio

def eh_repeticao(g, i, p, l):
     '''Verifica se ocorre uma repetição após uma jogada'''
     repeticao = False #Assumimos a repetição falsa
     copia2 = cria_copia_goban(g)
     jogada(copia2, i, p) #Altera-se a copia
     if gobans_iguais(copia2, l):
          repeticao = True
     del copia2
     return repeticao

def eh_jogada_legal(g, i, p, l):
     '''Verifica se uma jogada na interseção "i" com a pedra "p" é legal ou não'''
     if eh_pedra_jogador(obtem_pedra(g, i)):
          return False #Caso tente colocar uma pedra onde já há uma
     return not eh_suicidio(g, i, p) and not eh_repeticao(g, i, p ,l)
     #Simplesmente retorna True caso não seja suicidio e não seja repetição

def turno_jogador(g, p, l):
     '''Pede um input a um jogador e retorna True caso seja uma jogada valida.
         Se o jogador decidir passar, retorna False'''
     satisfaz = False #Esta vai quebrar o ciclo
     jogou = False #Muda caso o jogador decidir passar
     while satisfaz == False:
          resposta = input(f"Escreva uma intersecao ou 'P' para passar [{p.cor}]:")
          if isinstance(resposta, str) and\
              2 <= len(resposta) <= 3 and\
              eh_intersecao(str_para_intersecao(resposta)) and\
              "A" <= obtem_col(str_para_intersecao(resposta)) <= chr(len(g)+64) and\
              1 <= obtem_lin(str_para_intersecao(resposta)) <= len(g) and\
              eh_jogada_legal(g, str_para_intersecao(resposta), p, l): #Verifica que o input seja vaildo
                 jogada(g, str_para_intersecao(resposta), p) #Realiza a jogada
                 satisfaz = True
                 jogou = True
          if resposta == "P":
               satisfaz = True
     return satisfaz and jogou #Só será True se ambos predicados forem True, isto é,
                               # jogou e deu uma resposta valda

def transforma_pedra(p):
     '''Transforma a cor de uma pedra de forma a permitir turnos durante o jogo'''
     if p.cor == "X":
          return cria_pedra_branca()
     if p.cor == "O":
          return cria_pedra_preta()

def go(n, t1, t2):
     '''Função principal. Permite jogar uma partida de go'''
     if isinstance(n, int) and isinstance(t1, tuple) and isinstance(t2, tuple):
            try:
               eh_goban(cria_goban(n, t1, t2))
            except ValueError as e:
                 if str(e) == "cria_goban: argumentos invalidos":
                    raise ValueError("go: argumentos invalidos")
                 else:
                    raise e
            goban = cria_goban(n, t1, t2)
            passar = 0 #Nenhum jogador tem passado
            n_jogada = 0
            coloca = cria_pedra_preta() #Começa-se com uma pedra preta
            while passar < 2:
                 pontos = calcula_pontos(goban)
                 print(f"Branco (O) tem {pontos[0]} pontos")
                 print(f"Preto (X) tem {pontos[1]} pontos") #Indica os pontos de cada jogador
                 print(goban_para_str(goban))
                 if n_jogada == 0 or n_jogada%2 == 0:
                      goban_antigo = cria_copia_goban(goban) #Durante cada iteração, o goban_anterior vai ser igual
                 jogou = turno_jogador(goban, coloca, goban_antigo) #ao goban da jogada N-2
                 if not jogou:
                      passar += 1 #Se um dos jogadores passou
                 if jogou:
                      passar = 0 #Se algum jogou, a condição volta a ser zero
                 coloca = transforma_pedra(coloca)
                 n_jogada += 1
            print(f"Branco (O) tem {pontos[0]} pontos")
            print(f"Preto (X) tem {pontos[1]} pontos")
            print(goban_para_str(goban))  
            return pontos[0] > pontos[1]
     else:
          raise ValueError("go: argumentos invalidos")
     
go(9, (), ())