from src.utils.generateDictKey import generateDistKey

def generateFlags(prefix:str,value:list[str])->dict:
     return {f"{prefix}_{generateDistKey(v)}":True for v in value}
