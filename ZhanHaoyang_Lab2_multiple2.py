import numpy as np;
import time;
import matplotlib.pyplot as plt
starttime = time.time()

N = 1
list1 = []
Nlist = [];

while N != 1000000:
    n = N;
    smallcounter = 0
    while n != 1:
        if (n % 2) == 0:
            n = 3*n + 1;
            smallcounter += 1
        else:
            n = (3*n + 1) / 2;
        smallcounter += 2
    list1.append(smallcounter)
    Nlist.append(N)
    N += 1

endtime = time.time() 
elapsed = endtime - starttime;
print(elapsed);

x = Nlist;
y = list1;
plt.loglog(x,y, color ="red");
plt.xlabel("C(n)");
plt.ylabel("log10(n)");
plt.show();
