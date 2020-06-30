from spanishElems import spanish_elems_dict

def get_key(val, anyDict): 
    for key, value in anyDict.items(): 
         if val == value: 
             return key 
    
    print(f'Could not find key for "{val}"')

if __name__ == "__main__":
    
    line_lenght = 30
    arrow = '-->'.center(10)

    while True:

        userInput = input('Que elementos quieres buscar?\n')
        if userInput == 'exit':
            break
        userInput = userInput.split(' ')
        print()

        for elem in userInput:
            if elem in spanish_elems_dict.keys():
                name = spanish_elems_dict.get(elem)
                string = f'{elem} {name.center(len(name) * 3)}'
                print(''.center(len(string), '-'))
                print(string)
                continue
            
            if elem in spanish_elems_dict.values():
                name = get_key(elem, spanish_elems_dict)
                string = f'{elem} {name.center(len(elem) * 2)}'
                print(''.center(len(string), '-'))
                print(string)
                continue

            print(f'Could not find element "{elem}"')

        print(''.center(len(string), '-'))
        print()

