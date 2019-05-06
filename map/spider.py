import requests
import re
def pachong():
    url=r"http://www.stats.gov.cn/tjsj/pcsj/rkpc/6rp/html/A0101a.htm"
    headers = {"User-Agent": "Mozilla/5.0"}
    req = requests.get(url,headers=headers)
    req.encoding="gbk"
    html = req.text
    #各地人口总数
    src = '''<tr height=24 style='mso-height-source:userset;height:18.0pt'>.*?<td class=.*?x:num.*?>(.*?)</td>'''
    #地名
    name = u'''<tr height=24 style='mso-height-source:userset;height:18.0pt'>.*?([\u4e00-\u9fa5]+).*?([\u4e00-\u9fa5]+).*?<td class=.*?x:num.*?>.*?</td>'''
    src = re.compile(src,re.S)
    name = re.compile(name,re.S)
    value = re.findall(src,html)
    key = re.findall(name,html)
    address=[]
    for i in key:
         address.append(i[0]+i[1])
    address[0]="全国"
    address[5]="内蒙古"
    address[8]="黑龙江"
    result = dict(map(lambda x,y:[x,y],address,value))
    return result
