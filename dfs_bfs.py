from visualization_pyplot import GraphVisualization

class Queue:

    def __init__(self):
        self.items = []

    def empty(self):
        if (len(self.items) == 0):
            return True
        else:
            return False
 
    def put(self, e):
         self.items.append(e)
 
    def get(self):
        head = self.items[0]
        self.items.remove(self.items[0])
        return head

    def print(self):
         print(self.items)

class Vertex:                        # dinh
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.color = "black"         # black: chua duyet, red: da duyet, blue: ngo cut
        self.visited = False
        self.parent = ""

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()

    def neighbors_input(self):
        n = int(input("Nhap so luong dinh ke: "))
        print("Nhap cac dinh ke: ")
        for i in range(0, n):
            element = input()
            self.add_neighbor(element)

class Graph:                         # do thi
    vertices = {}
    dfs_traversal_output = []
    bfs_traversal_output = []
    visualizing = GraphVisualization()

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
        
    def add_egde(self):
        for vertex in self.vertices:
            for neighbor in self.vertices[vertex].neighbors:
                self.visualizing.addEdge(vertex, neighbor)
            
    def graph_input(self):
        x = int(input("Nhap so luong dinh: "))
        for i in range(0, x):
            name = input("Dinh thu " + str(i+1) + ": ")
            v = Vertex(name)
            v.neighbors_input()
            self.add_vertex(v)
    
    def _dfs(self, vertex):
        global Stack
        global Step
        vertex.color = "red"

        print("--------------------------------------------------------------")
        print("STEP ", str(Step), " :")
        
        print("   Stack: ", end = " ")
        print(Stack)
        Stack.pop()
        print("   Path: ", end = " ")
        print(self.dfs_traversal_output)
        self.dfs_traversal_output.append(vertex.name)
    
        Step += 1

        for v in reversed(vertex.neighbors):
            if ((self.vertices[v].color == "black") and (v not in Stack)):
                Stack.append(v)
        
        for v in reversed(Stack):  
            self.vertices[v].parent = vertex.name
            self._dfs(self.vertices[v])
        vertex.color = 'blue'

    def dfs(self):
        global Step
        global Stack
        Step = 1
        
        print("\n\n--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("DEPTH-FIRST SEARCH")
        print("--------------------------------------------------------------")
        name = input("Chon dinh xuat phat cho DFS: ")
        Stack = [name]
        self._dfs(self.vertices[name])
        print("--------------------------------------------------------------")
        print("STEP ", str(Step), " :")
        
        print("   Stack: ", end = " ")
        print(Stack)
        print("   Path: ", end = " ")
        print(self.dfs_traversal_output)
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------\n\n")

    def _bfs(self, vertex):
        vertex.visited = True
        global queue
        global Step1

        while not queue.empty():  
            print("--------------------------------------------------------------")
            print("STEP ", str(Step1), " :")
            
            print("   Queue: ", end = " ")
            queue.print()
            u = queue.get()
            print("   Path: ", end = " ")
            print(self.bfs_traversal_output)
            self.bfs_traversal_output.append(u)
        
            Step1 += 1        

            for v in self.vertices[u].neighbors:
                if self.vertices[v].visited == False:
                    self.vertices[v].visited = True
                    self.vertices[v].parent = u
                    queue.put(v)
        
    def bfs(self):
        global queue 
        global Step1
        Step1 = 1
        queue = Queue()

        print("\n\n--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("BREADTH-FIRST SEARCH")
        print("--------------------------------------------------------------")
        name = input("Chon dinh xuat phat cho BFS: ")
        queue.put(name)

        self._bfs(self.vertices[name])
        print("--------------------------------------------------------------")
        print("STEP ", str(Step1), " :")
        
        print("   Queue: ", end = " ")
        queue.print()
        print("   Path: ", end = " ")
        print(self.bfs_traversal_output)
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------\n\n")

def main():
    graph = Graph()
    graph.graph_input()
    graph.add_egde()

    graph.dfs()

    graph.bfs()
    
    graph.visualizing.visualize()

if __name__ == "__main__":
    main()