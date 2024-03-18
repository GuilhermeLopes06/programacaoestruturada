from random import randint
from time import sleep


def main():
    vida_aventureiro = 100
    ataque_aventureiro = randint(10,20)
    defesa_aventureiro = randint(1,5)
    vida_monstro = randint(60,80)
    ataque_monstro = randint(20,30)
    rodada = 1
    while True:
        print("-=" * 30)
        print(f"Rodada {rodada}" )
        print(f"Aventureiro: vida {vida_aventureiro} - att {ataque_aventureiro} - def {defesa_aventureiro}")
        print(f"Monstro: vida {vida_monstro} - att {ataque_monstro}")
        vida_monstro -= randint(1, ataque_aventureiro)
        vida_aventureiro -= randint(1,ataque_monstro-defesa_aventureiro)
        rodada += 1
        if vida_monstro <= 0:
            print(f"Rodada {rodada}")
            print("O monstro morreu!")
            break 
        elif vida_aventureiro <= 0:
            print(f"Rodada {rodada}")
            print("Você morreu!")
            break

main()

        
