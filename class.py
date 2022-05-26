class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
      self.name = name
      self.age = age
      self.tracks = tracks
      self.score = int(score)
    
    def change_name(self,name):
      self.name = name
    
    def change_age(self,age):
      self.age = int(age)

    def add_track(self,tracks):
      track = tracks.split()
      for i in track:
        self.tracks.append(i)
      self.tracks = tracks
    
    def get_score(self):
      return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX Back-end Front-end DBMS")
Bob.get_score()

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)
