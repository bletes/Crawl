import requests
from bs4 import BeautifulSoup
import xlwt
import json
import time
import re
#请求headers 模拟浏览器访问
#爬取数据，每页数据大于总产品数量，以获取所有产品信息
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'
}
jar={
    'Cookie':'__MYLOG_UID=39808281-9873-4a15-b48c-6128cf646095; __MYLOG_SID=27e0da04-a216-4eca-bd11-5bb8ac7c66ab; gr_user_id=857a3a41-b896-431e-8a3b-7d01c464a691; b191d4a76e67e693_gr_session_id_d3673ae5-1629-4c9b-9bfa-57a0b354744f=false; b191d4a76e67e693_gr_session_id=d3673ae5-1629-4c9b-9bfa-57a0b354744f; aliyungf_tc=56a36c379ee1b5a8834cecb82a5717bc1fd107eed7a1bd6b0ec88d105d3ed103; JSESSIONID=D64EA3E68D70DB9FC296037C50596A6B'
}
num=1
params = {"subUserId":"10011740923","commodityName":"","commodityTypeCode":"all","pageSize":'250',"currentPage":'{}'.format(num),"labelId":'null'}
    
response = requests.get('http://www.ecloudexam.com/jumpFindIndex', headers=headers,cookies=jar,params=params)
response.encoding='utf-8'
bs= BeautifulSoup(response.text)#, 'lxml')
bb=re.findall('[\u4e00-\u9fa5].*[\u4e00-\u9fa5]',response.text)
bb.reverse()
k=0#k trigger
for i in bb:
    if k==1 :
        #print(i,end=',')
        k+=1
        continue
    if k==2:
        print(i)
        k+=1
        continue
    if k==3:
        print(i)
        k+=1
        continue
    if k==4:
        #print(i)
        k+=1
        continue
    else:
        k=0
        if '网上报名' in i:
            print('')
            k+=1
            
##        if '宝山区' in i or '黄浦区' in i or '杨浦区' in i or '虹口区' in i:
##            print(i,end=',')
##            k+=1
        
oo=input('kkkkkk')
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
#dd=response.json()
#分析数据位置，准备存放入excel
new_list=dd['content']['list']
i = 0
for list in new_list:
    if i==0:
        j = 0
        for data in list.keys():
            sheet1.write(i, j, data)
            j += 1
        j = 0
        for data in list.values():
            sheet1.write(i+1, j, str(data))
            j += 1
        i += 1
    else:
        j = 0
        for data in list.values():
            sheet1.write(i+1, j, str(data))
            j += 1
        i += 1
# 文件保存
file_name='baoyun18-{}.csv'.format(time.strftime('%Y-%m-%d-%H-%M-%S'))
book.save('.\\'+file_name)

#读取前后两次数据，判断新增了哪些产品，删除了哪些产品
import pandas as pd
file='C:\\Users\\HP\\Desktop\\'+file_name#现在的文件
fn=pd.read_excel(file)#file now
file='C:\\Users\\HP\\Desktop\\baoyun18-2022-08-25-19-59-34.csv'#对照过去的文件
fp=pd.read_excel(file)#file past
#遍历并删除空白表格
fnl=[]
for i in fn['commissionUrl']:
    if i=='None':
        pass
    else:
        fnl.append(i)
for i in fn['commodityName']:
    if str(i)=='nan':
        pass
    else:
        fnl.append(i)
fpl=[]
for i in fp['commissionUrl']:
    if i=='None':
        pass
    else:
        fpl.append(i)
for i in fp['commodityName']:
    if str(i)=='nan':
        pass
    else:
        fpl.append(i)
for i in fnl:
    if i in fpl:
        pass     
    else:
        print('增加了',i)
for i in fpl:
    if i in fnl:
        pass      
    else:
        print('删除了',i)
#判断完成
