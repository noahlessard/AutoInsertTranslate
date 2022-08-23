#moms translator 
import pyautogui
import time
import cv2
import numpy as np
from PIL import Image
from PIL import ImageChops
from PIL import ImageTk
import pyperclip
import tkinter
from tkinter import *
from playsound import playsound

PassedPasteString = '1'
FailedPasteString = '2'
passimg = ''
failimg = ''


def GetLan():
    global PassedPasteString
    global FailedPasteString
    if (pyautogui.locateOnScreen('ArabicPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'موضوع تم اجتيازه'
        FailedPasteString = 'موضوع تعذر اجتيازه'        
        return 'Arabic'
    if (pyautogui.locateOnScreen('ChinesePIC.PNG', confidence = 0.9)):
        PassedPasteString = '通过有关本主题的考试'
        FailedPasteString = '未通过有关本主题的考试'
        return 'Chinese'
    if (pyautogui.locateOnScreen('DutchPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Geslaagd voor onderwerp'
        FailedPasteString = 'Niet geslaagd voor onderwerp'
        return 'Dutch'
    if (pyautogui.locateOnScreen('FrencePIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Note satisfaisante pour ce thème'
        FailedPasteString = 'Note insuffisante pour ce thème'

        return 'French'
    if (pyautogui.locateOnScreen('GermanPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Thema bestanden'
        FailedPasteString = 'Thema nicht bestanden'

        return 'German'
    if (pyautogui.locateOnScreen('GreekPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Επιτυχής ολοκλήρωση του θέματος'
        FailedPasteString = 'Ανεπιτυχής ολοκλήρωση του θέματος'

        return 'Greek'
    if (pyautogui.locateOnScreen('ItalianPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Argomento superato'
        FailedPasteString = 'Argomento non superato'

        return 'Italian'
    if (pyautogui.locateOnScreen('KoreanPIC.PNG', confidence = 0.9)):
        PassedPasteString = '항목 합격'
        FailedPasteString = '항목 불합격'

        return 'Korean'
    if (pyautogui.locateOnScreen('PolishPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Temat zaliczony'
        FailedPasteString = 'Temat niezaliczony'

        return 'Polish'
    if (pyautogui.locateOnScreen('PortugeusePIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Obteve aprovação no tópico'
        FailedPasteString = 'Não obteve aprovação no tópico'

        return 'Portugeuse'
    if (pyautogui.locateOnScreen('RussianPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Тема сдана'
        FailedPasteString ='Тема не сдана'

        return 'Russian'
    if (pyautogui.locateOnScreen('SpanishPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Tema aprobado'
        FailedPasteString ='Tema no aprobado'

        return 'Spanish'
    if (pyautogui.locateOnScreen('TurkishPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Konuda Başarılı Oldu'
        FailedPasteString ='Konuda Başarılı Olmadı'

        return 'Turkish'
    
    if (pyautogui.locateOnScreen('VietnamPIC.PNG', confidence = 0.9)):
        PassedPasteString = 'Chủ đề đã vượt qua'
        FailedPasteString ='Không vượt qua chủ đề'

        return 'Vietnam'

    
    else:
        return 'Not Found'


def GetTypeOfTarget():
    if (pyautogui.locateOnScreen('BaseDidNotPassTopic.PNG', confidence = 0.9 )):
        return 'DidNotPass' 
    if (pyautogui.locateOnScreen('BaseDidPassTopic.PNG', confidence = 0.9 )):
        return 'DidPass'  
    else:
        return 'Not Found'

def Solve():
    global passimg
    global failimg
    string = GetLan()
    print(string)

    typeTar = GetTypeOfTarget()
    print(typeTar)
    posScroll = pyautogui.locateCenterOnScreen('TargetPIC.PNG', confidence = 0.9 )
    pyautogui.moveTo(posScroll.x, posScroll.y)
    time.sleep(0.2)
    pyautogui.scroll(250)
    time.sleep(0.2)
    pyautogui.moveTo(600,10)
    posPaste = pyautogui.locateCenterOnScreen('TargetPIC.PNG', confidence = 0.9 )
    print(posPaste.x, posPaste.y)
    pyautogui.moveTo(posPaste.x - 10, posPaste.y + 20, 0.2)
    pyautogui.click(clicks=5, interval=0.3)
    pyautogui.press('delete')

    if (typeTar == 'DidPass'):
        print(PassedPasteString)
        pyperclip.copy(PassedPasteString)
        pyautogui.hotkey("ctrl", "v")
        
    if (typeTar == 'DidNotPass'):
        print(FailedPasteString)
        pyperclip.copy(FailedPasteString)
        pyautogui.hotkey("ctrl", "v")

    transpos = pyautogui.locateCenterOnScreen('TranslationStatusPIC.PNG', confidence = 0.9)

    pyautogui.click(transpos.x, transpos.y + 20)
    time.sleep(0.5)
    pyautogui.click(transpos.x, transpos.y + 70)

    time.sleep(0.5)

    
    if (typeTar == 'DidNotPass'):
        failimg = pyautogui.screenshot()
        failimgloc = pyautogui.locateCenterOnScreen('screenshotPIC.PNG', confidence = 0.9)
        failimg = failimg.crop((failimgloc.x-100, failimgloc.y, (failimgloc.x + 800), (failimgloc.y + 700)) )
        scrollLoc = pyautogui.locateCenterOnScreen('ScrollPIC.PNG', confidence = 0.9)
        pyautogui.click(scrollLoc)
        time.sleep(0.2)
        pyautogui.moveTo( pyautogui.locateCenterOnScreen('NextPIC2.PNG', confidence = 0.9))
        time.sleep(0.2)
        pyautogui.click()

    if (typeTar == 'DidPass'):
        passimg = pyautogui.screenshot()
        passimgloc = pyautogui.locateCenterOnScreen('screenshotPIC.PNG', confidence = 0.9)
        passimg = passimg.crop((passimgloc.x-100, passimgloc.y, (passimgloc.x + 800), (passimgloc.y + 700)) )
        scrollLoc = pyautogui.locateCenterOnScreen('ScrollPIC.PNG', confidence = 0.9)
        pyautogui.click(scrollLoc)
        time.sleep(0.3)
        pyautogui.click( pyautogui.locateCenterOnScreen('ExitPIC.PNG', confidence = 0.9) )

window = Tk()

window.geometry('600x1000')

def RunProgram():
    global passimg
    global failimg
    Solve()
    time.sleep(30)
    if(pyautogui.locateOnScreen('BaseDidNotPassTopic.PNG', confidence = 0.9 )):
        print('waiting extra time...')
        time.sleep(5.1)
    Solve()
    time.sleep(0.4)
    
    passimg = passimg.resize((600,430))
    failimg = failimg.resize((600,430))  
    passimg = ImageTk.PhotoImage(passimg)
    failimg = ImageTk.PhotoImage(failimg)
  

    label1 = tkinter.Label(image=passimg)
    label1.image = passimg
    label2 = tkinter.Label(image=failimg)
    label2.image = failimg

    label1.place(x=0, y=130)
    label2.place(x=0, y=540)

    time.sleep(8)
    playsound('brll.mp3')

    print(' ')
    
btn = Button(window, text="Start Program", font=("Arial Bold", 40), command = RunProgram)
btn.grid(column=1, row=0)


window.mainloop()
