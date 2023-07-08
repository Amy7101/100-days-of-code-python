# def square(a):
#     return a**2
# print(square(int(input("Please enter a value "))))


# # Sub- string test
# inp1 = input("Please provide the string value ")
# inp2 = input("Enter sub-string ")

# if inp2 in inp1:  # use of in in python
#     print("Yes it is sub string ")
# else:
#     print("NO it is not sub string ")

# Vowel test 
inp3 = input("Please provide the string value ")
count = 0
for i in range(len(inp3)):

    if inp3[i] in "aeiou":
        count = count + 1
        # print("Vowel")
    else:
        pass
        # print("NotVowel")

print(count)