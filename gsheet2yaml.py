'''
csv table header
Academic Conference Name,Location (Alpha),"Dates
(Grey = past; Green = March; Yellow = April; Blue = May)",Notes,Announcement Link,^

Academic Conference Name
Location (Alpha)
"Dates
(Grey = past; Green = March; Yellow = April; Blue = May)"
Notes
Announcement Link

'''

'''              
         item={}
         item['name']=row['Academic Conference Name']
         item['date']=row["Dates\n(Grey = past; Green = March; Yellow = April; Blue = May)"]
         item['location']=row['Location (Alpha)']
         item['notes']=row['Notes']
         item['link']=row['Announcement Link']
'''

import csv
import yaml
with open('_data/conferences.yml','w') as ymlfile:
  with open('conferences.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         
         #print('-----------------------')
         #print(row)
         item={}
         for k,v in dict(row).items():
             if k is None :
                 del row[k]
             else:
               item[k[:5]]=v
             #print(k)


         keys=['Acade','Annou','Dates','Locat','Notes']
         newitem={}
         for k in keys:
           newitem[k]=item[k].replace('\n','')
         #print(yaml.dump(newitem))

         #item[Location (Alpha)]
         #print('+++++++++++++++++++++++')
         ymlfile.write(yaml.dump([newitem]))
         #print('                        -----------------------')
     
