#Task 1: Reverse a String
#HINT: Review the Algorithms + Problem Solving Lecture!)
#Write code that takes a string as input and returns the string reversed
#i.e. “Hello” will be returned as “olleH

word = input('provide a word')

def reverse_word(word):
    reversed_word = ""     
    last_index = len(word) - 1
    for index in range(last_index, -1, -1):
        reversed_word += word[index]
        
    print(reversed_word)


    
reversed_word = reverse_word(word)


#Task 2: Capitalize a Letter
#Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World

#Thoughts:  split "hello world" into two words and capitalize first letter --- found a function doing research that created something similar to a title

the_given_string = input('proved a multi-word string    ')

def capitalize_first_letter(the_given_string):
    capitalized_words = the_given_string.title()
    print(capitalized_words)     
      

capitalized_words = capitalize_first_letter(the_given_string)

#Task 3: Palindrome
#A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	
#Write code that takes a user input and checks to see if it is a Palindrome and reports the result
#thoughts:  take a word, flip it and reverse it and then compare to see if it matches original.  if it matches it is a pallindrome
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




