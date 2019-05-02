

def correct_mail(path):
    file = open(path)

    i = 0

    while(i<15):
        for line in file:
            if 'from' in line or 'From' in line or 'CC' in line:
                file.seek(0)
                compose_window(file)
                return
            i += 1
    file.seek(0)
    inbox_window(file)
    return


def compose_window(file):
    flag = 0
    with open('new.txt', 'w') as new:
        for line in file:
            if flag == 0 and "CC" in  line or 'cc' in line:
                flag = 1
            if flag == 1 and "Save" in line and "Discard" in line:
                new.write("Send | Save | Discard\n")
                #continue
                break
            if flag == 1  and "Type here to search" not in line and "Arial" not in line and "Attachments" not in line:
                new.write(line)
    file.close()
    return


def inbox_window(file):
    lis = ['Quick reply Reply all Forward', 'Delete Addto whitelist Add to blacklist', 'Type here to search','Enhancement', 'Do you need more','storage space?', 'Address Book Calendar Tasks','My folders', 'Address Book Calendar  Jasks', 'Select all','Re:','attachment View','browser Download']
    text = []
    flag = 0
    with open('new.txt', 'w') as new:
        for line in file:
            if '@ixxo' in line or '@rockchain' in line:
                new.write(line)
                continue

            for words in lis:
                if words in line:
                    flag = 1
            if flag == 0:
                text.append(line)
            else:
                flag = 0
                text = []
        
        for line in text:
                new.write(line)
    file.close()
    return

#correct_mail("F:/Output/RAJAT/2018-08-06/04_32_27-screen-0.jpg.txt")