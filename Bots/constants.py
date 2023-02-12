import os


CHROME_PATH = r'MacintoshHD:/Users/lucafrattini/0/dev/chromedriver_mac_arm64'
BOTS = {'intern', 'gym', 'courses'}

"""
INTERN Constants
"""
URL_INTERNSHIPS = {
    'LinkedIn': '',
    'Venture Loop': '',
    'AngelList': '',
    'Vault': '',
    'UC Berkley Career': '',
    'Chegg': '',
    'Indeed': '',
    'ZipRecruiter': ''
}
LOCATIONS = ['Bay Area',
             'New York',
             'Zurich',
             'Boston',
             'Singapore',
             'Sidney']

""" 
GYM Constants 
"""
URL_GYM = 'https://x.tudelft.nl/products/bookable-product-schedule'
GYM_SESSIONS = ['fitn','hat','power y']
USERNAME_TUDELFT = 'lfrattini'
PASSWORD_TUDELFT = os.environ.get('TUDELFT_PASSWORD')
TEST_GYM_SESSION = GYM_SESSIONS[0]
TEST_TIME_SLOT = '17:00'

"""
COURSES Constants
"""
URL_COURSES = 'https://www.tudelft.nl'
COURSE_OPTIONS = ['bachelors','masters','phd']