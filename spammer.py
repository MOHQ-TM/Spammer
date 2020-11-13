import pyautogui, time, os


class color:
    GREEN = '\033[92m'
    GREEN1 = '\033[32m'
    WHITE = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[96m'
    YELLOW = '\033[93m'
    MAJENTA = '\033[95m'

def banner():

    os.system('clear')
	
	
    print(color.GREEN1 + '')
	
    print('███╗   ███╗ ██████╗ ██╗  ██╗ ██████╗     ████████╗███╗   ███╗')
    print('████╗ ████║██╔═══██╗██║  ██║██╔═══██╗    ╚══██╔══╝████╗ ████║')
    print('██╔████╔██║██║   ██║███████║██║   ██║       ██║   ██╔████╔██║')
    print('██║╚██╔╝██║██║   ██║██╔══██║██║▄▄ ██║       ██║   ██║╚██╔╝██║')
    print('██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝       ██║   ██║ ╚═╝ ██║')
    print('╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚══▀▀═╝        ╚═╝   ╚═╝     ╚═╝')
    print(color.GREEN + '                            ************************************')
    print('                            ** Telegram : @Hamiyan_Haj_Qassem **')
    print('                            **     Email : mohq@gmail.com     **')
    print('                            ************************************')
    print('Exit : ctrl+c')
    print('')


def spammer():

	try :

		banner()

		#You text
		text = input(color.BLUE + "Enter You Text : " + color.RED)

		try :
			#How much
			amount = int(input(color.BLUE + "How much : " + color.RED))
		except : 
			print ("just integer")
			time.sleep(3)
			spammer()

		#open file
		f = open('text.txt','w')

		#write file
		f.write(str(text))

		#time left
		tl=10

		#print time and text
		while tl>0 :
			
			banner()
			print(color.YELLOW + "Your Text ==>> " + color.MAJENTA , text)
			print('')
			print(color.YELLOW + "Time Left ==>>" + color.RED , tl)
			print('')
			print(color.YELLOW + "Amount ==>> " + color.GREEN , amount)
			time.sleep(1)
			tl = tl-1

		#amount
		a = 0
		
		#start spam
		while a < amount :
			a = a+1
			f = open('text.txt','r')

			for word in f:

				pyautogui.typewrite(word)
				pyautogui.press('Enter')


	except :
		os.system('clear')
		print (color.BLUE + "\nOK goodbye !!!")


spammer()
