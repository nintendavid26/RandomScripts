from ahk import AHK
ahk = AHK(executable_path=r"C:\Program Files\AutoHotkey\AutoHotkey.exe")
block=True
ahk.mouse_move(x=100, y=100, speed=10, blocking=block)
ahk.mouse_move(x=1000, y=100, speed=10, blocking=block)
ahk.mouse_move(x=1000, y=1000, speed=10, blocking=block)
ahk.mouse_move(x=100, y=1000, speed=10, blocking=block)
print(ahk.mouse_position)  #  (100, 100)