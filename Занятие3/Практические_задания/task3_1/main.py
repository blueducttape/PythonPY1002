def remove_whitespace(str_):

    word_list = str_.split(" ")
    words_list_without_empty_string = []
    for word in word_list:
        if word:
            words_list_without_empty_string.append(word)
    print(words_list_without_empty_string)

    return " ".join(words_list_without_empty_string)


if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
