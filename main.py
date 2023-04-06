import os 
import requests
import time
import discord
import json
from colorama import Fore , Style


os.system("cls")
os.system("title GodScript - T1zzo")
os.system("color f")

def painel():
    print(f"""{Fore.LIGHTRED_EX}                        
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.  
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~   Made by godscript
            :%`  ~#$$$m:        ~!~ ?$$$$$$    Version : 1.0
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
 """)

painel()


lang = input("Escolha um Idioma [en/pt]: ")
if lang not in ["en", "pt"]:
    print("Idioma inválido, tente novamente.")
    exit()


with open("language.txt", "w") as f:
    f.write(lang)


with open(f"lang/{lang}.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

os.system("cls")
painel()

opt = input(f"""
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}1{Fore.LIGHTYELLOW_EX}] {messages['menu_options']['1']}
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}2{Fore.LIGHTYELLOW_EX}] {messages['menu_options']['2']}
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}3{Fore.LIGHTYELLOW_EX}] {messages['menu_options']['3']}
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}4{Fore.LIGHTYELLOW_EX}] {messages['menu_options']['4']}
""")
if opt == "1":
    os.system("cls")
    os.system("python tools/webhook.py")
if opt== "2":
    os.system("cls")
    os.system("python tools/spam.py")
if opt== "3":
    os.system("cls")
    os.system("python tools/massdm.py")
if opt== "4":
    os.system("cls")
    os.system("python tools/password.py")

