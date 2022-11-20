from playsound import playsound
from time import sleep

data = {
    "a": "10",
    "b": "0111",
    "c": "0101",
    "d": "011",
    "e": "1",
    "f": "1101",
    "g": "001",
    "h": "1111",
    "i": "11",
    "j": "1000",
    "k": "010",
    "l": "1011",
    "m": "00",
    "n": "01",
    "o": "000",
    "p": "1001",
    "q": "0010",
    "r": "101",
    "s": "111",
    "t": "0",
    "u": "110",
    "v": "1110",
    "w": "100",
    "x": "0110",
    "y": "0100",
    "z": "0011",
    "1": "10000",
    "2": "11000",
    "3": "11100",
    "4": "11110",
    "5": "11111",
    "6": "01111",
    "7": "00111",
    "8": "00011",
    "9": "00001",
    "0": "00000",
    "?": "110011",
    "!": "010100",
    ".": "101010",
    ",": "001100",
    ";": "010101",
    ":": "000111",
    "+": "10101",
    "-": "0011110",
    "/": "01101",
    "=": "01110",
    " ": "111111"
}

message = input("Ingrese el mensaje a traducir: ")
tras = []

for i in message.lower():
    tras.append(data[i])

for j in range(len(tras)):
    print(message[j] + " - " + data[message[j].lower()])
    for x in tras[j]:
        if(x == "1"):
            playsound('assets\short.mp3')
        elif(x == "0"):
            playsound('assets\long.mp3')
    sleep(0.7)
