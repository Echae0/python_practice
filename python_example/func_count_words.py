def count_words(sentence):
    words = sentence.split()
    return print("단어 수: ", len(words))
    
    
if __name__ == "__main__":
    count_words("Hello World!")
    count_words("Python is a very good programming language.")
    count_words("How are you?")