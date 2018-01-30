# encoding: utf-8
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
time1 = time.time()
import requests
import  json

##############抓取url##############
url='http://shuju.wdzj.com/plat-data-custom.html/'

####设置请求头############
myheader={
    "Host": "shuju.wdzj.com",
    "Connection": "keep-alive",
    "Content-Length": "37",
    "Origin": "http://shuju.wdzj.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
    "X-Tingyun-Id": "dxHJmjQTO5o;r=205428918",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "http://shuju.wdzj.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8"
}


#######设置表单####################
form={
    "type":"0",
    "shujuDate":"2017-08-012017-08-31"
}

#############向服务器发送post请求##################
html=requests.post(url,data=form,headers=myheader).content
html2=json.loads(html)


#######################定义存储数据结构:列表################
amount=[]
platName=[]
newbackground=[]
incomeRate =[]
loanPeriod=[]
netInflowOfThirty=[]
stayStillOfTotal=[]
fullloanTime=[]
regCapital=[]
timeOperation =[]
totalLoanNum =[]
bidderNum=[]
avgBidMoney=[]
top10DueInProportion=[]
borrowerNum =[]
avgBorrowMoney=[]
top10StayStillProportion=[]
developZhishu =[]



##############循环解析json#####################
for each in html2:
    platName.append(each['platName'])
    amount.append(each['amount'])
    incomeRate.append(each['incomeRate'])
    loanPeriod.append(each['loanPeriod'])
    netInflowOfThirty.append(each['netInflowOfThirty'])
    stayStillOfTotal.append(each['stayStillOfTotal'])
    fullloanTime.append(each['fullloanTime'])
    regCapital.append(each['regCapital'])
    timeOperation.append(each['timeOperation'])
    totalLoanNum.append(each['totalLoanNum'])
    bidderNum.append(each['bidderNum'])
    avgBidMoney.append(each['avgBidMoney'])
    top10DueInProportion.append(each['top10DueInProportion'])
    borrowerNum.append(each['borrowerNum'])
    avgBorrowMoney.append(each['avgBorrowMoney'])
    top10StayStillProportion.append(each['top10StayStillProportion'])
    try:
        newbackground.append(each['newbackground'])
    except:
        newbackground.append("未知")
    try:
        developZhishu.append(each['developZhishu'])
    except:
        developZhishu.append("0")

##########打印长度
print len(newbackground),len(developZhishu)


######################################################写入excel设置问题#########################################
import xlsxwriter
workbook = xlsxwriter.Workbook("c:/pic/data/wdzj_spider.xlsx", options={'strings_to_urls': False})

format=workbook.add_format()
format.set_border(1)
format_title=workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('center')
format_title.set_bold()
format_ave=workbook.add_format()
format_ave.set_border(1)
format_ave.set_num_format('0.00')

data_format=workbook.add_format()
data_format.set_num_format('yyyy-mm-dd HH:MM:SS')
data_format.set_border(1)


##################################################写入excel数据##############################################
worksheet5 = workbook.add_worksheet('网贷数据')
title5 = [ u"排名",u"平台名称", u"成交量(万元)", u"平均预期收益率(%)", u"平均借款期限(月)", u"资金净流入(万元)", u"待还余额(万元)",
           u"满标用时(分)", u"注册资本(万元)", u"运营时间(月)", u"借款标数(个)", u"投资人数(人)", u"人均投资金额(万元)",
           u"前十大土豪待收金额占比(%)", u"借款人数(人)", u"人均借款金额(万元)", u"前十大借款人待还金额占比(%)",u"平台背景",u"发展指数排名"
          ]


################开始写入############################
worksheet5.write_row('A1',title5,format_title)
worksheet5.write_column('A2', range(1,len(platName)+1),format)
worksheet5.write_column('B2:',platName,format)
worksheet5.write_column('C2:',amount,format)
worksheet5.write_column('D2', incomeRate,format)
worksheet5.write_column('E2', loanPeriod,format)
worksheet5.write_column('F2', netInflowOfThirty,format)
worksheet5.write_column('G2', stayStillOfTotal,format)
worksheet5.write_column('H2', fullloanTime,format)
worksheet5.write_column('I2', regCapital,format)
worksheet5.write_column('J2', timeOperation,format)
worksheet5.write_column('K2', totalLoanNum,format)
worksheet5.write_column('L2', bidderNum,format)
worksheet5.write_column('M2', avgBidMoney,format)
worksheet5.write_column('N2', top10DueInProportion,format)
worksheet5.write_column('O2', borrowerNum,format)
worksheet5.write_column('P2', avgBorrowMoney,format)
worksheet5.write_column('Q2', top10StayStillProportion,format)
worksheet5.write_column('R2', newbackground,format)
worksheet5.write_column('S2', developZhishu,format)


#########关闭工作簿##############
workbook.close()
time2 = time.time()
print u'ok,爬虫结束!'
print u'总共耗时：' + str(time2 - time1) + 's'