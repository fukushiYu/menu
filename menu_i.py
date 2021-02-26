import os
#---------------------------------------------------------------
def check_services():
        c={'redis':'pgrep -a redis',
                'mon_redis':'ps -aux | grep mon_redis.py',
                'uvicorn/fapi':'pgrep -a uvicorn',
                'mysql':'pgrep -a mysql',
                'postgresql':'pgrep -a postgre',
                'nginx':'pgrep -a nginx',
        }
        for k,v in c.items():
                f=os.popen(v)
                r=f.readlines()
                if(len(r)>0):
                        print("O=>"+k+" alive \n\t"+r[0])
                else:
                        print("X=>"+k+" dead\n")
#---------------------------------------------------------------
