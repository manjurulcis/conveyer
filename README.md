readPython 3 program to simulate the production line around a single conveyor belt. OOP approach was adopted to
address the solution. The implemtation still need some work for full end-to-end simulation. 
Basically tested the simulation for 15 steps, and compute how many finished 
products come off the production line, and how many components of each 
type go through the production line without being picked up by any workers.

The solution can be improvised maintaining the same logic that we have in the current implementation. 

Currently the program is able to
- simulate the belt 
- count how many complete products were returned in the belt  
- how many components without being picked up 
- shows in which slots we have complete product

To run the program: 

$ python3 conveyor.py 

#######################################

Total products returned in belt:  3
Without being picked:  5

Output of finished items
['', '', '', '', '', '', '', 'P', '', 'P', '', '', '', '', 'P']

Returned 'P' in slot
4 A B
5 A B
11 A B

#######################################

Improvements: 

- Not able to show the belt with A, B , '', and P altoghether.
- Wasn't able to implement all the python best practices
- Code can be more pythonic
- object creation can be improvised  
- no unit testing done yet
- cleaning up the code

