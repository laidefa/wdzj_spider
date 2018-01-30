####清空数据#######
rm(list=ls())
gc()
options(scipen = 200)
#######导入相应包#########
library(XML)
library(RCurl)
library(RJSONIO)

############抓取url##############

url='http://shuju.wdzj.com/plat-data-custom.html'


#########定义抓取日期###########
shujuDate <- "2018-01-232018-01-23"

###发送post请求#
web<-postForm(url,type='0',shujuDate=shujuDate,.opts=curlOptions(url=url,ssl.verifyhost=FALSE,ssl.verifypeer=FALSE))


#####解析json#
p <-fromJSON(web)

#############定义抓取指标

amount <- ""
platName <- ""
newbackground <- ""
incomeRate <- ""
loanPeriod <- ""
netInflowOfThirty <- ""
stayStillOfTotal <- ""
fullloanTime <- ""
regCapital <- ""
timeOperation <- ""
totalLoanNum <- ""
bidderNum <- ""
avgBidMoney <- ""
top10DueInProportion <- ""
borrowerNum <- ""
avgBorrowMoney <- ""
top10StayStillProportion <- ""
developZhishu <- ""


##########循环解析字段##################

for(i in 1:length(p)){
  platName1 <-  p[[i]]$platName
  platName <-c(platName,platName1)
  
  newbackground1 <-  p[[i]]$newbackground
   if(length(newbackground1)>0){
   newbackground <-c(newbackground,newbackground1)
  }else{
   newbackground <-c(newbackground,"未知")
  }
  
  amount1 <- p[[i]]$amount
  amount <-c(amount,amount1)
  
  incomeRate1 <- p[[i]]$incomeRate
  incomeRate <- c(incomeRate,incomeRate1)
  
  loanPeriod1 <- p[[i]]$loanPeriod
  loanPeriod <- c(loanPeriod,loanPeriod1)
  
  netInflowOfThirty1 <- p[[i]]$netInflowOfThirty
  netInflowOfThirty <- c(netInflowOfThirty,netInflowOfThirty1)
  
  stayStillOfTotal1 <- p[[i]]$stayStillOfTotal
  stayStillOfTotal <- c(stayStillOfTotal,stayStillOfTotal1)
  
  fullloanTime1 <- p[[i]]$fullloanTime
  fullloanTime <- c(fullloanTime,fullloanTime1)
  
  regCapital1 <- p[[i]]$regCapital
  regCapital <- c(regCapital,regCapital1)
  
  timeOperation1 <- p[[i]]$timeOperation
  timeOperation <- c(timeOperation,timeOperation1)
  
  totalLoanNum1 <- p[[i]]$totalLoanNum
  totalLoanNum <- c(totalLoanNum,totalLoanNum1)
  
  bidderNum1 <- p[[i]]$bidderNum
  bidderNum <- c(bidderNum,bidderNum1)
  
  
  avgBidMoney1 <- p[[i]]$avgBidMoney
  avgBidMoney <- c(avgBidMoney,avgBidMoney1)
  
  top10DueInProportion1 <- p[[i]]$top10DueInProportion
  top10DueInProportion <- c(top10DueInProportion,top10DueInProportion1)
  
  borrowerNum1 <- p[[i]]$borrowerNum
  borrowerNum <- c(borrowerNum,borrowerNum1)
  
  avgBorrowMoney1 <- p[[i]]$avgBorrowMoney
  avgBorrowMoney <- c(avgBorrowMoney,avgBorrowMoney1)
  
  top10StayStillProportion1 <- p[[i]]$top10StayStillProportion
  top10StayStillProportion <- c(top10StayStillProportion,top10StayStillProportion1)
  
  developZhishu1 <- p[[i]]$developZhishu
   if(length(developZhishu1>0)){
    developZhishu <- c(developZhishu,developZhishu1)
  }else{
    developZhishu <- c(developZhishu,"0")
  }
 
}



###############合并数据##############
data <- data.frame(platName[-1],amount[-1],incomeRate[-1],loanPeriod[-1],netInflowOfThirty[-1],stayStillOfTotal[-1],
                   fullloanTime[-1],regCapital[-1],timeOperation[-1],totalLoanNum[-1],bidderNum[-1],avgBidMoney[-1],
                   top10DueInProportion[-1],borrowerNum[-1],avgBorrowMoney[-1],top10StayStillProportion[-1],newbackground[-1],developZhishu[-1]
                   
                   )



###############重命名列名称########
names(data) <- c("平台名称","成交量(万元)","平均预期收益率(%)","平均借款期限(月)","资金净流入(万元)","待还余额(万元)",
                 
                 "满标用时(分)","注册资本(万元)","运营时间(月)","借款标数(个)","投资人数(人)","人均投资金额(万元)",
                 "前十大土豪待收金额占比(%)","借款人数(人)","人均借款金额(万元)","前十大借款人待还金额占比(%)","平台背景","发展指数排名"
                 
                 )


####写出csv#########
write.csv(data,"C:/pic/data/网贷之家爬虫.csv",row.names = T)
