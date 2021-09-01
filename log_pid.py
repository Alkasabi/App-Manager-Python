import os

def join_sys(path):
	file_name="pid.txt"
	app_name=os.path.basename(path)
	pid = os.getpid()
	line=app_name + ","+str(pid) +"\n"
	f = open(file_name,"a")
	f.writelines(line)
	f.close()
	return line
