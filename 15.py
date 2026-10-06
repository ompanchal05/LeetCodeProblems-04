'''Write an code for abstraction and reversee the number'''

num = 12345
rev = 0

while num> 0:
    digit = num%10
    rev = rev*10    + digit
    num = num//10
print("Reversed number:", rev)
