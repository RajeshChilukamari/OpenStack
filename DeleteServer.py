##Importing require modules
from openstack import connection


##Creating Connection object
conn = connection.Connection(auth_url = "http://10.39.38.187/identity/v3", project_name = "admin", username = "admin", password = "openstack", user_domain_id = "default", project_domain_id = "default")

sId = "c2f4b698-f3af-4f02-9cd4-083428c5f011"

###Server deletion
def deleteServer(serverId):
	conn.compute.delete_server(serverId)

deleteServer(sId)
