import ctypes
import sys
import time


def suspender_windows():
    if sys.platform != "win32":
        raise SystemExit("Este script funciona apenas no Windows.")

    print("Suspendendo o Windows em 2 segundos...")
    time.sleep(2)

    resultado = ctypes.windll.powrprof.SetSuspendState(False, True, False)

    if resultado == 0:
        raise ctypes.WinError()


if __name__ == "__main__":
    suspender_windows()