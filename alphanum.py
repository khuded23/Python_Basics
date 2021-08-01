import string

letters = string.ascii_lowercase
# print(letters)

alpha = list()
for letter in letters:
    alpha.append(letter)
print(alpha)
num = list()
for i in range(0, 27):
    num.append(i)
print(num)

alphanum = dict()

for k in range(0, 26):
    # print(k)
    j = (alpha[k])
    # print(j)
    h = (num[k])
    # print(h)
    alphanum[j] = h
print(alphanum)
