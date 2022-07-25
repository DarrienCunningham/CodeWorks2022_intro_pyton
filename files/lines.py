def count():
    a = "files/"
    b = input("Enter a file: ")    #story.txt
    file_name = a + b
    file = open(file_name, "r")
    lines = 0
    for x in file:
        lines = lines + 1
    print(lines)
    file.close()
count()
