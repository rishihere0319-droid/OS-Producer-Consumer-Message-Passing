from multiprocessing import Process, Queue
import time
import random

def producer(queue):
    for i in range(6):  
        item = random.randint(1, 100)
        print(f"Producer trying to put: {item}")
        queue.put(item)  
        print(f"Producer successfully put: {item}")
        time.sleep(0.2)  

def consumer(queue):
    for i in range(6):
        time.sleep(2)   
        item = queue.get() 
        print(f"Consumer consumed: {item}")

if __name__ == "__main__":
    print("Student Name: Rishi Pal | Roll No: S100")
    print("-" * 40)
    
    q = Queue(maxsize=3)  
    
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print("Producer and Consumer have finished.")
