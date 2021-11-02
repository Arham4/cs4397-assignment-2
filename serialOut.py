#serialOut consists of functions to send serial commands to the train system
#serialOut doesn't need MessageQueues since there is no communication between tasks or threads

#9600 baud
#COM1
#FORMAT
##{OFE} {W1} {W2}

#RING, START, ACCELERATE, MOVE, DECELERATE, STOP
#RING
#START
#ACCELERATE, DECELERATE
#MOVE, STOP

#                       c         c   eng num  com  data
#ENGINE COMMAND (BITS) {11111110}{00}{AAAAAAA}{CC}{DDDDD}

import math

import serial

def formatSerial(kind, addr, com, data):
    if kind > 3:
        kindLen = math.floor(math.log(kind, 2))+1
    else:
        kindLen = 2

    assert math.floor(math.log(addr, 2))+1+kindLen <= 9, "Kind and addr are too large to format together"

    bytes = []
    bytes.append(0xFE)
    bytes.append((kind << (8-kindLen)) | (addr >> 1))
    bytes.append((((addr % 2) << 7) | (com << 5) | data))
    return bytearray(bytes)

key = {
"kind":{"switch":0b1, "route":0b11, "engine":0b0, "train":0b11001, "accessory":0b10, "group":0b11000},
"command":{"action":0b0, "extended":0b1, "relativespeed":0b10, "absolutespeed":0b11}
}

trainId = 23

commands = {
"bell":formatSerial(key['kind']['engine'], trainId, key['command']['action'], 0b11101),
"forwardDir":formatSerial(key['kind']['engine'], trainId, key['command']['action'], 0b0),
"decelerate":formatSerial(key['kind']['engine'], trainId, key['command']['relativespeed'], (-2)+5),
"accelerate":formatSerial(key['kind']['engine'], trainId, key['command']['relativespeed'], (2)+5),
"move":formatSerial(key['kind']['engine'], trainId, key['command']['absolutespeed'], 0b1000),
"halt":bytearray([0xFE, 0xFF, 0xFF]),
"start":formatSerial(key['kind']['engine'], trainId, key['command']['action'], 0b0),
"stop":formatSerial(key['kind']['engine'], trainId, key['command']['absolutespeed'], 0x0)
}

def sendSerial(serialData):
    port = serial.Serial('COM1', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

    try:
        port.write(serialData)
        port.flush()
    except:
        print("Unable to send command. The port was not configured properly.")

def sendCommand(nickname):
    sendSerial(commands[nickname])
