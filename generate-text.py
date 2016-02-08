# -*- coding: utf-8 -*-
# Calcule des workout + times pour un groupe de differente VMA
# Les vma par default vons de 13 a 20 (a configurer dans la variable VMA)

# La variable WORKOUT est la variable des travaux a faire,
# c'est une array avec comme valeur :
# [times, percentage, distance, repos]
# times sont le nombre de repetition
# percentage sont le percentate a laquelle vous avez la VMA
# repos et le temp de repo pour cette repetition

VMAS = xrange(14, 17)

# 3 *
WORKOUT = [[3, 90, 1200, "1m 45s de repos"],
           [1, 85, 5000, "3mn de repos"],
           [8, 100, 200, "45s de recup active"]]

WORKOUT = [[6, 90, 400, "recup 200m allure footing"],
           [6, 90, 300, "recup 100m de repos"],
           [6, 105, 200, "recupe 2'00 a l'arret"]]


# 3x1000 90% / 2x4000 85%
# WORKOUT = [[3, 90, 1000, "1'15 de repos"],
#            [2, 85, 4000, "1'30s de repos"]]

# 10x400 90% VMA
#WORKOUT = [[10, 90, 400, "1m de repos"]]


cl_float = lambda x: str(x)[:str(x).rfind(".")]

cl_floatz = lambda x: str(x)[:str(x).rfind(".")] \
            if str(x).endswith('.0') else str(x)


def mytime(temp):
    result = ""
    stemps = round(temp * 10) / 10
    minute = round(stemps - (stemps % 60)) / 60

    if minute > 0:
        result = result + cl_float(minute) + "mn"
    second = (round((stemps % 60) * 10)) / 10
    if second > 0:
        result = result + cl_floatz(round(second)) + "s"
    return result


def calculer_distance(vma, percent, distance):
    vma_ms = float(vma) * 1000 / 3600
    vma_100 = 100 / vma_ms  # temps au 100 m à 100 %  VMA
    return mytime(vma_100 / percent * distance)


def calculer_vitesse(vma, percent):
    r = round(vma * percent) / 100
    return cl_floatz(r)

for work in WORKOUT:
    (times, percent, distance, rest) = work

    dstr = "%d fois %dm a %d%% VMA"
    print (dstr % (times, distance, percent))
    print ("-" * len(dstr)) + "\n"
    for vma in VMAS:
        print("%dVMA => %s //" % (vma,
                                  calculer_distance(
                                      vma, percent, distance))),

        if distance > 400:
            print("400m => %s //" % (calculer_distance(vma, percent, 400))),

        print("Speed => %skph" %
              (calculer_vitesse(vma, percent)))

    print("")
    if rest:
        if times > 1:
            entre = 'entre session'
        else:
            entre = ''
        print("%s %s" % (rest, entre))
    print ("\n")
