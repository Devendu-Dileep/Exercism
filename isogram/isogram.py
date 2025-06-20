def is_isogram(stringc):
    stringc_lower=''.join(stringc.lower().split()).replace('-',"")
    return len(set(stringc_lower))==len(stringc_lower)

