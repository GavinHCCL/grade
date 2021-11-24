A = "A"
B = "B"
C = "C"
D = "D"
F = "F"
grades = [A,B,C,D,F]

Josh = [D, B]
Jack = [F, D]
Steve = [C, B]

program = "running"

students = { "josh": Josh, "jack": Jack, "steve": Steve }

while program == "running":
  question = input("Type [1] to view the kids grades \n\nType [2] to change them!\n")

  if question == "1":
    print(f"\nJosh:\n{Josh}\nJack:\n{Jack}\nSteve:\n{Steve}\n")

  if question == "2":
    who = input("\nWho do you want to change?\n").lower()
    if who in students:
      student = students[who]
      grade = input("\nFirst grade to change:\n").upper()
      if grade in grades:
          student[0] = grade

if program == "stop":
  print("Shutting down.")