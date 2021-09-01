import os
import time
import app_manager

client=app_manager.AppManager()
client.join_sys(__file__)



while True:
	time.sleep(1)
	print(__file__," running")

	pass