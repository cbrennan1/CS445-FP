# import requests

#Define Users in an object list
class accounts:
	def __init__(self, uid, name, address, phone, picture, is_active, date_created):
		self.uid = uid
		self.name = name
		self.address = address
		self.phone = phone
		self.picture = picture
		self.is_active = is_active
		self.date_created = date_created
list = []
list.append ( accounts('<uid0>', 'Virgil Bistriceanu', "10 West 31st ST", "312-567-5146", "http://cs.iit.edu/~virgil/pictures/virgil-head-small-200811.jpg", "true", "<date0>" ))
list.append ( accounts('<uid1>', 'Jane Smith', "123 2nd ST", "217-456-7890", "http://example.com/images/jane-smith.jpeg", "false", "<date1>" ))
list.append ( accounts('<uid2>', 'CSR #1', "101 W Main St.", "(847) 842-8048", "http://example.com/images/jane-smith.jpeg", "true", "<date2>" ))

for val in list:
	print( val.uid, val.name, val.address, val.phone, val.picture, val.is_active, val.date_created)


#Return website status
website = 'http://localhost:8080/bn/api'
def httpstatus(website):
    response = requests.get(website)
    status = response.status_code
    return status

#Return UID
def uidcheck(list):
	uid0 = list[0].uid
	uid1 = list[1].uid
	uid2 = list[2].uid
	return uid1, uid2, uid3