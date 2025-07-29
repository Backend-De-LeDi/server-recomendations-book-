import unicodedata

def generateDistKey(text):
     text = unicodedata.normalize("NFC",text).encode("ASCII","ignore").decode("utf-8")
     return text.lower().replace(' ','_')