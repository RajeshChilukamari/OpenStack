##Importing require modules
from openstack import connection


##Creating Connection object
conn = connection.Connection(auth_url = "http://192.168.38.187/identity/v3", project_name = "admin", username = "admin", password = "openstack", user_domain_id = "default", project_domain_id = "default")



###SERVER CREATION
nw = conn.network.find_network("public")
fId = conn.compute.find_flavor("m1.small")
iId = conn.compute.find_image("cirros-0.3.5-x86_64-disk")

def createServer(iId, fId, nw):
    return conn.create_server(name = "test1", image = iId, flavor = fId, network = nw)

server = createServer(iId, fId, nw)
