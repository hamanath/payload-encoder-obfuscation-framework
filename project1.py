import base64
import random
import codecs

#ENCODING 
def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def xor_encode(text, key=5):
    return ''.join(chr(ord(c) ^ key) for c in text)

def rot13_encode(text):
    return codecs.encode(text, 'rot_13')

#OBFUSCATION
def add_noise(text):
    noise = ''.join(random.choice('xyz123') for _ in range(3))
    return text + noise

def reverse_text(text):
    return text[::-1]

def split_text(text):
    return ' '.join(text)

#DETECTION
def detect(payload):
    patterns = ["malware", "attack", "virus", "hack"]
    for p in patterns:
        if p in payload.lower():
            return "Detected"
    return "Not Detected"


#MENU
while True:
    print("\n  PAYLOAD TOOL MENU ")
    print("1. Encode Payload")
    print("2. Obfuscate Payload")
    print("3. Detect Payload")
    print("4. Full Analysis (Best)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter payload: ")
        print("\nBase64:", base64_encode(text))
        print("XOR:", xor_encode(text))
        print("ROT13:", rot13_encode(text))

    elif choice == "2":
        text = input("Enter payload: ")
        print("\nReversed:", reverse_text(text))
        print("With Noise:", add_noise(text))
        print("Split:", split_text(text))

    elif choice == "3":
        text = input("Enter payload: ")
        print("\nDetection Result:", detect(text))

    elif choice == "4":
        text = input("Enter payload: ")

        print("\n--- ORIGINAL ---")
        print(text)
        print("Detection:", detect(text))

        b64 = base64_encode(text)
        print("\n--- BASE64 ---")
        print(b64)
        print("Detection:", detect(b64))

        xor = xor_encode(text)
        print("\n--- XOR ---")
        print(xor)
        print("Detection:", detect(xor))

        rot = rot13_encode(text)
        print("\n--- ROT13 ---")
        print(rot)
        print("Detection:", detect(rot))

        obs = add_noise(reverse_text(text))
        print("\n--- OBFUSCATED ---")
        print(obs)
        print("Detection:", detect(obs))

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")