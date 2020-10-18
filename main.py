
# group 1 | group 2 | group 3
# ---------------------------
# group 4 | group 5 | group 6
# ---------------------------
# group 7 | group 8 | group 9

############# Setup board #############
row_1 = [set([7]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([2]), set([6])]
row_2 = [set([4]), set([5]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([8]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9])]
row_3 = [set([9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([6]), set([5]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9])]

row_4 = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([4]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1])]
row_5 = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([3]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([5]), set([6]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9])]
row_6 = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([2]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([6]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([4]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([7])]

row_7 = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([9]), set([7]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([2]), set([1]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9])]
row_8 = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([3]), set([1, 2, 3, 4, 5, 6, 7, 8, 9])]
row_9 = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([5]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9]), set([1, 2, 3, 4, 5, 6, 7, 8, 9])]
############# Setup board #############

all_rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]

col_1 = [row_1[0], row_2[0], row_3[0], row_4[0], row_5[0], row_6[0], row_7[0], row_8[0], row_9[0]]
col_2 = [row_1[1], row_2[1], row_3[1], row_4[1], row_5[1], row_6[1], row_7[1], row_8[1], row_9[1]]
col_3 = [row_1[2], row_2[2], row_3[2], row_4[2], row_5[2], row_6[2], row_7[2], row_8[2], row_9[2]]

col_4 = [row_1[3], row_2[3], row_3[3], row_4[3], row_5[3], row_6[3], row_7[3], row_8[3], row_9[3]]
col_5 = [row_1[4], row_2[4], row_3[4], row_4[4], row_5[4], row_6[4], row_7[4], row_8[4], row_9[4]]
col_6 = [row_1[5], row_2[5], row_3[5], row_4[5], row_5[5], row_6[5], row_7[5], row_8[5], row_9[5]]

col_7 = [row_1[6], row_2[6], row_3[6], row_4[6], row_5[6], row_6[6], row_7[6], row_8[6], row_9[6]]
col_8 = [row_1[7], row_2[7], row_3[7], row_4[7], row_5[7], row_6[7], row_7[7], row_8[7], row_9[7]]
col_9 = [row_1[8], row_2[8], row_3[8], row_4[8], row_5[8], row_6[8], row_7[8], row_8[8], row_9[8]]

all_cols = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9]

group_1 = [row_1[0], row_1[1], row_1[2], row_2[0], row_2[1], row_2[2], row_3[0], row_3[1], row_3[2]]
group_2 = [row_1[3], row_1[4], row_1[5], row_2[3], row_2[4], row_2[5], row_3[3], row_3[4], row_3[5]]
group_3 = [row_1[6], row_1[7], row_1[8], row_2[6], row_2[7], row_2[8], row_3[6], row_3[7], row_3[8]]

group_4 = [row_4[0], row_4[1], row_4[2], row_5[0], row_5[1], row_5[2], row_6[0], row_6[1], row_6[2]]
group_5 = [row_4[3], row_4[4], row_4[5], row_5[3], row_5[4], row_5[5], row_6[3], row_6[4], row_6[5]]
group_6 = [row_4[6], row_4[7], row_4[8], row_5[6], row_5[7], row_5[8], row_6[6], row_6[7], row_6[8]]

group_7 = [row_7[0], row_7[1], row_7[2], row_8[0], row_8[1], row_8[2], row_9[0], row_9[1], row_9[2]]
group_8 = [row_7[3], row_7[4], row_7[5], row_8[3], row_8[4], row_8[5], row_9[3], row_9[4], row_9[5]]
group_9 = [row_7[6], row_7[7], row_7[8], row_8[6], row_8[7], row_8[8], row_9[6], row_9[7], row_9[8]]

all_groups = [group_1, group_2, group_3, group_4, group_5, group_6, group_7, group_8, group_9]

def check_win():
    for row in all_rows:
        for square_elements in row:
            if len(square_elements) > 1:
                return False
    return True

def remove_element_from_all_other_groups(value, index_matched_value, collection):
    collection_index = 0
    for element in collection:
        if index_matched_value != collection_index:
            try:
                collection[collection_index].remove(value)
            except KeyError:
                # already removed
                collection_index += 1
                continue
        collection_index += 1

def mark_sets(group):
    # collections can be all rows, all columns or all groups
    # for each item in the group, if there is only one option, then remove that option from the rest of the
    # possibilities for every other element in the group
    for row_col_or_group in group:
        # for square_elements in collection_type:
        collection_index = 0
        for possibilities in row_col_or_group:
            if len(possibilities) == 1:
                remove_element_from_all_other_groups(list(possibilities)[0], collection_index, row_col_or_group)
            collection_index += 1

def print_board():
    for row in all_rows:
        current_row = ''
        for square in row:
            current_row += repr(square)
        print (current_row)

def set_element_in_square(square, selected_element):
    new_square = set()
    for element in square:
        if element == selected_element:
            new_square.add(element)
    return new_square

while not check_win():
    print_board()
    print ()
    mark_sets(all_rows)
    print_board()
    print()
    mark_sets(all_cols)
    print_board()
    print()
    mark_sets(all_groups)
    print_board()
    print()
    # check_unique(all_groups)
    # print_board()
    # print()