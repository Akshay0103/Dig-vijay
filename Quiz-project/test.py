from User import Examiner,Candidate

e1=Examiner("Akshay",23)
print(e1)
e1.addQuestion("General Knowledge","easy")
e1.addQuestion("Science","easy")
e1.addQuestion("Maths","medium")
e1.addQuestion("Maths","Difficult")
e1.displayAllQuestions()

c1=Candidate("Ankit",16)
print(c1)
c1.viewTopics()
c1.run_test()
