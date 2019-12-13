class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            #path = []
            current = current_node
            cost = 0
            while current is not None:
                #path.append(current.position)
                if (maze[current.position[0]][current.position[1]]==0):
                    cost+=1
                else:
                    cost+=3
                current = current.parent
            #return path[;;-1] here if needed
            return cost

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: #add diagonal stuff here
            
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze)-1) or node_position[1] < 0: #change this if matrix is not square
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:
            
            if child in closed_list:
                continue
            
            if maze[child.position[0]][child.position[1]]==1:
                child.g = current_node.g + 3 #weight
            else:
                child.g = current_node.g + 1 #weight
                
            child.h = (abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])) #manhattan distance
            child.f = child.g + child.h
            
            if child in open_list:
                if child.g > open_list[open_list.index(child)].g:
                    continue
                else:
                    open_list[open_list.index(child)] = child
            else:
                open_list.append(child)


size = int(input())
start = tuple([int(i) for i in input().split()])
end = tuple([int(i) for i in input().split()])

#creating maze
maze = [[0 for i in range(size)] for j in range(size)] 
for q in range(size):    
    t = input().split()
    for i in range(len(t)):
        if t[i] == 'X':
            maze[q][i]=1

path = astar(maze, start, end)
print(path-1)
