import psutil
import os,signal

my_pid=os.getpid()
#print(my_pid)
print("python procces killer started")

for proc in psutil.process_iter():
    try:
        name=proc.name()
        if name=="python.exe" and proc.pid != my_pid:
            print(proc.pid ," killed")
            os.kill(proc.pid,0)
            
    except Exception as e:
        #print(e)
        pass
print("Finished....Press any key to exit ..")
input()
        
