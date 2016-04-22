from app import *
from Handler import ErrorHandler
Handlers = [
    # (r"/reverse/text/(\w+)/width/(\d{1,2})", ReverseHandler),
    (r"/weiboapi/getuserinfo", IndexHandler),
    # (r'/', FeedHandler),
    (r'/auth/login', AuthHandler),
    (r'/doubanurl', doubanurl),
    (r'/getkeywords', GetKeywords),
    (r'/weiboapi/startspider', StartSpider),
    (r'/weiboapi/getlongtext', LongText),
    (r".*", ErrorHandler),
]
