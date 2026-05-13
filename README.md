import random

class Logo:
    def __init__(self):
        self.logo = "Naruto Shippuden"

class PersonagemNaruto(Logo):
    def __init__(self, nome=" ", qi=0, taijutsu=0, ninjutsu=0, genjutsu=0):
        super().__init__()
        self.nome = nome
        self.qi = qi
        self.taijutsu = taijutsu
        self.ninjutsu = ninjutsu
        self.genjutsu = genjutsu

    def exibir(self):
        print(f"== {self.nome} ==")
        print(f"- QI: {self.qi} -")
        print(f"- Taijutsu: {self.taijutsu} -")
        print(f"- Ninjutsu: {self.ninjutsu} -")
        print(f"- Genjutsu: {self.genjutsu} -")
        print(f"- Logo: {self.logo} -")

# Lista das cartas
cartas = [
    PersonagemNaruto("Naruto", 6, 7, 8, 4),
    PersonagemNaruto("Sasuke", 7, 7, 10, 8),
    PersonagemNaruto("Sakura", 8, 6, 6, 7),
    PersonagemNaruto("Tsunade", 10, 10, 10, 7),
    PersonagemNaruto("Kakashi", 10, 9, 10, 8),
    PersonagemNaruto("Itachi", 10, 9, 10, 11),
    PersonagemNaruto("Shikamaru", 10, 4, 7, 6),
    PersonagemNaruto("Gai", 6, 10, 6, 6),
]

print("=" * 50)
print("   | CATÁLOGO DE CARTAS DISPONÍVEIS NO JOGO |    ")
print("=" * 50)

for personagem in cartas:
    personagem.exibir()
    print("-" * 30)

while True:
    entrada = input("\nAperte [ENTER] para iniciar o jogo e distribuir as cartas: ")
    if entrada == "":
        break
    else:
        print("Aperte a tecla ENTER para jogar.")

# Distribuição e Jogo
print("-" * 50)
print(" == DISTRIBUINDO AS CARTAS... ==")
print("-" * 50)

carta_jogador = random.choice(cartas)
carta_maquina = random.choice(cartas)
while carta_maquina == carta_jogador:
    carta_maquina = random.choice(cartas)

print("\n[ SUA CARTA ]")
carta_jogador.exibir()

print("\n-Escolha um atributo:  [1] QI, [2] Taijutsu, [3] Ninjutsu, [4] Genjutsu-")
escolha = input("Atributo: ")

#Verificação de Atributos
if escolha == "1":
    attr = "QI"
    atr_jogador = carta_jogador.qi
    atr_maquina = carta_maquina.qi
elif escolha == "2":
    attr = "Taijutsu"
    atr_jogador = carta_jogador.taijutsu
    atr_maquina = carta_maquina.taijutsu
elif escolha == "3":
    attr = "Ninjutsu"
    atr_jogador = carta_jogador.ninjutsu
    atr_maquina = carta_maquina.ninjutsu
else:
    attr = "Genjutsu"
    atr_jogador = carta_jogador.genjutsu
    atr_maquina = carta_maquina.genjutsu

print(f"\nSeu {attr}: {atr_jogador} | Máquina {attr}: {atr_maquina} ")

print("\n|  CARTA DA MÁQUINA  |")
carta_maquina.exibir()

#Verificação de Vencedor
if atr_jogador > atr_maquina:
    print("\n|  Você Venceu!  |")
elif atr_jogador < atr_maquina:
    print("\n|  Máquina Venceu!  |")
else:
    print("\n|  Empate!  |")

