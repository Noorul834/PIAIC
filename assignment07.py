# 7. Vowel Tester
# Write a Python program to test whether a passed letter is a vowel or not
# Program Console Output 1:
# Enter a character: A
# Letter A is Vowel
# Program Console Output 2:
# Enter a character: e
# Letter e is Vowel
# Program Console Output 2:
# Enter a character: N
# Letter N is not Vowel

vowels=["a", "A","e", "E","i","I,","o","O","u","U"]
letter=input("Enter a sound: ")
if letter in vowels :
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is not a vowel")