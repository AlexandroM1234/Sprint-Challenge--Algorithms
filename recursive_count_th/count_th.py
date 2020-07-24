'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # word can't be less than 2 because no "th"
    if len(word) < 2:
        return 0
    else:
        # then goes through the word looking for "th"
        if word[0:2] == "th":
            # if "th" is found return a 1 then pick up from the next index
            return 1 + count_th(word[2:])
        else:
            # if not found go to the next index
            return count_th(word[1:])
