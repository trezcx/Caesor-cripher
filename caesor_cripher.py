try:
    import pyperclip
except ImportError:
    print("-")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    print("Do you want to (e)encrypt or (d)decrypt")
    response = input(">").lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break    
    print("Enter e or d")

while True:
    maxKey = len(SYMBOLS) - 1
    print(f"Enter the key (0 to {maxKey}) to use")
    response = int(input(">"))


    if 0 <= response < len(SYMBOLS):
        key = response
        break


print(f"Enter your message to {mode}")
message = input(">")

message = message.upper()

translated = ""


for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        translated += SYMBOLS[num]
    else:
        translated += symbol
    
print(translated)

try:
    pyperclip.copy(translated)
except:
    pass
print(f"Full {mode}ed text copied to clipboard")

