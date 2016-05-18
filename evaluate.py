from parsers import *

__author__ = "Sushant Raikar"
__email__ = "sushantraikar123@yahoo.com"

class JsonParseError(RuntimeError):
    def __init__(self, args):
        self.args = args

def evaluate(st):
    """
    Returns python object
    Evaluates json string
    Errors out if json is invalid
    """
    if get_list(st): return evaluate_list(st)
    elif get_dict(st): return evaluate_dict(st)
    elif get_string(st): return evaluate_str(st)
    elif get_number(st): return evaluate_number(st)
    elif get_boolean(st): return evaluate_boolean(st)
    raise JsonParseError("unable to parse %s"%(st))

def evaluate_str(st):
    """
    Returns evaluated string
    Errors out if invalid
    """
    m = get_string(st)
    if m:
        data = m.groupdict()["content"]
        return data
    else:
        error()

def evaluate_number(st):
    """
    Returns evaluated number
    Errors out if invalid
    """
    m = get_number(st)
    if m:
        data = m.groupdict()
        if data["float"]: return float(data["float"])
        elif data["integer"]: return int(data["integer"])
        return None
    else:
        error()

def evaluate_boolean(st):
    """
    Returns evaluated boolean
    Errors out if invalid
    """
    m = get_boolean(st)
    if m:
        data = m.groupdict()["content"]
        if data == 'true': return True
        elif data == 'false': return False
        elif data == 'null': return None
        return None
    else:
        error()

def evaluate_list(st):
    """
    Returns evaluated list
    Errors out if invalid
    """
    m = get_list(st)
    ret = []
    if m:
        data = m.groupdict()["content"]
        data = find_commas(data)
        for d in data:
            ret.append(evaluate(d))
    else:
        error()
    return ret

def evaluate_dict(st):
    """
    Returns evaluated dict
    Errors out if invalid
    """
    m = get_dict(st)
    ret = {}
    if m:
        data = m.groupdict()["content"]
        data = find_commas(data)
        for d in data:
            m = get_key_value(d)
            if m:
                keyval = m.groupdict()
                ret[keyval["key"]] = evaluate(keyval["value"])
            else:
                error()
    return ret

def error():
    raise JsonParseError("unable to parse")
