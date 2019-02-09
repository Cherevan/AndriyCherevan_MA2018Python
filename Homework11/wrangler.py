"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if len(list1) <= 1:
        return list(list1)

    new_list = []

    for item in list1:
        if item not in new_list:
            new_list.append(item)

    return new_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    if len(list1) + len(list2) < 1:
        return []

    new_list = []

    for item in list1:
        if item in list2:
            new_list.append(item)

    return new_list


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    if len(list1) < 1:
        return list2
    if len(list2) < 1:
        return list1

    sum_len = len(list1) + len(list2)
    new_list = []
    id1 = 0
    id2 = 0

    while len(new_list) < sum_len:
        if list1[id1] < list2[id2]:
            new_list.append(list1[id1])
            id1 += 1
        else:
            new_list.append(list2[id2])
            id2 += 1

        if id1 == len(list1):
            new_list.extend(list2[id2:])
        elif id2 == len(list2):
            new_list.extend(list1[id1:])

    return new_list


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    last_pos = len(list1)
    middle = last_pos // 2

    if last_pos <= 1:
        return list1

    first_list = merge_sort(list1[:middle])
    last_list = merge_sort(list1[middle:])

    return merge(first_list, last_list)


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) < 1:
        return ['']

    first, rest = word[0], word[1:]
    rest_strings = gen_all_strings(rest)
    result = []

    for string in rest_strings:
        if string != '':
            for pos in range(len(string) + 1):
                new_word = string[:pos] + first + string[pos:]
                result.append(new_word)
        else:
            result.append(first)

    return rest_strings + result


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
