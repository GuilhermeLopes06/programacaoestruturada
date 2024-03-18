from random import randint
from time import sleep


def main():
    vida_aventureiro = 100
    ataque_aventureiro = randint(10,20)
    defesa_aventureiro = randint(1,5)
    vida_monstro = randint(60,80)
    ataque_monstro = randint(20,30)
    rodada = 1
    print(f"Aventureiro: vida {vida_aventureiro} - att {ataque_aventureiro} - def {defesa_aventureiro}")
    print(f"Monstro: vida {vida_monstro} - att {ataque_monstro}")
    while True:
        print("=-" * 20)
        print(f"Rodada {rodada}" )
        dano_aventureiro = randint(1, ataque_aventureiro)
        dano_monstro = randint(1,ataque_monstro) - defesa_aventureiro
        if dano_monstro < 0:
            dano_monstro = 0
        vida_monstro -= dano_aventureiro
        vida_aventureiro -= dano_monstro
        rodada += 1
        if vida_monstro <= 0:
            print("O monstro morreu!")
            break
        elif vida_aventureiro <= 0:
            print("Você morreu!")
            break
        print(f"Aventureiro: vida {vida_aventureiro} - att {ataque_aventureiro} - def {defesa_aventureiro}")
        print(f"Monstro: vida {vida_monstro} - att {ataque_monstro}")

main()


