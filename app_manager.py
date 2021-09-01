import subprocess
import time

import os
import time
import threading
import psutil

proc_list={}

class AppManager():

    def __init__(self,log="pid.log"):
        self.my_pid={}
        self.sys_pid=[]
        self.p={}
        self.log_name=log
        self.app_list=[]
        self.rate=3
    
    def resume(self):
        self.get_sys_pid()
        self.start_monitor()

    def get_sys_pid(self):
        self.sys_pid=[]
        for proc in psutil.process_iter():
        # check whether the process name matches
            try:
                self.sys_pid.append(int(proc.pid))
            except Exception as e:
                print( e )
        return self.sys_pid

    def set_rate(self, sec):
        self.rate=sec

    def run_all_app(self):
        for app in self.app_list:
            self.p[app]=subprocess.Popen(['python.exe',app]) 
            self.p[app].demond=True
            print(self.p[app].pid)
            time.sleep(1)
            pass

    def reset_log(self):
        try:
            open(self.log_name, 'w').close()
            self.update_my_pid()
            time.sleep(0.2)
            return self.my_pid
        except Exception :
            pass
 
    def run_app(self,app):
        self.p[app]=subprocess.Popen(['python.exe',app]) 
        self.p[app].demond=True
        
    def close_app(self,app):
        try:
            self.p[app].kill()
            print(app," Kiled")
        except Exception :
            print("Error can not kill ",app)

    def join_sys(self,path):
        app_name=os.path.basename(path)
        my_pid = os.getpid()
        line=app_name + ","+str(my_pid) +"\n"
        f = open(self.log_name,"a")
        f.writelines(line)
        f.close()
        return line

    def add_app(self,app_name):
        self.app_list.append(app_name)
        return self.app_list

    def remove_app(self,app_name):
        try:
            self.app_list.remove(app_name)
            return self.app_list
        except Exception :
            return self.app_list

    def monitor_loop(self):
        self.is_runing=True
        try:
            while self.is_runing:
                time.sleep(self.rate)
                self.get_sys_pid()
                for proc in self.p:
                    pid=self.p[proc].pid
                    print(pid)
                    if pid not in self.sys_pid:
                        print(proc,pid,'is not running')
                        self.run_app(proc)
                        print(proc,pid,'is running now')
                        time.sleep(0.1)

        except Exception as e:
            print(e)

    def start_monitor(self):
        self.th1=threading.Thread(target = self.monitor_loop )
        self.th1.start()
        return self.is_runing
        
    def stop_minitor(self):
        self.is_runing=False
        return self.is_runing




sv=AppManager()
sv.add_app("app1.py")
sv.run_all_app()
sv.start_monitor()
time.sleep(1)
sv.close_app("app1.py")