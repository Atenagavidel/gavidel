def calculate_average(grades):

  """Calculates the weighted average of a list of grades.



  Args:

    grades: A list of tuples, where each tuple contains the weight and grade of an exam.



  Returns:

    A string representing the letter grade equivalent to the average.

  """





  weighted_sum = sum(weight * grade for weight, grade in grades)

  total_weight = sum(weight for weight, _ in grades)




  average = weighted_sum / total_weight




  letter_grades = ['F', 'E', 'D', 'C', 'B', 'A']

  letter_grade = letter_grades[min(int(average), 5)]  


  return letter_grade




n = int(input())




grades = []

for _ in range(n):

  weight, grade = map(float, input().split())

  grades.append((weight, grade))




average_grade = calculate_average(grades)

print(average_grade)
