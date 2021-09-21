#!/usr/bin/python

import smbus
import PySimpleGUI as sg
import time
bus = smbus.SMBus(1)
address = 0x07
cmd = 0x01

def ConvertStringToBytes(src):
    converted = []
    for b in src:
        converted.append(ord(b))
    return converted

layout = [
    [sg.Text('Winkel und Radius eingeben')],
    [sg.Text('Winkel'), sg.InputText(key="degree")],
    [sg.Text('Radius'), sg.InputText(key="radius")],
    [sg.Button('Senden')]
]

window = sg.Window("Roundbot",layout)
bytesToSend = ConvertStringToBytes("Hello")
bus.write_i2c_block_data(address,cmd,bytesToSend)

while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    print('Folgende Eingabe erkannt:')
    print(values['degree'],values['radius'])
    degree = values["degree"]
    radius = values["radius"]
    senddeg = ConvertStringToBytes(degree)
    sendrad = ConvertStringToBytes(radius)
    data = ""
    bus.write_i2c_block_data(address,len(senddeg),senddeg)
    bus.write_i2c_block_data(address,len(sendrad),sendrad)
window.close()
