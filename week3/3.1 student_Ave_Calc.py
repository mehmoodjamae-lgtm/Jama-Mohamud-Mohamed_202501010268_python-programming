choice = 'Y':
quiz_1 = float (input('Enter Quiz1 mark: '))
quiz_2 = float (input('Enter Quiz2 mark: '))
quiz_3 = float (input('Enter Quiz3 mark: '))

average = (quiz_1 + Quiz_2 + Quiz_3)/ 3

if average >= 50:
    print ('PASS')
else:
    print('FAIL')

    choice = input ('continue? select Y/N:')