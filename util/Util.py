def size_mb(docs):
    return sum(len(s.encode('utf-8')) for s in docs) / 1e6

def trim(s):
    """Trim string to fit on terminal (assuming 80-column display)"""
    return s if len(s) <= 80 else s[:77] + "..."

def to_s(list):
    return ''.join(str(e)+", " for e in list)

