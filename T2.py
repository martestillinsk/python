#TRABALHO AVALIATIVO DE DECOMPOSIÇÃO DE MATRIZES LU
#ALUNOS: MATHEUS AURELIO E THAINA RIBEIRO
#PROFESSOR: FILIPO NOVO MOR
#DISCIPLINA: PROGRAMAÇÃO C

#Importa a biblioteca random, que dá acesso a todas as funções que ela disponibiliza
import random  

#Define uma função
def decomposicao_lu(n): 
    #Randint é uma função para gerar numeros aleatorios
    #O float faz a conversão para numero decimal(flutuante)
    A = [[float(random.randint(1, 9)) for a in range(n)] for a in range(n)] 

    #Inicializa as Matrizes, populando elas com zero incialmente
    L = [[0.0 for a in range(n)] for a in range(n)]
    U = [[0.0 for a in range(n)] for a in range(n)]

    #Mostra a Matriz "A"
    print("Matriz A:")
    #loops que percorrem todas as linhas e colunas da Matriz "A"
    for i in range(n): 
        for j in range(n):
    #O "7" serve para alinhamento, garantindo que todos os numeros fiquem alinhados à direita
    #".2f"" serve para mostrar 2 casas após a virgula
    #O uso do "end" é para evitar a quebra de linha após a saida de dados e permitir o formato de matriz
            print(f"{A[i][j]:7.2f}", end="  ")
        print()

    #Calculo da Matriz "U"
    #Loop que percorre todas as linhas da matriz "U"
    for k in range(n):    
    #"k" indica que vamos preencher os elementos da diagonal para cima, porque "U" é triangular superior. "
        for j in range(k, n):
            soma = 0.0
    #"s" é um índice auxiliar que anda pelos elementos anteriores, faz multiplicação cruzada de linha de "L" com coluna de "U" e -
    #- ajuda a montar os novos valores de "U".
    #O loop que preenche "U" começa na linha "k" e percorre as colunas para frente (porque "U" é superior).
            for s in range(k):
    #Formula onde ocorre a multiplicação cruzada, em que os resultados do produto são somados e armazenados na variavel "soma"
                soma += L[k][s] * U[s][j]  
    #Neste trecho pegamos a Matriz "A" e diminuimos os elementos que foram multiplicados -
    #- da linha da matriz "L"" e da coluna matriz "U"(multiplicação cruzada)e depois são -
    #- somados e guardados na variavel soma, subtraidos pelos valores de "A" e o resultado final é preenchido na matriz "U"
            U[k][j] = A[k][j] - soma  

    #Define os valores da diagonal principal da matriz ""L" como 1
        L[k][k] = 1.0

    #"k+1" indica que vamos preencher os elementos abaixo da diagonal, porque "L" é triangular inferior.
        for i in range(k + 1, n):
            soma = 0.0
    #"s" é um índice auxiliar que anda pelos elementos anteriores, Faz multiplicação cruzada de linha de L com coluna de U e -
    #- ajuda a montar os novos valores de L.
    #O loop que preenche L começa nas linhas abaixo da diagonal (k + 1 em diante), porque L é triangular inferior.
            for s in range(k):
    #Multiplicação entre a linha da matriz "L" e a coluna da matriz "u", o resultado produto é somado e guardado na variavel soma
                soma += L[i][s] * U[s][k]  

    #Se a diagonal da matriz "U" for diferente de zero pode prosseguir com o calculo 
            if U[k][k] != 0.0:
    #Formula para decomposição da matriz "L"
    #Os "()" dão prioridade no calculo
    #O resultado da expressão é atribuido a "L[i][k]", preenchendo a matriz "L" 
                L[i][k] = (A[i][k] - soma) / U[k][k]
    #Se não é exibido uma mensagem de erro, pois os valores armazenados na diagonal da matriz "U"-
    #- serão utilizados como divisor do calculo, divisão impossivel por zero!
    #Pivô são os elementos que se encontram na diagonal principal da matriz "U"
            else:
                print("Matriz singular ou pivô zero!")
                exit()

    #Retorna os valores calculados
    return L, U  


#Neste trecho é chamada a função, se não chamada a função o codigo não funciona
# Tamanho da matriz (suporta tamanhos maiores se necessario)
n = 3  

# Executa a função de decomposição
L, U = decomposicao_lu(n)

# Mostrar resultado das matrizes L e U 
print("\nMatriz L:")
for i in range(n):
    for j in range(n):
        print(f"{L[i][j]:7.4f}", end="  ")
    print()

print("\nMatriz U:")
for i in range(n):
    for j in range(n):
        print(f"{U[i][j]:7.4f}", end="  ")
    print()
