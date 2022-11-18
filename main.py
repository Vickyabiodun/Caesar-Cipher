#import the cipher logo
from art import logo

#create a variable alphabet with the alphabet repeated because if the word starts with z, it will throw error as the shift wouldnt be able to find any more letter
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]

#print the logo
print(logo)


#the function takes three parameter which determines the message, the shift amount and check if they are encodimg or decoding
def caesar(start_text, shift_amount, cipher_direction):
    #create a string that we'll be concatenating the input with
    end_text = ""
    #conditional statement to determine the direction of the shift
    if cipher_direction == "decode":
        shift_amount *= -1
    #this line check if its a symbol, a space or non-letter character so as to retain them in their original position    
    for char in start_text:
        if char not in alphabet:
            end_text += char
        #the index gives the number the letter ocuppies which is now being added to the shift to the determine the position of the new letter
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
        
    print(f"Here's the {cipher_direction}d result: {end_text}")


#to determine if the game should continue or not after the first run, the function is called in a while loop with the end of game variable set to false.
    
end_game=False
while not end_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #the shift is converted to modulus form because of high number entry since we cannot control the shift value that will be inputed
    shift = shift % 26

    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    #to determine if the game should keep rolling or start over
    start_over = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    if start_over == 'no':
            end_game=True
            print('Goodbye')
    else:
      end_game=False
