import os,dz

def banner():

    os.system('clear')

    print("""\033[1;37m    ###    ##    ## #### ##    ##  ######

   ## ##   ##   ##   ##  ###   ## ##    ##

  ##   ##  ##  ##    ##  ####  ## ##

 ##     ## #####     ##  ## ## ## ##   ####

 ######### ##  ##    ##  ##  #### ##    ##

 ##     ## ##   ##   ##  ##   ### ##    ##

 ##     ## ##    ## #### ##    ##  ######

==========================================

(!) Author  : AKING

(!) FBOOK   : AKING110

(!) Github  : AKING110

(!) Version : 1.9.0

(!) Type    : PAID

(√) \033[1;37mEnjoy Update Now ❤

==========================================""")

def Main():

    banner()

    print('\033[1;32m[√] Welcome To Cloning \033[1;37m')

    print('==========================================')

    print('\033[1;37m[1] Start Cloning\n[2] Dump File\n[0] \033[1;31mExit Programming\033[1;37m')

    print('==========================================')

    i = input('[√] Choose : ')

    if ('1') in i:

        os.system('python Run.py')

    elif ('2') in i:

        dz._login()

    elif ('0') in i:

        exit('[√]\033[1;31m Thanks For Use ')

    else:

        Main()

Main()
