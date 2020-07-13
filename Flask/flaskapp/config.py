import os
class Config:
   
    SECRET_KEY = '8a74d6b55af7824f00b861cf3b445fbe' # A secret key signs cookies when a user visits the site and therefore prevents cookie tampering
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "cpelkington2216@gmail.com"
    MAIL_PASSWORD = "oiap kyjs prxe fstq"
    
''' We should make sure we store the SECRET_KEY, SQLALCHEMY_DATABASE_URI,
MAIL_USERNAME and MAIL_PASSWORD as environment variables. You do this by 
going to Explorer, right clicking on 'This PC', clicking 'properties', 
clicking 'Advanced system settings', selecting environment variables and 
adding new system variables for each of these. Then in this code above we 
can set each variable equal to os.environ.get('envionment_variable_name')
'''