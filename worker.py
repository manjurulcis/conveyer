class Worker:
    """ This class provides a way to store belt worker's state """
    hand_one = ''
    hand_two = ''
    belt_position = 0
    
    def __init__(self):
        """ Placeholder for OOP implementation  """
        pass
    
    
    def is_hand_full(self):
        """ Checks if the workers has both the components A and B or not""" 
        if self.hand_one != '' and self.hand_two != '':
            return True
        return False
    
    
    def take_component(self, component, belt_position):
        """ Determines whether the worker has any finished product or need a component """
         
        if self.hand_one == '' and self.hand_two != component:
            self.hand_one = component
        elif self.hand_two == '' and self.hand_one != component:
            self.hand_two = component         
            
        self.belt_position = belt_position
        
        
    def reset(self):
        """ Requires when we need to reset the workers condition to initial stage"""
        self.hand_one = ''
        self.hand_two = ''
        self.belt_position = 0   