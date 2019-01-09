from os import listdir,remove,rmdir,mkdir
from os.path import isfile,join,splitext,dirname,basename

class Main():
    def __init__(self):
        self.subjects=[]
        for subject in listdir("Subjects\\"):
            self.load_subject("Subjects\\"+subject)
        
        print(self.get_subjects())

    def create_subject(self,tantargy,gyakvez,gyakvezemail,eido,gyakido,web):
        van=False
        for sub in self.subjects:
            if sub.tantargy == tantargy:
                van=True
        if not van:
            sub=Subject()
            sub.tantargy=tantargy
            sub.gyakvez=gyakvez
            sub.gyakvezemail=gyakvezemail
            sub.eido=eido
            sub.gyakido=gyakido
            sub.web=web
            self.subjects.append(sub)
            f=open("Subjects\\"+tantargy+".txt","w+")
            f.write(gyakvez+"\n")
            f.write(gyakvezemail+"\n")
            f.write(eido+"\n")
            f.write(gyakido+"\n")
            f.write(web+"\n")
            f.close()
        else:
            return 1

    def load_subject(self,path):
        f=open(path,"r").read().split("\n")
        sub=Subject()
        sub.gyakvez=f[0]
        sub.gyakvezemail=f[1]
        sub.eido=f[2]
        sub.gyakido=f[3]
        sub.web=f[4]
        sub.tantargy=splitext(basename(path))[0]
        self.subjects.append(sub)

    def get_subjects(self):
        out=[]
        for sub in self.subjects:
            out.append(sub.tantargy)
        return out

class Subject():
    tantargy=""
    gyakvez=""
    gyakvezemail=""
    eido=""
    gyakido=""
    web=""

Main()
