from ctypes import *
import ctypes
import os
def Connect_DLL():
    try:
        dllpath = os.path.join(os.path.dirname(__file__), 'dll\\csfml-audio-2.dll')
        bassdll = cdll.LoadLibrary(dllpath)
        return bassdll
    except:
        raise FileNotFoundError or ModuleNotFoundError or RuntimeError("Not Founded CSFML Audio Version 2(Or Modules for This DLL is not Founded!!!)")

def SetMusic_UINT16_FromFile(filename) -> c_int32:
    return Connect_DLL().sfMusic_createFromFile(filename)

def SetMusic_UINT16_FromStream(stream : c_int32) -> c_int32:
    return Connect_DLL().sfMusic_createFromStream(stream)

def PlayMusic(music : c_int32):
    Connect_DLL().sfMusic_play(music)

def SetLoop(music : c_int32, isLoop : bool):
    Connect_DLL().sfMusic_setLoop(music, isLoop)

def DestroyMusic(musicstream : c_int32):
    Connect_DLL().sfMusic_destroy(musicstream)

def Stop_Music(music_stream : c_int32):
    Connect_DLL().sfMusic_stop(music_stream)