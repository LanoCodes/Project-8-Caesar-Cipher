from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '~','`','!','@','#','$','%','^','&','*','(',')','_','+','-','=','?', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '~','`','!','@','#','$','%','^','&','*','(',')','_','+','-','=', '?']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for char in start_text:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
        
    print(f"\nHere's the {cipher_direction}d result: {end_text}\n")

caesar_cont = 'yes'
  
while caesar_cont == 'yes':
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  
  if shift > 26:
    shift %= 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  caesar_cont = input('Want to continue? Type "yes". If not, type "no"\n')
print('\nEt tu, Brute?....')