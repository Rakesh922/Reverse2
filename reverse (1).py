def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = "1234abcd"
 
print("Sample String : ", end="")
print(s)
 
print("Expected Output : ", end="")
print(reverse(s))