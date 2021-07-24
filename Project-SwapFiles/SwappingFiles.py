
def swapFileData(file1 , file2):
    with open (file1 , 'r') as file1Read:
        file1_data = file1Read.read()

    with open (file2 , 'r') as file2Read :
        file2_data = file2Read.read()

    with open(file2 , 'w') as f1:
        print(file1_data)
        f1.write(file1_data)

    with open(file1, 'w') as f2:
        print(file2_data)
        f2.write(file2_data)

    
swapFileData('testFile1.txt' , 'testFile2.txt')