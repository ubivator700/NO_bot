import no_vk_bot
import random

def send_msg(peer_id, botmessage=None, keyboard=None, photo=None):
    rnd = random.randint(1, 100000)
    post = {
        'peer_id': peer_id,
        'message': botmessage,
        'random_id': rnd,
        }

    if keyboard is not None:
        post['keyboard'] = keyboard.get_keyboard()

    if photo is not None:
        post["attachment"] = photo

    no_vk_bot.vk_session.method('messages.send', post)
