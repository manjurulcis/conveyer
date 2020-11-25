
import random
import copy

class Worker:
    handOne = ''
    handTwo = ''
    finishedProduct = 0
    beltPosition = 0
    
    def isHandFull(self):
        if self.handOne != '' and self.handTwo != '':
            return True
        
        return False
    
    def setWorkerData(self, component, beltPosition):
        if self.handOne == '' and self.handTwo != component:
            self.handOne = component
        elif self.handTwo == '' and self.handOne != component:
            self.handTwo = component 
            
        if self.handOne and self.handTwo:
            self.finishedProduct += 1      
            
        self.beltPosition = beltPosition
        
    def reset(self):
        self.handOne = ''
        self.handTwo = ''
        self.finishedProduct = 0
        self.beltPosition = 0      
        

 
w1 = Worker()
w2 = Worker()
w3 = Worker()
w_1 = Worker()
w_2 = Worker()
w_3 = Worker()
workers = [w1, w2, w3, w_1, w_2, w_3]

belt_products = []
belt_input = ['A', 'B', '']
belt_items = []
i = 0

def findNextAvailableWorker(workers, component):
    for worker in workers:
        writeState = False
        if worker != None and worker.isHandFull() == False and component != '':
            worker.setWorkerData(component, i) 
            writeState = worker.isHandFull()
        if (writeState):
            return worker
    return False    

def assembleProductAndReturnInBelt(currentBeltIndex, belt_products):
    for worker in workers:
        #dump(worker)
        if worker.finishedProduct == 1 and currentBeltIndex >= worker.beltPosition + 3:
            belt_items[currentBeltIndex] = 'P'
            w = copy.copy(worker)
            belt_products.append(w)
            worker.reset()
            print('TT', w.beltPosition, w.handOne, w.handTwo, w.finishedProduct)
            break
        
def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))  
         
while i < 10:
    component = belt_input[random.randint(0, 2)]
    belt_items.append(component)
    if (component != ''):
        availableWorker = findNextAvailableWorker(workers, component)
        assembleProductAndReturnInBelt(i, belt_products)
    #todo: write a function to check workers and if current index i-4 = worker's index, then put P in that index in belt items if the position is
    # print('Iteration ', i)
    # print('w1.....w2.....w3')
    # j = 0
    # output = ''
    # while j <= 3:
    #     if (j < len(belt_items)):
    #         output.join(belt_items[j])
    #         output.join('.....')
    #     j += 1   
    # print(output)    
    # print('w4...,,w5.....w6')
    i += 1
    
print(belt_items)
for w in belt_products:
    print(w.beltPosition, w.handOne, w.handTwo, w.finishedProduct) 


# [1'A', 2'A', 3'A', 1'B', 4'A', 2'B', 5'A', 'P', 3'B', 6'A', 'A', 'A', 4'B', 5'B', '', '', '', 'A', 'A', 6'B', 'B', 'B', '', '', '', 'B', 'A', 'A', 'A', '', 'B', '', 'A', 'A', 'B', 'B', 'A', '', '', '', 'B', '', 'A', 'A', 'A', '', 'B', 'A', 'A', 'A', 'B', 'A', '', 'B', '', '', 'B', 'B', 'A', '', '', 'B', 'A', 'A', 'A', 'A', '', 'B', '', '', '', 'B', '', '', '', '', 'B', 'B', 'A', 'A', 'B', '', 'B', 'A', '', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', '', 'B', '', 'A', 'B']