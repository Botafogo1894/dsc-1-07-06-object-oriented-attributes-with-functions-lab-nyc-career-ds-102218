class School:

    def __init__(self, name, roster = {}):
        self._name = name
        self._roster = roster

    def add_student(self, name, grade):
        try:
            self._roster[grade].append(name)
        except:
            self._roster[grade] = [name]

school = School("Middletown High School")

school.add_student("Dilyan", 12)

print(school._roster)
