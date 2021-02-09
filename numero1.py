
suce=[]
a=0
b=1
num = int(input("Posición: "))
for n in range(num):
    suce.append(a+b)
    ab = a + b
    a = b
    b = ab 
print(suce[-1])     
