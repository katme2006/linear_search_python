def linear_search(value_to_find, array_to_search_through):
    
    for i in array_to_search_through:
        if i == value_to_find:
            return array_to_search_through.index(i)

    

def linear_search_global(value_to_find, array_to_search_through):
    index_arr =[]
    index_counter =0
    for i in array_to_search_through:
        if i == value_to_find:
            index_arr.append(index_counter)
        index_counter += 1
    return index_arr


