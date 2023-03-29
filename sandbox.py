#Task 1: Reverse a String
#HINT: Review the Algorithms + Problem Solving Lecture!)
#Write code that takes a string as input and returns the string reversed
#i.e. “Hello” will be returned as “olleH


#Task 2: Capitalize a Letter
#Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World

#Thoughts:  split "hello world" into two words and capitalize first letter --- found a function doing research that created something similar to a title



#Task 3: Palindrome
#A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	
#Write code that takes a user input and checks to see if it is a Palindrome and reports the result
#thoughts:  take a word, flip it and reverse it and then compare to see if it matches original.  if it matches it is a pallindrome
   


#Bonus Challenge
#Task 4 : Compress a string of characters
#For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"
#counts the letters and puts it as and puts it in front, before going to next letter

#create a string for the compressed






oringial_string = 'mmeeyynnaarrdddd'

def compress_string(original_string):
    count_of_letters = 1
    compressed_string = ""
    last_index = len(original_string) - 1
 


    for index in range(len(original_string)):
        
#taking each letter and counting if there are repeats as it passes throught the string
        if index == last_index - 1:
            if original_string[last_index -1] == original_string[last_index]:
               count_of_letters += 1
               compressed_string = compressed_string + str(count_of_letters) + original_string[index]
             

            elif oringial_string[last_index - 1] != oringial_string[last_index]:
                count_of_letters += 1
                compressed_string = compressed_string + str(count_of_letters) + original_string[index]
#put the return and print here to end the loop to avoid erroring out as index passes through stru=ing to avoid comparing last index

            print(compressed_string)
            return(compressed_string)

                
        elif original_string[index] == oringial_string[index + 1]:
            count_of_letters += 1               

#if letter is not repeated, only adds the count and the letter as compressed string
        else:
            compressed_string = compressed_string + str(count_of_letters) + original_string[index]
            count_of_letters = 1

compress_string(oringial_string)



