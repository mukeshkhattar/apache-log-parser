#https://medium.com/devops-challenge/apache-log-parser-using-python-8080fbc41dda
'''
find top 10 offending IP addresses in apache_logs to detect dos
'''
import re
from collections import Counter
# Open file
with open('apache_logs', 'r') as f:
# Feed the file text into findall(); it returns a list of all the found strings
  regex = r'(\d{3}|\d{2}|[\d])\.(\d{3}|\d{2}|[\d])\.(\d{3}|\d{2}|[\d])\.(\d{3}|\d{2}|[\d])'
  ip_tuple_list = re.findall(regex, f.read())

ip_list=[]
for atuple in ip_tuple_list:
  ip_list.append(atuple[0]+'.'+atuple[1]+'.'+atuple[2]+'.'+atuple[3])

#create a dict with key:value pairs(ip:count) using Counter class. this dic stores count indesc order
ip_list_by_count=Counter(ip_list)

#Get the top 10 ips. This returms a list of tuples(ip:count)
my_top_10_ip=ip_list_by_count.most_common(10)

#print the top 10
for tuple in my_top_10_ip:
  print('ip:',tuple[0], 'count:', tuple[1])


'''
output:
ip: 66.249.73.135 count: 482
ip: 46.105.14.53 count: 364
ip: 130.237.218.86 count: 357
ip: 75.97.9.59 count: 273
ip: 50.16.19.13 count: 113
ip: 209.85.238.199 count: 102
ip: 68.180.224.225 count: 99
ip: 100.43.83.137 count: 84
ip: 208.115.111.72 count: 83
ip: 198.46.149.143 count: 82
'''



