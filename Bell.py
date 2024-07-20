import numpy as np
import pandas as pd

# Coincidence counts
N = {}

# Angles to match the titles in the Excel file
alfas = [-45, 0, 45, 90]
alfas_marks = ["a", "a_tag", "a+90", "a_tag+90"]

betas = [-225, 225, 675, 1125]
betas_marks = ["b", "b_tag", "b+90", "b_tag+90"]

# Read data from file and detect Coincidences
for a in alfas:
    for b in betas:
        dataframe = pd.read_excel("tomo.xlsx", f"a{a}b{b}")

        # A for Alice, B for Bob
        A = np.array(dataframe["A"])
        B = np.array(dataframe["B"])

        # Define treshold
        treshold = 0.575 * max(max(A), max(B))

        # Translation of the variable names
        alfa = alfas_marks[alfas.index(a)]
        beta = betas_marks[betas.index(b)]

        cnt = 0
        for frame in zip(A, B):
            if frame[0] > treshold and frame[1] > treshold:
                cnt += 1

        N[f"{alfa}{beta}"] = cnt


# Calculate the S parameter
def E(a, b):
    return (N[f"{a}{b}"] + N[f"{a}+90{b}+90"] - N[f"{a}{b}+90"] - N[f"{a}+90{b}"])/(N[f"{a}{b}"] + N[f"{a}+90{b}+90"] + N[f"{a}{b}+90"] + N[f"{a}+90{b}"])


def S(a, atag, b, btag):
    a = alfas_marks[alfas.index(a)]
    atag = alfas_marks[alfas.index(atag)]

    b = betas_marks[betas.index(b)]
    btag = betas_marks[betas.index(btag)]

    return abs(E(a, b) + E(atag, b) - E(a, btag) + E(atag, btag))


# Print final result
print(S(-45, 0, -225, 225))


