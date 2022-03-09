import pyautogui
import time
import os
import pathlib


T = .4

def check(times):
	if times >= 0:
		folder = pyautogui.locateOnScreen('folder.png')
		try:
			pyautogui.moveTo(folder.left, folder.top)
			pyautogui.click(button='right')
			time.sleep(T)

			send = pyautogui.locateCenterOnScreen("send.png")
			pyautogui.moveTo(send.x, send.y)
			pyautogui.click()
			time.sleep(T)
			
			zip = pyautogui.locateCenterOnScreen('zip.png')
			pyautogui.moveTo(zip.x, zip.y)
			pyautogui.click()

			pyautogui.moveTo(folder.left, folder.top)
			pyautogui.click(button='right')
			time.sleep(T)

			
			deel = pyautogui.locateCenterOnScreen('del.png')
			pyautogui.moveTo(deel.x, deel.y)
			pyautogui.click()
			print(times)
		except:
			pass
	else:
		return False


if __name__ == "__main__":

	times = input("How many times to zip:")
	times = int(times)
	while True:
		times -= 1
		if check(times) is False:
			break
	print("Done!")