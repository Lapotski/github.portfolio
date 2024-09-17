#Grading System

#Initiate Variables
scoreHomework=0
scoreMidterms=0
scoreFinals=0
finalGrade=0

#input values
scoreHomework=int(input("Homework Score out of 100: "))
scoreMidterms=int(input("Midterm Exam Score out of 100: "))
scoreFinals=int(input("Final Exam Score out of 100: "))

#calculate final grade

finalGrade=(scoreHomework*0.4)+(scoreMidterms*0.3)+(scoreFinals*0.3)

#Print and conditionals
print ("Final Grade:",finalGrade)

if finalGrade>=90:
    print("Letter Grade: A")
elif finalGrade >=80:
    print("Letter Grade: B")
elif finalGrade >=70:
    print("Letter Grade: C")
elif finalGrade >=60:
    print("Letter Grade: D")
else:
    print ("Letter Grade: F")