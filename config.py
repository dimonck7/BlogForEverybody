# -*- coding: utf8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' },
	{ 'name': 'StackExchange', 'url': 'https://openid.stackexchange.com' },
	{ 'name': 'Blogspot', 'url': 'https://<blogname>.blogspot.com' },
	{ 'name': 'LiveJournal', 'url': 'http://<username>.livejournal.com' },
	{ 'name': 'Wordpress', 'url': 'https://<username>.wordpress.com' },
	{ 'name': 'VerisignLabs', 'url': 'https://pip.verisignlabs.com' },
	{ 'name': 'Technorati', 'url': 'https://technorati.com/people/technorati/<username>' },]
    
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'blog2015everybody@gmail.com'
MAIL_PASSWORD = 'hahol123'

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'Post_Translate' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = 'FEqOVo+GJwctjw0NAbFHCmuWN968aPqdqmBQDvoGLtU=' # enter your MS translator app secret here

# administrator list
ADMINS = ['blog2015everybody@gmail.com']

# pagination
POSTS_PER_PAGE = 6
MAX_SEARCH_RESULTS = 50