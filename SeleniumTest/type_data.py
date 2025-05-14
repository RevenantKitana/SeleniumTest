import time

def typedata(element, text, delay=0.075):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)
