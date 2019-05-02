path = "F:/Output/RAJAT/2018-08-02/09_20_20-screen-0.jpg.txt"

def correct_office(path):
    file = open(path)

    flag = 0

    with open("new.txt", "w") as new:
        for line in file:
            if "Type here to search" in line:
                break
            if "Arial" in line or "Times New Roman" in line or "summary Register" in line:
                continue
            if flag == 1 and len(line) > 2:
                if "e " in line or '> ' in line:
                    new.write("-> "+line[2:]+"\n")
                else:
                    new.write(line)
            if flag == 0 and "File Edit" in line :
                flag = 1
                continue
    file.close()  
#correct_office(path)

