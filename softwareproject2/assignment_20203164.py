import pickle

dbfilename = 'assignment_20203164.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        for p in scdb :
            p['Score'] = int(p['Score'])
            p['Age'] = int(p['Age'])
 
        if parse[0] == 'add':
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]

        elif parse[0] == 'find':
            print("find를 선택하셨습니다.")
            for p in scdb:
                if p['Name'] == parse[1]:
                 print(p)
                    
        elif parse[0] == 'inc' :
            for p in scdb :
                if p['Name'] == parse[1] :
                    amount = int(parse[2])
                    for attr in sorted(p) :
                        p['Score'] += int(amount // 3)
                        print('{} = {}'.format(attr,p[attr]))

        elif parse[0] == 'del':
            tmp =[]
            for p in scdb:
                if p['Name'] != parse[1] :
                    tmp.append(p)
                scdb = tmp
            
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'quit':
            break

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print('{} {}  {}'.format(attr,'=', p[attr]), end = ' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)