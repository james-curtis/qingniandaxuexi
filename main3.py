# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

host = 'http://dxx.hngqt.org.cn'
studyHnProjectAdd = host + '/historystudy/studyHnProjectAdd'
studyHistoryAdd = host + '/historystudy/studyHistoryAdd'
studyAdd = host + '/study/studyAdd'
gifts = host + '/userLottery/doLottery'
#print(gift)
#exit()

def getnum():
    try:
        start = input('请输入起始ID，默认0\n')
        end = input('请输入结束ID，默认400\n')
    except:
        print('输入错误')
        exit()
    if start == '':
        start = 0
    if end == '':
        end = 400
    start = int(start)
    end = int(end)
    return [start,end]
    
def article():
    
    print('正在批量阅读青年湖南说...')
    num = getnum()
    for i in range(num[0], num[1]):
        r = requests.post(studyHnProjectAdd, headers=head, cookies={'sessionid': sessionid}, data={'projectId': str(i)})
        print('正在阅读ID为{}的文章：'.format(i) + r.text)
        
def study():
    print('正在批量初学青年大学习...')
    num = getnum()
    for i in range(num[0], num[1]):
        r = requests.post(studyAdd, headers=head, cookies={'sessionid': sessionid}, data={'projectId': str(i)})
        print('正在初学ID为{}的青年大学习：'.format(i) + r.text)
        
def study2():
    
    print('正在批量温习青年大学习...')
    num = getnum()
    for i in range(num[0], num[1]):
        r = requests.post(studyHistoryAdd, headers=head, cookies={'sessionid': sessionid}, data={'projectId': str(i)})
        print('正在温习ID为{}的青年大学习：'.format(i) + r.text)
    
    
def gift():
    print('正在批量抽奖')
    #num = getnum()
    #for i in range(num[0], num[1]):
    flag = True
    while flag:
        r = requests.post(gifts, headers=head, cookies={'sessionid': sessionid})
        #print(r.text)
        r = r.json()
        #print(r)
        try:
            print('正在抽奖，剩余积分{}，获得奖品：{}'.format(r['data']['awardDto']['remainTimes'],r['data']['awardDto']['awardName']))
            if int(r['data']['awardDto']['remainTimes']) < 10:
                print('积分不足自动停止')
                flag = False
        
        except:
            print(r)
            exit()
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sessionid = input('请输入sessionid\n')

    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045425 Mobile Safari/537.36 MMWEBID/6830 MicroMessenger/7.0.20.1781(0x27001439) Process/tools WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64'}

    operat = input('''请输入操作类型(数字)\n
    1.阅读文章\n
    2.学习视频\n
    3.温习视频\n
    4.批量抽奖\n
''')
    
    operat = int(operat)
    
    if operat == 1:
        article()
    elif operat == 2:
        study()
    elif operat == 3:
        study2()
    elif operat == 4:
        gift()
    else:
        print('选择错误，请重新运行')
        
        

