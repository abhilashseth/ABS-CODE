
from common import *


login_to_insta()
go_to_insta_id('nature')
follow_n_get_suggestion_box()

get_suggestion_box_user_name()

for user in config.INSTA_ID_LIST:
    print(config.INSTA_ID_LIST)
    print('LENGTH OF LIST: ', len(config.INSTA_ID_LIST))
    config.INSTA_ID_LIST.pop(0)
    go_to_insta_id(user)
    follow_n_get_suggestion_box()
    get_suggestion_box_user_name()





















