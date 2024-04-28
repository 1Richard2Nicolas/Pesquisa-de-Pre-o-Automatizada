import pyautogui

pyautogui.click(1777, 21, button=("left"))
pyautogui.sleep(1)

# Salvar o arquivo e fechar
pyautogui.click(147, 976, button=("left"))
pyautogui.sleep(2)
pyautogui.hotkey("ctrl", "b")
pyautogui.sleep(6)
pyautogui.hotkey("alt", "f4")
pyautogui.sleep(1)

# Abrir o outlook
pyautogui.press("win")
pyautogui.sleep(1)
pyautogui.write("Outlook")
pyautogui.sleep(1)
pyautogui.press("enter")
pyautogui.sleep(1)

# Aqui a execução estará colocando a janela e uma posição padrão (full screen) para que seja continuada a execução com os campos certos.
pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
pyautogui.click(936, 946, button='left')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'down')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'down')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
# Finalizando aqui...

# Começar novo e-mail
pyautogui.click(81, 109, button=("left"))
pyautogui.sleep(5)

# Aqui a execução estará colocando a janela e uma posição padrão (full screen) para que seja continuada a execução com os campos certos.
pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
pyautogui.click(614, 16, button='left')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'down')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'down')
pyautogui.sleep(1)
pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
# Finalizando aqui...

# Mudar formatação e corpo do e-mail

pyautogui.click(287, 22, button=("left"))
pyautogui.sleep(1)
pyautogui.click(542, 21, button=("left"))
pyautogui.sleep(1)
pyautogui.click(54, 324, button=("left"))
pyautogui.sleep(1)
pyautogui.click(798, 21, button=("left"))
pyautogui.sleep(1)
pyautogui.click(789, 138, button=("left"))
pyautogui.sleep(1)
pyautogui.click(214, 20, button=("left"))
pyautogui.sleep(1)
pyautogui.click(308, 196, button=("left"))
pyautogui.sleep(1)
pyautogui.press("backspace")
pyautogui.press("backspace")
pyautogui.press("backspace")
pyautogui.press("backspace")
pyautogui.press("backspace")
pyautogui.sleep(1)

# Endereçar o e-mail
# Título do e-mail
pyautogui.click(82, 747, button=("left"))
pyautogui.click(82, 747, button=("left"))
pyautogui.click(82, 747, button=("left"))
pyautogui.hotkey('ctrl', 'x')
pyautogui.sleep(1)
pyautogui.click(317, 277, button=("left"))
pyautogui.hotkey('ctrl', 'v')

# Remetentes
pyautogui.click(82, 747, button=("left"))
pyautogui.click(82, 747, button=("left"))
pyautogui.click(82, 747, button=("left"))
pyautogui.hotkey('ctrl', 'x')
pyautogui.sleep(1)
pyautogui.click(506, 178, button=("left"))
pyautogui.hotkey('ctrl', 'v')

# Cópias
pyautogui.click(82, 747, button=("left"))
pyautogui.click(82, 747, button=("left"))
pyautogui.click(82, 747, button=("left"))
pyautogui.hotkey('ctrl', 'x')
pyautogui.sleep(1)
pyautogui.click(503, 226, button=("left"))
pyautogui.hotkey('ctrl', 'v')

pyautogui.sleep(1)
pyautogui.click(936, 946, button=("left"))
pyautogui.press("backspace")
pyautogui.press("backspace")
pyautogui.sleep(10)

# Copiar o arquivo para o e-mail
pyautogui.click(245, 61, button=("left"))
pyautogui.sleep(1)
pyautogui.click(102, 106, button=("left"))
pyautogui.sleep(1)
pyautogui.click(222, 197, button=("left"))

# Enviar o e-mail
pyautogui.sleep(1)
pyautogui.click(60, 202, button=("left"))