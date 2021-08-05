import os
import sys
import time 



blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'

c=(yellow+"""
███╗░░░███╗██████╗░
████╗░████║██╔══██╗
██╔████╔██║██║░░██║
██║╚██╔╝██║██║░░██║
██║░╚═╝░██║██████╔╝
╚═╝░░░░░╚═╝╚═════╝░

░█████╗░██╗░░░░░░█████╗░███╗░░░███╗██╗███╗░░██╗
██╔══██╗██║░░░░░██╔══██╗████╗░████║██║████╗░██║
███████║██║░░░░░███████║██╔████╔██║██║██╔██╗██║
██╔══██║██║░░░░░██╔══██║██║╚██╔╝██║██║██║╚████║
██║░░██║███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝



\x1b[94m

╔═══╦╗─╔╦═══╦╗╔╗╔╦═══╦╗─╔╦╗─╔╦═══╦╗──╔╗
║╔═╗║║─║║╔═╗║║║║║╠╗╔╗║║─║║║─║║╔═╗║╚╗╔╝║
║║─╚╣╚═╝║║─║║║║║║║║║║║╚═╝║║─║║╚═╝╠╗╚╝╔╝
║║─╔╣╔═╗║║─║║╚╝╚╝║║║║║╔═╗║║─║║╔╗╔╝╚╗╔╝
║╚═╝║║─║║╚═╝╠╗╔╗╔╬╝╚╝║║─║║╚═╝║║║╚╗─║║
╚═══╩╝─╚╩═══╝╚╝╚╝╚═══╩╝─╚╩═══╩╝╚═╝─╚╝""")

print(c)

def e(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.3) 



x=3
while x<5:
     user=str(input(red+"\n ?? USERNAME : "))
     passw=str(input(green+"\n ☣️PASSWORD : "))
     if user=="alamin" and passw=="alamin":
      print("Login Succcessfull")
      sys.stdout.flush()
      time.sleep(2) 
      os.system("xdg-open https://www.facebook.com/Mdalamin54321")
      x=8
     else:
      print("Wrong Username  && Password⚠️ ")
      os.system("xdg-open https://www.facebook.com/Mdalamin54321")
      x=3
 

    
os.system('clear')

print(c)
e=(cyan+"\n\n        	Delovmemt By  Md Alamin Chowdowry")

print(e)

print("\n----------------------------------------------------------------")

d=(yellow+"[1] SMS BOMBER(Code copy by Toxic Noob)\n\n[2]MAIL BOMBER (NO SING UP)\n\n[3]MAIL BOMBER(SING UP) \n\n[4]FB CLONE")

print(d)
a=str(input("\nEnter Your Option: "))
if a=="1":
	   os.system("python3 bdsms.py")  
elif a=="2":
	   os.system("python3 mail2.py") 
elif a=="3":
	   os.system("python3 mail1.py")
elif a=="4":
	   os.system("python3 fb.py") 
	     
else:
		print("NO OPTION ")
		a=input()
	
	
	