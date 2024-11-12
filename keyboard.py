from multiprocessing.managers import Value


def gather_numbers():
    lista = []
    while True:
        print("Either type a number to add to the list or type done")
        x = input(": ")
        try:
            x = float(x)
            lista.append(x)
        except ValueError:
            if x.lower() == "done":
                break
            else:
                print("I said a number silly.")
    return lista

if __name__ == '__main__':
    print(gather_numbers())
