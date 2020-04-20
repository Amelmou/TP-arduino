import serial
import time


NOT_PRESSED = b'0'
PRESSED = b'1'

MAPPING_MORSE_TO_CHAR = {
    "._": "A",
    "_...": "B",
    "_._.": "C",
    "_..": "D",
    ".": "E",
    ".._.": "F",
    "__.": "G",
    "....": "H",
    "..": "I",
    ".___": "J",
    "_._": "K",
    "._..": "L",
    "__": "M",
    "_.": "N",
    "___": "O",
    ".__.": "P",
    "__._": "Q",
    "._.": "R",
    "...": "S",
    "_": "T",
    ".._": "U",
    "..._": "V",
    ".__": "W",
    "_.._": "X",
    "_.__": "Y",
    "__..": "Z",
    ".____": "1",
    "..___": "2",
    "...__": "3",
    "...._": "4",
    ".....": "5",
    "_....": "6",
    "__...": "7",
    "___..": "8",
    "____.": "9",
    "_____": "0"
}



def morse_arduino_to_pc():
    print('entrer votre code morse')
    tempsEcoule = 0
    debut = time.time()
    next_char = NOT_PRESSED
    val = ""
    status = False

    while True:
        char = arduino.read()
        if next_char == NOT_PRESSED and char == PRESSED:
            start = time.time()
            next_char = char

        while char == PRESSED :
            end = time.time()
            tempsEcoule = end - start
        
        # si l'appuie sur le button est > 2s c'est un - 
        # si non c'est un . 
        if next_char == PRESSED and char == NOT_PRESSED:  
            if tempsEcoule > 0.2:
                print("_")
                val += "_"
            else:
                print(".")
                val += "."

            tempsEcoule = 0
            next_char = char
            debut = time.time()
            status = True

        if next_char == NOT_PRESSED and char == NOT_PRESSED and status:
            end_2 = time.time()
            tempsEcoule_2 = end_2 - debut
            if tempsEcoule_2 > 1:
                print(val, " MAPPING_MORSE_TO_CHAR ", MAPPING_MORSE_TO_CHAR.get(val))
                val = ""
                status = False


if __name__ == '__main__':
    print("Initialisation ...")
    arduino = serial.Serial('COM3',9600)
    time.sleep(2)  # wait for the serial connection to initialize

    print('décodage')
    morse_arduino_to_pc()