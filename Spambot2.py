import time
import pyautogui


def main():
    time.sleep(3)

    text = open('spamMessage.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')


main()
