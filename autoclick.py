from tkinter import *
import pyautogui, time, keyboard

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Bem Vindo ao AutoClicker')
        self.lbl2=Label(win, text='Off')
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=150)
        self.b1=Button(win, text='Botão Direito', command=self.dir_btn)
        self.b1.place(x=100, y=100)
        self.b2=Button(win, text='Botão Esquerdo', command=self.esc_btn)
        self.b2.place(x=210, y=100)

    def dir_btn(self):
        pyautogui.hotkey('alt','tab')
        #pyautogui.press('i')
        time.sleep(0.2)

        for i in range(50):
            pyautogui.click(button='right', interval=0.05)

        self.lbl2['text'] = 'Off'

    def esc_btn(self):
        pyautogui.hotkey('alt','tab')
        #pyautogui.press('i')
        time.sleep(0.2)

        for i in range(50):
            pyautogui.click(button='left', interval=0.05)

        self.lbl2['text'] = 'Off'

window=Tk()
mywin=MyWindow(window)
window.title('AutoClicker')
window.geometry("400x300+10+10")
window.mainloop()