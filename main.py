from tabulate import tabulate
import matplotlib.pyplot as plt

# -------------------------------
# Author: Ramindu Walgama
# Date: 2022-07-18
# Index: 20001959
# Reg. No: 2020/CS/195
# -------------------------------

c = 256


def horspool(text_, pattern_, result_):
    n = len(text_)
    m = len(pattern_)

    # Preprocess pattern
    shift = [m] * c
    for i in range(m - 1):
        shift[ord(pattern_[i])] = m - i - 1

    # Search
    txt_pos = 0
    while txt_pos + m <= n:
        if text_[txt_pos + m - 1] == pattern_[m - 1]:
            pat_pos = m - 2
            while pat_pos >= 0 and text_[txt_pos + pat_pos] == pattern_[pat_pos]:
                pat_pos -= 1
            if pat_pos < 0:
                result_.append(txt_pos+1)
        txt_pos += shift[ord(text_[txt_pos + m - 1])]


if __name__ == '__main__':
    headers = ['Line', 'Module Code', 'Module Name', 'Matches', 'Indices']
    results = []
    total_matches = 0

    f = open('modules.txt', 'r')
    lines = f.readlines()
    f.close()

    for i in range(len(lines)):
        result = []
        line = lines[i]
        horspool(line, 'Handling', result)
        if result:
            line = line.split(' ', 1)
            matches = len(result)
            total_matches += matches
            # Adds search results as rows as in the below format
            # results.append([line_no, code, name, matches, result:(x, y, ...)])
            results.append([i+1, line[0], line[1], matches, result])
    print(tabulate(results, headers, tablefmt="fancy_grid"))
    print(tabulate([['Total Word Matches', total_matches]], ['Total Lines Found   ', len(results)], tablefmt="fancy_grid"))
