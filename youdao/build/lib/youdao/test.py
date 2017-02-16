#!/usr/bin/python
# coding=utf-8
from __future__ import print_function, unicode_literals

import re
import sys
import getopt
import requests
from collections import namedtuple
from termcolor import colored

reload(sys)
sys.setdefaultencoding('utf8')

KEY = '2010677391'
KEY_FROM = 'terminalYouDao'
TYPE = 'data'
DOC_TYPE = 'json'
API_VERSION = '1.1'
URL = 'http://fanyi.youdao.com/openapi.do'

TAG = namedtuple('TAG', 'value color')
TAG_DICT = {
    'translation': TAG('[%s]', 'green'),
    'fy': TAG('%s', 'green'),
    'orig': TAG('ex. %s', 'blue'),
    'trans': TAG('    %s', 'cyan'),
    'pos': TAG('%s'.ljust(12), 'green'),
    'acceptation': TAG('%s', 'yellow'),
    'errorCode': TAG('%s', 'red')
}

errorMsg = {
    0: '查询成功',
    20: '要翻译的文本过长',
    30: '无法进行有效的翻译',
    40: '不支持的语言类型',
    50: '无效的key',
    60: '无词典结果，仅在获取词典结果生效'
}


def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], ["help"])
    except getopt.GetoptError as e:
        pass

    # zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    # print(args)
    #
    # match = zhPattern.search(args)
    # # print(args)
    # # print(" ".join(args))
    # # match = re.findall(r'[\w.]+', " ".join(args).lower())
    # print(match)
    # if not match:
    #     print(111)
    #     match = re.findall(r'[\w.]+', " ".join(args).lower())
    # print(222)
    # 获得系统默认编码格式
    str = " ".join(args)
    sysCharType = sys.getfilesystemencoding()
    str2 = str.decode(sysCharType).encode('utf-8')
    check = str2.isalpha()
    if check:
        match = re.findall(r'[\w.]+', str.lower())
        words = "_".join(match)
    else:
        words = str.decode('utf8')
    print(words)

    if len(words) == 0:
        words = 'hello world'

    print(words)


main()
# if __name__ == '__main__':
#     main()
