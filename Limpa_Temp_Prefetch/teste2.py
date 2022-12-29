"""
    Desativar/ativar windows defender
"""

import wmi, os

# Desativa Windows defender
os.system('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /V DisableAntiSpyware /t REG_DWORD /D 1 /F ')


# Ativa Windows defender