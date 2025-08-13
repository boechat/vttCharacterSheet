class Personagem:
    def __init__(self, nome, idade, mutacao, nivel):
        self.nome = nome
        self.idade = idade
        self.mutacao = mutacao
        self.nivel = nivel
        self.poderes = []
        self.vida = 100  # Valor inicial
        self.energia = 100  # Valor inicial

    def adicionar_poder(self, poder):
        self.poderes.append(poder)
        print(f"Poder {poder} adicionado a {self.nome}!")

    def mostrar_ficha(self):
        print(f"=== Ficha de {self.nome} ===")
        print(f"Idade: {self.idade}")
        print(f"Mutação: {self.mutacao}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {self.vida}")
        print(f"Energia: {self.energia}")
        print("Poderes:")
        for p in self.poderes:
            print(f" - {p}")
        print("=========================")