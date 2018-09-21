#!/usr/bin/python
# -*- coding: utf-8 -*-
#made by Jack (github.com/jackthebaptist)

#Fakefetch 2.0 - with actual fetch

#-------- REQUIRED LIBS -------- 

#these should be on all distros by default

import getpass
import platform
import os
import sys
import argparse

#-------- DEFAULT VARIABLES -------- 

user = getpass.getuser()
kernel = platform.release()
arch = platform.machine()
osrel = "none"
desktop = "none"
CPT = "\033["

#-------- FUNCTIONS -------- 

def codechar(code):
    return CPT + str(code) + 'm'

class colour_code(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, codechar(value))

class foreground(colour_code): #foreground colours (text)
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

class background(colour_code): #background colours (selections)
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49


def osrel(): #find OS release name / distro
	global osrel
	if 'arch' in open("/etc/os-release").read():
		osrel = "Arch Linux"
	elif 'void' in open("/etc/os-release").read():
		osrel = "Void Linux"
	elif 'ubuntu' in open("/etc/os-release").read():
		osrel = "Ubuntu Linux"	
	elif 'ID=debian' in open("/etc/os-release").read():
		osrel = "Debian Linux"
	elif 'ID=devuan' in open("/etc/os-release").read():
		osrel = "Devuan Linux"
	elif 'gentoo' in open("/etc/os-release").read():
		osrel = "Gentoo Linux"
	elif 'clover' in open("/etc/os-release").read():
		osrel = "CloverOS"
	elif 'trisquel' in open("/etc/os-release").read():
		osrel = "Trisquel Linux"
	else:
		osrel = "\033[31mcould not detect"

def desktop(): #find desktop environment 
	global desktop
	desktop = os.popen("env | grep DESKTOP_SESSION").read()
	if 'Openbox' in desktop:
		desktop = "Openbox"
	elif 'i3' in desktop:
		desktop = "i3"
	elif 'Gnome' in desktop:
		desktop = "Gnome"
	elif 'Xfce' in desktop:
		desktop = "Xfce4"
	elif 'xfce' in desktop:
		desktop = "Xfce4"
	elif 'Plasma' in desktop:
		desktop = "KDE Plasma"
	elif 'LXDE' in desktop:
		desktop = "LXDE"
	else:
		desktop = "\033[31mcould not detect"

def disart(): #get correct distro art
	global test
	if osrel == "Void Linux":
		print(void_logo)
	elif osrel == "Debian Linux":
		print(debian_logo)
	elif osrel == "Devuan Linux":
		print(devuan_logo)
	elif osrel == "Ubuntu Linux":
		print(ubuntu_logo)
	elif osrel == "Gentoo Linux":
		print(gentoo_logo)
	elif osrel == "Arch Linux":
		print(arch_logo)
	elif osrel == "CloverOS":
		print(cloveros_logo)
	elif osrel == "Trisquel Linux":
		print(trisquel_logo)
	else:
		print(no_logo)
		
#-------- DETECTION CALLS -------- 

osrel()
desktop()

#-------- ASCII ART -------- 

pcinfo = """
\033[34m[\033[39m{}\033[34m]
\033[34m[OS]:\033[39m {} {}
\033[34m[Kernel]:\033[39m {} 
\033[34m[DE]:\033[39m {}

\033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
""".format(user,osrel,arch,kernel,desktop)


void_logo = """
\033[32m                __.;=====;.__
\033[32m            _.=+==++=++=+=+===;.          
\033[32m             -=+++=+===+=+=+++++=_        
\033[32m        .     -=:``     `--==+=++==.      
\033[32m       _vi,    `            --+=++++:            \033[34m[\033[39m{}\033[34m]
\033[32m      .uvnvi.       _._       -==+==+.           \033[34m[OS]:\033[39m {} {}
\033[32m     .vvnvnI`    .;==|==;.     :|=||=|.          \033[34m[Kernel]:\033[39m {}          
\033[39m+QmQQm\033[32mpvvnv; \033[39m_yYsyQQWUUQQQm #QmQ#\033[32m:\033[39mQQQWUV$QQmL    \033[34m[DE]:\033[39m {}
\033[39m -QQWQW\033[32mpvvo\033[39mwZ?.wQQQE\033[32m==<\033[39m QWWQ/QWQW.QQWW\033[32m(: \033[39mjQWQE
\033[39m  -$QQQQmmU'  jQQQ@\033[39m+=<\033[39mQWQQ)mQQQ.mQQQC\033[32m+;\033[39mjWQQ@'    \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
\033[39m   -$WQ8Y\033[39mnI:   \033[39mQWQQwgQQWV\033[39m`\033[39mmWQQ.jQWQQgyyWW@!
\033[32m     -1vvnvv.     `~+++`        ++|+++
      +vnvnnv,                 `-|===
       +vnvnvns.           .      :=-
        -Invnvvnsi..___..=sv=.     `
          +Invnvnvnnnnnnnnvvnn;.
            ~|Invnvnvvnvvvnnv)+`
               -~|((l)*|~\033[39m
               """.format(user,osrel,arch,kernel,desktop)


debian_logo = '''
         \033[31m_,met$$$$$gg.
      \033[31m,g$$$$$$$$$$$$$$$P.      \033[34m[\033[39m{}\033[34m]
    \033[31m,g$$P""          Y$$. .    \033[34m[OS]:\033[39m {} {}
   \033[31m,$$P'              `$$$.    \033[34m[Kernel]:\033[39m {}
  \033[31m ,$$P       ,ggs.     `$$b:  \033[34m[DE]:\033[39m {}
  \033[31m`d$$'     ,$P"'   .    $$$
   \033[31m$$P      d$'     ,    $$P   \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
   \033[31m$$:      $$.   -    ,d$$
   \033[31m$$\;      Y$b._   _,d$P
   \033[31mY$$.    `.`"Y$$$$P"
   \033[31m`$$b      "-.__
    \033[31m`Y$$
     \033[31m`Y$$.
       \033[31m`$$b.
         \033[31m`Y$$b.
            \033[31m`"Y$b._
                \033[31m`""""\033[39m'''.format(user,osrel,arch,kernel,desktop)

cloveros_logo = """
\033[32m               `omo``omo`
             `oNMMMNNMMMNo`              
           `oNMMMMMMMMMMMMNo`        
          oNMMMMMMMMMMMMMMMMNo  
          `sNMMMMMMMMMMMMMMNs`                 \033[34m[\033[39m{}\033[34m]\033[32m
     `omo`  `sNMMMMMMMMMMNs`  `omo`            \033[34m[OS]:\033[39m {} {}\033[32m
   `oNMMMNo`  `sNMMMMMMNs`  `oNMMMNo`          \033[34m[Kernel]:\033[39m {}\033[32m  
 `oNMMMMMMMNo`  `oNMMNs`  `oNMMMMMMMNo`        \033[34m[DE]:\033[39m {}\033[32m
oNMMMMMMMMMMMNo`  `sy`  `oNMMMMMMMMMMMNo
`sNMMMMMMMMMMMMNo.\033[33moNNs\033[32m.oNMMMMMMMMMMMMNs`       \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
`oNMMMMMMMMMMMMNs.\033[33moNNs\033[32m.oNMMMMMMMMMMMMNo`
oNMMMMMMMMMMMNs`  `sy`  `oNMMMMMMMMMMMNo
 `oNMMMMMMMNs`  `oNMMNo`  `oNMMMMMMMNs`
   `oNMMMNs`  `sNMMMMMMNs`  `oNMMMNs`
     `oNs`  `sNMMMMMMMMMMNs`  `oNs`
          `sNMMMMMMMMMMMMMMNs`
          +NMMMMMMMMMMMMMMMMNo
           `oNMMMMMMMMMMMMNo`
             `oNMMMNNMMMNs`
               `omo``oNs`
               """.format(user,osrel,arch,kernel,desktop)


ubuntu_logo = """ 
\033[33m            .-/+oossssoo+/-.
        `:+ssssssssssssssssss+:`
      -+ssssssssssssssssssyyssss+-
    .ossssssssssssssssss\033[39mdMMMNy\033[33msssso.
   /sssssssssss\033[39mhdmmNNmmyNMMMMh\033[33mssssss/        \033[34m[\033[39m{}\033[34m]\033[33m
  +sssssssss\033[39mhm\033[33myd\033[39mMMMMMMMNddddy\033[33mssssssss+       \033[34m[OS]:\033[39m {} {}\033[33m
 /ssssssss\033[39mhNMMM\033[33myh\033[39mhyyyyhmNMMMNh\033[33mssssssss/      \033[34m[Kernel]:\033[39m {}\033[33m
.ssssssss\033[39mdMMMNh\033[33mssssssssss\033[39mhNMMMd\033[33mssssssss.     \033[34m[DE]:\033[39m {}\033[33m
+ssss\033[39mhhhyNMMNy\033[33mssssssssssss\033[39myNMMMy\033[33msssssss+ 
oss\033[39myNMMMNyMMh\033[33mssssssssssssss\033[39mhmmmh\033[33mssssssso     \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
oss\033[39myNMMMNyMMh\033[33msssssssssssssshmmmh\033[33mssssssso
+ssss\033[39mhhhyNMMNy\033[33mssssssssssss\033[39myNMMMy\033[33msssssss+
.ssssssss\033[39mdMMMNh\033[33mssssssssss\033[39mhNMMMd\033[33mssssssss.
 /ssssssss\033[39mhNMMM\033[33myh\033[39mhyyyyhdNMMMNh\033[33mssssssss/
  +sssssssss\033[39mdm\033[33myd\033[39mMMMMMMMMddddy\033[33mssssssss+
   /sssssssssss\033[39mhdmNNNNmyNMMMMh\033[33mssssss/
    .ossssssssssssssssss\033[39mdMMMNy\033[33msssso.
      -+sssssssssssssssss\033[39myyy\033[33mssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.
            """.format(user,osrel,arch,kernel,desktop)

trisquel_logo = """
\033[36m                         ▄▄▄▄▄▄
                      ▄█████████▄
      ▄▄▄▄▄▄         ████▀   ▀████
   ▄██████████▄     ████▀   ▄▄ ▀███
 ▄███▀▀   ▀▀████     ███▄   ▄█   ███        \033[34m[\033[39m{}\033[34m]\033[36m
▄███   ▄▄▄   ████▄    ▀██████   ▄███        \033[34m[OS]:\033[39m {} {}\033[36m
███   █▀▀██▄  █████▄     ▀▀   ▄████         \033[34m[Kernel]:\033[39m {}\033[36m
▀███      ███  ███████▄▄  ▄▄██████          \033[34m[DE]:\033[39m {}
\033[36m ▀███▄   ▄███  █████████████\033[34m████▀
\033[36m  ▀█████████    ███████\033[34m███▀▀▀               \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
    ▀▀███▀▀     ██████▀▀
               ██████▀   ▄▄▄▄
              █████▀   ████████
              █████   ███▀  ▀███
               ████▄   ██▄▄▄  ███
                █████▄   ▀▀  ▄██
                  ██████▄▄▄████
                     ▀▀█████▀▀
                     """.format(user,osrel,arch,kernel,desktop)

gentoo_logo = """
\033[35m         -/oyddmdhs+:.
     -o$\033[39mdNMMMMMMMMNNmhy+\033[35m-`
   -y\033[39mNMMMMMMMMMMMNNNmmdhy\033[35m+-
 `o\033[39mmMMMMMMMMMMMMNmdmmmmddhhy\033[35m/`
 om\033[39mMMMMMMMMMMMN\033[35mhhyyyo\033[39mhmdddhhhd$\033[35mo`        \033[34m[\033[39m{}\033[34m]\033[35m
.y\033[39mdMMMMMMMMMMd\033[35mhs++so/s\033[39mmdddhhhhdm$\033[35m+`      \033[34m[OS]:\033[39m {} {}\033[35m
 oy\033[39mhdmNMMMMMMMN\033[35mdyooy\033[39mdmddddhhhhyhN\033[35md.      \033[34m[Kernel]:\033[39m {}\033[35m      
  :o\033[39myhhdNNMMMMMMMNNNmmdddhhhhhyym\033[35mMh      \033[34m[DE]:\033[39m {}\033[35m
    .:\033[39m+sydNMMMMMNNNmmmdddhhhhhhmM\033[35mmy      
       /m\033[39mMMMMMMNNNmmmdddhhhhhmMNh\033[35ms:      \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
    `o$\033[39mNMMMMMMMNNNmmmddddhhdmMNhs\033[35m+`      
  `s\033[39mNMMMMMMMMNNNmmmdddddmNMmhs\033[35m/.
 /N\033[39mMMMMMMMMNNNNmmmdddmNMNdso\033[35m:`
+M\033[39mMMMMMMNNNNNmmmmdmNMNdso\033[35m/-
yM\033[39mMNNNNNNNmmmmmNNMmhs+/\033[35m-`
/h\033[39mMMNNNNNNNNMNdhs++/\033[35m-`
`/\033[39mohdmmddhys+++/:\033[35m.`
  `-//////:--.
  """.format(user,osrel,arch,kernel,desktop)

arch_logo = """
\033[34m                   -`
                  .o+`
                 `ooo/
                `+oooo:
               `+oooooo:        \033[34m[\033[39m{}\033[34m]
               -+oooooo+:       \033[34m[OS]:\033[39m {} {}
             \033[34m`/:-:++oooo+:      \033[34m[Kernel]:\033[39m {} 
            \033[34m`/++++/+++++++:     \033[34m[DE]:\033[39m {}
           \033[34m`/++++++++++++++:
          `/++ooooooooo\oooo/`  \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
         ./ooosssso++osssssso+`
        .oossssso-````/ossssss+`
       -osssssso.      :ssssssso.
      :osssssss/        osssso+++.
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/
 """.format(user,osrel,arch,kernel,desktop)


devuan_logo = """
\033[35m  ..,,;;;::;,..                   
           `':ddd;:,. 
                 `'dPPd:,. 
                     `:b$$b`. 
                        'P$$$d`    \033[34m[\033[39m{}\033[34m]
                         \033[35m.$$$$$`   \033[34m[OS]:\033[39m {} {}
                         \033[35m;$$$$$P   \033[34m[Kernel]:\033[39m {} 
                      \033[35m.:P$$$$$$`   \033[34m[DE]:\033[39m {}
                  \033[35m.,:b$$$$$$$;' 
             .,:dP$$$$$$$$b:' 		\033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m \033[35m
      .,:;db$$$$$$$$$$Pd'` 
 ,db$$$$$$$$$$$$$$b:'` 
:$$$$$$$$$$$$b:'` 
 `$$$$$bd:''` 
   `'''` 


""".format(user,osrel,arch,kernel,desktop)

# -------- DISTROS NOT FOUND -------- 

no_logo = """
\033[31mE: distro not found!\033[39m 
make an issue at 'https://github.com/jackthebaptust/fakefetch' to get it added
"""

# -------- ARGS -------- 

parser = argparse.ArgumentParser()
parser.add_argument('-d','--distro', choices=['arch','void','gentoo','trisquel','ubuntu','debian','devuan','cloveros'], help='Choose which distro you want to display')
args = parser.parse_args()
if args.distro == "void":
	print(void_logo)

elif args.distro == "gentoo":
    print(gentoo_logo)

elif args.distro == "trisquel":
    print(trisquel_logo)

elif args.distro == "debian":
    print(debian_logo)

elif args.distro == 'devuan':
    print(devuan_logo)

elif args.distro == "ubuntu":
	print(ubuntu_logo)

elif args.distro == "cloveros":
    print(cloveros_logo)
    
elif args.distro == "arch":
	print(arch_logo)

else:
    disart()


	

