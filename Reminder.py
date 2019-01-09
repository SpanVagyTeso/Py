from os import listdir,remove,rmdir,mkdir
from os.path import isfile,join,splitext,dirname
from datetime import *

class Main():
    def __init__(self):
        self.users = []
        for i in listdir("Reminders\\"):
            user = self.create_user(int(i))
            self.users.append(user)
        self.load_reminders()

    def check_reminders(self):
        remove = []
        out = []
        for user in self.users:
            for rem in user.Reminders:
                if rem.time < datetime.now():
                    out.append((user.id,rem.title,rem.text))
                    remove.append((rem,user))
                    self.delete_path_reminder(user.id,rem.title)

                elif rem.time < (datetime.now()+timedelta(days=1)) and rem.counter == 0:
                    out.append((user.id,rem.title,rem.text))
                    rem.counter+=1
        for i in remove:
            for user in self.users:
                if i[1] == user:
                    user.Reminders.remove(i[0])

        return out

    def get_reminders(self,id):
        out= None
        for user in self.users:
            print(str(user.id)+" "+str(id))
            if int(user.id) == int(id):
                out=user.Reminders
        return out

    def get_reminder(self,id,title):
        out = None
        for user in self.users:
            if int(user.id) == int(id):
                for rem in user.Reminders:
                    if rem.title == title:
                        out=rem

        return out

    def delete_reminder(self, id, title):
        drem = None
        for user in self.users:
            if user.id == int(id):
                for rem in user.Reminders:
                    if rem.title == title:
                        drem = rem
                        break
            if not drem == None:
                user.Reminders.remove(drem)
                self.delete_path_reminder(id,title)
                return "Done"
        return "Missing Title"

    def delete_path_reminder(self,id,title):
        path="Reminders\\"+str(id)+"\\"+title+".txt"
        remove(path)
        rmdir(dirname(path))


    def load_reminders(self):
        for user in self.users:
            path="Reminders\\"+str(user.id)+"\\"
            files = listdir(path)
            for file in files:
                rem=Reminder()
                f= open(path+file,"r").read().split("\n")
                time=f[0]
                if len(time) == 4:
                    rem.time = datetime(datetime.now().year,int(time[0:2]),int(time[2:4]))
                elif len(time) == 8:
                    rem.time = datetime(datetime.now().year,int(time[0:2]),int(time[2:4]),int(time[4:6]),int(time[6:8]))
                rem.text=f[1]
                rem.title=splitext(file)[0]
                user.Reminders.append(rem)

    def create_reminder(self,id,time,title,text):
        reminder=Reminder()
        reminder.text=text
        reminder.title=title
        reminder.time=time
        valid = False

        for user in self.users:
            if int(id) == int(user.id):
                valid = True
                user.append(reminder)
                break
        if not valid:
            user = self.create_user(int(id))
            user.Reminders.append(reminder)
            self.users.append(user)
            mkdir("Reminders\\"+str(id))

        f = open("Reminders\\"+str(id)+"\\"+title+".txt","w+")
        f.write(time+"\n")
        f.write(text)
        f.close()

    def create_user(self,id):
        user = User()
        user.id=id
        user.Reminders=[]
        return user


class Reminder():
    time=None
    title=""
    text=""
    counter=0

class User():
    id=0
    Reminders= None

a = Main()
