def sttFormat():
    file1 = open('Pwords.txt', 'r')
    file2 = open('Ewords.txt', 'r')
    first_delay = r'"1s"'
    second_delay=r'"2s"'


    lines1 = file1.readlines()
    lines2 = file2.readlines()
    with open("langConvert.txt", "w") as fp:
        for x in range(100):
            translation = "[speaker: Ricardo] " + lines1[x] + f"<break time={first_delay}" + "/>" + "\n" + "[speaker:Matthew] " + lines2[x] + f"<break time={second_delay}" + "/>"
            print(translation)
            fp.writelines(translation)
    file1.close()
    file2.close()


sttFormat()