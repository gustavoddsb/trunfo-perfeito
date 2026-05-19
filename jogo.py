import random
import time

from cartas import cartas

# Inicio do Jogo

print("=" * 52)
time.sleep(0.2)

print("| Bem-vindo ao nosso jogo: Super Naruto!           |")

time.sleep(0.2)

print("=" * 52)

time.sleep(0.4)

print("|                                                  |")
print("-" * 52)
print("Aqui estão todas as cartas do nosso jogo:          |")
print("-" * 52)

time.sleep(0.5)

# Exibir todas as cartas
for carta in cartas:

    carta.exibir()

    print("|                                                  |")
    print("=" * 52)

# Embaralhar cartas

print("\n[ Embaralhando as cartas do deck... ]")

time.sleep(1.5)

random.shuffle(cartas)

# Placar de Usuário x CPU

pontos_usuario = 0
pontos_cpu = 0

# Repetir rodadas

while pontos_usuario < 2 and pontos_cpu < 2 and len(cartas) >= 2:
    print("\n" + "-" * 50)
    print(" == NOVA RODADA ==")
    print("-" * 50)

    time.sleep(1)

    # Carta do Usuário

    carta_usuario = cartas.pop()

    carta_usuario.exibir_carta_jogo("USUÁRIO")

    # Escolha de Atributo

    print("\nAtributos disponíveis:")
    print("[1] QI")
    print("[2] Taijutsu")
    print("[3] Ninjutsu")
    print("[4] Genjutsu")

    escolha = ""

    while escolha not in ["1", "2", "3", "4"]:

        escolha = input("\nEscolha o número do atributo para lutar: ").strip()

    # Verificação da escolha do atributo

    if escolha == "1":
        atributo = "QI"
        val_usuario = carta_usuario.get_qi()
    elif escolha == "2":
        atributo = "Taijutsu"
        val_usuario = carta_usuario.get_taijutsu()
    elif escolha == "3":
        atributo = "Ninjutsu"
        val_usuario = carta_usuario.get_ninjutsu()
    else:
        atributo = "Genjutsu"
        val_usuario = carta_usuario.get_genjutsu()

    print("\n[ Revelando carta do oponente... ]")

    time.sleep(1.5)

    # Carta da CPU

    carta_cpu = cartas.pop()

    carta_cpu.exibir_carta_jogo("CPU")

    # Verificação da escolha da CPU

    if escolha == "1":
        val_cpu = carta_cpu.get_qi()
    elif escolha == "2":
        val_cpu = carta_cpu.get_taijutsu()
    elif escolha == "3":
        val_cpu = carta_cpu.get_ninjutsu()
    else:
        val_cpu = carta_cpu.get_genjutsu()

    #v Comparação de atributos

    print("\n[ Analisando combate... ]")

    time.sleep(1.5)

    print("\n" + "=" * 50)

    print(f"CONFRONTO DE {atributo.upper()}")

    print(f"{carta_usuario.get_nome()} ({val_usuario}) VS "f"{carta_cpu.get_nome()} ({val_cpu})")

    print("=" * 50)

    time.sleep(1)

    # Resultado da comparação

    if val_usuario > val_cpu:

        print(f"\n VITÓRIA! "f"{carta_usuario.get_nome()} venceu!")

        pontos_usuario += 1

    elif val_cpu > val_usuario:

        print(f"\n DERROTA! "f"{carta_cpu.get_nome()} venceu!")

        pontos_cpu += 1

    else:

        print("\n EMPATE!")

    # Placar 
    # Placar 

    print("\n" + "-" * 50)

    print(
        f"PLACAR: Usuário {pontos_usuario} "f"x {pontos_cpu} CPU")
    print("-" * 50)

    # Verificar vencedor melhor de 3

    if pontos_usuario == 2 or pontos_cpu == 2:

        break

    # Perguntar se deseja continuar

    continuar = input("\nDeseja jogar outra rodada? (s/n): ").lower().strip()

    if continuar != "s":

        print("\nJogo encerrado pelo usuário!")

        break

    time.sleep(1.5)