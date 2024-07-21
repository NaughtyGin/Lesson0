number_of_HW_completed = 12 # Количество выполненных ДЗ
number_of_hours_spent = 1.5 # Количество затраченных часов
course_title = 'Python' # Название курса
average_lead_time = number_of_hours_spent / number_of_HW_completed # Среднее время выполнения одного ДЗ в часах
print('Курс:', course_title, ', всего выполнено ДЗ:', number_of_HW_completed, ', затрачено часов:', number_of_hours_spent, ', среднее время выполнения', average_lead_time, 'часов или', int(average_lead_time * 60), 'минут.')
