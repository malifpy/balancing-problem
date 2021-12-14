import math
def printNode(depth, *args):
    if depth > 0:
        print("|   " * (depth - 1) + "|  ", *args)
    else:
        print(*args)

def var2rec(depth, l, real):
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

        printNode(depth, l1, ':', l2)

        printNode(depth, '-->', l1, '!=', l2)
        var2rec(depth + 1, l1 + l2, real + l3)

        printNode(depth, '-->', l1, '==', l2)
        var2rec(depth + 1, l3, real + l1 + l2)

        # printNode(depth, l1, '=', l2)
        # var2rec(depth + 1, l3)
    elif length == 1:
        printNode(depth, l)
    elif not real or length == 0:
        printNode(depth, [])
    else: # length == 2 dan bisa dicompare dengan sesuatu
        l1 = [l[0]]
        l2 = [l[1]]
        l3 = [real[0]]

        printNode(depth, l1, ':', l3)

        printNode(depth, '-->', l1, '!=', l3)
        var2rec(depth + 1, l1, real + l1)

        printNode(depth, '-->', l1, '==', l3)
        var2rec(depth + 1, l2, real + l2)

def var2(l):
    printNode(0, l)
    var2rec(1, l, [])

if __name__ == "__main__":
    var2(list("ABCDE"))