from Course_Enrollment import *

mysystem=EnrollmentSystem()
c1=Course("Maths",2)
c2=Course("CS",5)
c3=Course("Physics",1)
s1=Student("Rehan")
s2=Student("Bhavesh")
s3=Student("Kautilya")

mysystem.enroll(c1,s1)
mysystem.enroll(c1,s2)
mysystem.enroll(c1,s3)
mysystem.drop(c1,s1)
mysystem.enroll(c1,s3)
mysystem.drop(c1,s1)