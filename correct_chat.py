

def correct_chat(path):
    file = open(path) 

    from dateutil.parser import parse

    def is_date(string): #check if string is a date
        try: 
            parse(string)
            return True
        except ValueError:
            return False

    with open("new.txt", 'w') as new: #add path here
        for line in file:
            if len(line) >= 10 and is_date(line):
                new.write("*************** "+line[:len(line)-1]+" ********************\n")
                continue
            if 'Rocket.Chat' in line:
                new.write(" Rocket Chat\n ")
                continue
            if len(line)>2 and ("Type here to search" not in line) and ("RAS so" not in line):
                new.write(line+"\n")
                continue
            if "Type here to search" in line:
                break
            