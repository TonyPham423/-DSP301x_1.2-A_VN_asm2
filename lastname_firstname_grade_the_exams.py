


#TASK 1

while True:
    try:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        data  = open(filename+'.txt', 'r')
        file = data.read()
        print('Successfully opened ' + filename + '.txt') 
        break
    except:
        print('File cannot be found. Please try again!')

#THIS IS TASK 2

splitdata = file.split("\n")
print('**** ANALYZING ****')
valid_line = 0
invalid_line = 0
valid_lines = []
final = []
for line in splitdata:
    # scan với điều kiện: Một dòng không hợp lệ chứa danh sách khác 26 giá trị được phân tách bằng dấu phẩy
    splitline = line.split(',')
    # scan với điều kiện:1 dòng không hợp lệ không chứa ký tự “N” theo sau là 8 ký tự số
    if len(splitline[0]) != 'N' and len(splitline[0]) != 9:
        invalid_line +=1 
        print('Invalid line of data: N# is invalid\n' + line)
    elif splitline[0] < 'N00000000' or splitline[0] >'N99999999':
        invalid_line +=1 
        print('Invalid line of data: N# is invalid\n' + line)
    elif len(splitline) != 26:
        invalid_line +=1 
        print('Invalid line of data: does not contain exactly 26 values:\n'+ line)
    # các trường hợp còn lại là dòng hợp lệ
    else:
        valid_lines.append(splitline)
        valid_line +=1 
        final.append(splitline[0])
if invalid_line == 0:
    print('No errors found!')
print('**** REPORT ****')
print('Total valid lines of data: ' + format(valid_line))
print('Total invalid lines of data: ' + format(invalid_line))


#THIS IS TASK 3

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
split_answer = answer_key.split(',')
total_stu = valid_line
high_grade = 0
grades = []
skip_answer = {}
flase_answer = {}

for splitline in valid_lines:
    if len(splitline) != 26 or not len(splitline[0]) != 'N' and len(splitline[0]) != 9: continue
    
    # Calculate grade_score
    grade_score = 0
    for num in range(len(split_answer)):
        if splitline[num+1] == split_answer[num]:
            grade_score += 4
        elif splitline[num+1] == '':
            skip_answer[num+1] = skip_answer.get(num+1, 0) + 1
        else:
            grade_score -=1
            flase_answer[num+1] = flase_answer.get(num+1, 0) + 1 
    #Total student of high scores
    grades.append(grade_score)
    if grade_score > 80:
        high_grade +=1 

print("Total student of high scores:",format(high_grade))

grades2 = []
for grade in grades:
    grades2.append(grade)
grades2.sort()
dict_grade = {}
dict_grade[splitline[0]] = grade_score
sum_of_grades = sum(grades)
avg = (sum_of_grades / len(grades))

print("Mean (average) score:",format(avg,".2f"))
print("Highest score:",max(grades))
print("Lowest score:",min(grades))
print("Range of scores:", (max(grades) - min(grades)))

# Median score
if len(grades) % 2 != 0:
    grades2.sort()
    print("Median score:",grades2[int(len(grades)//2+1)])
else:
    grades2.sort()
    median = (grades2[int(len(grades)/2-1)] + grades2[int(len(grades)/2)])/2
    print("Median score:", median)

num_skip = 0  
num_flase = 0  
skip_list = []  
flase_list = []
#Question that most people skip
for qst, num in skip_answer.items():
    if num > num_skip:
        num_skip = num
skip_rate = round(num_skip / total_stu, 3)

for qst, num in skip_answer.items():
    if num == num_skip:
        x = ' - '.join([str(qst), str(num), str(skip_rate), ])
        skip_list.append(x)
str_skip = ', '.join(skip_list)

#Question that most people answer incorrectly
for qst, num in flase_answer.items():
    if num > num_flase:
        num_flase = num
#flase_rate
flase_rate = round(num_flase / total_stu, 3)
for qst, num in flase_answer.items():
    if num == num_flase:
        y = ' - '.join([str(qst), str(num), str(flase_rate)])
        flase_list.append(y)
str_flase = ', '.join(flase_list)
print('Question that most people skip: ', format(str_skip))
print('Question that most people answer incorrectly: ', format(str_flase))

#THIS IS TASK 4

final_grades = filename + "_grades.txt"
grades_file = open(final_grades,'w')
grades_file.write("#This is what " + final_grades + " should look like" + '\n')
for i in range(len(final)):
    forfile = (final[i] + ','+ str(grades[i])+'\n')
    grades_file.write(forfile)
grades_file.close()

