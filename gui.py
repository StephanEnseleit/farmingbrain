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
    [sg.Text('Höhe'), sg.InputText(key="height")],
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
    print(values['degree'],values['radius'],height['height'])
    degree = values["degree"]
    radius = values["radius"]
    height = values["height"]
    senddeg = ConvertStringToBytes(degree)
    sendrad = ConvertStringToBytes(radius)
    sendh = ConvertStringToBytes(height)
    data = []
    # 0 indicates degree value being sent
    # 1 indicates radius value being sent
    bus.write_i2c_block_data(address,0,senddeg)
    bus.write_i2c_block_data(address,1,sendrad)
    bus.write_i2c_block_data(address,2,sendh)
window.close()
