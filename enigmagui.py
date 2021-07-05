import tkinter as tk
from collections import deque

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.startWidgets()

    def startWidgets(self):
        self.encryptMessage = tk.Button(self)
        self.encryptMessage['text'] = 'ENCRYPT'
        self.encryptMessage['command'] = self.encryptWidgets
        self.encryptMessage.config(width=10, height=2)
        self.encryptMessage.pack(side='top', padx=10, pady=10)

        self.decryptMessage = tk.Button(self)
        self.decryptMessage['text'] = 'DECRYPT'
        self.decryptMessage['command'] = self.decryptWidgets
        self.decryptMessage.config(width=10, height=2)
        self.decryptMessage.pack(side='top', padx=10, pady=10)

        self.quit = tk.Button(self, text='QUIT', fg='red', command=self.master.destroy)
        self.quit.config(width=10, height=2)
        self.quit.pack(side='bottom', padx=10, pady=10)

    def encryptWidgets(self):
        self.encryptMessage.pack_forget()
        self.decryptMessage.pack_forget()

        self.encryptLabel = tk.Label(self, text='Message you would like to encrypt:')
        self.encryptLabel.pack(side='top', padx=10, pady=10)

        self.encryptEntry = tk.Entry(self)
        self.encryptEntry.pack(side='top', padx=10, pady=10)

        self.EsubmitButton = tk.Button(self, text='SUBMIT', command=self.encrypt)
        self.EsubmitButton.config(width=10, height=2)
        self.EsubmitButton.pack(side='bottom', padx=10, pady=10)

    def decryptWidgets(self):
        self.encryptMessage.pack_forget()
        self.decryptMessage.pack_forget()

        self.decryptLabel = tk.Label(self, text='Message you would like to decrypt:')
        self.decryptLabel.pack(side='top', padx=10, pady=10)
        
        self.decryptEntry = tk.Entry(self)
        self.decryptEntry.pack(side='top', padx=10, pady=10)

        self.DsubmitButton = tk.Button(self, text='SUBMIT', command=self.decrypt)
        self.DsubmitButton.config(width=10, height=2)
        self.DsubmitButton.pack(side='bottom', padx=10, pady=10)

    def encrypt(self):
        self.encryptLabel.pack_forget()
        self.encryptEntry.pack_forget()
        self.EsubmitButton.pack_forget()

        message = self.encryptEntry.get()
        splitMsg = list(message)
        encryptedMsg = []
        for char in splitMsg:
            if char.isalpha():
                letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                letterIndex = letters.index(char.lower())
                algro = (len(message) + 26) % 26
                if algro == 0:
                    algro = 1
                encryptedLetter = self.shift(letters, algro)
                encryptedMsg.append(encryptedLetter[letterIndex])
            elif char.isdigit():
                numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                numberIndex = numbers.index(char)
                algro = (len(message) + 10) % 10
                if algro == 0:
                    algro = 1
                encryptedNumber = self.shift(numbers, algro)
                encryptedMsg.append(encryptedNumber[numberIndex])
            else:
                encryptedMsg.append(char)

        self.msg = ''.join(encryptedMsg)
        self.display()

    def decrypt(self):
        self.decryptLabel.pack_forget()
        self.decryptEntry.pack_forget()
        self.DsubmitButton.pack_forget()

        message = self.decryptEntry.get()
        splitMsg = list(message)
        decryptedMsg = []
        for char in splitMsg:
            if char.isalpha():
                letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                letterIndex = letters.index(char.lower())
                algro = (len(message) + 26) % 26
                if algro == 0:
                    algro = 1
                decryptedLetter = self.shift(letters, 0 - algro)
                decryptedMsg.append(decryptedLetter[letterIndex])
            elif char.isdigit():
                numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                numberIndex = numbers.index(char)
                algro = (len(message) + 10) % 10
                if algro == 0:
                    algro = 1
                decryptedNumber = self.shift(numbers, 0 - algro)
                decryptedMsg.append(decryptedNumber[numberIndex])
            else:
                decryptedMsg.append(char)

        self.msg = ''.join(decryptedMsg)
        self.display()

    def shift(self, aList, number):
        rotatedList = deque(aList)
        rotatedList.rotate(number)
        return list(rotatedList)

    def display(self):
        self.msgEntryText = tk.StringVar()
        self.msgEntry = tk.Entry(self, state='readonly', textvariable=self.msgEntryText)
        self.msgEntryText.set(self.msg)
        self.msgEntry.pack(side='top', padx=10, pady=10)

        self.msgCopy = tk.Button(self)
        self.msgCopy['text'] = 'COPY'
        self.msgCopy['command'] = self.copy
        self.msgCopy.config(width=10, height=2)
        self.msgCopy.pack(side='top', padx=10, pady=10)

        self.restartButton = tk.Button(self)
        self.restartButton['text'] = 'RESTART'
        self.restartButton['command'] = self.restart
        self.restartButton.config(width=10, height=2)
        self.restartButton.pack(side='top', padx=10, pady=10)

    def copy(self):
        root.clipboard_clear()
        root.clipboard_append(self.msg)
        root.update()

    def restart(self):
        self.msgEntry.pack_forget()
        self.msgCopy.pack_forget()
        self.restartButton.pack_forget()
        self.quit.pack_forget()

        self.startWidgets()

root = tk.Tk()
root.geometry('300x300')
root.title('Enigma GUI')
app = Application(master=root)
app.mainloop()