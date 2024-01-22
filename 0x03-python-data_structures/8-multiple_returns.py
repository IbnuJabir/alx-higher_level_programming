#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    f = sentence[0] if ln > 0 else "None"
    return (ln, f)
