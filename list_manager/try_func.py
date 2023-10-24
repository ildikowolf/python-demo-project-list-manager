import algorithms

def int_or_str_list(list):

    try:
        list = [int(s) for s in list]
    except (ValueError, TypeError):
        list = [b.lower() for b in list]

    return list

def input_as_int():

    len_list = input('Kérem adja meg a lista hosszát (számként): ')
    input_is_an_int = False

    while input_is_an_int is False:

        try:
            len_list == int(len_list)
        except (ValueError, TypeError):
            len_list = input('Kérem egy számot adjon meg: ')
        else:
            input_is_an_int = True


    return len_list

def sorting_by_alg(list):

    r_list = []
    an_input = input('Kérem válasszon egy rendező algoritmust (1 = bubblesort/2 = insertion sort/3 = minsort): ')
    sorting_is_selected = False

    while sorting_is_selected is False:

        try:
            if an_input == '1':
                r_list = algorithms.bubble_sort(list)
                sorting_is_selected = True

            elif an_input == '2':
                r_list = algorithms.insertion_sort(list)
                sorting_is_selected = True

            elif an_input == '3':
                r_list = algorithms.minsort(list)
                sorting_is_selected = True
            else:
                an_input = input('Kérem 1 és 3 között válasszon egy számot: ')

        except ValueError as e:
            print(e)

    return r_list

def reversed_or_not(list):

    order = input('Kérem adja meg, hogy nővekvő vagy csökkenő sorrendbe legyen a lista (1 = nővekvő/2 = csökkenő): ')
    list_is_ordered = False

    while list_is_ordered is False:

        try:
            if order == '1':
                list_is_ordered = True
            elif order == '2':
                list_is_ordered = True
                list.reverse()
            else:
                order = input('Kérem 1 és 2 között válasszon: ')

        except ValueError as e:
            print(e)

    return list