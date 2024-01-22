
def get_companies(file):
    companies = []
    reader = open(file)
    try:
        #process file
        line = reader.readline()
        while line != '': #'' is EOF character
            print(line, end='')
            strippedLine = line.strip()
            print(strippedLine, end='')
            companies.append(strippedLine)

        print('there are %d companies', len(companies)) 
    finally:
        reader.close()
    
    return companies