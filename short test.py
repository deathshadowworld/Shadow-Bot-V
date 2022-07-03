string = 'postgres://qrsjiaiibkiozj:9910b86315f47670711ff8531af15533bc2048589d9545a223a6aac79e1a376f@ec2-44-198-82-71.compute-1.amazonaws.com:5432/db748l2vl4o7k5'
data = []

strurl = string.replace('postgres://','')
temp1 = strurl.split(':')
data.append(temp1[0])
temp2 = temp1[1].split("@")
data.append(temp2[0])
data.append(temp2[1])
temp3 = temp1[2].split("/")
data.append(temp3[0])
data.append(temp3[1])

#strurl = strurl.split(':')
#strurl = strurl[1].split('@')
#strurl = strurl[3].split('/')

print (data)