##Importing require modules
from openstack import connection
from datetime import timedelta
from datetime import datetime
import csv
import time

##Creating Connection object
conn = connection.Connection(auth_url = "http://10.39.38.187/identity/v3", project_name = "admin", username = "admin", password = "openstack", user_domain_id = "default", project_domain_id = "default")

server = conn.compute.find_server("test1")

##pulling Server details
s1 = conn.compute.get_server(server.id)

##Server details
sname = s1.name
print("Server Name is {}" .format(sname))

sId = s1.id
print("Server Id: {}" .format(sId))


##Image details
imgId = s1.image['id']
print("Image Id: {}" .format(imgId))

imgName = conn.compute.get_image(imgId)['name']
print("Image Name is: {}" .format(imgName))


##Network details
netName = list(s1.addresses)[0]
print("Network name is {}" .format(netName))

ipv4 = s1.addresses[netName][1]['addr']
print("IPv4 is {}" .format(ipv4))



##Flavor details
fid = s1.flavor['id']
f = conn.compute.find_flavor(fid)
hdisk = f['disk']
ram = f['ram']
fname = f['name']
vcpus = f['vcpus']
print("Flavor Id: {}\nFlavor Name: {}\nHard Disk size: {}\nRAM size: {}\nvCPUs: {}" .format(fid, fname, hdisk, ram, vcpus))


##Created time(converting UTC timestamp to IST)
utctime = s1.created_at
#print(utctime) ##2019-08-16T08:24:10Z
ctime = datetime.strptime(utctime, '%Y-%m-%dT%H:%M:%SZ') + timedelta(minutes = 330)
print("Created time: {}" .format(ctime))



##Writing to csv files
def WriteCSV(sId, sname, imgId, imgName, fid, fname, vcpus, ram, hdisk, netName, ipv4, ctime):
    #Headings
    l1 = ["Server Id","Server Name", "Image Id", "Image Name", "Flavor Id", "Flavor Name", "vCPUs", "RAM(GB)", "Hard Disk(GB)", "Network Name", "IPv4 address", "Server Created Time(IST)"]

    #Values
    l2 = [sId, sname, imgId, imgName, fid, fname, vcpus, (ram/1024), hdisk, netName, ipv4, ctime]

    ##Writing into file
    with open('output1.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(l1)
        writer.writerow(l2)

        
WriteCSV(sId, sname, imgId, imgName, fid, fname, vcpus, ram, hdisk, netName, ipv4, ctime)
