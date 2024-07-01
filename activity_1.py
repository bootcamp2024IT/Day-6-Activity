#day 6 activity1
pal = input("Enter any word: ").replace(" ", "").upper()
is_palindrome = True

for i in range(len(pal) // 2):
    if pal[i] != pal[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")