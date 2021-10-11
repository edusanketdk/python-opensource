# Creating a recursive function 
def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return  
    # function call itself  
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
  
  
disks = int(input('Enter no. of disks: '))  
  
tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function  
