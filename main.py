from vk_api.longpoll import VkEventType, VkLongPoll
from bot import *
from database import *
def handle_message(activity):
	request = activity.text.lower()
	user_id = activity.user_id
	if request=='поиск':
		bot.get_age(user_id)
		bot.get_city(user_id)
		bot.finding(user_id)
		bot.show_retrieved(user_id)
	elif request=='смотреть':
		if bot.get_user_id()!= 0:
			bot.show_retrieved(user_id)
		else:
			bot.print('Ошибка')
	elif request=='очистить':
		delete_database()
		create_database()
	else:
		bot.print(user_id, '{bot.name(user_id)}'
			'"поиск" - поиск людей\n'
			'"очистить" - удаляет старую БД и создает новую\n'
			'"показать" - просмотр следующей записи в БД')
for activity in bot.longpoll.listen():
	if activity.type==VkEventType.MESSAGE_NEW and activity.to_me:
		handle_message(activity)