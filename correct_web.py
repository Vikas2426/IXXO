def correct_web(path):
    file = open(path)
    flag = 0
    with open("new.txt", "w") as new:
        for line in file:
            if len(line)<2:
                continue
            if flag == 0 and "http" in line:
                flag = 1
                new.write(line[line.index("h"):])
                continue
            if "Type here to search" in line :
                break 
            if flag == 1:
                new.write(line)
    file.close()

#correct_web("F:/Output/ADITYA/2018-08-13/08_02_02-screen-0.txt")