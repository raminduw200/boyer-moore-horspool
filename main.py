from tabulate import tabulate

# -------------------------------
# Author: Ramindu Walgama
# Date: 2022-07-18
# Index: 20001959
# Reg. No: 2020/CS/195
# -------------------------------

c = 256  # Number of characters in the alphabet


# Preprocess pattern
def horspool_preprocess(pattern_, m_):
    """
    Preprocess the pattern into shift array.
    1. Fill the array with the length of the pattern first since the characters which are not in the pattern should be
    filled with the length of the pattern(m) to skip the search in the text.
    2. Fill the array with the length of the pattern for the characters which are in the pattern. Filling with the
    length of the pattern - index - 1 since search begins from the end of the pattern.

    :param pattern_: pattern which needs to search in the text.
    :param m_: length of the pattern.
    :return: shift array/preprocessed array; shift[i] is the number of characters to shift the pattern to the right to
             match the text.
    """
    shift = [m_] * c  # 1
    for i in range(m_ - 1):  # 2
        shift[ord(pattern_[i])] = m_ - i - 1
    return shift


# Search
def horspool_search(text_, n_, pattern_, m_, shift_, result_):
    """
    Search the pattern in the text using Boyer-Moore-Horspool Algorithm.
    1. Initialize the search index to the end of the pattern.
    2. Search is continuous until the search index is less than the length of the text - length of the search pattern.
    3. If the character at the search index in the text is equal to the character at the end of the pattern, then
    assign pattern position to one before last index(last index being checked in the if condition).
    4. search continues until the from right to left till the pattern position is 0(since loop execute one more addition
     execution (pat_pos >= 0) pat_position index will be -1) or mismatch found.
    5. If mismatch found, then shift the pattern to the right by the shift value of the character at the search index in

    :param text_: text which search needs to perform
    :param n_: length of the text
    :param pattern_: pattern which needs to search in the text.
    :param m_: length of the pattern.
    :param shift_: preprocessed array
    :param result_: an array to append the result
    :return: void
    """
    txt_pos = 0  # 1
    while txt_pos + m_ <= n_:  # 2
        if text_[txt_pos + m_ - 1] == pattern_[m_ - 1]:  # 3
            pat_pos = m_ - 2
            while pat_pos >= 0 and text_[txt_pos + pat_pos] == pattern_[pat_pos]:  # 4
                pat_pos -= 1
            if pat_pos < 0:
                result_.append(txt_pos + 1)
        txt_pos += shift_[ord(text_[txt_pos + m_ - 1])]  # 5


if __name__ == '__main__':
    results = {}
    total_matches = 0

    # Read dataset
    f = open('modules.txt', 'r')
    lines = f.readlines()
    f.close()

    # input and lower case since search is incasesensitive
    patterns = input("Enter search string/strings separated by ','(Example: Imaging,Ionising): ").lower()

    for pattern in patterns.split(','):
        m = len(pattern)

        shift = horspool_preprocess(pattern, m)

        # iterate through lines (index of the line)
        for i in range(len(lines)):
            result = []
            line = lines[i]
            n = len(line)
            horspool_search(line.lower(), n, pattern, m, shift, result)

            if result:
                # separate the module code from the module name
                line = line.split(' ', 1)
                matches = len(result)
                total_matches += matches

                # if the search string is already in the dictionary
                if i in results:
                    old_result = results[i]
                    results.update({i: [i + 1, line[0], line[1], old_result[3] + matches, old_result[4] + result]})
                else:
                    # Adds search results as rows as in the below format
                    # results.append([line_no, code, name, matches, result:(x, y, ...)])
                    results[i] = [i + 1, line[0], line[1], matches, result]

    # Print the results in table format using tabulate module
    headers = ['Line', 'Module Code', 'Module Name', 'Matches', 'Indices']
    print(tabulate(results.values(), headers, tablefmt="fancy_grid"))
    print(tabulate([['Total Word Matches', total_matches]], ['Total Lines Found   ', len(results)],
                   tablefmt="fancy_grid"))
