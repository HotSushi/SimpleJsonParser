import re

__author__ = "Sushant Raikar"
__email__ = "sushantraikar123@yahoo.com"

def get_list(st):
    """
    Returns re.match object
    searches for square brackets greedily
    if found returns the middle content
    """
    rex = re.compile(r"""
            \s*
            \[(?P<content>.*)\]   #All list content
            \s*
        """, re.VERBOSE)
    m = rex.match(st)
    return m

def get_dict(st):
    """
    Returns re.match object
    searches for curly brackets greedily
    if found returns the middle content.
    """
    rex = re.compile(r"""
            \s*
            \{(?P<content>.*)\}   #All dictionary content
            \s*
        """, re.VERBOSE)
    m = rex.match(st)
    return m

def get_key_value(st):
    """
    Returns re.match object
    parses key: value
    """
    rex = re.compile(r"""
            \s*
            \"(?P<key>.+?)\"    #get key enclosed in ""
            \s*:\s*
            (?P<value>.*)       #get value till string ends
        """, re.VERBOSE)
    m = rex.match(st)
    return m

def get_string(st):
    """
    Returns re.match object
    parses string enclosed between " "
    """
    rex = re.compile(r"""
            \s*
            \"(?P<content>.*)\"
            \s*
        """, re.VERBOSE)
    m = rex.match(st)
    return m

def get_number(st):
    """
    Returns re.match object
    parses number
    returns {"integer": value if integer parsed, "float": value if float parsed}
    """
    rex = re.compile(r"""
            \s*
            (?P<float>[-+]?\d+\.\d+)|
            (?P<integer>[-+]?\d+)
            \s*
        """, re.VERBOSE)
    m = rex.match(st)
    return m

def get_boolean(st):
    """
    Returns re.match object
    parses and returns true/false/null
    """
    rex = re.compile(r"""
            \s*
            (?P<content>true|false|null)
            \s*
        """, re.VERBOSE)
    m = rex.match(st)
    return m

def find_commas(st):
    """
    Returns list of string
    finds commas in a string which are at the current depth
    for ex in following string only one comma is counted
    "{ { [ ] } }, [ [ ] ]"
    fn will return ["{ { [ ] } }" , "[ [ ] ]"]
    """
    ret_list = []
    cur,curly_count, square_count = 0,0,0
    for i in range(len(st)):
        if st[i] == '{': curly_count += 1
        elif st[i] == '}': curly_count -= 1
        elif st[i] == '[': square_count += 1
        elif st[i] == ']': square_count -= 1
        elif st[i] == ',':
            if curly_count == square_count == 0:
                ret_list.append(st[cur:i])
                cur = i + 1
    ret_list.append(st[cur:])
    return ret_list
