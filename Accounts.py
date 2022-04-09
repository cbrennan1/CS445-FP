import requests

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
website = 'https://www.google.com'
def httpstatus(website):
    response = requests.get(website)
    status = response.status_code
    return status
# Add User
def adduser():
	list.append ( accounts('<uid3>', 'John Smith', "123 Main ST", "312-456-7890", "http://example.com/images/john-smith.jpeg", "false", "<date3>" ))
	newuserdata = list[3]
	x = requests.post(website, data = newuserdata)
	status = x.status_code
#Return UID
def uidcheck0():
	return list[0].uid
	

def uidcheck1():
	return list[1].uid

def uidcheck2():
	return list[2].uid

print("\nUIDS")
uid0 = uidcheck0()
uid1 = uidcheck1()
uid2 = uidcheck2()
