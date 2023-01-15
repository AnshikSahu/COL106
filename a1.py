# COL106 Assignment 1
#
# Approach: Growth algorithm for creating a Stack
#           Weighing each movement by a factor
#
class Stack:# Creating a user defined implementation of Stack datatype
#
    def __init__(self):# Constructor for Stack
    #
    # Input Parameter: self : The current object
    # Output: NONE
    #
        self.stack=[None]*1000# Base memory space for stack
        self.size=0# Number of elements in stack
#
    def grow(self):# Function to increase the size of memory space for stack if necessary
    #
    # Input Parameter: self : The current object
    # Output: NONE
    #
        length=len(self.stack)# Calculating current memory space
        if(self.size==length):# Checking if the stack is at full capacity
            temp=[None]*(2*length)# Doubling the size of memory space
            for i in range(length):# loop to go through each index of stack; Terminates when i=length
                temp[i]=self.stack[i]# copying each elements into new memory space
            self.stack=temp# aliasing the new stack into the object
#
    def pileup(self,x):# Function to place an element at the top of the stack
    #
    # Input Patameters: self : The current object
    #                    x   : The element to place at top
    # Output: NONE
    #
        self.grow()# Increasing size of memory space if needed
        self.stack[self.size]=x# Placing x at the top of stack
        self.size=self.size+1# Updating the size of stack
#
    def falldown(self):# Function to remove and return the top element from stack
    #
    # Input Parameters: self : The current object
    # Output: The element at top
    #
        self.size=self.size-1# Updating the size of stack
        return self.stack[self.size]# Returning the element at top
#
def findPositionandDistance(P):# Function to implement a drone program
#
# Input Parameter: P : String : The drone program
# Output : List : The first three elements provide final position of the drone as coordinates and the fourth element  provides the total distance travelled
#
    sign=1# Stores the direction of motion( 1 for along +ve axis and -1 for along -ve axis)
    stack=Stack()# Creating a stack object
    weight=1# Stores the factor by which each movement is to be weighted
    num=0# Stores the factor by which weight is to be changed(num=0 is no change instead of weight becoming 0)
    x=0# The current x coordinate
    y=0# The current y coordinate
    z=0# The current z coordinate
    xtemp=0#change in x coordinate
    ytemp=0#change in y coordinate
    ztemp=0#change in z coordinate
    dtemp=0##change in distance
    distance=0# The total distance travelled
    length=len(P)# The size of the drone program
    for i in range(length):# loop to go through each index of P; Terminates when i=length
    #
    # The ith character of the program P can be of four types: "+" or "-" : To specify the direction of motion
    #                                                           "X" or "Y" or "Z" : To specify the axis of motion
    #                                                           "(" or ")" : To update the weight
    #                                                           a digit phich is a part of num
    # The if-elif-else block checks for each possible character and operates accordingly
    #
        if(P[i]=="+"):
            sign=1# Updating the direction of motion to the +ve axis
        elif(P[i]=="-"):
            sign=-1# Updating the direction of motion to the -ve axis
        elif(P[i]=="X"):
            xtemp=xtemp+sign# Updating the x coordinate
            dtemp=dtemp+1# Updating the total distance travelled
        elif(P[i]=="Y"):
            ytemp=ytemp+sign# Updating the y coordinate
            dtemp=dtemp+1# Updating the total distance travelled
        elif(P[i]=="Z"):
            ztemp=ztemp+sign# Updating the z coordinate
            dtemp=dtemp+1# Updating the total distance travelled
        elif(P[i]=="("):
            x=x+xtemp*weight
            y=y+ytemp*weight
            z=z+ztemp*weight
            distance=distance+dtemp*weight
            xtemp=0
            ytemp=0
            ztemp=0
            dtemp=0
            num=num+(num==0)# changing num=0 to 1 as num=0 is no change instead of weight becoming 0
            stack.pileup(weight)# adding the current value of weight to stack
            weight=weight*num# Updationg the value of weight
            num=0# Re-initialising num
        elif(P[i]==")"):
            x=x+xtemp*weight
            y=y+ytemp*weight
            z=z+ztemp*weight
            distance=distance+dtemp*weight
            xtemp=0
            ytemp=0
            ztemp=0
            dtemp=0
            weight=stack.falldown()# Updating weight to its previous value
        else:
            num=num*10+int(P[i])# Adding the digit to num at ones place
    x=x+xtemp*weight
    y=y+ytemp*weight
    z=z+ztemp*weight
    distance=distance+dtemp*weight
    xtemp=0
    ytemp=0
    ztemp=0
    dtemp=0
    return [x,y,z,distance]# returning the output list
