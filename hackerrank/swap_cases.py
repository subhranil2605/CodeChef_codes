sentence = input()
print(''.join(s.lower() if s.isupper() else s.upper() for s in sentence))

print(sentence.swapcase())
