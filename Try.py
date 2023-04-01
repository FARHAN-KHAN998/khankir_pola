"""

import os
import random

print(ab)

"""


#---------{ADMIN INFO}-----------
# AUTHOR   : FARHAN KHAN
# TEAM     : COBRA-404-CYBER
# GITHUB   : COBRA-404-CYBER
# WHATSAPP : 01838847447
#--------------------------------
import os
import sys
import marshal
import base64
import time
import requests
import random
try:
  import cython
  from Cython.build.BuildExecutable import build
except:
  os.system("pip install cython > /dev/null")
try:
  os.system("mkdir /sdcard/CODE-X--COMPILER")
except:
  pass

os.system("clear")

def slw(S):
  for i in S:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)
def clear():
  os.system("clear")
  print(logo)
def line():
  print("\033[1;37m------------------------------------------------")
def marsal():
  clear()
  ab = ""
  bc = ""
  ca = ""
  a = "_COBRA_404_CYBER"
  for i in range(90000):
    ab+=a
    bc+=a
    ca+=a
  print("\033[1;37m[\033[38;5;196m!\033[1;37m]\033[38;5;196m THIS IS ONLY FOR THE LETEST VERSION OF PYTHON")
  print("\033[1;37m[\033[38;5;196m!\033[1;37m]\033[38;5;196m DONT USE ANY PYTHON2 OR PYTHON3 FILE FOR IT")
  line()
  try:
    f=input("\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER FILE PATH : ")
    file=open(f,"r")
    code=file.read()
  except FileNotFoundError:
    print("\033[1;37m[\033[38;5;196m!\033[1;37m]\033[38;5;196m FILE NOT FOUND PLZ TRY AGAIN")
    time.sleep(1)
    os.system("clear")
    marsal()
  enc=compile(code,"i","exec")
  mr=marshal.dumps(enc)
  line()
  out=input("\033[1;37m[\033[38;5;46m+\033[38;5;46m] FILE SAVE AS : ")
  lok=open(out,"w")
  lok.write(f"#{ab}\n#{bc}\n#{ca}\nimport marshal\nexec(marshal.loads("+repr(mr)+"))")
  os.system(f"mv {out} /sdcard/CODE-X--COMPILER")
  os.system("clear")
  print("""\033[1;37m

 ██████  ██████  ██████  ███████  \033[38;5;46m   ██   ██ \033[1;37m
██      ██    ██ ██   ██ ██         \033[38;5;46m  ██ ██  \033[1;37m
██      ██    ██ ██   ██ █████      \033[38;5;46m   ███   \033[1;37m
██      ██    ██ ██   ██ ██        \033[38;5;46m   ██ ██  \033[1;37m
 ██████  ██████  ██████  ███████  \033[38;5;46m   ██   ██ \033[1;37m

------------------------------------------------
\033[1;37m❲\033[38;5;46m+\033[1;37m❳\033[38;5;46m YOUR FILE COMPILED SUCCESSFULLY \033[1;37m
\033[1;37m❲\033[38;5;46m+\033[1;37m❳\033[38;5;46m CHECK YOUR SDCARD CODE-X--COMPILER \033[1;37m
------------------------------------------------

""")
  os.system("xdg-open https://www.facebook.com/Cobra.404.Cyber/")
  sys.exit()

def cpython():
  clear()
  file=input("\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER FILE PATH : \033[38;5;196m")
  try:
    file=open(file,"r").read()
  except FileNotFoundError:
    print("\033[1;37m[\033[38;5;196m!\033[1;37m]\033[38;5;196m FILE NOT FOUND TRY AGAIN")
    time.sleep(1)
    cpython()
  os.system(f"cythonize -i -2 {file}> /dev/null")
#  os.system("clear")
  print("""\033[1;37m

 ██████  ██████  ██████  ███████  \033[38;5;46m   ██   ██ \033[1;37m
██      ██    ██ ██   ██ ██         \033[38;5;46m  ██ ██  \033[1;37m
██      ██    ██ ██   ██ █████      \033[38;5;46m   ███   \033[1;37m
██      ██    ██ ██   ██ ██        \033[38;5;46m   ██ ██  \033[1;37m
 ██████  ██████  ██████  ███████  \033[38;5;46m   ██   ██ \033[1;37m

------------------------------------------------
\033[1;37m❲\033[38;5;46m+\033[1;37m❳\033[38;5;46m YOUR FILE COMPILED SUCCESSFULLY \033[1;37m
\033[1;37m❲\033[38;5;46m+\033[1;37m❳\033[38;5;46m CHECK THE PATH THAT YOU PROVIDE US :) \033[1;37m
------------------------------------------------

""")
  os.system("xdg-open https://www.facebook.com/Cobra.404.Cyber/")
  sys.exit()



logo="""\033[1;37m

 ██████  ██████  ██████  ███████  \033[38;5;46m   ██   ██ \033[1;37m
██      ██    ██ ██   ██ ██         \033[38;5;46m  ██ ██  \033[1;37m
██      ██    ██ ██   ██ █████      \033[38;5;46m   ███   \033[1;37m
██      ██    ██ ██   ██ ██        \033[38;5;46m   ██ ██  \033[1;37m
 ██████  ██████  ██████  ███████  \033[38;5;46m   ██   ██ \033[1;37m

------------------------------------------------
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ AUTHOR     : FARHAN KHAN 
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ TEAM       : COBRA-404-CYBER
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ FACEBOOK   : @FarhanXTermux
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ TOOLS TYPE : COMPILER
------------------------------------------------"""
print(logo)
slw("\033[38;5;46m WELLCOME TO CODE X PROJECT BY COBRA 404 CYBER\n")
time.sleep(1)
clear()
print("""[01] ENCRYPT YOUR CODE
[02] JOIN OUR PUBLIC GROUP FOR SUPPORT
[03] FOLLOW OUR PAGE FOR MORE TOOLS 
[04] CONTACT ME ON FACEBOOK 
[00] EXIT TOOL""")
line()
usr=input("[+] YOUR CHOICE : ")
usr=usr.replace(" ","")
if usr in ["1","01"]:
  pass
elif usr in ["2","02"]:
  os.system("xdg-open https://www.facebook.com/groups/1354738058401296/?ref=share&mibextid=NSMWB")
  sys.exit()
elif usr in ["3","03"]:
  os.system("xdg-open https://www.facebook.com/Cobra.404.Cyber/")
  sys.exit()
elif usr in ["4","04"]:
  os.system("xdg-open https://www.facebook.com/FarhanXTermux?mibextid=ZbWKwL")
  sys.exit()
elif usr in ["0","00"]:
  sys.exit()
else:
  print("\n\n[!] WRONG OPTION ENTERED..\n\n")
  sys.exit()

clear()
print("""[01] PY-MARSHAL
[02] CPYTHON {BEST}
[00] EXIT""")
line()
ec = input("[+] YOUR CHOICE : ")
ec = ec.replace(" ","")
if ec in ["1","01"]:
  marsal()
elif ec in ["2","02"]:
  cpython()
elif ec in ["0","00"]:
  sys.exit()
else:
  print("\n\nWRONG OPTION ENTERED..\n")
  sys.exit()