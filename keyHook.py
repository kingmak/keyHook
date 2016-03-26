import platform

def winHook():
    try:
        import win32api
    except ImportError:
        raise ImportError('win32api needs to be installed')

    while True:
        for i in range(33, 127):
            if win32api.GetAsyncKeyState(i) == -32767:
                print chr(i)
                
def osxHook():
    print 'OSX KEY HOOK'

def linuxHook():
    print 'LINUX KEY HOOK'

def getKeys():
    _platform = platform.platform()

    if 'Windows' in _platform:
        winHook()

    elif 'Darwin' in _platform:
        osxHook()

    elif 'Linux' in _platform:
        linuxHook()

    else:
        raise Exception('Platform not supported')
