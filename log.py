Traceback (most recent call last):
  File "anime.py", line 45, in <module>
    irc.connect(server,channel,nickname)
  File "anime.py", line 31, in connect
    self.irc.connect((server, 6697))                                                         #connects to the server
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
