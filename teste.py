def solution(s):
    if (len(s)/2.0).is_integer():
        return [s[i:i + 2] for i in range(0, len(s), 2)]
    else:
        return [s[i:i + 2].ljust(2, "_") for i in range(0, len(s), 2)]

k = 2 # number of characteres
s = "ericka"

solution(s)
