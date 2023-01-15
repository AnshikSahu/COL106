class Router:
    def __init__(self,name):
        self.name,self.path_size,self.neighbours,self.connection_to_source,self.in_consideration,self.index=name,0,[],None,False,None
class Network:
    def __init__(self,number_of_routers,connections):
        self.number_of_routers=number_of_routers
        self.routers=[Router(i) for i in range(number_of_routers)]
        for connection in connections :
            ((self.routers[connection[0]]).neighbours).append((connection[1],connection[2]))
            ((self.routers[connection[1]]).neighbours).append((connection[0],connection[2]))
class Heap:
    def __init__(self,size):
        self.heap,self.heap_size=[None]*size,0
    def enqueue(self,router):
        self.heap[self.heap_size],router.index,router.in_consideration=router,self.heap_size,True
        self.heap_size+=1
        if(self.heap_size>1): self.heapUP(self.heap_size-1)
    def heapUP(self,introduced_router_position):
        while(self.heap[introduced_router_position].path_size>self.heap[(introduced_router_position-1)//2].path_size):
            self.heap[introduced_router_position].index,self.heap[(introduced_router_position-1)//2].index=(introduced_router_position-1)//2,introduced_router_position
            self.heap[introduced_router_position],self.heap[(introduced_router_position-1)//2]=self.heap[(introduced_router_position-1)//2],self.heap[introduced_router_position]
            introduced_router_position=(introduced_router_position-1)//2
            if(introduced_router_position==0): break
    def heapDown(self,current):
        while(2*current+1<self.heap_size):
            if(2*current+2==self.heap_size):
                if(self.heap[current].path_size<self.heap[2*current+1].path_size):
                    self.heap[current].index,self.heap[2*current+1].index=2*current+1,current
                    self.heap[2*current+1],self.heap[current]=self.heap[current],self.heap[2*current+1]
                    current=2*current+1
                else: break
            else:
                greater= 2*current+1 if (self.heap[2*current+1].path_size>=self.heap[2*current+2].path_size) else 2*current+2
                if(self.heap[current].path_size<self.heap[greater].path_size):
                    self.heap[current].index,self.heap[2*current+1].index,self.heap[current],self.heap[greater]=greater,current,self.heap[greater],self.heap[current]
                current=greater
    def extract_max(self):
        maximum,self.heap[0],current=self.heap[0],self.heap[self.heap_size-1],0
        self.heap_size-=1
        self.heapDown(current)
        return maximum
    def Update(self,router):
        if(router.index==0): self.heapDown(0)
        elif(router.index*2+1>=self.heap_size): self.heapUP(router.index)
        elif(self.heap[(router.index-1)//2].path_size<router.path_size): self.heapUP(router.index)
        else: self.heapDown(router.index)
def findMaxCapacity(n,links,s,t):
    network,heap=Network(n,links),Heap(len(links)+1)
    network.routers[s].connection_to_source,network.routers[s].path_size=network.routers[s],float("INF")
    heap.enqueue(network.routers[s])
    while(heap.heap_size>0):
        largest=heap.extract_max()
        if(largest.name==t):break
        for link in largest.neighbours:
            if(not network.routers[link[0]].in_consideration):
                network.routers[link[0]].path_size=min(largest.path_size,link[1])
                network.routers[link[0]].connection_to_source=largest
                heap.enqueue(network.routers[link[0]])
            elif(network.routers[link[0]].path_size<min(largest.path_size,link[1]) and network.routers[link[0]].path_size!=0):
                network.routers[link[0]].path_size=min(largest.path_size,link[1])
                network.routers[link[0]].connection_to_source=largest
                heap.Update(network.routers[link[0]])
    path_size,current_router,path=network.routers[t].path_size,t,[]
    while(current_router!=s):
        path.append(network.routers[current_router].name)
        current_router=network.routers[current_router].connection_to_source.name
    path.append(s)
    path=path[::-1]
    return (path_size,path)