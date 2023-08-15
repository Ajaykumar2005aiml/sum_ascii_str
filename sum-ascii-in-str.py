s=input()
m=[]
for i in range(len(s)):
  m.append(ord(s[i]))
if sum(m) % 8 ==0:
  print(1)
else:
  print(0)
