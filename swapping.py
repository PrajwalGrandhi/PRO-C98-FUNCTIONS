def swapFileContent():
    f1=input("Enter the file name: ")
    f2=input("Enter the second file name: ")

    file1=open(f1,'r')
    file2=open(f2,'r')

    data_a=file1.read()
    data_b=file2.read()

    print("\nFile Content Before Swapping: ")
    print("File1: ",data_a,"\n")
    print("File2: ",data_b,"\n")

    with open(f1, 'w') as a:
         a.write(data_b)

    with open(f2, 'w') as b:
        b.write(data_a)

    print("\nFile Content After Swapping: ")
    print("File1: ",file1.read(),"\n")
    print("File2: ",file2.read())

swapFileContent()