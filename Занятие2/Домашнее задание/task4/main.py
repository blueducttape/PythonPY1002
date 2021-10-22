if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 9, 8, 7, 6, 0]
    first_value = list_[0]
    max_value_index = 0
    max_value = list_[max_value_index]
    for index, current_value in enumerate(list_):
        if current_value >= max_value:
            max_value = current_value
            max_value_index = index
    del list_[max_value_index]
    list_.insert(max_value_index, first_value)
    del list_[0]
    list_.insert(0, max_value)
    print(list_)



