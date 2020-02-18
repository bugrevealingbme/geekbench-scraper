import requests
from bs4 import BeautifulSoup
import csv
import mysql.connector
import urllib.request
import sys
import re

cihaz= 1
bug=0
while (bug != 15):
        url = "https://browser.geekbench.com/android_devices/"+str(cihaz)+""
        headers = {'User-Agent': 'Mozilla/5.0'}
        url_oku = requests.get(url, headers=headers)
        html_content = url_oku.text               
        soup = BeautifulSoup(html_content, 'lxml')
        cihaz+=1
		
        cihazyazilacak = soup.find("title").text
        if ("404" in cihazyazilacak.strip()):
            bug+=1
            continue
        else:
          bug=0
		  
        score = soup.findAll('div' , { 'class' : 'score'       })
        desc  = soup.findAll('div' , { 'class' : 'description' })
        name  = soup.findAll('td'  , { 'class' : 'name'        })
        value = soup.findAll('td'  , { 'class' : 'value'       })

        try:
            modelname          = value[0].text
            eklemodel = (modelname.replace("'","").replace(":","").strip())
            modelname = eklemodel
            newmodelname = re.sub(r'.*?.\(', '', modelname)
            if(newmodelname == modelname):
              outmodelname = modelname.replace(" ","")
            else:
              newmodelname = newmodelname.replace(")","")
              try:
                if (int(newmodelname) >= 2010):
                  outmodelname = modelname.replace("(","").replace(")","").replace(" ","")  
                else:
                  outmodelname = modelname
                  outmodelname = outmodelname.replace(" ","")	   
              except:
                 outmodelname = modelname
                 outmodelname = outmodelname.replace(" ","")			

            if(desc[2].text == 'Metal Score'):
                singlecorescore   = score[0].text
                multicorescore    = score[1].text
                batteryscore      = score[3].text
            elif(desc[2].text == 'OpenCL Score'):
                singlecorescore    = score[0].text
                multicorescore     = score[1].text
                batteryscore       = score[4].text
            else:
                pass


            cnx = mysql.connector.connect(host='localhost',user='root',password='',database='phonedb')
            cursor = cnx.cursor()
            # sql = ('INSERT INTO geekbench'
                # '(singlecorescore,multicorescore,batteryscore,modelname)'
                # 'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')

            # rows = ([singlecorescore,multicorescore,metalscore,batteryscore,modelname])
            cursor.execute("UPDATE `tidphones` SET `singlecorescore` = '" + singlecorescore +"', `multicorescore` = '" +multicorescore +"', `batteryscore` = '" +batteryscore+"' Where Outmodel = '"+ outmodelname.strip() +"'")
			
            # cursor.execute(sql, rows)
            cnx.commit()
            cursor.close()
        
            print("Eklendi: "+modelname)
        except:	
            print("Hata")		
            pass
			
cihaz= 1
bug=0
while (bug != 15):
        url = "https://browser.geekbench.com/ios_devices/"+str(cihaz)+""
        headers = {'User-Agent': 'Mozilla/5.0'}
        url_oku = requests.get(url, headers=headers)
        html_content = url_oku.text               
        soup = BeautifulSoup(html_content, 'lxml')
        cihaz+=1
		
        cihazyazilacak = soup.find("title").text
        if ("404" in cihazyazilacak.strip()):
            bug+=1
            continue
        else:
          bug=0
		  
        score = soup.findAll('div' , { 'class' : 'score'       })
        desc  = soup.findAll('div' , { 'class' : 'description' })
        name  = soup.findAll('td'  , { 'class' : 'name'        })
        value = soup.findAll('td'  , { 'class' : 'value'       })

        try:
            modelname          = "Apple "+value[0].text
            eklemodel = (modelname.replace("'","").replace(":","").strip())
            modelname = eklemodel
            newmodelname = re.sub(r'.*?.\(', '', modelname)
            if(newmodelname == modelname):
              outmodelname = modelname.replace(" ","")
            else:
              newmodelname = newmodelname.replace(")","")
              try:
                if (int(newmodelname) >= 2010):
                  outmodelname = modelname.replace("(","").replace(")","").replace(" ","")  
                else:
                  outmodelname = modelname
                  outmodelname = outmodelname.replace(" ","")	   
              except:
                 outmodelname = modelname
                 outmodelname = outmodelname.replace(" ","")			

            if(desc[2].text == 'Metal Score'):
                singlecorescore   = score[0].text
                multicorescore    = score[1].text
                batteryscore      = score[3].text
            elif(desc[2].text == 'OpenCL Score'):
                singlecorescore    = score[0].text
                multicorescore     = score[1].text
                batteryscore       = score[4].text
            else:
                pass


            cnx = mysql.connector.connect(host='localhost',user='root',password='',database='phonedb')
            cursor = cnx.cursor()
            # sql = ('INSERT INTO geekbench'
                # '(singlecorescore,multicorescore,batteryscore,modelname)'
                # 'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')

            # rows = ([singlecorescore,multicorescore,metalscore,batteryscore,modelname])
            cursor.execute("UPDATE `tidphones` SET `singlecorescore` = '" + singlecorescore +"', `multicorescore` = '" +multicorescore +"', `batteryscore` = '" +batteryscore+"' Where Outmodel = '"+ outmodelname.strip() +"'")
			
            # cursor.execute(sql, rows)
            cnx.commit()
            cursor.close()
        
            print("Eklendi: "+modelname)
        except Exception as e:
            print("Hata"+e)		
            pass
			
print("Bitti.")