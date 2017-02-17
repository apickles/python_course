emails=['me@gmail.com','you@hotmail.com', 'they@gmail.com']

for item in emails:
    if 'gmail' in item:
        print(item)
    else:
        print('not gmail')
a=["Trickier"]
for i in a:
    print(i)
lst=["Terribly Tricky"]
for word in lst:
    for letter in word[-6:]:
        print(letter)
