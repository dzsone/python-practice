#!/user/bin/env python
#coding=utf-8
import requests,json
import datetime
import time
import threading

class url_request():
    times = []
    error = []
    success = []
    def req(self,AppID,url):
        myreq=url_request()
        headers = {'Content-type': 'application/json','Authorization':'t=1523241518498;a=214ea227fb4f;o=317149262790582;ot=1;n=1;p=;m=;s=cb35cd3e6b336bcbac83ba03dae8e9765375bb20;'}
        payload = json.dumps({
                                "timestamp":1523241518498,
                                "oid": "317149262790582",
                                "oidType": 1,
                                "networkMode": "1",
                                "mac": "",
                                "appId": "214ea227fb4f",
                                "sign": "cb35cd3e6b336bcbac83ba03dae8e9765375bb20",
                                "signals":[{"bssid":"c83a35079cd0","rssi":-82},{"bssid":"e4f3f53a7a16","rssi":-74},{"bssid":"c83a351878e8","rssi":-86}]
                             })
        r = requests.post("http://47.98.31.212/v2/test/scene/api",headers=headers,data=payload)
        #data = r.json()
        ResponseTime=float(r.elapsed.microseconds)/1000 #获取响应时间，单位ms
        myreq.times.append(ResponseTime) #将响应时间写入数组
        if r.status_code !=200 :
            myreq.error.append("0")

        if r.status_code == 0:
            myreq.success.append("0")
if __name__=='__main__':
    myreq=url_request()
    threads = []
    starttime = datetime.datetime.now()
    print("request start time %s" %starttime)

    nub = 6 #设置并发线程数
    ThinkTime = 0.5 #设置思考时间
    for i in range(1, nub+1):
        t = threading.Thread(target=myreq.req, args=('12','http://m.ctrip.com/webapp/cpage/#mypoints'))
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        #print "thread %s" %t #打印线程
        t.setDaemon(True)
        t.start()
    t.join()

    endtime = datetime.datetime.now()
    print("request end time %s" %endtime)
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times))/float(len(myreq.times))) #计算数组的平均值，保留3位小数
    print ("Average Response Time %s ms" %AverageTime) #打印平均响应时间
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second) #计算总的思考时间+请求时间
    #print ("Concurrent processing %s" %nub) #打印并发数
    #print ("use total time %s s" %(totaltime-float(nub*ThinkTime))) #打印总共消耗的时间
    print("success request %s" % myreq.success.count("0")) #打印成功请求数
    print ("fail request %s" %myreq.error.count("0")) #打印错误请求数