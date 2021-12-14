import math
def printNode(depth, *args):
    if depth > 0:
        print("|   " * (depth - 1) + "|  ", *args)
    else:
        print(*args)

def var1rec(depth, l):
    # Diberikan sejumlah koin l
    # Salah satu dari koin tersebut lebih berat dari yang lain
    # hanya dengan menggunakan timbangan, bagaimana
    # cara mengetahui koin yang lebih berat?

    length = len(l)
    if length > 1:

        binSize = math.ceil(length / 3)
        l1 = l[:binSize]
        l2 = l[binSize: 2 * binSize]
        l3 = l[2 * binSize:]

        # Berbagai macam kemungkinan

        printNode(depth, l1, '>', l2)
        var1rec(depth + 1, l1)

        printNode(depth, l1, '<', l2)
        var1rec(depth + 1, l2)

        printNode(depth, l1, '=', l2)
        var1rec(depth + 1, l3)
    else:
        printNode(depth, l)


def var1(l):
    printNode(0, l)
    var1rec(1, l)

if __name__ == "__main__":
    var1(list("ABCD"))