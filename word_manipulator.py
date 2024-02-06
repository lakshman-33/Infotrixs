#import argparse module
import argparse
#create function to count word occurences in the text
def count_word_occurrences(text, target_word):
    return text.lower().count(target_word.lower())
#create function to replace word in the text
def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)
#create main function that perfoms main action
def main():
#intialize the try block  
# add the arguments 
# use if statement pass the arguments  
    try:
        parser = argparse.ArgumentParser(description="Word Manipulation Utility")
        parser.add_argument("input_file", type=argparse.FileType('r'), help="Input text file for manipulation")
        parser.add_argument("--count", help="Count occurrences of a word in the text")
        parser.add_argument("--replace", nargs=2, help="Replace occurrences of a word with another word")
        
        
        args = parser.parse_args()
        with args.input_file as file:
            input_text = file.read()
        
        manipulated_text = input_text
        
        if args.count:
            count = count_word_occurrences(manipulated_text, args.count)
            print(f"'{args.count}' appears {count} times in the text.")
        
        if args.replace:
            old_word, new_word = args.replace
            manipulated_text = replace_word(manipulated_text, old_word, new_word)
        
        print("Manipulated Text:", manipulated_text)
#intialize the exception block    
    except Exception as e:
        print("An error occurred:", e)

#calling the main function
if __name__ == "__main__":
    main()
