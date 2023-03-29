word = input('provide a word   ')

def reverse_word(word):
    reversed_word = ""     
    last_index = len(word) - 1
    for index in range(last_index, -1, -1):
        reversed_word += word[index]
        
    return(reversed_word)

reversed_word = reverse_word(word)

def verifying_palindrome(word, reversed_word):
    confirmation = word == reversed_word
    if confirmation == True:
            print('Palindrome')
    else:
         print("not Palindrome")


verifying_palindrome(word, reversed_word)



