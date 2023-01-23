import numpy as np
n = int(input("Enter a number:\n"));
C = [];
while n:
    if (n % 2) == 0:
        n = n // 2;
    else:
        n = (3*n) + 1;
    C.append(n);
    if int(C[-1]) == 1:
        break;
print(C);