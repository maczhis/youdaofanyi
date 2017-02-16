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


def send_request(words):
    # Logout
    # GET http://apis.juhe.cn/mobile/get
    try:
        response = requests.get(
            url=URL,
            params={
                "keyfrom": KEY_FROM,
                "key": KEY,
                "type": TYPE,
                "doctype": DOC_TYPE,
                "version": API_VERSION,
                "q": words

            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },

            data={
            },
        )

        result = response.json()
        return result
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def dict2flatlist(d):
    for key, value in d.items():
        if type(d[key]) == dict:
            dict2flatlist(d[key])
        elif type(d[key]) == list:
            for x in d[key]:
                if type(x) == dict:
                    for m, n in x.items():
                        if type(x[m]) == list:
                            s = ''
                            for y in x[m]:
                                s = s + y
                            print(colored(s, 'blue'))
                        else:
                            if m == 'key':
                                m = 'ex'
                            print(colored(m, 'red') + '. ' + colored(n, 'green'))

                else:
                    print(colored(x, 'yellow'))
        else:
            if key == 'key':
                key = 'ex'
            print(colored(key, 'red') + '. ' + colored(value, 'green'))
            # print(colored(value, 'green'))


def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], ["help"])
    except getopt.GetoptError as e:
        pass

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

    if len(words) == 0:
        words = 'hello world'

    response = send_request(words)
    errorCode = response['errorCode']
    response.pop('errorCode')
    response.pop('query')
    sorted(response, reverse=True)
    errorMsgs = errorMsg[errorCode]
    if errorCode == 0:
        errorMsgs = errorMsgs + ':' + words

    print(colored(errorMsgs, 'cyan'))

    dict2flatlist(response)

    if not response:
        return


if __name__ == '__main__':
    main()
