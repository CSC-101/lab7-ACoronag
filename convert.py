def str_to_float(string:str):
    try:
        return float(string)
    except ValueError:
        return None

