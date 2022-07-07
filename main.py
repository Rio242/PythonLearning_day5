# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆




#Write your code below this row 👇

#initilize total_height variable  
total_height = 0

# for loop to add contents of student_heights array
for height in student_heights:
  total_height += height
print(total_height)

# average height formula
average = total_height/len(student_heights)

print(f"The average hegiht of the sudent is {average}")
