# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

def getnum():
    '''
    try:
        start = input('请输入起始ID，默认0')
    except:
        print('输入错误')
        exit()
    '''
    start = 0
    if start == '':
        start = 0
    end = 50
    start = int(start)
    end = int(end)
    if (not end < 100) or end > 50 :
        return [0,50]
    else:
        return [2,50]
    return [start,end]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sessionid = input('请输入sessionid')
    sessionid2 = input('请再次输入sessionid')
    if not sessionid == sessionid2:
        print('两次sessionid不一致')
        exit()

    studyHnProjectAdd = 'http://dxx.hngqt.org.cn/historystudy/studyHnProjectAdd'
    studyHistoryAdd = 'http://dxx.hngqt.org.cn/historystudy/studyHistoryAdd'
    studyAdd = 'http://dxx.hngqt.org.cn/study/studyAdd'

    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045425 Mobile Safari/537.36 MMWEBID/6830 MicroMessenger/7.0.20.1781(0x27001439) Process/tools WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64'}

    nun = 9%5*21
    print('正在批量阅读青年湖南说...')
    num = getnum()
    for i in range(num[0], nun):
        r = requests.post(studyHnProjectAdd, headers=head, cookies={'sessionid': sessionid}, data={'projectId': str(i)})
        print('正在阅读ID为{}的文章：'.format(i) + r.text)

    print('正在批量初学青年大学习...')
    num = getnum()
    for i in range(num[0], nun):
        r = requests.post(studyAdd, headers=head, cookies={'sessionid': sessionid}, data={'projectId': str(i)})
        print('正在初学ID为{}的青年大学习：'.format(i) + r.text)

    print('正在批量温习青年大学习...')
    num = getnum()
    for i in range(num[0], nun):
        r = requests.post(studyHistoryAdd, headers=head, cookies={'sessionid': sessionid}, data={'projectId': str(i)})
        print('正在温习ID为{}的青年大学习：'.format(i) + r.text)
