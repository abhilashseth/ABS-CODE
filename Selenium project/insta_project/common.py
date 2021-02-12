from model.driver import Driver
import config
import time

DRIVER = Driver()
DRIVER_OBJ = DRIVER.DRIVER_OBJ


def login_to_insta():
    DRIVER_OBJ.get(config.INSTAGRAM_HOST)
    time.sleep(5)

    # LOGIN
    USERNAME = DRIVER_OBJ.find_element_by_class_name(config.TXT_USERNAME_TEXT_BOX_ID)
    USERNAME.send_keys(config.USERNAME)
    PASSWORD = DRIVER_OBJ.find_elements_by_class_name(config.TXT_USERNAME_TEXT_BOX_ID)[1]
    PASSWORD.send_keys(config.PASSWORD)
    DRIVER_OBJ.find_element_by_xpath(config.BTN_LOGIN_XPATH).click()
    time.sleep(5)
    notification_off()

def notification_off():
    # NOTIFICATIONTURNOFF
    DRIVER_OBJ.find_element_by_xpath(config.BTN_NOTNOW_XPATH).click()

def search_on_search_bar():
    #SEARCHBAR
    SEARCHBAR = DRIVER_OBJ.find_element_by_xpath(config.TXT_SEARCH_BAR).click()
    DRIVER_OBJ.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('NATURE')
    time.sleep(5)

def go_to_insta_id(insta_id):
    # GOTO INSTAID
    print('\n\nNOW GOING TO INSTA ID: ', insta_id)
    insta_id = '/' + insta_id + '/'
    DRIVER_OBJ.get(config.INSTAGRAM_HOST+insta_id)
    time.sleep(5)

def already_following():
    try:
        print('FOLLOW BUTTON STAUS: ', DRIVER_OBJ.find_element_by_xpath(config.BTN_FOLLOW_XPATH).text)
        if str(DRIVER_OBJ.find_element_by_xpath(config.BTN_FOLLOW_XPATH).text) != config.INSTA_FOLLOW_TEXT:
            return True
    except:
        return False
    return False


def click_follow():
    try:
        DRIVER_OBJ.find_element_by_xpath(config.BTN_FOLLOW_XPATH).click()
    except:
        DRIVER_OBJ.find_element_by_xpath(config.BTN_FOLLOW_XPATH_FALLBACK1).click()

    time.sleep(2)

def get_suggestion_box_user_name():
    # GET_SUGGESTION_BOX_INSTAID
    for i in range(3, 13):
        print(i)
        INSTAID = ''
        try:
            INSTAID = DRIVER_OBJ.find_element_by_xpath(
                config.NAME_INSTAID_XPATH_PART1 + str(i) + config.NAME_INSTAID_XPATH_PART2).text
        except:
            print('NAME_INSTAID_XPATH_PART1_FALLBACK1')
            INSTAID = DRIVER_OBJ.find_element_by_xpath(
                config.NAME_INSTAID_XPATH_PART1_FALLBACK1 + str(i) + config.NAME_INSTAID_XPATH_PART2_FALLBACK1).text

        print(INSTAID)
        if INSTAID not in config.INSTA_ID_LIST:
            config.INSTA_ID_LIST.append(INSTAID)

def click_to_get_suggestion_box():
    DRIVER_OBJ.find_element_by_xpath(config.BTN_SUGGESTION_ARROW).click()


def follow_n_get_suggestion_box():
    if already_following():

        print("ALREADY FOLLOWING")
        click_to_get_suggestion_box()
    else:
        print("NOT FOLLOWED So NOW I AM GONNA FOLLOW")
        click_follow()