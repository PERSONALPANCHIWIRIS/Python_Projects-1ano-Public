def eh_territorio(arg):
    '''Retorna o valor lógico de verdade se é um territorio possível (de acordo com as condições do problema), e errado se for o caso contrario'''
    if isinstance(arg, tuple) and\
        1<= len(arg) <= 26 and\
        isinstance(arg[0], tuple):
            for i in arg:
                if type(i) != tuple or \
                    len(i) != len(arg[0]) or len(i) > 99 or not isinstance(i, tuple):
                    return False
                for b in i:
                    if b not in (0,1, 1.0, 0.0):
                        return False 
            return True
    else:
        return False

colunas = {  1 : "A",
             2 : "B",
             3 : "C",
             4 : "D",
             5 : "E",
             6 : "F",
             7 : "G",  #Dicionário definido no ambiente geral de forma a este não ser definido cada vez que seja necessário dentro de cada função
             8 : "H",
             9 : "I",
             10: "J",
             11 : "K",
             12: "L",
             13: "M",
             14: "N",
             15: "O",
             16: "P",
             17: "Q",
             18: "R",
             19: "S",
             20: "T",
             21: "U",
             22: "V",
             23: "W",
             24: "X",
             25: "Y",
             26: "Z"}

def obtem_ultima_intersecao(arg):
    '''Retorna um tuplo correspondente à última interseção de um território, este assumido como possível'''
    tuplo = ()
    tuplo = tuplo + (colunas[len(arg)],) + (len(arg[0]),)
    return tuplo

def eh_intersecao(y):
    '''Verifica se um valor dado corresponde a uma possível interseção'''
    if isinstance(y, tuple) and\
        len(y) == 2 and type(y[0]) == str and len(y[0]) == 1 and "A"<=y[0]<="Z" and type(y[1]) == int and 1 <= y[1] <= 99: #Uma unica letra entre a e z e um numero entre 1 e 99, nessa ordem.
            return True 
    else:
        return False
    
def eh_intersecao_valida(arg, tup): #recebe dois tuplos: o territorio (arg) e a intereçao (tup)
    '''Verifica, dado um territorio, se a interseção dada pertence ao mesmo'''
    if eh_territorio(arg) and eh_intersecao(tup): #Verifica ambos elementos como validos
        verticais = len(arg)
        horizontais = len(arg[0])
        if "A" <= tup[0] <= colunas[verticais] and tup[1] <= horizontais:
            return True
        else:
            return False
    else:
        return False 

def eh_intersecao_livre(arg, tup):
    '''Verifica se uma interseção está livre, isto é, não tem montanhas'''
    if eh_intersecao_valida(arg, tup): #valida, não só que seja o primeiro parametro seja um territorio e o segundo uma interseção, mas também que estes sejam validos
        uni_letra = ord(tup[0]) -65 #Esta variável é igual à ordem da linha para cada letra
        coluna = arg[uni_letra] 
        intersecao_elemento = coluna[tup[1]-1]
        return intersecao_elemento == 0
    else:
        return False
    
def eh_canto(arg, tup): #Verifica se a interseção é algum dos cantos do territorio
    return tup[0] == "A" and tup[1] == len(arg[0]) or tup[0] == "A" and tup[1] == 1 or (ord(tup[0]) -64) == len(arg) and tup[1] == len(arg[0]) or (ord(tup[0]) -64) == len(arg) and tup[1] == 1
    
def adjacentes_fronteira(arg, tup):
    tuplo = ()
    '''Retorna as interceções adjacentes das que estão nos limites'''
    if eh_canto(arg, tup):
        if tup[0] == "A" and tup[1] == len(arg[0]): # superior esquerda
            adjacentes = ((tup[0], tup[1]-1), (chr(ord(tup[0])+1), tup[1]))
        if tup[0] == "A" and tup[1] == 1: # inferior esquerda
            adjacentes = ((chr(ord(tup[0])+1), tup[1]), (tup[0], tup[1]+1))
        if (ord(tup[0]) -64) == len(arg) and tup[1] == len(arg[0]): #superior direita
            adjacentes = ((tup[0], tup[1]-1), (chr(ord(tup[0])-1), tup[1]))
        if (ord(tup[0]) -64) == len(arg) and tup[1] == 1:#inferior direita
            adjacentes = ((chr(ord(tup[0])-1), tup[1]), (tup[0], tup[1]+1))
    else:
        if tup[0] == "A":
            adjacentes = ((tup[0], tup[1]-1), (chr(ord(tup[0])+1), tup[1]), (tup[0], tup[1]+1)) #linha vertical esquerda
        if ord(tup[0]) -64 == len(arg):
            adjacentes = ((tup[0], tup[1]-1), (chr(ord(tup[0])-1), tup[1]) ,(tup[0], tup[1]+1)) #linha vertical direita
        if tup[1] == 1:
            adjacentes = ((chr(ord(tup[0])-1), tup[1]), (chr(ord(tup[0])+1), tup[1]), (tup[0], tup[1]+1)) #linha horizontal inferior
        if tup[1] == len(arg[0]):
            adjacentes = ((tup[0], tup[1]-1), (chr(ord(tup[0])-1), tup[1]), (chr(ord(tup[0])+1), tup[1])) #linha horizontal superior
    for i in adjacentes:
        if eh_intersecao_valida(arg, i): #Verifica se as interseções geradas pertencem ao territorio
            tuplo = tuplo + (i, )
    return tuplo

def obtem_intersecoes_adjacentes(arg, tup):
    '''Retorna as coordenadas das 4 interseções adjacentes à indicada, caso esta seja valida'''
    if eh_intersecao_valida(arg, tup):
        if tup[0] == "A" or (ord(tup[0]) -64) == len(arg) or tup[1] == 1 or tup[1] == len(arg[0]):
           return adjacentes_fronteira(arg, tup) # Caso a interseção fornecida pertença aos limites do territorio
        else:
            return ((tup[0], tup[1]-1), (chr(ord(tup[0])-1), tup[1]), (chr(ord(tup[0])+1), tup[1]), (tup[0], tup[1]+1)) #retorna as 4 interseçoes adjacentes
    else:
        return False #Se não é uma interseçao valida (como verificado na condição) gera o valor lógico False dado que os parametros não respeitam todas ou algumas das anteriores funções

def sort_colunas(lista):
    i = 0 # Assume o primeiro tuplo como o minimo
    while i != len(lista):
        for b in range(i+1, len(lista)):
            anterior = lista[i]
            seguinte = lista[b]
            if seguinte[1] < anterior[1]: # se encontrar um tuplo menor, troca-os
                lista[b], lista[i] = lista[i], lista[b]
        i += 1 #Caso não encontrar um tuplo menor, este é identificado como o menor de todos
        # A lista se encontra organizada de menor a maior em termos de linha. Falta para as colunas.
    i = 0
    while i != len(lista):
        for b in range(i+1, len(lista)):
            anterior = lista[i]
            seguinte = lista[b]
            if seguinte[0] < anterior[0] and seguinte[1]==anterior[1]: # se encontrar um tuplo menor em coluna, troca-os
                lista[b], lista[i] = lista[i], lista[b]
        i += 1
    return lista

def ordena_intersecoes(tup):
    '''Ordena as interseçoes fornecidas pelo utilizador em ordem crescente, assumindo que o parametro é um tuplo de tuplos'''
    lista = list(tup)
    return tuple(sort_colunas(lista))

def construcao_corpo(arg):
    l = 0 # numero de linhas já estruturadas
    ind_linha = len(arg[0]) 
    corpo = ""
    while l < len(arg[0]):
            corpo = corpo + str(ind_linha) + " "
            for i in arg:
                    if i[ind_linha -1] == 0: # Procura o ultimo elemento de cada tuplo
                       corpo = corpo + ". "
                    if i[ind_linha -1] == 1:
                       corpo = corpo + "X "
            if ind_linha > 9:
                if ind_linha == 10:
                    corpo = corpo + str(ind_linha)
                    corpo = corpo + "\n "
                else:
                    corpo = corpo + str(ind_linha)
                    corpo = corpo + "\n"
            else:     #Esta condição permite que os elementos estejam organizados considerando os dois carateres dos números de dois digitos
                corpo = corpo + " " + str(ind_linha)
                corpo = corpo + "\n "
            l += 1 # Uma linha estruturada
            ind_linha += -1
    return corpo
    
def construcao_linha_topo(arg):
    linha_topo = ""
    for i in range(1, len(arg)+1):
        linha_topo = linha_topo + colunas[i] + " " # Cria a string para a linha de letras
    linha_topo.rstrip() # Remove o espaço branco que sobra
    return linha_topo

def territorio_para_str(arg):
    '''Transforma o territorio numa string que pode ser executada pela função print'''
    if eh_territorio(arg):
        final = ""
        linha_topo = construcao_linha_topo(arg)
        corpo = construcao_corpo(arg)
        if len(arg[0]) > 9:
            final = final + "   " + linha_topo.rstrip() + "\n" + corpo +"  "+ linha_topo.rstrip()
        else:
            final = final + "   " + linha_topo.rstrip() + "\n " + corpo +"  "+ linha_topo.rstrip() # Caso sejam 9 ou menos linhas, antes do "corpo" é preciso um espaço de forma a que fique organizado
        return final
    else:
        raise ValueError('territorio_para_str: argumento invalido')
    
def pertence_cadeia(arg, tup):
     # caso uma interseção adjacente pertença à cadeia, considera-a como tal
    montanha = False #Caso a interseção seja uma montanha, irá mudar.
    if isinstance(tup[0], str):
        ind_coluna = ord(tup[0]) - 65
        if ind_coluna >= 0 and ind_coluna < len(arg) and tup[1] > 0 and tup[1] <= len(arg[0]):
            coluna = arg[ind_coluna]
            intersecao = coluna[tup[1] - 1]
            if intersecao == 1:
                montanha = True
    return montanha

def vizinhanca(arg, tup , avaliado):
    tuplo_2 = ()
    eh_montanha = pertence_cadeia(arg, tup)
    adjacentes = obtem_intersecoes_adjacentes(arg, tup)
    for i in adjacentes:
        if eh_montanha == pertence_cadeia(arg, i) and i not in avaliado:
            avaliado.add(i)  # Adiciona a interseção atual às já visitadas
            tuplo_2 = tuplo_2 + (i, )
            tuplo_2 = tuplo_2 + vizinhanca(arg, i, avaliado)
    return tuplo_2

def obtem_cadeia(arg, tup):
    avaliado = set()
    '''Dada uma interseção, retorna, organizadamente, as interseções da cadeia da mesma'''
    if eh_intersecao_valida(arg, tup):
        tuplo = () # tuplo final com tudo organizado.
        tuplo = tuplo + (tup, )
        avaliado.add(tup)
        restantes =  vizinhanca(arg, tup, avaliado)
        tuplo = tuplo + restantes
        return ordena_intersecoes(tuplo)
    else:
        raise ValueError ("obtem_cadeia: argumentos invalidos")

def obtem_vale(arg, tup):
    '''Retorna um tuplo que contem todos os vales do territorio'''
    avaliado = set()
    if eh_intersecao_valida(arg, tup) and\
     pertence_cadeia(arg, tup): #Se o tuplo é uma montanha
        cadeia_de_montanhas = obtem_cadeia(arg, tup)
        for i in cadeia_de_montanhas: #Por cada montanha na cadeia
            adjacentes = obtem_intersecoes_adjacentes(arg, i)
            for b in adjacentes: 
                if not pertence_cadeia(arg, b) and b not in avaliado: # Avalia cada interseção adjacente e, se for um vale, adiciona-o ao tuplo resultado e considera-o com já avaliado
                    avaliado.add(b)
        return ordena_intersecoes(avaliado)
    else:
        raise ValueError("obtem_vale: argumentos invalidos")

def verifica_conexao(arg, tup1, tup2):
    '''Verifica se dois argumentos, duas interseções dadas, pertencem à mesma cadeia, seja de montanhas ou vazia'''
    if eh_intersecao_valida(arg, tup1) and eh_intersecao_valida(arg, tup2):
        cadeia = obtem_cadeia(arg, tup1)
        return tup2 in cadeia
    else:
        raise ValueError("verifica_conexao: argumentos invalidos")
    
def calcula_numero_montanhas(arg):
    '''Retorna o numero de montanhas num dado territorio'''
    if eh_territorio(arg):
        soma = 0 #Numero total de montanhas
        for i in arg:
             montanhas = i.count(1) #Por cada coluna, conta o numero de montanhas nesta
             soma += montanhas 
        return soma
    else:
        raise ValueError("calcula_numero_montanhas: argumento invalido")

def calcula_numero_cadeias_montanhas(arg):
    '''Calcula o numero de cadeia de montanhas que há no territorio'''
    if eh_territorio(arg):
        n_cadeias = 0
        ja_visto = set()  # Usar um conjunto para armazenar as interseções já vistas
        for i in range(len(arg)):
            for j in range(len(arg[0])):
                if arg[i][j] == 1:  # Se é uma montanha
                    intersecao = (colunas[i + 1], j + 1)
                    if intersecao not in ja_visto:
                        cadeia = obtem_cadeia(arg, intersecao)
                        ja_visto.update(cadeia)  # Atualiza o conjunto com a cadeia
                        n_cadeias += 1
        return n_cadeias
    else:
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")

def calcula_tamanho_vales(arg):
    '''Retorna o numero total de vales no territorio'''
    if not eh_territorio(arg):
        raise ValueError("calcula_tamanho_vales: argumento invalido")
    vales_vistos = set()
    for i in range(len(arg)):
        for b in range(len(arg[0])):
            if arg[i][b] == 1: #Se é uma montanha, irá chamar a função de obter os vales
                intersecao = (colunas[i + 1], b + 1)
                if intersecao not in vales_vistos:
                    vales = obtem_vale(arg, intersecao) #Se é um espaço vazio, avalia se é um vale
                    vales_vistos.update(vales)
    return len(vales_vistos) #O numero de todos os vales já avaliados
