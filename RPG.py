import random
import os
import time
import re
#variavel
fisico = 0
#RPG TESTANDO DEF
vida = 100
vida2 = 60
vida3= 200
sp = 30
def jogador():
    print("JOGADOR                      :")
    print(f"Vida: {vida}                    :")
    if vida < 50:
        print ("(vida baixa)😫:")
    return(f"SP: {sp}                       :\n------------------------------")
ataque = 0
dano2 = 0
dado3 = 0
dano3 = 0
dado = 0
dado2 = 0
defesa = 0.85

habilidade=0
contador = 0
contador2 = 0
multi=1
gold1 = random.randint(20,35)
loot = random.randint(1,2)
#habilidades

#ataques normais  com dano definido pelo dado
ataque = 0


#ataques que consomem sp(sem alteração do dado)
fogo = 15
agua = 10
terra = 17
buff = 1.75
cura = 23


#escolha
y=0
x=0
dodge = 0
#monstruário
def goblin_carniceiro():
    print("______________________________\nGOBLIN CARNICEIRO            :")
    if vida2 < 30:
        print("o goblin está com pouca vida👿:")
    return(f"Vida: {vida2}                     :")
def atk_goblin():
    return (f"\no goblin carniceiro o atacou dando lhe uma estocada com sua adaga\n causando {dano2} de dano ")

def hobgoblin():
    print("_________________________________\nHOBGOBLIN SUPREMO               :")
    if vida3 < 100:
        print("o HOBGOBLIN está com pouca vida👿:")
    return(f"Vida: {vida3}                       :")
def atk_hobgoblin():
    return (f"\n HOBGOBLIN lhe atacou usando soco esmagador\n causando {dano3} de dano ")
def proximo():
    print == ("aperte enter para próximo turno(●'◡'●)")
def clear():
    os.system('cls')
resposta= {"murilex","murilo"}
nome2 = 0     
nome = input("digite seu nome:\n")  
nome2 = nome.lower().strip()
if nome2 in resposta:
     print("você é betinha🤣")
     time.sleep(5)
     os.system('cls')
#
#
#
#
#
#tentando cria a primeira batalha
print ("você encontrou um goblin carniceiro")  
print ("batalhar? ")
while True:  
    escolha = input("y-sim x-não")
    escolha = escolha.lower()
    if escolha in ("y","s","si","sim"):
        y = 1
    if escolha in ("x","n","não"):
        print ("preguiçoso")
        break
    else:
        print ("escolha invalida")
    if y == 1 :
        os.system('cls')
        print ("iniciando batalha...")
        time.sleep(3)
        os.system('cls')
        while True:
  
            if contador > 0:
                contador -= 1
                multi = 1.75
            elif contador == 0:
                multi = 1
            dado2 = random.randint (1,3)
            if dado2 == 1:
                dano2 = 10
            if dado2 == 2:
                dano2 = 15
            if dado2 == 3:
                dano2 = 23
            contador2 +=1

            print(goblin_carniceiro(),"\n                             :\n                             :")
            print(jogador(),"\n                       \n                        ")
            if contador2 >= 3:
                print("*goblin:você ainda insiste em me derrotar humano desprezivel?*\n")              
            próximo = input("aperte enter para ir para menu de batalha")
            os.system('cls')
            print ("menu de batalha")
            menuatk = input("1-ataques fisicos(roletar dado)\n2-habilidades\n3-defender(recupera sp)\n")


            if menuatk ==  "1":
                fisico = input("1-espadada\n2-flechada(chance de dodge)")
                if fisico == "1":
                        os.system('cls')
                        print ("rodando dados...")
                        dado = random.randint (1,20)
                        time.sleep(2)
                        print (f"os numeros foram {dado} caro viajante")
                        if dado <= 10:
                            ataque = 8
                            print ("você deu 8 de dano(ataque péssimo)")
                            vida2 = vida2 - ataque*multi
                        if dado > 10 and dado <=20:
                            ataque = random.randint(14,20)
                            vida2 = vida2 - ataque*multi
                            print (f"você deu {ataque} de dano(bom ataque)")
                        if dado > 20:
                            ataque = random.randint(21,27)
                            vida2 = vida2 - ataque*multi
                            print (f"VOCÊ DEU {ataque}DE DANOOO (òtimo ataque)")
                        print (atk_goblin())
                        vida = vida - dano2
                        proximo = input("aperte enter para próximo turno(●'◡'●)")
                        os.system('cls')
                if fisico == "2":
                    dodge = random.randint (0,2)
                    os.system('cls')
                    print ("rodando dados...")
                    dado = random.randint (1,20)
                    time.sleep(2)

                    print (f"o numero do dado foi {dado} caro viajante")
                    if dado <= 10:
                        ataque = 4
                        print ("você deu 4 de dano(ataque péssimo)")
                    vida2 = vida2 - ataque*multi
                    if dado > 10 and dado <=20:
                        ataque = random.randint(7,13)
                        vida2 = vida2 - ataque*multi
                        print (f"você deu {ataque} de dano(bom ataque)")
                    if dado > 20:
                        ataque = random.randint(13,16)
                        vida2 = vida2 - ataque*multi
                        print (f"VOCÊ DEU {ataque}DE DANOOO (òtimo ataque)")
                    if dodge == 0 or dodge == 1:
                        print (atk_goblin())
                        vida = vida - dano2
                    else:
                        print("\nvocê desviou do ataquee,goblin não deu dano")
                    

                    proximo = input("aperte enter para próximo turno(●'◡'●)")
                    os.system('cls')
            if menuatk == "2":
                habilidade = input("escolha sua habilidade\n1-fogo 2-agua 3-terra\n4-buff 5-cura\n")
                os.system('cls')
                
                if habilidade == "4":
                    if sp > 8:
                        contador += 2
                        sp=sp - 8
                        print ("você aumentou seu dano em 75% por 2 turnos\n")
                        print (atk_goblin())
                        vida = vida - dano2
                    
                    elif sp < 8:
                        print("stamina points insulficientes")
                        time.sleep(2)
                        print (atk_goblin())
                        vida = vida - dano2
                        
                    
                if habilidade == "1":
                    if sp >= 5:
                        sp=sp - 5
                        vida2 = vida2 - fogo*multi
                        print (f"voce jogou bola de fogo causando {fogo*multi} de dano(powwww💥♨️🔥)")
                        print (atk_goblin())
                        vida = vida - dano2
                        
                    elif sp < 5:
                        print("stamina points insulficientes")
                        time.sleep(2)
                        print (atk_goblin())
                        vida = vida - dano2
                                        
                if habilidade == "2": 
                    if sp >= 4:   
                        sp = sp - 4
                        vida2 = vida2 - agua*multi
                        print (f"voce jogou rajada de aguaaa causando {agua*multi} de dano(splashhh🫗)")
                        print (atk_goblin())
                        vida = vida - dano2
                    elif sp < 4:
                        print("stamina points insulficientes")
                        time.sleep(2)
                        print (atk_goblin())
                        vida = vida - dano2
                if habilidade == "3":
                    if sp >= 6:
                        sp = sp - 6
                        vida2 = vida2 - terra*multi
                        print (f"voce fez um terremoto causando {terra*multi} de dano (crackkkk!!💥)")
                        print (atk_goblin())
                        vida = vida - dano2
                    elif sp < 6:
                        print ("stamina points insulficientes")
                        time.sleep(2)
                        print (atk_goblin())
                        vida = vida - dano2
                if habilidade == "5":
                    if sp >= 6:
                        print (f"voce se curou ,curando {cura} pontos de vida")
                        vida =vida+cura
                        sp = sp - 6
                    
                    elif sp < 5:
                        print("stamina points insulficientes")
                        time.sleep(2)
                        print (atk_goblin())
                        vida = vida - dano2
                proximo = input("aperte enter para próximo turno(●'◡'●)")
            if menuatk == "3":
                print("voce irá defender parcialmente o próximo ataque ,e recuperar stamina")
                dano2 =dano2 * defesa                        
                print (atk_goblin())
                vida = vida - dano2
                time.sleep (1)
                proximo = input("aperte enter para próximo turno(●'◡'●)")
                os.system('cls')


                sp = sp + 10
            else:
                 print("inválido")


                    

            if vida2 <= 0:
                os.system('cls')
                print ("goblin carniceiro derrotado!")
                time.sleep(0.4)
                print(".")
                
                time.sleep(0.4)
                os.system('cls')
                print("..")
                
                time.sleep(0.4)
                os.system('cls')
                print("...")
                
                time.sleep(0.4)
                os.system('cls')
                print("....")
                time.sleep(0.6)
                os.system('cls')
                print("HAHAHAHAHAHHH seu inferior,estou na minha forma real👹")
                print("=voce irá ver o meu real poder=")
                time.sleep(4)
                break
            elif vida <= 0:
                print ("você foi derrotado! seu lixo")
                break      
    while True:
            print("notificação:\nLVL.Up  aumento de estatísticas\nsp reastaurado")
            sp = 45
            print("a segunda batalha se iniciará!")      
            os.system('cls')
            print ("iniciando batalha...")
            time.sleep(3)
            os.system('cls')
            while True:
                    
                if contador > 0:
                    contador -= 1
                    multi = 1.75
                elif contador == 0:
                    multi = 1
                dado3 = random.randint (1,3)
                if dado3 == 1:
                    dano3 = 20
                if dado3 == 2:
                    dano3 = 25
                if dado3 == 3:
                    dano3 = 32
                contador2 +=1

                print(hobgoblin(),"\n                             :\n                             :")
                print(jogador(),"\n                       \n                        ")
                if contador2 == 3:
                        print("*HobGoblin:estou na minha melhor forma,você irá perder,escória!*\n")
                próximo = input("aperte enter para ir para menu de batalha")
                os.system('cls')
                print ("menu de batalha")
                menuatk = input("1-ataques fisicos(roletar dado)\n2-habilidades\n3-defender(recupera sp)")
    
    
                if menuatk ==  "1":
                    fisico = input("1-slash(espada)\n2-ir para londe e usar arco (chance de dodge)")
                    if fisico == "1":
                            os.system('cls')
                            print ("rodando dados...")
                            dado = random.randint (1,20)
                            time.sleep(2)
                            print (f"o numero do dado foi {dado} caro viajante")
                            if dado <= 10:
                                ataque = 8
                                print ("você deu 8 de dano(ataque péssimo)")
                                vida3 = vida3 - ataque*multi
                            if dado > 10 and dado <=20:
                                ataque = random.randint(15,23)
                                vida3 = vida3 - ataque*multi
                                print (f"você deu {ataque} de dano(bom ataque)")
                            if dado > 20:
                                ataque = random.randint(23,30)
                                vida3 = vida3 - ataque*multi
                                print (f"VOCÊ DEU {ataque}DE DANOOO (òtimo ataque)")
                            print (atk_hobgoblin())
                            vida = vida - dano3
                            proximo = input("aperte enter para próximo turno O_O")
                            os.system('cls')
                    if fisico == "2":
                                        dodge = random.randint (0,2)
                                        os.system('cls')
                                        print ("rodando dados...")
                                        dado = random.randint (1,20)
                                        time.sleep(2)
                    
                                        print (f"o numero do dado foi {dado} caro viajante")
                                        if dado <= 10:
                                            ataque = 10
                                            print (f"você deu {ataque} de dano(ataque péssimo)")
                                        vida2 = vida2 - ataque*multi
                                        if dado > 10 and dado <=20:
                                            ataque = random.randint(12,18)
                                            vida2 = vida2 - ataque*multi
                                            print (f"você deu {ataque} de dano(bom ataque)")
                                        if dado > 20:
                                            ataque = random.randint(18,23)
                                            vida2 = vida2 - ataque*multi
                                            print (f"VOCÊ DEU {ataque}DE DANOOO (òtimo ataque)")
                                        if dodge == 0 or dodge == 1:
                                            print (atk_goblin())
                                            vida = vida - dano2
                                        else:
                                            print("\nvocê desviou do ataquee,goblin não deu dano")
                if menuatk == "2":
                                    habilidade = input("escolha sua habilidade\n1-fogo 2-agua 3-terra\n4-buff 5-cura\n")
                                    os.system('cls')
                                    
                                    if habilidade == "4":
                                        if sp > 8:
                                            contador += 2
                                            sp=sp - 8
                                            print ("você aumentou seu dano em 75% por 2 turnos\n")
                                        
                                        elif sp < 8:
                                            print("stamina points insulficientes")
                                            time.sleep(2)
                                            print (atk_hobgoblin())
                                            vida = vida - dano3
                                            
                                        
                                    if habilidade == "1":
                                        if sp >= 5:
                                            sp=sp - 5
                                            vida3 = vida3 - fogo*multi
                                            print (f"voce jogou bola de fogo causando {fogo*multi} de dano(powwww💥♨️🔥)")
                                            print (atk_hobgoblin())
                                            vida = vida - dano3
                                            
                                        elif sp < 5:
                                            print("stamina points insulficientes")
                                            time.sleep(2)
                                            print (atk_hobgoblin())
                                            vida = vida - dano3
                                                            
                                    if habilidade == "2": 
                                        if sp >= 4:   
                                            sp = sp - 4
                                            vida3 = vida3 - agua*multi
                                            print (f"voce jogou rajada de aguaaa causando {agua*multi} de dano(splashhh🫗)")
                                            print (atk_hobgoblin())
                                            vida = vida - dano3
                                        elif sp < 4:
                                            print("stamina points insulficientes")
                                            time.sleep(2)
                                            print (atk_hobgoblin())
                                            vida = vida - dano3
                                    if habilidade == "3":
                                        if sp >= 6:
                                            sp = sp - 6
                                            vida3 = vida3 - terra*multi
                                            print (f"voce fez um terremoto causando {terra*multi} de dano (crackkkk!!💥)")
                                            print (atk_hobgoblin())
                                            vida = vida - dano3
                                        elif sp < 6:
                                            print ("stamina points insulficientes")
                                            time.sleep(2)
                                            print (atk_hobgoblin())
                                            vida = vida - dano3
                                    if habilidade == "5":
                                        if sp >= 6:
                                            print (f"voce se curou ,curando {cura} pontos de vida")
                                            vida =vida+cura
                                            sp = sp - 6
                                            
                                        elif sp < 5:
                                            print("stamina points insulficientes")
                                            time.sleep(2)
                                            print (atk_hobgoblin())
                                            vida = vida - dano3
                                    proximo = input("aperte enter para próximo turno(●'◡'●)")

                if menuatk == "3":
                        print("voce irá defender o próximo ataque ,e recuperar stamina")

                        sp = sp + 10
                        dano3 = dano3 * defesa
                        print (atk_hobgoblin())
                        vida = vida - dano3
                        time.sleep (1)
                        proximo = input("aperte enter para próximo turno(●'◡'●)")
                        os.system('cls')
                if menuatk != 1 and menuatk != 2 and menuatk != 3:
                    print("inválido")        
                if vida3 <= 0:
                        print(f"goblin caí diante de {nome}")
                        proximo()
                        print("' visualizar sistema sistema adquirido'")
                        print("você conceguiu derrotar goblin carnicêiro evoluido")
                        proximo()
                        os.system('cls')
                        print(f"+20 exp\n+{gold1} gold")
                        if loot == 1:
                            print("você ganhou escudo de bronze")
                            defesa = 0.8
                if vida <= 0:
                        print ("sistema: uma pequena ajuda no tutorial\n _-__--___--\n  +75hp\n--__--__--__")
                        vida = 75
                        proximo = input("aperte enter para próximo turno(●'◡'●)")
                        time.sleep(3)
                        clear


                
                
        
