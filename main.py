"""
Python 3 program to simulate the production line around a single conveyor belt.

copyright: (c) 2020 by Habibul Islam
"""

import random
import copy
from worker import Worker 

workers = []                # holds the list of workers
belt_input = ['A', 'B', ''] # defines the source of elements in the belt
belt_items = []             # holds list of items in the belt

def find_next_available_worker(workers, component, i):
    """Checks which worker is available to pick the component or return the finished product"""
    for worker in workers:
        check_state = False
        # Implements the condition of worker's current state 
        # and checks if the worker now able to take a component or not
        # also keeps the the belt's current index value for final calculation
        # worker != None and
        if  worker.is_hand_full() == False and component != '':
            worker.take_component(component, i) 
            check_state = worker.is_hand_full()
            belt_items[i] = ''
        if check_state:
            #print('Finished Product:', worker.belt_position, worker.hand_one, worker.hand_two, worker.finished_product, i)
            return worker
    return False      


def assemble_and_retrun_in_belt(current_belt_index, workers):
    """Check which worker is ready to return complete product 'P' item"""

    # May need some more testing to really make sure it always returns the corrent value 
    for worker in workers:
        # As ssembled product back on the belt on the fourth subsequent slot, we need to go 3 step ahead from current belt position
        if belt_items[current_belt_index] == '' and worker.finished_product == 1 and current_belt_index >= worker.belt_position + 3:
           belt_items[current_belt_index] = 'P' # keep the complete product in the belt 
           w = copy.copy(worker)                # Added this tweak to append the complete product in the existing list
           worker.reset()                       # Worker again free to take new component
           if w.is_hand_full() == 1:
            return 1
       
    return 0;   
    
    
def main (): 
    finished_products = 0      # holds the finished/assembled products
            
    # 3 pairs of workers in both side of the belt
    # workers = [w1, w2, w3, w_1, w_2, w_3]
    worker_count = 0
    while worker_count <= 5:
        worker = Worker()
        workers.append(worker)
        worker_count += 1
        
    total_component_count = 0
    i = 0
    all_component = '  '
    
    print("Items in Belt for first 100 slots:")
    # while i < 100: 
    while i < 100: # for 100 steps it will be "while i < 100"
        component = belt_input[random.randint(0, 2)] # randomly generates A, B,'' at the start of the belt 
        belt_items.append(component)
        if (component != ''):
            total_component_count += 1
            next_available_worker = find_next_available_worker(workers, component, i) #
        if (component == ''):    
            finished_products += assemble_and_retrun_in_belt(i, workers)
            
        i += 1
        all_component = all_component + component + ',  '
        #print(i, component)
        
        
    ## TODO: Into improvise the logic so that it also shows the exisitng components with 'P' 
    
       
    print("Total products returned in belt: ", finished_products)
    print("Without being picked: ", total_component_count - finished_products*2) # each product has two components   
    # for w in workers:
    #     print(w.belt_position, w.hand_one, w.hand_two, w.finished_product)
    print(" ")
    print("Output of finished items")
    print(belt_items)
    print(" ")
    print(all_component)
    print("Returned 'P' in slot")
    

if __name__ == "__main__":
    main()

