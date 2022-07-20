from tabulate import tabulate
import matplotlib.pyplot as plt

# -------------------------------
# Author: Ramindu Walgama
# Date: 2022-07-18
# Index: 20001959
# Reg. No: 2020/CS/195
# -------------------------------

c = 256  # Number of characters in the alphabet


# TODO: Comment the code.
# TODO: update readme
# TODO: Take user input


# Preprocess pattern
def horspool_preprocess(pattern_, m_):
    shift_ = [m_] * c
    for _ in range(m_ - 1):
        shift_[ord(pattern_[_])] = m_ - _ - 1
    return shift_


# Search
def horspool_search(text_, n_, pattern_, m_, shift_, result_):
    txt_pos = 0
    while txt_pos + m_ <= n_:
        if text_[txt_pos + m_ - 1] == pattern_[m_ - 1]:
            pat_pos = m_ - 2
            while pat_pos >= 0 and text_[txt_pos + pat_pos] == pattern_[pat_pos]:
                pat_pos -= 1
            if pat_pos < 0:
                result_.append(txt_pos + 1)
        txt_pos += shift_[ord(text_[txt_pos + m_ - 1])]


if __name__ == '__main__':
    results = []
    total_matches = 0

    f = open('modules.txt', 'r')
    lines = f.readlines()
    f.close()

    pattern = input("Enter a search string: ").lower()
    m = len(pattern)

    shift = horspool_preprocess(pattern, m)

    for i in range(len(lines)):
        result = []
        line = lines[i]
        n = len(line)
        horspool_search(line.lower(), n, pattern, m, shift, result)
        if result:
            line = line.split(' ', 1)
            matches = len(result)
            total_matches += matches
            # Adds search results as rows as in the below format
            # results.append([line_no, code, name, matches, result:(x, y, ...)])
            results.append([i + 1, line[0], line[1], matches, result])

    headers = ['Line', 'Module Code', 'Module Name', 'Matches', 'Indices']
    print(tabulate(results, headers, tablefmt="fancy_grid"))
    print(tabulate([['Total Word Matches', total_matches]], ['Total Lines Found   ', len(results)],
                   tablefmt="fancy_grid"))
