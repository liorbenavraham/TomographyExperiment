import numpy as np
import random

gen_random = lambda n: [random.randint(0, 1) for i in range(n)]

# Bases
states = ["HHVV", "HVVH"]

for num in [500, 1000, 2000]:
    VA = np.zeros(num)
    VB = np.zeros(num)

    HA = np.zeros(num)
    HB = np.zeros(num)

    for state in states:

        bits = gen_random(num)

        for i in range(len(bits)):
            if state == "HHVV":
                if bits[i] == 0:
                    VA[i] = 1
                    VB[i] = 1
                else:
                    HA[i] = 1
                    HB[i] = 1
            else:
                if bits[i] == 0:
                    VA[i] = 1
                    HB[i] = 1
                else:
                    HA[i] = 1
                    VB[i] = 1

        Vcnt = 0
        Hcnt = 0

        if state == "HHVV":
            for x, y in zip(VA, VB):
                if x == 1 and y == 1:
                    Vcnt += 1
            for x, y in zip(HA, HB):
                if x == 1 and y == 1:
                    Hcnt += 1
        else:
            for x, y in zip(VA, HB):
                if x == 1 and y == 1:
                    Vcnt += 1
            for x, y in zip(HA, VB):
                if x == 1 and y == 1:
                    Hcnt += 1

        print(f"num of bits: {num}")
        print(f"state: {state}: V count = {Vcnt}")
        print(f"state: {state}: H count = {Hcnt}")
        print(f"Probabilities (V,H): ({Vcnt/num},{Hcnt/num})\n")

