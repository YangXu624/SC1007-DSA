import gc

def main():
    listA = []
    listB = []

    listA.append(listB)
    listB.append(listA)

    del listA, listB

    gc.enable()
    obj = gc.collect()
    print(obj)


if __name__ == "__main__":
    main()