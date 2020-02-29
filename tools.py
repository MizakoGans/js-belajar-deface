import os
import sys
import time
import termcolor
from os import system
from sys import stdout
from sys import exit
from termcolor import colored
from termcolor import cprint
from time import sleep

def logo():
    os.system('clear')
    banner = colored('''
──────────────────────────────────────────
╔╦╗┌─┐┌─┐┌─┐┌─┐┌─┐  ╔═╗┬─┐┌─┐┌─┐┌┬┐┌─┐┬─┐
 ║║├┤ ├┤ ├─┤│  ├┤   ║  ├┬┘├┤ ├─┤ │ │ │├┬┘
═╩╝└─┘└  ┴ ┴└─┘└─┘  ╚═╝┴└─└─┘┴ ┴ ┴ └─┘┴└─
──────────────────────────────────────────
Author  : Mizako Gans

Team    : GRAY SCHOOL CYBER

Github  : https://github.com/mizz

Pesan   : Ini adalah tools untuk membuat
          script deface secara praktis
          terimakasih sudah menggunakan
          tools ini
──────────────────────────────────────────

''', 'green', attrs=['bold'])
    for char in banner:
        sleep(0.001)
        stdout.write(char)
        stdout.flush()

def conti():
    input(colored('Tekan Enter Untuk Melanjutkan', 'green', attrs=['bold', 'blink']))
    sleep(2)
    system('clear')

def logo2():
    sleep(2)
    banner2 = colored('''
──────────────────────────────────────────''', 'yellow', attrs=['bold'])
    bannerlogo = colored('''
╔╦╗┌─┐┌─┐┌─┐┌─┐┌─┐  ╔═╗┬─┐┌─┐┌─┐┌┬┐┌─┐┬─┐
 ║║├┤ ├┤ ├─┤│  ├┤   ║  ├┬┘├┤ ├─┤ │ │ │├┬┘
═╩╝└─┘└  ┴ ┴└─┘└─┘  ╚═╝┴└─└─┘┴ ┴ ┴ └─┘┴└─''', 'white', attrs=['bold', 'blink'])
    banner3 = colored('''
──────────────────────────────────────────
    
''', 'yellow', attrs=['bold'])

    for char2 in banner2:
        sleep(0.01)
        stdout.write(char2)
    for char3 in bannerlogo:
        sleep(0.01)
        stdout.write(char3)
        stdout.flush()
    for char4 in banner3:
        sleep(0.01)
        stdout.write(char4)


def tools():
    title = input(colored('''┌─[root]─[~Masukan Title Script]
└──╼ # ''', 'red', attrs=['bold']))
    print('')
    nick = input(colored('''┌─[root]─[~Masukan Nick Lo]
└──╼ # ''', 'red', attrs=['bold']))
    print('')
    logo = input(colored('''┌─[root]─[~Masukan Link Logo]
└──╼ # ''', 'red', attrs=['bold']))
    print('')
    team = input(colored('''┌─[root]─[~Masukan Nama Team Lo]
└──╼ # ''', 'red', attrs=['bold']))
    print('')
    message = input(colored('''┌─[root]─[~Masukan Pesan Lo]
└──────────────────────────────────────────────────────────────────────────────╼
''', 'red', attrs=['bold']))
    thanksto = input(colored('''┌─[root]─[~Thanks To]
└──╼ # ''', 'red', attrs=['bold']))
    print('')
    abg = input(colored('''─[root]─[~Masukan Url Background]
└──╼ # ''', 'red', attrs=['bold']))

    sleep(2)
    system('clear')
    cprint('Sedang Membua Script...', 'green', attrs=['bold', 'blink'])
    sleep(5)


    sc = open('script.html', 'w')

    mscript1 = ('''<!DOCTYPE html><html><head><title>''')
    mscript2 = title
    mscript3 = ('''</title></head>''')
    mscript4 = ('''<body bgcolor="black">''')
    mscript5 = ('''<center><font face="Courier new" size="20" font style="text-shadow: blue 12px 5px 20px;" color="LightBlue">''')
    mscript6 = nick
    mscript7 = ('''</font></center>''')
    mscript8 = ('''<br>''')
    mscript9 = ('''<br>''')
    mscript10 = ('''<br><center><img src="''')
    mscript11 = logo
    mscript12 = ('''" width="300" height="300"></center>''')
    mscript13 = ('''<br>''')
    mscript14 = ('''<br>''')
    mscript15 = ('''<br><center><font face="Courier new" size="6" font style="text-shadow: 0px 0px 70px white;" color="LightBlue">''')
    mscript16 = team
    mscript17 = ('''</font></center>''')
    mscript19 = ('''<br>''')
    mscript20 = ('''<br>''')
    mscript21 = ('''<br><center><font face="Courier new" size="5" font style="text-shadow: blue 0px 0px 70px;" color="LightBlue">Message</font></center>''')
    mscript22 = ('''<br><center><font face="Courier new" size="4" font style="text-shadow: lightblue 0px 0px 70px;" color="white">''')
    mscript23 = message
    mscript24 = ('''</font></center>''')
    mscript25 = ('''<br>''')
    mscript26 = ('''<br>''')
    mscript27 = ('''<br><center><font face="Courier new" size="5" font style="text-shadow: 0px 0px 70px white;" color="LightBlue">Thanks To</font></center>''')
    mscript28 = ('''<br>''')
    mscript29 = ('''<br><marquee behavior="scroll" direction="left" scrollamount="10" scrolldelay="70" width="100%">''')
    mscript30 = ('''<br><center><font face="Courier new" size="4" font style="text-shadow: lightblue 0px 0px 70px;" color="white">''')
    mscript31 = thanksto
    mscript32 = ('''</marque></font></center>''')
    mscript33 = ('''<style type="text/css"> body{background: url(''')
    mscript34 = abg
    mscript35 = ('''no-repeat fixed black; position: relative; width: 100%; height: 100%; background-size: 100%;''')
    mscript36 = ('''}</style>''')
    mscript37 = ('''</body></html>''')

    sc.write(mscript1)
    sc.write(mscript2)
    sc.write(mscript3)
    sc.write(mscript4)
    sc.write(mscript5)
    sc.write(mscript6)
    sc.write(mscript7)
    sc.write(mscript8)
    sc.write(mscript9)
    sc.write(mscript10)
    sc.write(mscript11)
    sc.write(mscript12)
    sc.write(mscript13)
    sc.write(mscript14)
    sc.write(mscript15)
    sc.write(mscript16)
    sc.write(mscript17)
    sc.write(mscript19)
    sc.write(mscript20)
    sc.write(mscript21)
    sc.write(mscript22)
    sc.write(mscript23)
    sc.write(mscript24)
    sc.write(mscript25)
    sc.write(mscript26)
    sc.write(mscript27)
    sc.write(mscript28)
    sc.write(mscript29)
    sc.write(mscript30)
    sc.write(mscript31)
    sc.write(mscript32)
    sc.write(mscript33)
    sc.write(mscript34)
    sc.write(mscript35)
    sc.write(mscript36)
    sc.write(mscript37)

    cprint('Script Berhasil di buat', 'green', attrs=['bold'])
    cprint('Script terletak di folder ini', 'green', attrs=['bold'])
    time.sleep(3)
    cprint('User Exiting', 'green', attrs=['bold'])


try:
    logo()
    conti()
    logo2()
    tools()
except KeyboardInterrupt:
    system('clear')
    cprint('user exit')