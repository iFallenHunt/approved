ntest = int(input('Enter the number of grades for the course: '))
cod = int(input('Enter the student code: '))
passed = int
disapproved = int
cont = int
average = int
grade = int
sum = int

passed = 0
disapproved = 0

while cod != 0:
  sum = 0
  average = 0 
  for cont in ntest :
    print('enter the grade: ')
    sum = sum + grade
  mean = sum / ntest
  if average >= 7:
      passed = passed + 1
  else:
      disapproved  = disapproved  + 1 
  input('Enter the student code')
print('The number of passes is: ', passed)
print('The number of failed students is: ', disapproved )
