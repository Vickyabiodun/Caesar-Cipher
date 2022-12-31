<h1>Caesar Cipher</h1>

<p>Welcome to the Caesar Cipher tutorial! In this tutorial, we will go over the code for a Caesar Cipher, which is a simple form of encryption that involves shifting the letters of a message a certain number of places down the alphabet.</p>

<h2>Getting Started</h2>

<p>To begin, let's go over the code imports and variables at the top of the script:</p>

<pre><code>#import the cipher logo
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
</code></pre>

<p>Here, we are importing the <code>logo</code> variable from the <code>art</code> library, which is just a simple ASCII art representation of the word "Caesar Cipher". We are also creating a variable <code>alphabet</code> which is a list of the letters of the alphabet, repeated three times. This is done because we want to make sure that we have enough letters to shift to in the event that the shift amount is larger than the length of the alphabet.</p>

<h2>The Caesar Cipher Function</h2>

<p>Next, let's go over the main Caesar Cipher function:</p>

<pre><code>def caesar(start_text, shift_amount, cipher_direction):
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
        new_position = position
shift_amount
end_text += alphabet[new_position]

print(f"Here's the {cipher_direction}d result: {end_text}")
</code></pre>

<p>This function takes three arguments:</p>
<ul>
  <li><code>start_text</code>: the message that we want to encrypt or decrypt</li>
  <li><code>shift_amount</code>: the number of places that we want to shift the letters of the message</li>
  <li><code>cipher_direction</code>: a string that specifies whether we want to "encode" (encrypt) or "decode" (decrypt) the message</li>
</ul>
<p>The function starts by creating an empty string called <code>end_text</code>, which we will use to store the encrypted or decrypted message.</p>
<p>Next, we have a conditional statement that checks the value of <code>cipher_direction</code>. If it is "decode", we multiply the shift amount by -1. This is because to decrypt a message, we need to shift the letters in the opposite direction of the original encryption.</p>
<p>After that, we have a <code>for</code> loop that iterates over each character in <code>start_text</code>. If the character is not a letter (i.e. it is a symbol, a space, or some other non-letter character), we simply add it to <code>end_text</code> without modifying it. Otherwise, we find the position of the letter in the <code>alphabet</code> list, add the shift amount to it, and use that new position to determine the letter that we will add to <code>end_text</code>.</p>
<p>Finally, we print out the encrypted or decrypted message along with a message indicating whether it was encoded or decoded.</p>
<h2>The Main Loop</h2>
<p>The rest of the code is a loop that allows the user to keep encrypting or decrypting messages until they choose to stop:</p>
<pre><code>end_game=False
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
</code></pre>
<p>The loop starts by setting the variable <code>end_game</code> to <code>False</code>. As long as <code>end_game</code> is <code>False</code>, the loop will continue to run. Inside the loop, we prompt the user for the direction (encode or decode), the message, and the shift amount. We also convert the shift amount to modulus form using the <code>%</code> operator, which ensures that it is always between 0 and 25 (since there are 26 letters in the alphabet). This is useful in case the user enters a shift amount that is larger than 26.</p>

<p>After that, we call the <code>caesar</code> function with the appropriate arguments and print out the result. Finally, we prompt the user to either continue or exit the loop, and we update the value of <code>end_game</code> accordingly.</p>
<h2>Conclusion</h2>
<p>That's it! You now know how the Caesar Cipher works and how to use the code provided.</p>
<p>I hope this tutorial was helpful! If you have any questions or need further clarification, feel free to ask.</p>


