def imprimir_matriz(valor):
    for linha in matriz:
        print(" ".join(f"{valor:3}" for valor in linha))
    print()

while True: 
    N = int(input("Digite a ordem da matriz (digite de 0 para encerrar): "))
    if N == 0:
        print("Código Encerrado")
        break
    if 0 <= N <= 100:
        matriz = [[0 for _ in range(N)]for _ in range(N)]
        valor = 1
        for i in range(N):
            for j in range(N):
                matriz[i][j] = valor
                valor += 1 
        imprimir_matriz(matriz)
else:
    print("Número Inválido")