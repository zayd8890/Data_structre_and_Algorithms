from collections import deque
import time
import threading
class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

    def place_orders(self, orders):
        for order in orders:
            self.enqueue(order)
            time.sleep(0.5)
        print("Current orders:")
        q.print_orders()
    def print_orders(self):
        return print(self.buffer)
    
    def serve_orders(self):
        time.sleep(1)
        loop = True
        while loop:
            if len(self.buffer) == 0:
                loop = False
                print("No more orders to serve.")
                break
            print(f"Serving order: {self.dequeue()}")
            time.sleep(2)
# Example usage:
if __name__ == "__main__":
    q = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=q.place_orders, args=(orders,))
    t2 = threading.Thread(target=q.serve_orders)

    
        
    t1.start()
    t2.start()
    t1.join()
    t2.join()
        
