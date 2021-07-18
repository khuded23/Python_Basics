
import paramiko
import datetime

def getconf(device):

	ise1onvo = "10.19.148.132"
	ise1omio = "10.24.81.196"

	filename = output_filename
	f = open(filename,'a')

	if "expertcity.com" not in device:
		device = device + '.expertcity.com'

	commands = ["show version"]

	client = paramiko.SSHClient()
	client.load_system_host_keys()
	#client.set_missing_host_key_policy(paramiko.WarningPolicy)
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		print("connecting to:",device)
		client.connect(device, port=22, username="khuded", password="#Network2021",timeout=20)


		for cmd in commands:
			stdin, stdout, stderr = client.exec_command(cmd)
			print('Command executed')
			output = stdout.readlines()
			#print (output)
			res1 = ",".join(output)
			res = res1.split(" ")
			#print(res)

			if ise1onvo and ise1omio in res:
				print("new ISE-Servers   updated" +  "  on" , device)
				f.write("new ISE-Servers: " + ise1onvo + "  and  " + ise1omio+"   have been updated" +  " on  " + str(device) + '\n')
			else:
				f.write("ATTENTION!!! new ISE-Servers have NOT been updated" +  "  on  " + str(device) + '\n')

		f.close()
		return output

	except:
		output = print("Error fetching data or connecting to device:  " + device + "  are you connected to vpn? is your hostname right?")
		f.write("Couldn't connect to device  " + str(device) + '\n')


	finally:
		client.close()


def removetabspace(list1):
	new_list1=[]
	for x in list1:
		p = x.strip()
		q = p.strip(":")
		new_list1.append(q)
	return (new_list1)



input_filename = str(input("please provide the filename of the list of devices:")).strip()
output_filename = str(input("please provide the filename for output:")).strip()
#uname = str(input("please enter freeipa uname:")).strip()
#password = str(input("please enter freeipa password:")).strip()
startime = datetime.now()

new_file = open(input_filename)
output = new_file.read()

host_list = output.split("\n")
print(host_list)
#print(len(host_list))

for host in host_list:
	#print(host)
	new = getconf(host)
