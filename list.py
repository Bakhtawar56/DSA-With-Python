marks = [95,98,89,"maths"]
print(marks[0:2])



for score in marks:
    print(score)
    marks.append(98)
    print(marks)
    marks.insert((0),99)
    print(marks)