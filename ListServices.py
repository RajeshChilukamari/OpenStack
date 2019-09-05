##Importing require modules
from openstack import connection


##Creating Connection object
conn = connection.Connection(auth_url = "http://192.168.38.187/identity/v3", project_name = "admin", username = "admin", password = "openstack", user_domain_id = "default", project_domain_id = "default")


##List all images
def listAllImages():
    for image in conn.compute.images():
        print("Image Id: ", image.id, " Image Name: ", image.name)

listAllImages()



##List all flavors
def listAllFlavors():
    for flavor in conn.compute.flavors():
        print("Flavor Id: ", flavor.id, " Flavor Name: ", flavor.name)

listAllFlavors()



##list all servers
def listAllServers():
    for server in conn.compute.servers():
        print("Server Id: ", server.id, "Server Name: ", server.name)

listAllServers()



##list networks
def listAllNetworks():
    for nw in conn.network.networks():
        print("Network Id: ", nw.id, "Network Name: ", nw.name)

listAllNetworks()
