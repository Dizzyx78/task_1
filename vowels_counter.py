import re
while True:
    text=input()
    #print(text)

    if text.isalpha() == False:
        print("Error. Type only letters.")
    elif re.search(r'[a-zA-Z]',text ):
        break
    else:
        print("Error. Type in Latin.")

result1=0
result2=0
result3=0
result4=0
result5=0
result6=0

for a in text:
    #print(a)

    if a == "a":
        result1+=1
    elif a == "o":
        result2+=1
    elif a == "u":
        result3=1
    elif a == "i":
        result4+=1
    elif a == "e":
        result5+=1
    elif a == "y":
        result6+=1

print("a -", result1, "o -", result2, "u -", result3, "i -", result4, "e -", result5, "y -", result6)