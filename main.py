wiersze=open('slowa.txt','r')
tab=[]
tab1=[]
for wiersz in wiersze:
    tab.append(wiersz.strip().split())

for i in tab:
    for j in i:
        tab1.append(j)

# ZAD 6.1.
# print(tab1)
# licznikLieteraA=0
# for i  in tab1:
#     if i[len(i)-1]=="A":
#         licznikLieteraA+=1
# print(licznikLieteraA)

# ZAD 6.2.
# licznik=0
# for i in range(len(tab1)-1):
#     if tab1[i].find(tab1[i+1]):
#         licznik+=1
# print(licznik)
# ZAD 6.3.

