#get all maicai.api
import requests
from bs4 import BeautifulSoup
import xlwt
import json
import time
import re
#请求headers 模拟浏览器访问
#爬取数据，每页数据大于总产品数量，以获取所有产品信息
def one():
##headers = {
##    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
##    'Cookie':'DDXQSESSID=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d'    
##}
##
##headers = {
##    'Host': 'maicai.api.ddxq.mobi',
##    'Connection': 'keep-alive',
##    'ddmc-city-number': '0101',
##    'ddmc-build-version': '2.96.0',
##    'ddmc-os-version': 'Windows 10 x64',
##    'ddmc-channel': 'applet',
##    'xweb_xhr': '1',
##    'ddmc-latitude': '31.40404',
##    'Cookie': 'DDXQSESSID=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d',
##    'ddmc-api-version': '9.61.0',
##    'ddmc-longitude': '121.494746',
##    'ddmc-SDKVersion': '2.21.3',
##    'ddmc-time': '1664000239',
##    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
##    'ddmc-device-id': 'osP8I0Syo_AG_0sB3NhCxXl2xBas',
##    'ddmc-uid': '6251572436f194000124fe6c',
##    'Content-Type': 'application/x-www-form-urlencoded',
##    'ddmc-app-client-id': '4',
##    'ddmc-station-id': '5b8d232ec0a1ea3a278b8b7e',
##    'Accept': '*/*',
##    'Sec-Fetch-Site': 'cross-site',
##    'Sec-Fetch-Mode': 'cors',
##    'Sec-Fetch-Dest': 'empty',
##    'Referer': 'https://servicewechat.com/wx1e113254eda17715/468/page-frame.html',
##    'Accept-Language': 'en-us,en',
##    'Accept-Encoding': 'gzip, deflate',
##    'Date': 'Sat, 24 Sep 2022 06:17:20 GMT',
##    'Content-Type': 'application/json;charset=UTF-8',
##    'Connection': 'keep-alive',
##    'Server': 'Tengine',
##    'Vary': 'Accept-Encoding',
##    'X-Traceid': 'amesh-service^^50e66b3a51700356cc676f1de2f769aa|1664000240044',
##    'X-Proxy': 'lb27gw.psht3.mc.ops',
##    'Content-Encoding': 'gzip',
##    'Content-Length': '35579'
##}
##headers = {
##    'ddmc-city-number': '0101',
##    'ddmc-build-version': '2.96.0',
##    'ddmc-channel': 'applet',
##    'xweb_xhr': '1',
##    'ddmc-latitude': '31.40404',
##    'Cookie': 'DDXQSESSID=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d',
##    'ddmc-api-version': '9.61.0',
##    'ddmc-longitude': '121.494746',
##    'ddmc-SDKVersion': '2.21.3',
##    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
##    'ddmc-device-id': 'osP8I0Syo_AG_0sB3NhCxXl2xBas',
##    'ddmc-uid': '6251572436f194000124fe6c',
##    'Content-Type': 'application/x-www-form-urlencoded',
##    'ddmc-app-client-id': '4',
##    'ddmc-station-id': '5b8d232ec0a1ea3a278b8b7e',
##    'X-Traceid': 'amesh-service^^50e66b3a51700356cc676f1de2f769aa|1664000240044',
##    'X-Proxy': 'lb27gw.psht3.mc.ops',
##}
    headers = {
        'ddmc-city-number': '0101',
        'ddmc-build-version': '3.5.1',
        'ddmc-channel': 'applet',
        
        
        'ddmc-latitude': '31.184838',
        'Cookie': 'DDXQSESSID=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d',
        
        'ddmc-longitude': '121.494746',
        
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6500',
        'ddmc-device-id': 'osP8I0Syo_AG_0sB3NhCxXl2xBas',
        'ddmc-uid': '6251572436f194000124fe6c',
        'Content-Type': 'application/x-www-form-urlencoded',
        'ddmc-app-client-id': '4',
        'ddmc-station-id': '53eb382d7f8b9ac3b18b4573'
    }




    jar={
        'Cookie':'DDXQSESSID=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d'
    }
    num=1

    params = {'djencrypt':'Fpf3DH4RtGxjmylKZVIpHW4CkNAd6ZE4Kseac%2FJmT2QTWgtm8H3fbRYNUNaPqhqVkJpYWQjul%2FgrmW1cDlktx1XFEZTgO4yNgdG7aAcsM3jS66an04npNuNbnffUP8ex3AgHG1hdbqBKPMVhM7K6tQCcnNZ5kxdSUsQWNMjlKyDpOf1ecnpdIiglMNYAsLwMLPrLhfV0FMFB2vcxr3R%2B%2Bq%2FZ1ol3N5ZbPc98HgmXmgnFRa8OWFiBADnkc%2B0rvHKAlWUgzSt98d9mhFa7XpzhtOWG2jxFWsD0H0Ia0N3JCPOYV9CvfPhHvKW4q1Okx59hkSe73Rs2RZfFlFpNBUYbyZyXpAenBBWBejntoJxF8z0Z%2F95Ezl9kShrPRPYE2wYu38CUSPqw41CmmMgTqajkQWBRl4tMSqU%2BBC5UtOE3gGIl2ODtbfYwT52ex3HXpg%2FM4reAunbxhcjxK6br%2FM2eyG5%2F825kYpmUh4rpTZondmOCn%2BjpehVyvVdPN5caenvGtGFYnsy6HPMlZffCQjZ5dEfwX3ALdwZKN8KvUQ11IYbGjW8%2FV36O2Bu7FyOwLIzxYK0kv1lpb4HxftVb%2FooAs8J7QtSYzo%2FOA76bfETcRkiw6ryUaOFvhq%2B0k2rbY%2BsW9pmbvUPeR%2BUtC6bLgwPXqFAoO84%2FnbnIUYTnBJcHxR3jb97NIhpOEWIKinYAjg5vzrYWK2BoKa49B%2F%2F%2BtklsPO4blyYXNX41a%2BX%2FdQ4N4P%2F5GJEuFKV9Tc%2FB9VlDt9M9%2BYHvYV3dqy9iFvH3P3GVIPUtsy9FvIbiE%2FAD3xDQ%2BXegWPAgV5IJ38KchERps8c1ebMrnf%2BYEPglET6k%2FxvhDEAVJw1vlpmT8XwQocVYTvmvYyA3w%2FBDVhf7ebFsnsz%2Fw%2F%2Fpo%2B6plvQIIq3ccC4Q%2BNrrFNM3cwo8nE5zZwJoLOkOf8yBveAyy8YLf9cYgYeU94P%2BJaN4u5G4SlWwwXjcPvVOh2vfATlJOJy6T4nsFrgPzUfvEY8Ang4Ab05WuCsuOWoMtQyTBg864WpqZz6d1UFbk0ycB%2BrlMTGfZjdNw0kraW1sYjKxsDW8bJZgYtVhUQd6dC7zO0ZYRz1InnImdeuP%2BC3bf%2FcLRUF2k4cyBNCgExRyK8pSgmyW%2BW6V6Rab84m6c9YSOUMogqQRCRLUwbBPNhWu%2BEIEQc8vljDwR6lOfeSwKhYXKRnscIlwD%2Brq8oVU%2FaZvNkXF1n5EZHuOa6q%2FL9mib4BwyHhw2uKkfx5kuRK%2BmZfbut%2BtTRH4WXSBqjlbbDacKSuDKj%2FpCXK4G2xJSf635453qOfG8TFYwkdmtGd5eXuKM3u7q3HZnAK5%2FaBYF3jymbFv8q5DoJNhp3DZfTMwXwx6LAyhu8%2FimQh3JfvQQDpE%2Fou8nyS3hKIlpQg50AO%2FTlrrsDeqT2yAEI2t1qzI894mwquWMVGs5VOUW4NYIJth5Wn5AgKydmRJal4%2FqY6UU3MmTyWx7nsYJGhd9FZ4d2cYVsSqedkSJxXW54OYMcRcwAYaoocwhDeyE013NqAIIhyy3shX0VJTFd5urvKnlCYYlYuRI3PTdPqvdKHjS19kYw6c8xQGPvvo%2FFb0qGHYLmk%2Fx1Gzp1OaxjK9%2F3Un6vduYi2Pu%2B%2Fj86Ipny4DnfGqMu5nNH8CKQVtvX8Vye1yOGXH8KXNF9iSHiwUybok%2BkqQJ%2B2Jyed14VNvS%2FmPnhTuKCk1ioSZDULRGKs5MRzvJ5bfyJYqCMqXGiXGZa1VwRWo3u7EBjrevAhnlmzYRNKwWVji180WLpQoZwS4xS3bbAm7h43MqpoTS6orBPPyaGwoR7RIfmpPQhvZ5Ce4igrvOwbgvRG6zndvrDEcUpjwI6z65cneW1YCs9rHHCwRlD6hYwoRCQrwUwQKDlbvt5AdHV4t%2FaaT7Ni5'}
    #,cookies=jar
    response = requests.get('https://maicai.api.ddxq.mobi/homeApi/categoriesNewDetail?uid=6251572436f194000124fe6c&longitude=121.494746&latitude=31.40404&station_id=5b8d232ec0a1ea3a278b8b7e&city_number=0101&api_version=9.61.0&app_version=2.96.0&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d&openid=osP8I0Syo_AG_0sB3NhCxXl2xBas&h5_source=&time={}&device_token=WHJMrwNw1k%2FGyJukJEWNgJFhNyKPN65cX52hhVGcvki4aue0FXYGQLgMR9aWMmca3Pt0R7VSCaPrWWBLzntOVjDJ29nlwFGU%2FdCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&category_id=5fe6dadb80153b2faa7b75a0&version_control=new&nars=fbeb3d49ba016827a481665a4663e2cf&sesi=%7B%22sesiT%22%3A%22nVcTfey3fb1af72db63accb5d1a26e9dbd1d031%22%2C%22sdkV%22%3A%222.0.0%22%7D'.format(round(time.time())),headers=headers,verify=False)
    response = requests.get('https://maicai.api.ddxq.mobi/homeApi/categoriesNewDetail?uid=6251572436f194000124fe6c&longitude=121.630323&latitude=31.184838&station_id=5b779e2e01a6eaaf048b9eba&city_number=0101&api_version=9.63.0&app_version=2.98.0&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d&openid=osP8I0Syo_AG_0sB3NhCxXl2xBas&h5_source=&time={}&device_token=WHJMrwNw1k%2FGyJukJEWNgJFhNyKPN65cX52hhVGcvki4aue0FXYGQLgMR9aWMmca3Pt0R7VSCaPrWWBLzntOVjDJ29nlwFGU%2FdCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&category_id=6352612cd5811d001e7acca7&version_control=new&nars=2c9a710c8ab86300572e5d0c8a81b2ec&sesi=%7B%22sesiT%22%3A%22IiDtCSm5c85eaa54ee1c406a365b5ded37aa93f%22%2C%22sdkV%22%3A%222.0.0%22%7D'.format(round(time.time())),headers=headers,verify=False)
    response = requests.get('https://maicai.api.ddxq.mobi/homeApi/categoriesNewDetail?uid=6251572436f194000124fe6c&longitude=121.630323&latitude=31.184838&station_id=53eb382d7f8b9ac3b18b4573&city_number=0101&api_version=10.3.0&app_version=3.3.0&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d&openid=osP8I0Syo_AG_0sB3NhCxXl2xBas&h5_source=&time={}&device_token=WHJMrwNw1k%2FGyJukJEWNgJFhNyKPN65cX52hhVGcvki4aue0FXYGQLgMR9aWMmca3Pt0R7VSCaPrWWBLzntOVjDJ29nlwFGU%2FdCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&category_id=6352612cd5811d001e7acca7&version_control=new&nars=91819646f6647e11f0cffa7d356576f0&sesi=%7B%22sesiT%22%3A%22KyXplEt9740483858a392ed0794bea4b789285c%22%2C%22sdkV%22%3A%222.0.0%22%7D'.format(round(time.time())),headers=headers,verify=False)
    response = requests.get('https://maicai.api.ddxq.mobi/homeApi/categoriesNewDetail?uid=6251572436f194000124fe6c&longitude=121.630323&latitude=31.184838&station_id=53eb382d7f8b9ac3b18b4573&city_number=0101&api_version=10.4.0&app_version=3.4.1&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d&openid=osP8I0Syo_AG_0sB3NhCxXl2xBas&h5_source=&time={}&device_token=WHJMrwNw1k%2FGyJukJEWNgJFhNyKPN65cX52hhVGcvki4aue0FXYGQLgMR9aWMmca3Pt0R7VSCaPrWWBLzntOVjDJ29nlwFGU%2FdCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&category_id=6352612cd5811d001e7acca7&version_control=new&nars=bfaaea2bc684dc80102801bc93588bd2&sesi=%7B%22sesiT%22%3A%22smgJ1lP873bd6086863651b168234166711ee19%22%2C%22sdkV%22%3A%222.0.0%22%7D'.format(round(time.time())),headers=headers,verify=False)
    response = requests.get('https://maicai.api.ddxq.mobi/homeApi/categoriesNewDetail?uid=6251572436f194000124fe6c&longitude=121.630323&latitude=31.184838&station_id=53eb382d7f8b9ac3b18b4573&city_number=0101&api_version=10.5.0&app_version=3.5.1&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d&openid=osP8I0Syo_AG_0sB3NhCxXl2xBas&h5_source=&time={}&device_token=WHJMrwNw1k%2FGyJukJEWNgJFhNyKPN65cX52hhVGcvki4aue0FXYGQLgMR9aWMmca3Pt0R7VSCaPrWWBLzntOVjDJ29nlwFGU%2FdCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&category_id=6352612cd5811d001e7acca7&version_control=new&nars=bfaaea2bc684dc80102801bc93588bd2&sesi=%7B%22sesiT%22%3A%22smgJ1lP873bd6086863651b168234166711ee19%22%2C%22sdkV%22%3A%222.0.0%22%7D'.format(round(time.time())),headers=headers,verify=False)
    response = requests.get('https://maicai.api.ddxq.mobi/homeApi/categoriesNewDetail?uid=6251572436f194000124fe6c&longitude=121.630323&latitude=31.184838&station_id=53eb382d7f8b9ac3b18b4573&city_number=0101&api_version=10.5.0&app_version=3.5.1&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d&openid=osP8I0Syo_AG_0sB3NhCxXl2xBas&h5_source=&time={}&device_token=WHJMrwNw1k%2FGyJukJEWNgJFhNyKPN65cX52hhVGcvki4aue0FXYGQLgMR9aWMmca3Pt0R7VSCaPrWWBLzntOVjDJ29nlwFGU%2FdCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&category_id=6352612cd5811d001e7acca7&version_control=new&nars=bfaaea2bc684dc80102801bc93588bd2&sesi=%7B%22sesiT%22%3A%22smgJ1lP873bd6086863651b168234166711ee19%22%2C%22sdkV%22%3A%222.0.0%22%7D'.format(round(time.time())),headers=headers,verify=False)
    response = requests.get('https://maicai.api.ddxq.mobi/homeApi/categoriesNewDetail?uid=6251572436f194000124fe6c&longitude=121.630323&latitude=31.184838&station_id=53eb382d7f8b9ac3b18b4573&city_number=0101&api_version=10.5.0&app_version=3.5.1&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d&openid=osP8I0Syo_AG_0sB3NhCxXl2xBas&h5_source=&time={}&device_token=WHJMrwNw1k%2FGyJukJEWNgJFhNyKPN65cX52hhVGcvki4aue0FXYGQLgMR9aWMmca3Pt0R7VSCaPrWWBLzntOVjDJ29nlwFGU%2FdCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&category_id=6352612cd5811d001e7acca7&version_control=new&nars=4d427e9368ad73cc4ef2558343c004cb&sesi=%7B%22sesiT%22%3A%22tnkwyQLba22b6a9d46b710e0bdcdf6ea87d0d26%22%2C%22sdkV%22%3A%222.0.0%22%7D'.format(round(time.time())),headers=headers,verify=False)
    response = requests.get('https://maicai.api.ddxq.mobi/homeApi/categoriesNewDetail?uid=6251572436f194000124fe6c&longitude=121.630323&latitude=31.184838&station_id=53eb382d7f8b9ac3b18b4573&city_number=0101&api_version=10.7.0&app_version=3.7.1&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=d2u35d265h4hghy92yv124666duu81740vpdk36120u4g6tifgpi833ig4ohw18d&openid=osP8I0Syo_AG_0sB3NhCxXl2xBas&h5_source=&time={}&device_token=WHJMrwNw1k%2FGyJukJEWNgJFhNyKPN65cX52hhVGcvki4aue0FXYGQLgMR9aWMmca3Pt0R7VSCaPrWWBLzntOVjDJ29nlwFGU%2FdCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&category_id=6352612cd5811d001e7acca7&version_control=new&nars=2422343dd2999edc86d709534a6d4f92&sesi=%7B%22sesiT%22%3A%22mKw5EENdd1db2d772284c9f6255e5c855b7923e%22%2C%22sdkV%22%3A%222.0.0%22%7D'.format(round(time.time())),headers=headers,verify=False)
    #response = requests.get('https://imgnew.ddimg.mobi/product/fe1d92da3b0c4e4987f36433d1c8e357.jpg?imageView2/2/w/170/h/170/q/60/ignore-error/1/format/webp',headers=headers,verify=False)
    response.encoding='utf-8'
    r=response.text
    cc=r.replace('\n','').replace(' ','')
    aa=json.loads(cc)
    k=0
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
    #dd=response.json()
    #分析数据位置，准备存放入excel
    new_list=aa['data']['cate'][0]['products']
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
    file_name='全部鸡鸭禽-{}.csv'.format(time.strftime('%Y-%m-%d-%H-%M-%S-%A'))
    book.save('gz-log\\'+file_name)
while True:
    nowtime = time.strftime('%Y-%m-%d %H:%M')
    if (time.mktime(time.localtime())-(1620741480+0))%3600<60:
        try:
            one()
        except:
            pass
        time.sleep(300)
    else:
        time.sleep(5)
