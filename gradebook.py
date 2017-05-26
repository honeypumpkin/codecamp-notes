# create a list to hold grades
grades = []
continue_entry = True

# prompt and collect grades, use while loop
while continue_entry:

    #prompt for score and credits
    score = float(input('Your grade (0.0-4.0):'))
    num_credits = int(input('Credits:'))

    # put each grade in a dictionary
    grade = {'score': score, 'credits': num_credits}
    grades.append(grade)

    # prompt to ask if continue
    user_continue = input('Enter another grade? [y/n]:')
    if user_continue == 'n':
        continue_entry = False

quality_score = 0
total_credits = 0
    #or can use list comprehension to call a sum of list
    #all_credits = [a_grade['credits'] for a_grade in grades]
    #total_credits = sum(all_credits)

# calculate GPA (using accumulator pattern)
for a_grade in grades:
    quality_score += a_grade['credits'] * a_grade['score']
    total_credits += a_grade['credits']
    
gpa = quality_score / total_credits


# print GPA
print('GPA: ', gpa)
