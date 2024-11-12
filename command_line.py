import sys
def convert_float(parameter):
    try:
        parameter = float(parameter)
    except ValueError:
        print("not a number")
    return parameter

if __name__ == '__main__':
    print(convert_float(sys.argv))
