import ctypes
import winreg


path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

with winreg.OpenKey(
    winreg.HKEY_CURRENT_USER,
    path,
    0,
    winreg.KEY_READ | winreg.KEY_WRITE,
) as key:
    current_theme, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
    new_theme = 0 if current_theme else 1

    winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, new_theme)
    winreg.SetValueEx(key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, new_theme)

ctypes.windll.user32.SendMessageW(
    0xFFFF,
    0x001A,
    0,
    "ImmersiveColorSet",
)

print("Tema alterado para", "claro." if new_theme else "escuro.")