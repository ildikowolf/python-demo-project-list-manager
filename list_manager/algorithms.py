import try_func

def minsort(t_list):

    list = try_func.int_or_str_list(t_list)

    for i in range(len(list) - 1):
        min_index = i
        minimum = list[min_index]

        for j in range(i + 1, len(list)):
            if minimum > list[j]:
                min_index = j
                minimum = list[j]

        list[i], list[min_index] = minimum, list[i]
        '''
            # lehetne így is az előző sor:
            temp = list[i]
            list[i] = minimum
            list[min_index] = temp
        '''

    return list

def insertion_sort(t_list):

    list = try_func.int_or_str_list(t_list)
    first = 0
    next_position = len(list) - 2

    while next_position >= first:
        next = list[next_position]
        current = next_position

        while (current < len(list) - 1) and (list[current] > list[current + 1]):
            current = current + 1
            list[current - 1], list[current] = list[current], list[current - 1]

        list[current] = next
        next_position = next_position - 1

    return list

def bubble_sort(t_list):

    list = try_func.int_or_str_list(t_list)
    stop_val = False

    while not stop_val:
        stop_val = True

        for step in range(len(list) - 1):

                if list[step] > list[step + 1]:
                    list[step], list[step + 1] = list[step + 1], list[step]
                    stop_val = False

    return list