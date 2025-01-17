from PTdict import pt_dict
from spanishElems import spanish_elems_dict as sp_elems
from nameFinder import get_key

def table_printer(anyList):
    new_list = []
    for i in anyList[1:]:
        new_list.append(i.center(20))
    final_list = anyList[0].ljust(20) + ' '.join(new_list)
    lenght = len(final_list)
    print(''.center(lenght, '-'))
    print(final_list)


while True:

    table_info = {
    'name':['Name:'],
    'atomic mass':['Atomic mass:'],
    'atomic number':['Atomic number:'],
    'electrons':['Electrons:'],
    'group':['Group:'],
    'period':['Period:'],
    'type':['Type:'],
}

    user_input = input('What elements do you want to compare?\n')
    if user_input == 'exit':
        break
    user_input = user_input.split()
    print('\n')
    
    for i in user_input:
        if len(i) > 2:
            i = get_key(i, sp_elems)
        if not i:
            continue
        elem = pt_dict[i]
        for k in elem.keys():
            table_info[k].append(elem[k])
    
    for k in table_info.keys():
        table_printer(table_info[k])
    print('\n')
    