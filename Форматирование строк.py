# Использование %:
team1_num = 6
team2_num = 6
output1 = "В команде Мастера кода участников: %d !" % team1_num
output2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(output1)
print(output2)
# Использование format():
score_2 = 42
team1_time = 18015.2
output3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
output4 = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(output3)
print(output4)
# Использование f-строк:
score_1 = 40
score_2 = 42
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = 82
time_avg = 350.4
output5 = f"Команды решили {score_1} и {score_2} задач."
output6 = f"Результат битвы: {challenge_result}"
output7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
print(output5)
print(output6)
print(output7)