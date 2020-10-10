class person:
    def __init__(self, fname, lname, health, status):
        self.f_name = fname
        self.l_name = lname
        self.health = health
        self.status = status

def introduce(self):
    print("Hello, my name is {}".format(self.f_name, self.l_name))

def emote(self):
    emotion = random.randrange(1,3)
    if emotion == 1:
        print("{} is happy today".format(self.fname))
    elif emotion == 2:
        print("{} is sad right now".format(self.lname))


def status_change(self):
    if self.health == 100:
        print("{} is totaly healthy!".format(self.fname))
    elif self.health >= 76:
        print("{} is a little tired today".format(slef.fname))
    elif self.health >= 53:
        print("{} feels unwell".format(self.fname))
    elif self.health >= 40:
        print("{} goes to the doctor".format(self.fname))
    else:
        print("{} is unconscious".format(self.fname))

azmul = person("Azmul", "Ali", 99, status=True)
sami = person("sami","ahmed", 88, status=False)
hafsa = person("hafsa", "Jia", 57, status=True)

print("{} is my friend?".format(azmul.f_name, azmul.status))
print("{} is my friend?".format(sami.f_name, sami.status))