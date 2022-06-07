import random
class Student:
    def __init__(self, name,max_day):      #1
        self.name = name
        self.max_day=max_day                      #2
        self.gladness = 50
        self.progress = 0
        self.money= 1000
        self.alive = True
    def __iter__(self):                         # ітерування об'єкта
        self.days=0
        return self
    def __next__(self):                        #4 код ітерації
        self.days+=1
        if self.days>self.max_day:
            raise StopIteration      # зупинка ітерації
        return self.days

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money-=20

    def to_work(self):
        print("I have to work")
        self.gladness-=1
        self.progress -= 0.005
        self.money+=7

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 3:
            print("Passed externally…")
            self.alive = False
        elif self.money<=0:
            print("I'm looser")
            self.alive=False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube==4:
            self.to_work()
        self.must()
        self.end_of_day()
        self.is_alive()

    def must(self):
        if self.money<=50:
            self.to_work()
        if self.progress<=-0.1:
            self.to_study()


nick = Student(name="Nick",max_day=365)
for day in nick:
    if nick.alive == False:
        break
    nick.live(day)