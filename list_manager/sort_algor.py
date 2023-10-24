import try_func

input_list = []
list_len = try_func.input_as_int()

for index in range(int(list_len)):

    if index > 0:
        data = input('Kérem adja meg a következő elemet: ')

    else:
        data = input('Kérem adja meg az első elemet: ')

    input_list.append(data)

sorted_list = try_func.sorting_by_alg(input_list)
result_list = try_func.reversed_or_not(sorted_list)
print(result_list)