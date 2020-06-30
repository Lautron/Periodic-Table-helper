from PTdict import pt_dict


def find_z(elem):
    if elem:
        z = pt_dict[elem]['atomic number']
        return z

# rows = {
#     row1: [],
#     row1: [],
#     row1: [],
# }

while True:
    item_counter = 0
    user_input = input('What elements do you want to search?\n')
    print()
    if user_input == 'exit':
        break
    user_input = user_input.split(' ')
    for elem in user_input:
        z = find_z(elem)
        if z:
            print(f'{elem} --> {z}')
            item_counter += 1
        if item_counter % 3 == 0:
            print()
