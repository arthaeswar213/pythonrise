import pyttsx3
import os

# pyttsx3.speak("Welcome to Windows tools")
i=1

while True:

	if i <= 1 :
		print(" Please tell me which app you want me to open : "  , end='')
	else :
		print(" Please tell me which app you want me to open next : "  , end='')
	p = input()

	# print(p)
	# os.system(p)

	if (("run" in p) or ("open" in p)) and ("chrome" in p) :
	  os.system("chrome")
	  print("I have opened chrome")
	  i=i+1

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")
	  print("I have opened notepad")
	  i=i+1

	elif (("run" in p) or ("open" in p))  and ("player" in p) and ("media" in p):
	  os.system("wmplayer")
	  print("I have opened windows media player")
	  i=i+1
	
	elif (("run" in p) or ("open" in p))  and (("calculator" in p) or ("calc" in p)):
	  os.system("calc")
	  print("I have opened Calculator")
	  i=i+1
	
	elif (("run" in p) or ("open" in p))  and ("paint" in p) :
	  os.system("mspaint")
	  print("I have opened Paint")
	  i=i+1	
	  
	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("Cant find the app you requested in my library")


