from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import network
import time

ssid = input("Enter SSID: ")
pw = input("Enter PASS: ")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,pw)
while not wlan.isconnected():
    print(".")
    time.sleep(1)
print(wlan.ifconfig())