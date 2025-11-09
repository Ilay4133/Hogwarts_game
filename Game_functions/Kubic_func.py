import random


def kubik(kubiks_edges=25) -> float:
    kubik_val = random.randint(1, kubiks_edges)
    kubik_koef = round((kubik_val / kubiks_edges), 1)
    return kubik_koef
