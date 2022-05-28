class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self , name , age ,tracks,score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = str(score)
    
    def change_name(self,name1):
        self.name = name1
        return name1
     
    def change_age(self,age1):
        self.age = age1
        return age1

         
    def add_track(self ,track):
        return self.tracks.append(track)

           
    def get_score(self):
       return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()



print(Bob.name)
print(Bob.score)
print(Bob.tracks)