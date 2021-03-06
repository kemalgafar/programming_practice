# My solutions for Chapter 1 of Crack the Coding Interview

"""
NOTES:
"""


def quest_1_1():
    """
    Question 1.1: Is Unique

    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    """

    test_string = input("Please enter in a test string.\n>>\t")

    str_length = len(test_string)
    set_of_chars = set()

    for char in test_string:
        set_of_chars.add(char)

    # V.1 solution using sets
    if str_length != len(set_of_chars):
        print("V.1: The input string does not have all unique characters.")
    else:
        print("V.1: The input string has all unique characters")

    # V.2 solution using NO additional data structures
    for char in test_string:
        if test_string.count(char) > 1:
            print("V.2: The input string does not have all unique characters.")
            break
        print("V.2: The input string has all unique characters")


def quest_1_2():
    """
    Question 1.2: Check Permutation

    Given two strings, write a method to decide if one is a permutation of the
    other.
    """

    str_one = input("Please enter in the first string.\n>>\t")
    str_two = input("Please enter in the second string.\n>>\t")
    dict_one = {}
    dict_two = {}

    # White spaces have been removed in the string comparision
    # To include white spaces, remove the .replace(" ","") method
    for char in str_one.replace(" ",""):
        dict_one[char] = str_one.count(char)

    for char in str_two.replace(" ",""):
        dict_two[char] = str_two.count(char)

    if dict_one != dict_two:
        print("The two strings are not permutations of each other.")
    else:
        print("The two strings are permutations of each other.")


def quest_1_3():
    """
    Question 1.3: URLify

    Write a method to replace all spaces in a string with '%20'. You may assume
    that the string has sufficient space at the end to hold the additional
    characters, and that you are given the "true" length of the string.

    EXAMPLE:
    Input:   "Mr John Smith     ", 13
    Output:  "Mr%20John%20Smith"
    """

    str_with_ws = input("Please enter in the test string.\n>>\t")
    str_url = str_with_ws.replace(" ","%20")

    print("Input:    \"" + str_with_ws + "\t\", ", len(str_with_ws))
    print("Output:   \"" + str_url + "\"")


def quest_1_4():
    """
    Question 1.4: Palindrome Permutation

    Given a string, write a function to check if it is a permutation of a
    palindrome. The palindrome does not need to be limited to just dictionary
    words.

    EXAMPLE:

    Input:   Tact Coa
    Output:  True (permutations: "taco cat", "atco cta", etc.)
    """

    dict_of_chars = {}
    odd_char_ctr = 0
    odd_char = None
    left_str_index = 0
    right_str_index = -1
    count_of_chars = 0

    input_str = input("Please enter in the test string.\n>>\t").lower()

    list_of_input = list(input_str)

    for char in input_str:
        if char != " ":
            dict_of_chars[char] = input_str.count(char)

    for key in dict_of_chars:
        count_of_chars += dict_of_chars[key]
        if dict_of_chars[key] % 2 != 0:
            odd_char_ctr += 1
            odd_char = key

    if odd_char_ctr > 1:
        print("Output:  False, the input string has no possible permutations")
    else:
        while count_of_chars > 0:
            for key in dict_of_chars:
                if dict_of_chars[key] > 1:
                    while list_of_input[left_str_index] == " ":
                        left_str_index += 1
                    while list_of_input[right_str_index] == " ":
                        right_str_index -= 1

                    list_of_input[left_str_index] = key
                    left_str_index += 1

                    list_of_input[right_str_index] = key
                    right_str_index -= 1

                    dict_of_chars[key] -= 2
                    count_of_chars -= 2

            # Only need to increment from one side becuase all the even-paired
            # chars have been used already, all thats left is the odd_char
            # which will replace the first non-whitespaced index in the
            # list. left_str_index and right_str_index have converged
            # this final push will insert the odd_char
            if list_of_input[left_str_index] == " ":
                while list_of_input[left_str_index] == " ":
                    left_str_index += 1
                list_of_input[left_str_index] = odd_char
                count_of_chars -= 1
            else:
                if odd_char != None: # Needed in the case of even str length
                    list_of_input[left_str_index] = odd_char
                    count_of_chars -= 1

        output_str = "".join(list_of_input)
        print ("Output:  True (permutations: \"" + output_str + "\", etc.)")


def quest_1_5():
    """
    Question 1.5: One Away

    There are three types of edits that can be performed on strings: insert a
    character, remove a character, or replace a character. Given two strings,
    write a function to check if they are one edit (or zero edits) away.

    EXAMPLE:

    pale,    ple      -> true
    pales,   pale     -> true
    pale,    bale     -> true
    pale,    bake     -> false
    """

    return_val = False
    edits_ctr = 0

    str_one = input("Please enter in the first string.\n>>\t")
    str_two = input("Please enter in the second string.\n>>\t")

    # Handles Replacemnt and zero-edits
    if len(str_one) == len(str_two):
        for i, char in enumerate(str_one):
            if str_one[i] != str_two[i]:
                edits_ctr += 1
    # Handles char inserts and removals. Insures that there is max one char
    # addition. Char inserts/removals become the same problem by always
    # assigning the smaller string to str_one then checking againt the longer
    # string (str_two)
    else:
        if abs(len(str_one) - len(str_two)) < 2:
            if len(str_one) > len(str_two):
                str_one, str_two = str_two, str_one
            str_two_index = 0
            for i, char in enumerate(str_one):
                while str_one[i] != str_two[str_two_index]:
                    edits_ctr += 1
                    str_two_index += 1
                str_two_index += 1
        else:
            edits_ctr = abs(len(str_one) - len(str_two))

    if edits_ctr < 2:
        return_val = True

    print(str_two + ",\t" + str_one + "\t->  " + str(return_val).lower())


def quest_1_6():
    """
    Question 1.6: String Compression

    Implement a method to perform basic string compression using the counts of
    repeated characters. For example, the string aabcccccaaa would become
    a2b1c5a3. If the "compressed" string would not become smaller than the
    original string, your method should return the original string. You can
    assume the string has only uppercase and lowercase letters (a-z)
    """

    output_str = ""
    i = 0

    test_str = input("Please enter in a string.\n>>\t")

    while i < len(test_str):
        char_ctr = 1
        i_shift = 0
        while test_str[i] == test_str[i + i_shift]:
            char_ctr += 1
            i_shift += 1
            if i + i_shift >= len(test_str):    #WHY IS >=  ?
                break
        output_str += (test_str[i] + str(char_ctr - 1))
        i += i_shift

    if len(output_str) >= len(test_str):   #remove eq? see question
        print(test_str)
    else:
        print(output_str)


def quest_1_7():
    """
    Question 1.7: Rotate Matrix

    Given an image represented by an NxN matrix, where each pixel in the image
    is 4 bytes, write a method to rotate the image by 90 degrees. Can you do
    this in place?
    """


def quest_1_8():
    """
    Question 1.8: Zero Matrix

    Write an algorithm such that if an element in an MxN matrix is 0, its entire
    row and column are set to 0.
    """


def quest_1_9():
    """
    Question 1.9: String Rotation

    Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, s1 and s2, write code to check if s2 is a
    rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a
    rotation of "erbottlewat")
    """

    str_one = "waterbottle"
    str_two = "erbottlewat"

    def isSubstring(str_one, str_two):
        is_sub_str = False
        if len(str_one) != len(str_two):
            pass
        else:
            str_one_looped = (str_one + str_one)
            if str_two in str_one_looped:
                is_sub_str = True
        return is_sub_str

    print (isSubstring(str_one, str_two))


#Make a dictionary carousel where you ask which function to run
#have the carousel display the docstring and then call the test script
#well, each func will call the test itself
#quest_1_1()
#quest_1_2()
#quest_1_3()
#quest_1_4()
#quest_1_5()
#quest_1_6()
#quest_1_7()
#quest_1_8()
#quest_1_9()
