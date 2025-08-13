from ficha import Personagem
from poderes import POWERS

def escolher_poder():
    print("Escolha um poder:")
    for i, p in enumerate(POWERS, 1):
        print(f"{i}. {p}")
    escolha = int(input("Número do poder: "))
    return POWERS[escolha - 1]

def main():
    print("=== Criação de Personagem Mutante ===")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    mutacao = input("Tipo de mutação: ")
    nivel = int(input("Nível: "))

    personagem = Personagem(nome, idade, mutacao, nivel)

    while True:
        adicionar = input("Deseja adicionar um poder? (s/n) ").lower()
        if adicionar == "s":
            poder = escolher_poder()
            personagem.adicionar_poder(poder)
        else:
            break

    personagem.mostrar_ficha()

if __name__ == "__main__":
    main()