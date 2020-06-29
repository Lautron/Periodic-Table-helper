

ptDict = {'Actinium': ['Ac', '89', '227', '138'], # Element: [Symbol, Z, A, Nº]
 'Aluminum': ['Al', '13', '26.982', '14'],        # Element: list[0], list[1], list[2], list[3]
 'Americium': ['Am', '95', '243', '148'],
 'Antimony': ['Sb', '51', '121.76', '71'],
 'Argon': ['Ar', '18', '39.948', '22'],
 'Arsenic': ['As', '33', '74.922', '42'],
 'Astatine': ['At', '85', '210', '125'],
 'Barium': ['Ba', '56', '137.327', '81'],
 'Berkelium': ['Bk', '97', '247', '150'],
 'Beryllium': ['Be', '4', '9.012', '5'],
 'Bismuth': ['Bi', '83', '208.98', '126'],
 'Bohrium': ['Bh', '107', '264', '157'],
 'Boron': ['B', '5', '10.811', '6'],
 'Bromine': ['Br', '35', '79.904', '45'],
 'Cadmium': ['Cd', '48', '112.411', '64'],
 'Calcium': ['Ca', '20', '40.078', '20'],
 'Californium': ['Cf', '98', '251', '153'],
 'Carbon': ['C', '6', '12.011', '6'],
 'Cerium': ['Ce', '58', '140.116', '82'],
 'Cesium': ['Cs', '55', '132.905', '78'],
 'Chlorine': ['Cl', '17', '35.453', '18'],
 'Chromium': ['Cr', '24', '51.996', '28'],
 'Cobalt': ['Co', '27', '58.933', '32'],
 'Copernicium ': ['Cn ', '112', '285', '173'],
 'Copper': ['Cu', '29', '63.546', '35'],
 'Curium': ['Cm', '96', '247', '151'],
 'Darmstadtium ': ['Ds ', '110', '271', '161'],
 'Dubnium': ['Db', '105', '262', '157'],
 'Dysprosium': ['Dy', '66', '162.5', '97'],
 'Einsteinium': ['Es', '99', '252', '153'],
 'Erbium': ['Er', '68', '167.259', '99'],
 'Europium': ['Eu', '63', '151.964', '89'],
 'Fermium': ['Fm', '100', '257', '157'],
 'Flerovium': ['Fl', '114', '289', '175'],
 'Fluorine': ['F', '9', '18.998', '10'],
 'Francium': ['Fr', '87', '223', '136'],
 'Gadolinium': ['Gd', '64', '157.25', '93'],
 'Gallium': ['Ga', '31', '69.723', '39'],
 'Germanium': ['Ge', '32', '72.64', '41'],
 'Gold': ['Au', '79', '196.967', '118'],
 'Hafnium': ['Hf', '72', '178.49', '106'],
 'Hassium': ['Hs', '108', '267', '159'],
 'Helium': ['He', '2', '4.002', '2'],
 'Holmium': ['Ho', '67', '164.93', '98'],
 'Hydrogen': ['H', '1', '1.007', '0'],
 'Indium': ['In', '49', '114.818', '66'],
 'Iodine': ['I', '53', '126.904', '74'],
 'Iridium': ['Ir', '77', '192.217', '115'],
 'Iron': ['Fe', '26', '55.845', '30'],
 'Krypton': ['Kr', '36', '83.798', '48'],
 'Lanthanum': ['La', '57', '138.905', '82'],
 'Lawrencium': ['Lr', '103', '262', '159'],
 'Lead': ['Pb', '82', '207.2', '125'],
 'Lithium': ['Li', '3', '6.941', '4'],
 'Livermorium': ['Lv', '116', '292', '176'],
 'Lutetium': ['Lu', '71', '174.967', '104'],
 'Magnesium': ['Mg', '12', '24.305', '12'],
 'Manganese': ['Mn', '25', '54.938', '30'],
 'Meitnerium': ['Mt', '109', '268', '159'],
 'Mendelevium': ['Md', '101', '258', '157'],
 'Mercury': ['Hg', '80', '200.59', '121'],
 'Molybdenum': ['Mo', '42', '95.96', '54'],
 'Moscovium': ['Mc', '115', '288', '173'],
 'Neodymium': ['Nd', '60', '144.242', '84'],
 'Neon': ['Ne', '10', '20.18', '10'],
 'Neptunium': ['Np', '93', '237', '144'],
 'Nickel': ['Ni', '28', '58.693', '31'],
 'Nihonium': ['Nh', '113', '284', '171'],
 'Niobium': ['Nb', '41', '92.906', '52'],
 'Nitrogen': ['N', '7', '14.007', '7'],
 'Nobelium': ['No', '102', '259', '157'],
 'Oganesson': ['Og', '118', '294', '176'],
 'Osmium': ['Os', '76', '190.23', '114'],
 'Oxygen': ['O', '8', '15.999', '8'],
 'Palladium': ['Pd', '46', '106.42', '60'],
 'Phosphorus': ['P', '15', '30.974', '16'],
 'Platinum': ['Pt', '78', '195.084', '117'],
 'Plutonium': ['Pu', '94', '244', '150'],
 'Polonium': ['Po', '84', '210', '126'],
 'Potassium': ['K', '19', '39.098', '20'],
 'Praseodymium': ['Pr', '59', '140.908', '82'],
 'Promethium': ['Pm', '61', '145', '84'],
 'Protactinium': ['Pa', '91', '231.036', '140'],
 'Radium': ['Ra', '88', '226', '138'],
 'Radon': ['Rn', '86', '222', '136'],
 'Rhenium': ['Re', '75', '186.207', '111'],
 'Rhodium': ['Rh', '45', '102.906', '58'],
 'Roentgenium ': ['Rg ', '111', '272', '161'],
 'Rubidium': ['Rb', '37', '85.468', '48'],
 'Ruthenium': ['Ru', '44', '101.07', '57'],
 'Rutherfordium': ['Rf', '104', '261', '157'],
 'Samarium': ['Sm', '62', '150.36', '88'],
 'Scandium': ['Sc', '21', '44.956', '24'],
 'Seaborgium': ['Sg', '106', '266', '160'],
 'Selenium': ['Se', '34', '78.96', '45'],
 'Silicon': ['Si', '14', '28.086', '14'],
 'Silver': ['Ag', '47', '107.868', '61'],
 'Sodium': ['Na', '11', '22.99', '12'],
 'Strontium': ['Sr', '38', '87.62', '50'],
 'Sulfur': ['S', '16', '32.065', '16'],
 'Tantalum': ['Ta', '73', '180.948', '108'],
 'Technetium': ['Tc', '43', '98', '55'],
 'Tellurium': ['Te', '52', '127.6', '76'],
 'Tennessine': ['Ts', '117', '295', '178'],
 'Terbium': ['Tb', '65', '158.925', '94'],
 'Thallium': ['Tl', '81', '204.383', '123'],
 'Thorium': ['Th', '90', '232.038', '142'],
 'Thulium': ['Tm', '69', '168.934', '100'],
 'Tin': ['Sn', '50', '118.71', '69'],
 'Titanium': ['Ti', '22', '47.867', '26'],
 'Uranium': ['U', '92', '238.029', '146'],
 'Vanadium': ['V', '23', '50.942', '28'],
 'Wolfram': ['W', '74', '183.84', '110'],
 'Xenon': ['Xe', '54', '131.293', '77'],
 'Ytterbium': ['Yb', '70', '173.054', '103'],
 'Yttrium': ['Y', '39', '88.906', '50'],
 'Zinc': ['Zn', '30', '65.38', '35'],
 'Zirconium': ['Zr', '40', '91.224', '51']}

def infoSearcher(list):
    print(f'The symbol is: {list[0]}\nThe atomic number is: {list[1]}\nThe Atomic mass is: {list[2]}\n'
          f'The number of neutrons is: {list[3]}\n')

def searchBySymbol(userInput):
    for list in ptDict.values():
        if list[0] == userInput:
            infoSearcher(list)

def searchByAtomicNumber(userInput):
    for list in ptDict.values():
        if list[1] == userInput:
            infoSearcher(list)

def searchByAtomicMass(userInput):
    for list in ptDict.values():
        atomicMass = str(round(float(list[2])))
        if atomicMass == userInput:
            infoSearcher(list)

def searchByNeutrons(userInput):
    for list in ptDict.values():
        if list[3] == userInput:
            infoSearcher(list)


def main(selectInput, userInput):
  switch = {
    'x': searchBySymbol,
    'z': searchByAtomicNumber,
    'a': searchByAtomicMass,
    'n': searchByNeutrons
  }
  function = switch.get(selectInput, "Invalid input")
  function(userInput)


while True:
    selectInput = input('Press X (to search by symbol), Z (to search by atomic number), A (to search by atomic mass),\nN (to search by neutrons)\n'
                        'Or type exit to leave\n')
    userInput = input('Write what you want to search\n')
    selectInput = selectInput.lower()
    main(selectInput, userInput)



