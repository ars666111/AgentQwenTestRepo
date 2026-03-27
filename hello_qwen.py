#!/usr/bin/env python3
"""Анимированный 'Hello Qwen' - буквы меняются по порядку"""

import sys
import time

def animate_hello_qwen():
    text = "hello qwen"
    length = len(text)
    
    # Анимация: сначала заглавные по порядку, потом строчные по порядку
    while True:
        # Делаем буквы заглавными по очереди слева направо
        for i in range(length):
            animated_text = ""
            for j, char in enumerate(text):
                if j <= i:
                    animated_text += char.upper()
                else:
                    animated_text += char
            # Возвращаем курсор в начало строки и выводим текст
            sys.stdout.write('\r' + animated_text)
            sys.stdout.flush()
            time.sleep(0.1)
        
        # Делаем буквы строчными по очереди слева направо
        for i in range(length):
            animated_text = ""
            for j, char in enumerate(text):
                if j <= i:
                    animated_text += char.lower()
                else:
                    animated_text += char.upper()
            # Возвращаем курсор в начало строки и выводим текст
            sys.stdout.write('\r' + animated_text)
            sys.stdout.flush()
            time.sleep(0.1)

if __name__ == "__main__":
    try:
        animate_hello_qwen()
    except KeyboardInterrupt:
        # Чистый выход при нажатии Ctrl+C
        sys.stdout.write('\n')
        sys.stdout.flush()
