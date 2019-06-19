# THE IMPORTANT APPROACH TO LOCK MACHINE IN ONE GO

#import os

#Hel = os.environ["windir"]
#os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')


import tkinter as tk
import subprocess as sub
import pyautogui as py
import time
import random
import os
import ctypes



py.FAILSAFE = False

root = tk.Tk() 
list1 = ['komodo', 'idea64', 'PHP Storm ', ' Visual Studio' , 'NetBeans' , 'eclipse_PHP', 'eclipse_Java' , 'Ruby' , 'pycharm64' ] 

canvas1 = tk.Canvas (root, width=700, height=800)

#canvas1.configure(background='black')

filename = tk.PhotoImage(file = "C:\\Users\\karanaro\\Desktop\\image_logo.png")
background_label = tk.Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)





############################################################################################################################################


class Paint:
	def paint_mouse(self):
		time.sleep(2)
		sub.call('start mspaint', shell = True)
		time.sleep(2)
		screenWidth, screenHeight = py.size()
		currentMouseX, currentMouseY = py.position()
		py.moveTo(100, 150)
		py.click()
		py.moveRel(None, 10)  # move mouse 10 pixels down
		py.doubleClick()
		py.moveTo(300,280, duration=.75, tween=py.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
		py.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
		py.press('esc')
		py.keyDown('shift')
		py.press(['left', 'left', 'left', 'left', 'left', 'left'])
		py.keyUp('shift')
		py.hotkey('ctrl', 'c')
		distance = 500
		while distance > 0:
			py.dragRel(distance, 0, duration=0.14)   # move right
			distance -= 10
			py.dragRel(0, distance, duration=0.14)   # move down
			py.dragRel(-distance, 0, duration=0.14)  # move left
			distance -= 15
			py.dragRel(0, -distance, duration=0.14)  # move up
		py.moveTo(1250,8, 3, py.easeInQuad)
		for i in range(1):
			py.click(1250,8)
		py.PAUSE = 0.5
		py.typewrite(['tab'])
		py.PAUSE = 2
		py.typewrite(['enter'])
		time.sleep(2)
#		for i in range(4):
#			py.keyDown(['alt'])
#			time.sleep(2)
#			py.typewrite(['tab'])
#			py.keyUp(['alt'])
	


second = Paint()

############################################################################################################################################

class _outlook:
	def outlook(self):
		py.typewrite(['win'])
		py.PAUSE = 0.5
		py.typewrite('outlook' , interval = 0.25 )
		py.PAUSE = 0.25
		py.typewrite(['enter'])
		time.sleep(4)
		py.click(23,75)
		_list = ['komal', 'karanaro', 'swati', 'prerna']
		for i in range(4):
			py.typewrite(_list[i])
			py.PAUSE = 0.35
			py.typewrite(['enter'])
		py.PAUSE = 0.5		
		py.typewrite(['tab'])
		py.typewrite('nilesh')
		py.typewrite(['enter'])
		py.PAUSE = 0.5	
		py.click(723,633)
		py.typewrite('Demo Mail To Test The Automation Framework For EXCEL SHORE PLUS' , interval= 0.20)
		py.click(723,633)
		py.typewrite('\n  BLANK MESSAGE: PLEASE IGNORE THIS MESSAGE', interval=0.25)
		py.moveTo(26,190, 2, py.easeInQuad)
		py.click(26,190)
		py.PAUSE = 0.5
		py.typewrite(['tab'])
		py.pause = 0.2
		py.typewrite(['enter'])
		time.sleep(3)
		sub.call('taskkill /F /IM outlook.exe' , shell = True)
		py.PAUSE = 0.5
		


third = _outlook()



############################################################################################################################################
############################################################################################################################################


class _fileexp:
	def explorer(self):
		py.typewrite(['win'])
		py.typewrite('explorer' , interval = 0.25)
		py.PAUSE = 0.35
		py.typewrite(['enter'])
		py.PAUSE = 1
		for i in range(2):
			py.click(386,748)
		time.sleep(2)
		pass
		for i in range(0,2,1):
			py.click(524,375)
		time.sleep(2)
		py.typewrite(['enter'])
		time.sleep(1)
		py.moveTo(1195,880, 3, py.easeInQuad)
		py.click(button = 'right')
		py.typewrite(['up'])
		py.PAUSE = 0.15
		py.typewrite(['up'])
		py.PAUSE = 0.15
		py.typewrite(['right'])
		py.PAUSE = 0.15
		py.typewrite(['up'])
		py.PAUSE = 0.15
		py.typewrite(['up'])
		py.PAUSE = 0.15
		py.typewrite(['up'])
		py.PAUSE = 0.15
		py.typewrite(['up'])
		py.PAUSE = 0.15
		py.typewrite(['enter'])
		py.PAUSE = 0.15
		rand = str(random.randint(1,200))
		py.typewrite('random' , interval=0.25)
		py.typewrite(rand)
		for i in range(2):
			py.typewrite(['enter'])
		py.typewrite('test file \n next we will save this test file with a random name \n Then Next we will rename it and then delete it', interval= 0.15)
		py.PAUSE = 1.5
		#py.typewrite('\n \n \n \n \n After alt tabs we will now save this edited file' , interval= 0.15)
		time.sleep(1)
		py.keyDown('alt')
		time.sleep(0.2)
		py.press('tab')
		time.sleep(0.2)
		py.keyUp('alt')
		py.hotkey('alt', 'f4')
		py.pause = 2
		py.typewrite(['tab'])
		py.typewrite(['enter'])
		py.typewrite(['space'])
		py.pause = 0.50
		py.typewrite(['f2'])
		rand = str(random.randint(1,200))
		py.typewrite('random' , interval=0.25)
		py.typewrite(rand)
		py.typewrite(['enter'])
		py.pause = 0.50
		py.typewrite(['space'])
		py.pause = 0.50
		py.typewrite(['delete'])
		py.typewrite(['enter'])
		
		py.moveTo(1279,0 , 3 , py.easeInQuad)
		for i in range(2):
			py.click(1279,0)




explore = _fileexp()



############################################################################################################################################
############################################################################################################################################



class browserTest:

	def open_close(self):
		pass


	def open_minimize(self):
		sub.call([r'y.bat'])



	def stress_test(self):
		sub.call([r'100URL.bat'])
		py.hotkey('win', 'r')
		py.typewrite('notepad', interval= 0.2)
		py.typewrite(['enter'])
		py.typewrite('The test is complete' , interval = 0.25)
		time.sleep(1)
		sub.call('taskkill /F /IM notepad.exe')

	def close(self):
		sub.call('cmd /c "taskkill /f /im explorer.exe && start explorer"')




fourth = browserTest()


############################################################################################################################################


class generate_data:

	def start_matrix(self): 
	       sub.call([r'C:\Users\Karanaro\Desktop\the_new-thng_loop.bat'])
	           	
	

	def start_batch_manually(self):
			sub.call([r'C:\Users\Karanaro\Desktop\runthis.bat'])	
	
	
	#class ApplyData:
	def AutomateOpenAndAct(self):
		time.sleep(8)
		py.hotkey('ctrl', 'n')
		#py.typewrite(['enter'])
		time.sleep(3)
		py.typewrite('\n \n Random text `` Used For Testing --- Tool Detector Tools Automate Data Generation', interval=0.15)
		time.sleep(2)
		py.typewrite('\n \n This file will be stored in the default destination' , interval=0.15)
		time.sleep(2)
		py.typewrite('\n \n We will save it now and close this program and move on to the next in the list' , interval=0.15)
		time.sleep(1)
		py.typewrite('\n \n THANK-YOU ' , interval=0.15)
		time.sleep(2)
		py.hotkey('ctrl','s')
		time.sleep(1)
		rand = str(random.randint(1,200))
		py.typewrite('random' , interval=0.35)
		py.typewrite(rand)
		time.sleep(5)
		py.typewrite(['enter'])	
	
	
	

	def Notpresent(self):
		time.sleep(3)
		pass
		py.hotkey('win', 'r')
		time.sleep(2)
		py.typewrite('notepad' , interval=0.15)
		py.typewrite(['enter'])
		time.sleep(3)
		py.typewrite('Sorry, This software is a paid software and key is not available to Users' , interval=0.3)
		time.sleep(2)
		py.typewrite('\n \n \n Moving on to the next in the list' , interval=0.2)
		time.sleep(3)
		sub.call(r'taskkill /F /IM notepad.exe' , shell = True)	
	

	def forIdea(self):
		time.sleep(17)
		sub.call('echo this is idea test', shell = True)
		py.moveTo(1195,880, 3, py.easeInQuad)
		time.sleep(1)
		py.click(1195, 800)
		py.pause = 2
		
		py.hotkey('alt', 'ctrl' , 'shift' , 'insert')

		py.pause = 2
		py.typewrite(['enter'])
		time.sleep(2)
		py.hotkey('ctrl','s')
		time.sleep(1)
		rand = str(random.randint(1,200))
		py.typewrite('random' , interval=0.35)
		py.typewrite(rand)
		time.sleep(5)
		py.typewrite(['enter'])	
		py.typewrite('\n \n Idea Editor, Random data to test the same for before that was done before' , interval=0.2)
		time.sleep(5)	
		py.typewrite('\n \n This file will be stored in the default destination' , interval=0.2)
		time.sleep(2)
		py.typewrite('\n \n We will save it now and close this program and move on to the next in the list' , interval=0.2)
		time.sleep(2)
		py.typewrite('\n \n THANK-YOU ' , interval=0.2)
		time.sleep(2)
		py.hotkey('ctrl','s')
		time.sleep(5)
		py.typewrite(['enter'])	
	
	
	def toolDetector(self):
		sub.call([r'C:\Users\Karanaro\Desktop\test1.bat'])
		first.AutomateOpenAndAct()
		time.sleep(1)
		sub.call('taskkill /F /IM komodo.exe', shell = True)
		pass
		sub.call([r'C:\Users\Karanaro\Desktop\test2.bat'])
		first.forIdea()
		time.sleep(1)
		sub.call('taskkill /F /IM idea64.exe', shell = True)
		py.typewrite(['enter'])
		sub.call([r'C:\Users\Karanaro\Desktop\test3.bat'])
		time.sleep(5)
		time.sleep(2)
		first.Notpresent()
		time.sleep(2)
		sub.call('taskkill /F /IM phpstorm64.EXE', shell = True)
		#sub.call([r'C:\Users\Karanaro\Desktop\test4.bat'])
		#time.sleep(2)
		#first.Notpresent()
		#time.sleep(2)
		#sub.call('taskkill /F /IM webstorm64.exe', shell = True)
		sub.call([r'C:\Users\Karanaro\Desktop\test5.bat'])
		first.AutomateOpenAndAct()
		time.sleep(2)
		sub.call('taskkill /F /IM devenv.exe', shell = True)	
		py.hotkey('win', 'r')
		py.typewrite('notepad')
		py.typewrite(['enter'])
		time.sleep(1)
		py.typewrite('The test for tool detector is complete', interval= 0.15)
		py.pause = 1
		sub.call('taskkill /F /IM notepad.exe', shell = True)


first = generate_data()

class _lock_Hibernate:
	def _locksys(self):
		winpath = os.environ["windir"]
		os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')
		

	def _Hibernatesys(self):
		os.system(r'%windir%\system32\rundll32.exe powrprof.dll,SetSuspendState Hibernate')               

_lock = _lock_Hibernate()



###########################################################################################################


class _incognito:
	def Incognito(self):
		py.moveTo(1112,1002, 3, py.easeInQuad)
		py.click(button = 'left')



incog = _incognito()



###############################################################################################################


class runAll:

	def openO(self):
		
###########################################################################################################

	
###############################################################################################################
		
#		py.confirm('Do you want to continue with tool-detector test ?')
		first.toolDetector()


#		py.confirm('Do you want to continue with explorer test ?')
		
		explore.explorer()


#		py.confirm('Do you want to start with paint test ?.')
		#PUT AN IF BLOCK INSIDE IT
		second.paint_mouse()

#		py.confirm('Open Outlook and send the messages to everyone in the team')
		third.outlook()


#		py.confirm('Do you want to continue with browser test ?')
		fourth.open_minimize()
		fourth.stress_test()
		fourth.close()


		
		

		#
#

main = runAll()



main.openO()

#############################################################################################################################################
##############################################################################################################################################

#button1 =tk.Button (root, text='Run The Matrix ',command= first.start_matrix)
#canvas1.create_window(100,50, window=button1)#
#

#button2 = tk.Button(root, text = 'Run the TOOLS manually' , command = first.start_batch_manually)
#canvas1.create_window(350, 453, window= button2)#
#
#

#button3 = tk.Button (root, text='Run the Framework automatically ', command= main.openO)
#canvas1.create_window(350,493, window=button3)
###
#

#button4 = tk.Button (root, text='Lock The MACHINE ', command= _lock._locksys)
#canvas1.create_window(100,100, window=button4)#
#
#

#button5 = tk.Button (root, text='Hibernate The MACHINE ', command= _lock._Hibernatesys)
#canvas1.create_window(100,150, window=button5)#
#
#

#button6 = tk.Button (root, text='Start Incognito Mode', command= incog.Incognito)
#canvas1.create_window(350,593, window=button6)#
#

##button4 = tk.Button(root , text = 'Test01', command = __init__)
##canvas1.create_window(340, 393, window = button4)
#canvas1.pack()
#root.mainloop()


try:
	pass



except:
	pass
	pass