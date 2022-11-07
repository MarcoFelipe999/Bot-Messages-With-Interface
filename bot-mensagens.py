from time import sleep
import pyautogui
from PySimpleGUI import (
    Window, Button,Text, Image, Input, Column, Push, theme)

theme("Black")
layout_esquerda = [
    [Image(filename='botmes.png')]
]
layout_direita = [
    [Text("Mensagem do Bot"), Input()],
    [Button('Enviar Mensagem'), Push()],
    [Image(filename = 'funciona_resized.png'), Push()],
]
layout = [
    [Column(layout_esquerda), Column(layout_direita)]
]
window = Window(
    'Bot messenger',
    layout = layout,
    element_justification='c'
)
while True:
    event,values = window.read()
    match (event):
        case 'Enviar Mensagem':
            for i in range(10):  # Quantidade de mensagens
                sleep(1)
                pyautogui.typewrite(values[1])
                sleep(1)
                pyautogui.press("enter")  # Assim que a mensagem for digitada irá apertar enter automaticamente

        case None:
            break
    window.close()

