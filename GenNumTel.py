from random import randint
import ctypes
from time import sleep
from colorama import Fore, Back, Style, init

init()

ctypes.windll.kernel32.SetConsoleTitleW("Générateur numéro de téléphone By DRAIX and Freeze")

print(Fore.YELLOW + """
                                ██████╗░██████╗░░█████╗░██╗██╗░░██╗
                                ██╔══██╗██╔══██╗██╔══██╗██║╚██╗██╔╝
                                ██║░░██║██████╔╝███████║██║░╚███╔╝░
                                ██║░░██║██╔══██╗██╔══██║██║░██╔██╗░
                                ██████╔╝██║░░██║██║░░██║██║██╔╝╚██╗
                                ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝ Générateur By DRAIX and Freeze\n""")

demande =int(input("combien voulez vous en génerer ? "))

for i in range(0,demande):
    random1 = randint(0, 9)

    random2 = randint(0, 9)

    random3 = randint(0, 9)

    random4 = randint(0, 9)

    random5 = randint(0, 9)

    random6 = randint(0, 9)

    random7 = randint(0, 9)

    random8 = randint(0, 9)

    num = "+336" + str(random1) + str(random2) + str(random3) + str(random4) + str(random5) + str(random6) + str(
        random7) + str(random8)

    print(num)


    fichier = open('list.txt', 'a')
    fichier.write(str(num)+"\n")
    fichier.close()


    sleep(0.0000000001)
    
