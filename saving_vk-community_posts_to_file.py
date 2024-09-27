import vk_api
import vk_token

token = vk_token.token_id
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

GROUP_ID = 'идентификатор сообщества'
POSTS_COUNT = 100


def get_wall_posts(group_id, posts_count, offset=0):
    return vk.wall.get(owner_id=f'-{group_id}', count=posts_count, offset=offset)


def save_posts_to_txt(posts, post_number, filename="filename.txt"):
    with open(filename, 'a', encoding='utf-8') as f:
        for post in posts['items']:
            text = post.get('text', '').strip()
            if text:
                f.write('\n\n')
                f.write(f"Пoст № {post_number}. {text}\n\n")
                f.write('_______________________________________________________\n'
                        '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
                        '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n'
                        )
                post_number += 1
    return post_number


def parse_all_posts(group_id, posts_count):
    offset = 0
    post_number = 1
    while True:
        posts = get_wall_posts(group_id, posts_count, offset)
        if posts['items']:
            print(f"Количество полученных постов: {len(posts['items'])}")
            post_number = save_posts_to_txt(posts, post_number)
            print(f"Обработано постов: {post_number}")
            offset += posts_count
        else:
            print("Постов для сохранения больше нет!")
            break


parse_all_posts(GROUP_ID, POSTS_COUNT)
