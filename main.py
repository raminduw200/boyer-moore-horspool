# -------------------------------
# Author: Ramindu Walgama
# Date: 2022-07-18
# Index: 20001959
# Reg. No: 2020/CS/195
# -------------------------------

c = 256


def horspool(text, pattern):
    n = len(text)
    m = len(pattern)

    # Preprocess pattern
    shift = [m] * c
    for i in range(m - 2):
        shift[ord(pattern[i])] = m - i - 1

    # Search
    txt_pos = 0
    while txt_pos + m <= n:
        if text[txt_pos+m-1] == pattern[m-1]:
            pat_pos = m - 2
            while pat_pos >= 0 and text[txt_pos+pat_pos] == pattern[pat_pos]:
                pat_pos -= 1
            if pat_pos < 0:
                print(txt_pos)
        txt_pos += shift[ord(text[txt_pos+m-1])]


if __name__ == '__main__':
    horspool('abcdefghijabcklmnopqrabcstuvwxyzabc', 'abc')
