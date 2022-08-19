import re

class MakeTool():
    '''生成'''
    def __init__(self):
        pass

    def check_re(self, data, type):
        """正则表达式数据校验"""
        type_dict = {
            'email': r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}',
            'url': r'^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+',
            'phone': r'^1(3|4|5|7|8|9)[0-9]{9}',
            'id_card': r'^\d{17}[\d|x]|\d{15}',
            'ip': r'^(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)'
        }
        if type_dict[type]:
            res = re.search(type_dict[type], data)
            if res:
                return res.group(0)
        return None