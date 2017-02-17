import glob2
import datetime

filelist=glob2.glob("f*.txt")



def create_file():
    with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%f"),"w") as ffile:
        for f in filelist:
            sfile=open(f,'r')
            content= 
            ffile.write(content+"\n")


create_file()
