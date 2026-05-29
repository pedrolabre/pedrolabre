import os

def solicitar_lista_numeros():
    """Solicita uma lista de números inteiros e valida a entrada."""
    while True:
        entrada = input("Digite uma lista de números inteiros separados por vírgula: ")
        try:
            numeros = [int(num.strip()) for num in entrada.split(",")]
            return numeros
        except ValueError:
            print("Entrada inválida! Tenha certeza de digitar apenas números inteiros separados por vírgula.")

def salvar_tupla_em_arquivo(tupla, arquivo):
    """Tupla é salva em um arquivo."""
    with open(arquivo, "w") as f:
        f.write(",".join(map(str, tupla)))

def ler_arquivo_e_recuperar_dados(arquivo):
    """Dados do arquivo são lidos e convertidos de volta para uma lista de números."""
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            conteudo = f.read()
            return [int(num) for num in conteudo.split(",")]
    else:
        print("Arquivo não encontrado!")
        return []

def calcular_estatisticas(numeros):
    """Calcula e exibe o maior, menor e a média dos números."""
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)
    print(f"\nEstatísticas dos números:")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Média dos números: {media:.2f}")

# Nome do arquivo para armazenar os números
arquivo = "numeros.txt"

# a) Solicite ao usuário uma lista de números inteiros.
numeros = solicitar_lista_numeros()

# b) Ordene a lista e a converta em uma tupla.
numeros_ordenados = sorted(numeros)
tupla_numeros = tuple(numeros_ordenados)

#c) Armazene a tupla em um arquivo chamado "numeros.txt".
salvar_tupla_em_arquivo(tupla_numeros, arquivo)
print(f"Tupla salva no arquivo '{arquivo}' com sucesso!")

# d) Leia os dados do arquivo e recupere os números.
numeros_recuperados = ler_arquivo_e_recuperar_dados(arquivo)
print(f"Números recuperados do arquivo: {numeros_recuperados}")

#  e) Identifique e exiba os dados:
if numeros_recuperados:
    calcular_estatisticas(numeros_recuperados)
