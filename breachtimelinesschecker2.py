import json
import time
import pyHIBP
from pyHIBP import pwnedpasswords as pw


yearbreachlist = {}
unclassified = []
yearbreachlist['unclassified'] = []
with open('databreach.csv', 'rU') as f:
    for line in f:
        time.sleep(1.5)
        try:
                username = line.split(':')[0]

                resp = pyHIBP.get_account_breaches(account=username, truncate_response=False)
        except:
                print("erroneous/blank request")
        #print(resp)
        if(resp == False):
            #print("it's a bear")

#			unclassified.append(line)			

#			print(unclassified)
            breachyear = "unclassified"
            yearbreachlist[breachyear].append(line)
            continue
        else:


            #print("\n")
            #print("\n")
            for element in resp:
                #print("\n")
                #print(element)
                #print(element['BreachDate'])				
                breachdate = element['BreachDate']
                breachyear = breachdate[0:4]
                #print(breachyear)
                
                doesbreachyearexist = yearbreachlist.get(breachyear)
                if (doesbreachyearexist == None):
                    yearbreachlist[breachyear] = []
                else:
                    yearbreachlist[breachyear].append(line)
            pass

f = open('filesbyear.txt', 'w')
for year in yearbreachlist:
    for usernamepassword in yearbreachlist[year]:
        usernamepassword = usernamepassword[:len(usernamepassword)-2]
        line = str(usernamepassword) + ":" + str(year) + "\n"
        f.write(line)
f.close
