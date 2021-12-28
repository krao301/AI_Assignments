##Finding the maze path using A* searching algorithm

#Node class is a class for all the nodes used for A* path finding
#parent reprensts the parent node to the current node represented as (x,y)coordinates, position is also represented as (x,y) coordinates in the matrix
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 #g is the cost of moving from start node to current node
        self.h = 0 #h is heuristic function
        self.f = 0 #f(n) = g(n) + h(n)

    def __eq__(self, other):
        return self.position == other.position

#astarsearch is the function to 
def astarsearch(maze, start, end):
    #Returns a list of tuples as a path from the given start to the given end in the given maze

    # Create start and end node
    start_node = Node(None, start)#start node has no parent node, its coordinates are given as arguments
    #for start node g,h and f are initialised to zero as 
    start_node.g = 0 
    start_node.h = 0
    start_node.f = 0
    end_node = Node(None, end)#while initialising in the beginning the parent node of endnode is initialised to none and g,h,f are initialised to zero
    end_node.g = end_node.h = end_node.f = 0

    #open list and closed are priority queues maintained 
    #Initialize both open and closed list
    open_list = []
    closed_list = []

    #Add the start node to open list
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):#loop through the open list to find the node having f lesser than the current node
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = [] #list used to track the path, returned by the astarsearch function
            current = current_node
            while current is not None:
                path.append(current.position) # appends the current node
                current = current.parent # current keeps updating until there is no parent node left i.e. start node
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares i.e. left,right,bottom,up,(diagonally)left-down,left-up,right-down,right-up

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1]) 

            # Make sure node_position is within the range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)#here current node becomes the parent to the new node created

            # Append new_node to children list
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1 #cost of reaching child node is 1 greater than cost of reaching current node
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2) 
            #here hueristic function takes adjacency as measure i.e. nodes next to given node (left,right,bottom,up) have hueristic 1 and (diagonally)left-down,left-up,right-down,right-up) have hueristic 2  
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (8, 7)

    path = astarsearch(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()