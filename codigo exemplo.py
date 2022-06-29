import pyautogui as pi
from time import sleep

lista = []

email = input('Digite seu email: ')
senha = input('Digite sua senha: ')
sleep(2)
pi.press('win')
sleep(2)
pi.write('google chrome')
sleep(2)
pi.press('enter')
sleep(5)
pi.click(1195, 129, duration=5)
sleep(2)
pi.press('enter')
sleep(5)
pi.write(email)
sleep(2)
pi.press('enter')
sleep(2)
pi.write(senha)
sleep(2)
pi.press('enter')
sleep(5)
pi.click(77, 210)
for i in range(len(lista)):
    sleep(5)
    pi.write(lista[i])
    sleep(2)
    pi.press('tab')
    sleep(2)
pi.press('tab')
sleep(2)
pi.write('Trabalho pyautogui')
sleep(2)
pi.press('tab')
sleep(2)
pi.write('teste')
sleep(2)
pi.hotkey('Ctrl', 'enter')


