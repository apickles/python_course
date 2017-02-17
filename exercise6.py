file1=open("file1.txt",'r')
content1=file1.read()
file2=open("file2.txt",'r')
content2=file2.read()
file3=open("file3.txt",'r')
content3=file3.read()
filename=datetime.datetime.now()
def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M-%f"),"w") as file:
        file.write("content1"+"\n"+"content2"+"\n"+"content3"+"\n"+)

create_file()
