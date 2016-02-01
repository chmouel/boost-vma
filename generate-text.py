# -*- coding: utf-8 -*-
# Calcule des workout + times pour un groupe de differente VMA
# Les vma par default vons de 13 a 20 (a configurer dans la variable VMA)

# La variable WORKOUT est la variable des travaux a faire,
# c'est une array avec comme valeur :
# [times, percentage, distance, repos]
# times sont le nombre de repetition
# percentage sont le percentate a laquelle vous avez la VMA
# repos et le temp de repo pour cette repetition

VMAS = [12, 13, 14,
        15, 16,
        17, 18,
        19, 20]

WORKOUT = [[3, 90, 1000, "45s de repos"],
           [2, 85, 2000, "30s de repos"],
           [1, 80, 3000, False]]


WORKOUT = [[3, 90, 1000, "1'15 de repos"],
           [2, 85, 4000, "1'30s de repos"]]


def cl_float(x):
    x = str(x)
    return x[:x.rfind(".")]


def mytime(temp):
    result = ""
    stemps = round(temp * 10) / 10
    minute = round(stemps - (stemps % 60)) / 60

    if minute > 0:
        result = result + cl_float(minute) + " mn "
    second = (round((stemps % 60) * 10)) / 10
    if second < 0:
        second = 00
    result = result + cl_float(round(second)) + " s"
    return result


def calculer_distance(vma, percent, distance):
    vma_ms = float(vma) * 1000 / 3600
    vma_100 = 100 / vma_ms  # temps au 100 m à 100 %  VMA
    return mytime(vma_100 / percent * distance)


def calculer_vitesse(vma, percent):
    return round(vma * percent) / 100

for work in WORKOUT:
    (times, percent, distance, rest) = work

    dstr = "%d fois %dm a %d%% VMA"
    print (dstr % (times, distance, percent))
    print ("-" * len(dstr)) + "\n"
    for vma in VMAS:
        print("%d de VMA => %s, 400m => %s %skph" %
              (vma,
               calculer_distance(vma, percent, distance),
               calculer_distance(vma, percent, 400),
               calculer_vitesse(vma, percent)
              ))

    print("")
    if rest:
        print("%s entre session" % (rest))
    print ("\n")
