def ispalindrome(text):
    text=text.lower().replace(" ","")
    return text == text[::-1]

word = input("Lest try your word: ")

if ispalindrome(word):

    print("It is a palindrome")
else:
    print("It is not a palindrome")