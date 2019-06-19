import socket
import sys
import datetime
import webbrowser
import requests
import bs4

#res = requests.get('https://xdcc.horriblesubs.info/',headers = {'User-agent': 'your bot 0.1'})
#res.raise_for_status()

print(datetime.datetime.today().weekday())

channel = "#horriblesubs"
server = "irc.ircii.net"
nickname = "nintendavid"

searchDays={6:"shingeki",4:"jojo"}

class IRC:
    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "n")

    def connect(self, server, channel, botnick):
        #defines the socket
        print ("connecting to:"+server)
        self.irc.connect((server, 6697))                                                         #connects to the server
        self.irc.send("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot!n") #user authentication
        self.irc.send("NICK " + botnick + "n")               
        self.irc.send("JOIN " + channel + "n")        #join the chan

    def get_text(self):
        text=self.irc.recv(2040)  #receive the text

        if text.find('PING') != -1:                      
            self.irc.send('PONG ' + text.split() [1] + 'rn') 

        return text

irc = IRC()
irc.connect(server,channel,nickname)