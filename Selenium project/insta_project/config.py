WEB_DRIVER_PATH = '/home/abhilash/Documents/Project/personal-project/Selenium project/chromedriver_linux64/chromedriver'
INSTAGRAM_HOST = 'https://www.instagram.com'
INSTA_FOLLOW_TEXT = 'Follow'

# LOGIN PAGE
USERNAME = '<>'
PASSWORD = '<>'
TXT_USERNAME_TEXT_BOX_ID = '_2hvTZ'
BTN_LOGIN_XPATH = '//*[@id="loginForm"]/div/div[3]/button'

##NOTIFICATIONTURNOFF
BTN_NOTNOW_XPATH = '/html/body/div[4]/div/div/div/div[3]/button[2]'

#SEARCHBAR
TXT_SEARCH_BAR = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div'


#FOLLOW_BUTTON
BTN_FOLLOW_XPATH = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button'
BTN_FOLLOW_XPATH_FALLBACK1 = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button'

BTN_UNFOLLOW_XPATH = '/html/body/div[4]/div/div/div/div[3]/button[1]'


#SUGGESTION_BOX
#SUGGESTION_BOX > FOLLOWBUTTON

#SUGGESTION_BOX > INSTAID_TEXT
NAME_INSTAID_XPATH_PART1 = '//*[@id="react-root"]/section/main/div/div[1]/div[2]/div/div/div/ul/li['
NAME_INSTAID_XPATH_PART2 = ']/div/div/div/div/div[2]/a'

NAME_INSTAID_XPATH_PART1_FALLBACK1 = '//*[@id="react-root"]/section/main/div/div[2]/div[2]/div/div/div/ul/li['
NAME_INSTAID_XPATH_PART2_FALLBACK1 = ']/div/div/div/div/div[2]/a'


#SUGGESTION_ARROW_BUTTON
BTN_SUGGESTION_ARROW = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[2]/button'

##INSTAID_LIST
INSTA_ID_LIST = []