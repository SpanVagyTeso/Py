from os import listdir,remove,rmdir
from os.path import isfile,join,splitext,dirname

class Main():
    def __init__(self):
        self.users = []
        for i in listdir("Reminders\\"):
            user = User()
            user.id=int(i)
            user.Reminders = []
            self.users.append(user)
        self.load_reminders()

    def check_reminders(self):
        out = []
        for user in self.users:
            for rem in user.Reminders:
                if rem.time == "majd":
                    out.append((user.id,rem.title,rem.text))
                    self.delete_reminder("Reminders\\"+str(user.id)+"\\"+str(rem.title)+".txt")
        return out

    def delete_reminder(self,path):
        remove(path)
        rmdir(dirname(path))

    def load_reminders(self):
        for user in self.users:
            path="Reminders\\"+str(user.id)+"\\"
            files = listdir(path)
            for file in files:
                rem=Reminder()
                f= open(path+file,"r").read().split("\n")
                rem.time=f[0]
                rem.text=f[1]
                rem.title=splitext(file)[0]
                user.Reminders.append(rem)

    def create_reminder(self,id,time,title,text):
        reminder=Reminder()
        reminder.text=text
        reminder.title=title
        reminder.time=time
        self.users[0].Reminders.append(reminder)
        f = open("Reminders\\"+str(id)+"\\"+title+".txt","w+")
        f.write(time+"\n")
        f.write(text)
        f.close()

class Reminder():
    time=""
    title=""
    text=""

class User():
    id=0
    Reminders= None

a = Main()
