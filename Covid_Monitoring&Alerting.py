from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import requests
import urllib.request
import urllib
import sys
import os
import json
from datetime import datetime
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config 


################################ CONFIG #####################################
MY_ADDRESS = 'USER@gmail.com'                #put a gmail account address 
PASSWORD = 'PASSWORD'                        #Password of gmail account 

names  = ["user1","user2"]                   #Users to be alerted name list 
emails = ["user1@gmail.com","user2@live.fr"] #Users to be alerted email list 

alert_counties=["france", "tunisia"]         #List of countries to monitor
update_interval=600                         #Refrehsing interval (in seconds)
##############################################################################

now = datetime.now() 
template=Template("""  
Dear ${Name}, 
        =============CoronaVirus Update [${Country}]=============
        Date: ${date}
        Total Cases: ${data1}
        New Cases : ${data2}
        Total Deaths: ${data3}
        New Deaths: ${data4}
        Active Cases: ${data6}
        Total Recovered: ${data7}
        Critical Cases: ${data5}""")


def sendEmail(county,data):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
  
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       
        message = template.substitute(Name=name,Country=county,date=now.strftime("%m/%d/%Y, %H:%M:%S"),data1=str(int(data[0])),data2=data[1],data3=data[2],data4=data[3],data5=data[6],data6=data[4],data7=data[5])
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="CoronaVirus Update [{}]".format(county)
        msg.attach(MIMEText(message, 'plain'))        
        s.send_message(msg)
        del msg        
        print("[+] Email sent.")
    s.quit()
    return 

def update(county,data):
    with open("./logs"+counttime.sleepy+".txt",'w') as f :
        f.write(" ".join(data))

def read(county): 
    with open("./logs"+county+".txt",'r') as f :
        x=f.readline()
    if(x==""): 
        data=['0','0','0','0','0','0','0']
        update(county,data)
        return data 
    else: 
        return x.split()
        
def init_driver():
    print("[!] Loading Page.. ")
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu') 
    driver = webdriver.Chrome(chrome_options=options)
    print("[+] Driver loaded .. ")
    url_to_scrape="https://www.worldometers.info/coronavirus/"
    driver.get(url_to_scrape)
    time.sleep(60)
    return driver

def check_update(driver):
    table=driver.find_elements_by_xpath('//*[@id="main_table_countries"]/tbody')
    for row in table[0].find_elements_by_xpath('./tr'):
        county=row.find_element_by_xpath('./td').text
        if county.lower() in alert_counties : 
            data=[]
            for col in row.find_elements_by_xpath('./td'):
                if col.text=="":
                    data.append('0')
                else : 
                    data.append(col.text)
            if data[1:]!=read(county): 
                update(county,data[1:])
                sendEmail(county,data[1:])


driver=init_driver()
while(1):
    print("[?]",now.strftime("%m/%d/%Y, %H:%M:%S")) 
    check_update(driver)
    print("[!] Reloading .. ")
    driver.refresh()
    time.sleep(update_interval)