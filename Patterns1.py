print("Half Pyramid Patterns Of Stars(*):")
n = int(input("EPAnter The Number Of Rows:"))
for i in range (n):
    for j in range(i+1):
        print("* " , end="")
    print()