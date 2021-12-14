import math
def printNode(depth, *args):
    if depth > 0:
        print("|   " * (depth - 1) + "|  ", *args)
    else:
        print(*args)

def var3rec(depth, l, real, knowHere):
    # Diberikan sejumlah koin l
    # Salah satu dari koin tersebut lebih berat dari yang lain
    # hanya dengan menggunakan timbangan, bagaimana
    # cara mengetahui koin yang lebih berat?

    length = len(l)
    if length > 2:

        binSize = math.ceil((length // 2) / 2)
        l1 = l[:binSize]
        l2 = l[binSize: 2 * binSize]
        l3 = l[2 * binSize:]

        # print(l1, l2, l3)

        # Berbagai macam kemungkinan

        printNode(depth, l1, '!=', l2)
        var3rec(depth + 1, l1 + l2, real + l3, True)

        printNode(depth, l1, '==', l2)
        var3rec(depth + 1, l3, real + l1 + l2, knowHere)

        # printNode(depth, l1, '=', l2)
        # var3rec(depth + 1, l3)
    elif length == 1 and knowHere:
        printNode(depth, l)
    elif not real or length == 0:
        printNode(depth, "TIDAK BISA DITENTUKAN")
    elif length == 1 and not knowHere:
        printNode(depth, l, '!=', [real[0]])
        var3rec(depth + 1, l, real, not knowHere)

        printNode(depth, l, '==', [real[0]])
        printNode(depth + 1, "TIDAK ADA")
    else: # length == 2 dan bisa dicompare dengan sesuatu
        l1 = [l[0]]
        l2 = [l[1]]
        l3 = [real[0]]

        printNode(depth, l1, '!=', l3)
        var3rec(depth + 1, l1, real + l1, True)

        printNode(depth, l1, '==', l3)
        var3rec(depth + 1, l2, real + l2, knowHere)

def var3(l):
    printNode(0, l)
    var3rec(1, l, [], False)

if __name__ == "__main__":
    var3(list("ABCDE"))