import threading
import time

lock = threading.Lock()



def sleeper(n, name):
    lock.acquire()
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    lock.release()

    
    lock.acquire()
    print('{} has woken up from sleep \n'.format(name))
    lock.release()
    
    
    
    
t1 = threading.Thread(target = sleeper, name = 'thread1', args =(10, 'thread1') )
 
 
t1.start()
  
print('hello')
print('what is going on')
 