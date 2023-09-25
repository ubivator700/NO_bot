import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_tools
import db
import time

UPSKILLS_TOKEN = 'vk1.a.S4Q1L6UHrlY4EhqtdfGsukOXrux9LrdaSuHH03_cjhiuyA0wzJPFUkgyZtEpSc_etAKKfW-4T35HHPAwMcb-vq-P_Lz4kHgECDQQLmRgCZqsvKo6mRQvhHc7urvnpu2RcAnHm9lTHoOn-HCi2BESqIVYehxhmOB3_6Lb_vonGQOmSNIuxEUn_tP6vCED_o0fUFV1F3m3tsDxLKXncA1MMQ'
GROUP_ID = '221561257'
vk_session = vk_api.VkApi(token=UPSKILLS_TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vkf = vk_session.get_api()
meth = vk_api.requests_pool.VkRequestsPool(vk_session)


def bot():
    print('STARTED')
    for event in longpoll.listen():
        if event.type == VkBotEventType.GROUP_JOIN:
            u_id = str(event.object['user_id'])
            print('joined')
            vk_tools.send_msg(u_id, 'Спасибо за подписку!')

        if event.type == VkBotEventType.GROUP_LEAVE:
            u_id = str(event.object['user_id'])
            vk_tools.send_msg(u_id, 'Будем ждать вас!')
            print('left')
            vk_session.get_api()
            
            

        if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
            event_data = event.message
            user_id = event_data['peer_id']
            user_list = vkf.users.get(user_ids=user_id, fields='city')
            profile = user_list[0]
            user_name = profile['first_name']
            user_city = profile['city']['title']
            print(user_city)

            db.add_user(event_data['peer_id'], user_city, 'ВК', event_data['text'])
            time.sleep(10)

while __name__ == '__main__':
    try:
        bot()
    except Exception as e:
        print('\n\n---VK BOT EXEPTION---\n\n')
        print(e)
        print('\n\n---END OF VK BOT EXEPTION---\n\n')
