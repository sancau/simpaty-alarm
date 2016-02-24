#usings
import colorama
import ctypes
import time
import winsound

#init
colorama.init()

#title
print(colorama.Fore.GREEN +
      'ИДЁТ МОНИТОРИНГ SIMPATY. ТРЕВОГИ НЕ ОБНАРУЖЕНЫ\n')

#variables

#signals if the event was catched during the current program runtime
alarmPerforming = False
 
#get data from os windows
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool,
                                     ctypes.POINTER(ctypes.c_int),
                                     ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        titles.append(buff.value)
    return True

#on catch window event
def performAlarm():
 
    alarmPerforming = True

    while True:
        print(colorama.Fore.RED +
              'ВНИМНИЕ! ТРЕВОГА СИМПАТИ! ПРОВЕРЬ КАМЕРУ!')
        Freq = 2500 # Set Frequency To 2500 Hertz
        Dur = 1000 # Set Duration To 1000 ms == 1 second
        winsound.Beep(Freq,Dur)
        time.sleep(1)                     	   

#main detecting cycle 
while not alarmPerforming:   
    titles = []
    EnumWindows(EnumWindowsProc(foreach_window), 0)

    #based on S!MPATY alarm message title
    for item in titles:
        if 'Message:' in item:
            if not alarmPerforming:
                performAlarm()
    time.sleep(1)   
