from bs4 import BeautifulSoup
from requests import get
from sys import argv

if not "--help" in argv:
	URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQgxtRuvH2J_wEy2Khiq8i_Yy_LzYy9yvDs9i1ixUFW8oVK9wOhAW9_M42wo1JVvGmaYFegPqVF4oIE/pubhtml?gid=1544454712&single=true"

	page = get(URL)


	soup = BeautifulSoup(page.text, "html.parser")
	result = []

	class Student:
		def __init__(self, number, city, year, admission, level, solved_problems):
			self._number = int(number) if number else number
			self._city = city
			self._year = year
			self._admission = admission
			self._level = level
			self._solved_problems = sorted(solved_problems)

		def equal_to_another_student(self, another_student):
			same_city = self._city == another_student._city if self._city != "any" else True
			same_year = self._year == another_student._year if self._year != "any" else True
			same_admission = self._admission == another_student._admission if self._admission != "any" else True
			same_level = self._level == another_student._level if self._level != "any" else True
			same_solved_problems = self._solved_problems == another_student._solved_problems if self._solved_problems != sorted("any") else True

			return same_city and same_year and same_admission and same_level and same_solved_problems


	values = ["311", "312", "313", "314", "307", "308", "309",
			"310", "303", "304", "305", "306", "325", "326", "327", "328", "320",
			"321", "322", "323", "324", "315", "316", "317", "318", "319"
	]

	for val in soup.findAll("tr"):
		parameters = []
		student_exercises = []
		for idx, opt in enumerate(val):
			if idx > 4:
				if opt.text == "✓":
					student_exercises.append(values[idx-5])
			else:
				parameters.append(opt.text)
		parameters.append(student_exercises)
		result.append(Student(*parameters))

	city = input("Введите город: ")
	year = input("Введите класс: ")
	admission = input("Введите основание для поступления: ")
	level = input("Введите выданный уровень: ")
	exercises = []
	count = input("Введите кол-во решенных практических задач: ")
	if count != "any":
		for i in range(int(count)):
			exercise = input("Введите номер задачи(смотрите номер в таблице): ")
			exercises.append(exercise)
	else:
		exercises = "any"

	student_to_find = Student(None, city, year, admission, level, exercises)
	print("\n----------------\n")

	for student in result:
		if student_to_find.equal_to_another_student(student):
			print("===========================")
			print("Найдено совпадение: ")
			print(f'Номер в таблице: {student._number-1}')
			print(f'Решенные задачи: {student._solved_problems}, Город: {student._city}, Уровень: {student._level}, Класс: {student._year}, Поступление: {student._admission}')
			print("============================")
else:
	print("Эта программа поможет вам найти себя в таблице результатов ЛКШ.\n")
	print("Как пользоваться этой программой?\n")
	print("После нескольких секунд ожидания, Вас попросят ввести ваши данные.")
	print("Когда вас попоросят ввести город, введите то, что вводили в анкете на вопрос о городе.")
	print("Когда вас попоросят ввести основание для поступления, введите то, что вводили в личном кабинете на вопрос о способе поступления.")
	print("Когда вас попоросят ввести класс, введите то, что вводили в анкете на вопрос о классе. (Вводите ТОЛЬКО число)")
	print("Когда вас попоросят ввести паралель, введите ту паралель, которую вы получили решив тематическую анкету.")
	print("Когда вас попоросят ввести кол-во задач, введите кол-во решенных практических задач.")
	print("Когда вас попоросят ввести номер решенной задачи, зайдите в таблицу результатов, найдите вашу решенную задачу и посмотрите на трехзначное число, а потом введите его.")
	print("="*50)
	print("ВАЖНОЕ ЗАМЕЧАНИЕ: если вы хотите, например, найти всех учеников у которых класс может быть любым, но город -- Москва, то там где у вас спрашивают класс, напишите any. (Применимо ко всем параметрам)")
