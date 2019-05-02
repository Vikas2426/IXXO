
def correct_code(path):
    file = open(path)
    with open("new.txt", "w+") as new:
        for line in file:
            for word in line.split():
                try: 
                    int(word)
                    new.write(line[line.index(word):])
                except ValueError:
                    continue
        file.close()

