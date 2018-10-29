class School:

    def __init__(self, name, roster = {}):
        self._name = name
        self._roster = roster

    def add_student(self, name, grade):
        try:
            self._roster[grade].append(name)
        except:
            self._roster[grade] = [name]

    def grade(self, grade):
        return self._roster[grade]

    def sort_roster(self):
        new_roster = self._roster.copy()
        for key in new_roster.keys():
            new_roster.update({key: sorted(new_roster[key])})
        return sorted(new_roster.items(), key = lambda item: item[0])


school = School("Middletown High School")

school.add_student("Dilyan", 12)
school.add_student("Kelly Slater", 9)
school.add_student("Tony Hawk", 10)
school.add_student("Ryan Sheckler", 10)
school.add_student("Bethany Hamilton", 11)

print(school._roster)
