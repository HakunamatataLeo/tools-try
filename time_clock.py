import time
def mini(sec):
    pas= int(time.time())+int(sec)
    while 1:
    	now= int(time.time())
    	if  now == pas:
            return    	   
        else:
            print "1yo"

if __name__ == "__main__":
    t = raw_input("input Time:")
    mini(t)
