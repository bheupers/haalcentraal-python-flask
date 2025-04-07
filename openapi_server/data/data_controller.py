import json


def recursive_partial_match(args:dict, element:dict, level="root"):
    """Compare values in args dict with values in element for same keys.
    Return true if it matches for all keys and values in args
    """
    if isinstance(args, dict) and isinstance(element, dict):
        setargs = set(args.keys())
        setelement = set(element.keys())
        if not setargs.issubset(setelement):
            return False
        for k in setargs:
            if not recursive_partial_match(args[k], element[k], level=f"{level}-{k}"):
                return False
        return True
    else:
        return args == element


class DataController:
    """
    Handle read data operations
    """
    _alldata: list[dict]

    def __init__(self, filename:str):
        f = open(filename) 
        self._alldata = json.load(f) 

    
    def search(self, args:dict):
        """
        Search in dictionary
        """
        result = []
        for el in self._alldata:
            if recursive_partial_match(args, el):
                result.append(el)
        return result
