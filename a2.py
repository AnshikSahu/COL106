class Stone:# Each element in the heap is an object of this class
#
    def __init__(self,order,index,value):# constructot for the class
    #
    # Input Parameters: self: Current object
    #                   order: Keeps record of when the object was created
    #                   index: Index of current object in the list containing the heap
    #                   value: The value to be stored in the object
        self.order=order# the order in which the object was created
        self.index=index# the position of object in the heap
        self.weight=value# the value stored in the object
        self.left=None# the object before the current object initially(before creating the minHeap)
        self.right=None# the object after the current object initially(before creating the minHeap)
#
#
    def __gt__(self,other):# checks weather an object is greater than the other
    #
    # Input Parameters: self,other : the objects to be compared
    #
    # Output: Boolean
    #
            return self.weight>other.weight# comparing the weights of the objects
#
#
    def __lt__(self,other):# checks weather an object is lesser than the other
    #
    # Input Parameters: self,other : the objects to be compared
    #
    # Output: Boolean
    #
            return self.weight<other.weight# comparing the weights of the objects
#
#
    def __str__(self):# redundant for current assignment
        return str(self.weight)
#
#
#
#
class Heap_of_Stones:# A minHeap with elements of datatype Stone
#
    def __init__(self,values):# colstructor for the class
    #
    # Input Parameters: self: The current object
    #                   values: A list of values which are to be arranged in a minHeap
    #
        self.number_of_stones=len(values)# The number of values
        self.stones=[None]*self.number_of_stones# The list containing the Heap
        for index in range(self.number_of_stones):# Terminates when i becomes equal to the number of values
            stone=Stone(index,index,values[index])# Creating an objec t of the class Stone to represent an element
            self.stones[index]=stone# Storing the object in the list
            if(index>0):# checking if current element has an element to its left
                stone.left=self.stones[index-1]# updating the current element
                self.stones[index-1].right=stone# updating the previous element
        self.stack_the_stones()# arranging the elements in a minHeap
#
#
    def smallest_stone(self):# returns the element with the lowest value/weight
    #
    # Input Parameters: self: the current object
    #
    # Output: object of class Stone
    #
        return self.stones[0]# the smallest stone is at the top of the heap
#
#
    def above_the_stone(self,index):# returns the index of the parent of the current element in the heap
    #
    # Input Parametrers: self: The current object
    #                   index: The position of the element in the list representing the heap
    # Output: int or None
    #
        if(index>0):# checking if the element has a parent
            return (index-1)//2# The index of the parent
        else:
            return None# returning None if there is no parent
#
#
    def below_the_stone(self,index,number_of_stones):# returns the index of the children of current element
    #
    # Input parameters: self: The current object
    #                   index: The index of current element
    #                   number_of_stones: The number of elements in the heap
    #
    # Output: tuple containing the index of left and right child
    #
        left_child=2*index+1# index of the left child
        right_child=2*index+2# index of the right child
        if(left_child>=number_of_stones):# checking if any children exist
            left_child=None# updating the value as there is no left child
            right_child=None# updating the value as there is no right child
        elif(right_child>=number_of_stones):# checking if right child exist
            right_child=None# updating the value as there is no right child
        return (left_child,right_child)# returning the children as a tuple
#
#
    def swap_stones(self,stone,other_stone):# swaps the position of two elements in the heap
    #
    # Input Parameters: self: The current object
    #                   stone,other_stone: The elements to be exchanged
    #
        self.stones[stone.index],self.stones[other_stone.index]=other_stone,stone# exchanging the elements
        stone.index,other_stone.index=other_stone.index,stone.index# updating the elements
#
#
    def move_stone_towards_the_top(self,stone):# recurrsively moves the element upwards in the heap until it is at its correct position(HeapUp) assuming the elements above are in correct posistion
    #
    # Input Parameters: self: the current object
    #                   stone: The element to be moved
    #
        if(stone.index>0):# checking if the element is not the topmost
            parent_stone=self.stones[self.above_the_stone(stone.index)]# the parent of the element
            if(stone<parent_stone):# checking if the element has reached the current position
                self.swap_stones(stone,parent_stone)# swapping element with the parent
                self.move_stone_towards_the_top(stone)# counting to the next step
#
#
    def move_stone_towards_the_base(self,stone):# recurrsively moves the element downwards in the heap until it is at its correct position(HeapDown) assuming the elements below are in correct posistion
    #
    # Input Parameters: self: the current element
    #                   stone: the element to be moved
    #
        child_stones=self.below_the_stone(stone.index,self.number_of_stones)# finding the index of the children of the element
        if(child_stones[0]!=None or child_stones[1]!=None):# checking if the element is not at the base
            if(child_stones[0]==None):# checking if there is no left child
                temporary_stone=self.stones[child_stones[1]]# the stone to be exchanged with is the only element below
            elif(child_stones[1]==None):# checking if there is no right child
                temporary_stone=self.stones[child_stones[0]]# the stone to be exchanged with is the only element below
            else:# both childred exist
                left_child_stone=self.stones[child_stones[0]]# the left child
                right_child_stone=self.stones[child_stones[1]]# the right child
                if(left_child_stone<right_child_stone):# the smaller child is the one with which the element is to be exchanged
                    temporary_stone=left_child_stone
                else:
                    temporary_stone=right_child_stone
            if(temporary_stone<stone):# checking if the element has reached its correct position
                self.swap_stones(stone,temporary_stone)# exchanging the elements
                self.move_stone_towards_the_base(stone)# contuing to the next step
#
#
    def stack_the_stones(self):# converts a heap to a minHeap
    #
    # Input Parameters: self: the current object
    #
        for index in range(self.number_of_stones-1,-1,-1):# going through the heap starting from the second-last element
            self.move_stone_towards_the_base(self.stones[index])# moving each element to its current element
#
#
    def organize_stone(self,stone):# moves an element to its correct position assuming all other elements are in correct position
    #
    # Input Parameters: self: the current object
    #                   stone: the element to be moved
    #
        parent_index=self.above_the_stone(stone.index)# index of the parent of the element
        if(parent_index!=None):# checking if the element is not the topmost
            parent_stone=self.stones[parent_index]# parent of the element
            if(parent_stone>stone):# checking if the correct position is upwards
                self.move_stone_towards_the_top(stone)# moving the element upwards
            else:# the correct position is downwards
                self.move_stone_towards_the_base(stone)# moving the element downwards
        else:# the only way is downwards
            self.move_stone_towards_the_base(stone)# moving the element downwards
#
#
    def __str__(self):# redundant for current assignment
        string=""
        for stone in self.stones:
            string=string+str(stone)+" "
        return string
#
#
#
#
class Particle:# a datatype to define a particle
#
    def __init__(self,name,mass,position,velocity):# constructor for the class
    #
    # Input Parameters: self: the current object
    #                   name: the name/identity of the particle
    #                   mass: the mass of the particle
    #                   position: the position of the particle
    #                   velocity: the velocity of the particle
        self.name=name
        self.mass=mass
        self.position=position# position at time of last update
        self.velocity=velocity
        self.time_of_last_update=0# all particles are initially updated
#
#
    def __str__(self):# redundant for current assignment
        return str([self.name,self.mass,self.position,self.velocity,self.time_of_last_update])
#
#
#
#
class System_of_particles:# a datatype defining a system of particles moving in 1-dimension
#
    def __init__(self,particles):# constructor for the class
    #
    # Input Parameters: self: The current object
    #                   particles: a list containing all the particles in the system in their initial state
    #
        self.particles=particles
        self.number_of_particles=len(particles)# the number of particles in the system
        self.time=0# starting the system
        times_of_collisiosn=self.time_of_collision()# calculating the time of collision between every pair of adjacent particles
        self.heap_of_collisions=Heap_of_Stones(times_of_collisiosn)# arranginh the times of collision in a minHeap
#
#
    def two_particle_collision(self,left_particle,right_particle):# calculates the time taken by two particles to collide
    #
    # Input Parameters: self: the current object
    #                   left_particle: the particle on the left
    #                   right_particle: the particle on the right
    #
    # Output: float : the time taken for the particles to collide
    #
        left_particle_position=left_particle.position+left_particle.velocity*(self.time-left_particle.time_of_last_update)# the current position of the left particle
        right_particle_position=right_particle.position+right_particle.velocity*(self.time-right_particle.time_of_last_update)# the current position of the right particle
        distance=right_particle_position-left_particle_position# the distance between the two particles
        relative_velocity=left_particle.velocity-right_particle.velocity# velocity of approach of the two particles
        if(relative_velocity<=0):# checking if collision is not possible
            time_taken_to_collide=float("INF")# the particles take infinite time to collide
        else:# the particles can possibly collide
            time_taken_to_collide=distance/relative_velocity# time taken is distance divided by speed
        return time_taken_to_collide# returning the time taken for the particles to collide
#
#
    def time_of_collision(self):# calculates the time of collision for a list of particles
    #
    # Input Parameters: self: The current object
    #
    # Output: list of float : list containing the times of collision of every pair of adjacent particles
    #
        times_of_collision=[]
        for i in range(self.number_of_particles-1):# going through each pair of adjacent particles
            left_particle=self.particles[i]# the left particle
            right_particle=self.particles[i+1]# the right particle
            time_taken_to_collide=self.two_particle_collision(left_particle,right_particle)# time taken for the two particles to collide
            times_of_collision.append(time_taken_to_collide)# adding the time to the list
        return times_of_collision# returning the list of times
#
#
    def update_particles(self,left_particle,right_particle):# updates the properties of the two colliding particles after collision
    #
    # Input Parameter: self: the current object
    #                  left_particle: the left colliding particle
    #                  right_particle: the right colliding particle
    #
        position_at_collision=left_particle.position+left_particle.velocity*(self.time-left_particle.time_of_last_update)# the position of collision
        left_particle.position=position_at_collision# updating the position of the particle
        right_particle.position=position_at_collision# updating the position of the particle
        right_particle.time_of_last_update=self.time# updating the time of last update
        left_particle.time_of_last_update=self.time# updating the time of last update
        m1=left_particle.mass
        m2=right_particle.mass
        v1=left_particle.velocity
        v2=right_particle.velocity
        left_particle.velocity=((m1-m2)*v1+2*m2*v2)/(m1+m2)# updating the velocity of the particle
        right_particle.velocity=(2*m1*v1+(m2-m1)*v2)/(m1+m2)# updating the velocity of the particle
#
#
    def update_system(self):# updates the system after collision
    #
    # Input Parameter: self: the current object
    #
        fastest_collision=self.heap_of_collisions.smallest_stone()# the element of heap representing the fastest possible collision
        left_particle=self.particles[fastest_collision.order]# the left colliding particle 
        right_particle=self.particles[fastest_collision.order+1]# the right colliding particle
        self.time=fastest_collision.weight# updating the time of the system
        self.update_particles(left_particle,right_particle)# updating the colliding particles
        fastest_collision.weight=self.two_particle_collision(left_particle,right_particle)#updating the element of heap representing the collision between the two particles
        self.heap_of_collisions.organize_stone(fastest_collision)# moving the element to its correct position
        left_collision=fastest_collision.left# the element of heap representing the collision left to the current collision
        right_collision=fastest_collision.right# the element of heap representing the collision right to the current collision
        if(left_collision!=None):# checking if there is a collision to the left
            left_collision.weight=self.two_particle_collision(self.particles[fastest_collision.order-1],left_particle)+self.time# updating the time of the collision to the left
            self.heap_of_collisions.organize_stone(left_collision)# moving the left colision to its correct position in the heap
        if(right_collision!=None):# checking if there is a collision to the right
            right_collision.weight=self.two_particle_collision(right_particle,self.particles[fastest_collision.order+2])+self.time# updating the time of the collision to the right
            self.heap_of_collisions.organize_stone(right_collision)# moving the right colision to its correct position in the heap
#
#
    def look_inside_system(self):# returns certain properties of system when the next collision occurs
    #
    # Input parameters: self: the current object
    #
    # Output: tuple containg the time of next collision, the particle colliding, the p;osition of next collision
    #
        fastest_collision=self.heap_of_collisions.smallest_stone()# the element of heap representing the fastest possible collision
        if(fastest_collision.weight==float("INF")):# checing if no collision is possible
            return None# no data for next collision
        left_particle=self.particles[fastest_collision.order]# the left colliding particle
        position_at_collision=left_particle.position+left_particle.velocity*(fastest_collision.weight-left_particle.time_of_last_update)# position of collision
        time_at_collision=fastest_collision.weight# the time of collision
        """return (floor(time_at_collision,4),left_particle.name,floor(position_at_collision,4))"""# Uncomment if floor/round down is needed
        return (round(time_at_collision,4),left_particle.name,round(position_at_collision,4))# returning the necessary data after rounding it off
#
#
    def __str__(self):# redundant for current assignment
        for particle in self.particles:
            print(particle)
        return ""
#
#
#
#
def floor(number,number_of_digits_after_decimal_required):# rounds off numbers to the largest number with required decimal places less than or equal to the number
#
# Input Parameters: number: the number to be rounded off
#                   number_of_digits_after_decimal_required: the number of decimal places in the returned value
    split=str(number).split(".")# seprating the integer and decimal part
    new_number=split[0]+"."+split[1][:number_of_digits_after_decimal_required]# combining the integer and new decimal part
    return float(new_number)
def listCollisions(M,x,v,m,T):# function to list first m collisions within a cerain time
#
# Input Parameters: M: list containing the masses of all particles
#                   x: list containing the initial positions of all particles
#                   v: list containing the initial velocities of all particles
#                   m: the maximum number of collisions to be reported
#                   T: the time period in which the collisions are to be reported
#
# Output: the list of possible collisions within given specifications
#
    particles=[]
    number_of_particles=len(M)# the number of particles
    for i in range(number_of_particles):# Terminates when i equals the number of particles
        particle=Particle(i,M[i],x[i],v[i])# creating an object of class Particle for each particle
        particles.append(particle)# adding the particle to the list
    system_of_particles=System_of_particles(particles)# creating a system of particles with the given particles
    collisions=[]# list containing the list of every collision as a tuple
    for i in range(m):# Terminates when i equals to the maximum number of possible collisions to be reported
        collision=system_of_particles.look_inside_system()# calculating the properties of the next collision
        system_of_particles.update_system()# updating the system of particles
        if(collision==None or system_of_particles.time>T):# checking if there are no more possible collisions or the time period of search is exceeded
            break# ending the search
        collisions.append(collision)# adding current collision and its properties to the list
    return(collisions)# returning the properties of the required number of collisions