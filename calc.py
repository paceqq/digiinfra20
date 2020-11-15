# Python program to demonstrate
# command line arguments
 
import sys
 
# Anzahl Argumente
n = len(sys.argv)
print("Anzahl übergebener Argumente:", n)
 
# Übergebene Argumente
print("\nName des Skripts:", sys.argv[0])
 
print("\nÜbergebene Argumente:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition von Zahlen
Sum = 0

for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nErgebnis:", Sum)