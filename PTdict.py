import pprint, csv

ptFile = open('Periodic Table of Elements.csv')
ptFileReader = csv.reader(ptFile)

ptDict = {}
for row in ptFileReader:
    if row[1] == 'Element':
        continue
    ptDict[row[2]] = {'name':row[1], # Name
                      'atomic number':row[0], # Atomic number
                      'atomic mass':row[3], # Atomic mass
                      'electrons':row[4],  # Number of neutrons
                      'period':row[7], # Number of electrons
                      'group':row[8],
                      'type':row[15],
                      }

# print(ptDict)
# ptDict = pprint.pformat(ptDict)
# print(ptDict['H'])
