uuidChars = ("a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
             "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
             "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z")

class systemsettings(object):
    def __init__(self):
        self.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        self.EMAIL_USE_TLS = False #是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
        self.EMAIL_USE_SSL = True #是否使用SSL加密，qq企业邮箱要求使用
        self.EMAIL_HOST = 'smtp.qq.com' #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
        self.EMAIL_PORT = 587  #发件箱的SMTP服务器端口
        self.DEFAULT_FROM_EMAIL = 'zmlhongyi@vip.qq.com'
        self.EMAIL_HOST_USER ='zmlhongyi@vip.qq.com'#发送邮件的邮箱地址
        self.EMAIL_HOST_PASSWORD = 'nuioxvvpjgkxbcij'   #发送邮件的邮箱密码(这里使用的是授权码)    """description of class"""

    def short_uuid(self,long_uuid:str):
        res = ''
        for i in range(8):
            sub = long_uuid[i*4:i*4+4]
            x = int(sub,16)
            res += uuidChars[x % 0x3E]
        return res