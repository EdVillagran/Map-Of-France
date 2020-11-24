#!/usr/bin/env python3
from data import *
from Node import Node
from collections import deque
import sys

'''

Program Purpose: Use BFS,DFS,DFID & A*Search Algorithms
        to find path from start to goal city in France.
        -Program is ran by ./Map_of_France.py  start  goal
'''

'''
bfs(Breadth-First-Search)
Parameters: start & goal cities
Purpose: find goal city using BFS algorithm
'''
def bfs(start, goal):
    Map=Map_Info()
    france_map=Map.store_roads_without_weight()

    #nodes Opened flag
    count=0

    #bfs uses a queue instead of a stack like dfs
    #initiating variables to use
    closed = {start}
    open = deque([(start, [])])
    New_children=[]
    children=[]

    #While open list isnt empty
    while open:
        #add current, path from open list
        current, path = open.popleft()

        #Display new children while there is some
        if len(New_children) != 0:
            print("New Children are (",*New_children,")")
            #Clear New children list for next round
            New_children.clear()

        #Display all children
        if len(children)!=0:
            print("Children are (",*children,")")
            #Clear all children from list for next round
            children.clear()

        #Print output
        print("\nExpanding",current)
        print("Closed list is (", *closed,")")

        #add current to closed
        closed.add(current)

        #for each neighbor of current city
        for neighbor in france_map[current]:

            #If neighbor is goal display nodes and full path
            if neighbor == goal:
                print("\nNodes Opened",count)
                return path + [current, neighbor]

            #If in closed add to children of it
            if neighbor in closed:
                children.append(neighbor)
                continue
            #add neighbor and path list to open
            open.append((neighbor, path + [current]))

            #increase node opened flag
            count+=1

            #if neighbor not in closed then add to children and new children
            if neighbor not in closed:
               children.append(neighbor)
               New_children.append(neighbor)

            #add neighbor to closed
            closed.add(neighbor)
        #print open list
        print("Open list is (", *[x for x,y in open],")")

    #Return no path found
    return None

'''
dfs(depth-first-search)
Parameters: start & goal cities
Purpose: find goal city using DFS algorithm
'''

def dfs(start, goal):
    #Dfs uses a stack instead of queue
    Map=Map_Info()
    OPEN = [(start, [start])]
    france_map=Map.store_roads_without_weight()
    CLOSED = set()
    countNodes=0

    while OPEN:

        (node, path) = OPEN.pop()



        if node not in CLOSED:
            #increase nodes opened flag
            countNodes+=1

            #if goal then return path and print nodes expanded
            if node == goal:
                print("\n",countNodes, "nodes expanded.")
                return path

            #add current to closed
            CLOSED.add(node)

            #for each neighbor add neighbor and path to neighbor to open
            for neighbor in france_map[node]:
                OPEN.append((neighbor, path + [neighbor]))

            #print output
            print("\nExpanding", node)
            print("Children are (",*[x for x in france_map[node]],")")
            print("New children are (",*[x for x in france_map[node] if x not in CLOSED],")")
            print("Open list is (", *{x for x,y in OPEN},")")
            print("Closed list is (",*CLOSED,")")


'''
 dfs_for_DFID
 Parameters: start & goal cities, max depth to reach
 Purpose: This Seperate DFID function is used for the DFID search.
        Unlike the regular DFID, it only goes up to the max depth
        given each time.

'''

def dfs_for_DFID(start, goal,depth):
    #Works just like my dfs, but only extends up to certain depth

    Map=Map_Info()
    #Necessary variables
    france_map=Map.store_roads_without_weight()
    level=0
    OPEN = [(start, [start])]
    pathlevel=[]
    CLOSED = set()
    countNodes=0
    current_depth=0

    while OPEN:

        while current_depth<=depth:

            (vertex, path) = OPEN.pop()


            if vertex not in CLOSED:
                countNodes+=1
                pathlevel.append((vertex,level))

                if vertex == goal:
                    print("\nNodes opened:",countNodes)
                    return path

                CLOSED.add(vertex)


                for neighbor in france_map[vertex]:
                    OPEN.append((neighbor, path + [neighbor]))


                #Print all the information

                print("\n\nExpanding", vertex)

                print("Open list", end=' ' )
                #Print output
                if OPEN== None:
                    print("None")
                for nodes in {x for x,y in OPEN}:
                    for nodes2 in pathlevel:
                        if nodes==nodes2[0]:
                            print(nodes2, end=' ')

                print("\nClosed list is", end=' ')
                if CLOSED== None:
                    print("None")
                for nodes in CLOSED:
                    for nodes2 in pathlevel:
                        if nodes==nodes2[0]:
                            print(nodes2, end=' ')

                print("\nChildren are ",end=' ')
                for nodes in [x for x in france_map[vertex]]:
                    for nodes2 in pathlevel:
                        if nodes==nodes2[0]:
                            print(nodes2, end=' ')

                print ("\nNew Children are (",*[x for x in france_map[vertex] if x not in CLOSED],")")
                current_depth+=1
                level+=1

        print("\nDepth has been reached\n")
        break



'''
DFID(Depth-First-Iterative-Deepening)
Parameters: start & goal cities, and max depth to reached
Purpose: Use DFS to a certain layer each time until goal is Found.
        Returns the path found.
'''
def DFID(start, goal, depth):

    for d in range(0, depth):
        print("\nDFID LEVEL:",d)
        result = dfs_for_DFID(start, goal, d+1)
        if result is None:
            continue
        else:
            print("DFID Path Found:",result)
            print("Used depth ",d)

'''
Astar
Parameters: start & goal cities, a heuristic value
Purpose: A* being an informed search, uses a heuristic
        value to make each step more optimal towards reaching
        the goal. It does so by not expanding cities that are
        already expensive. The logic for the code used is from
        the text rich-astar2.pdf provided in class.
'''

def Astar(start, goal, h):
    #Step 1
    # 1. Start with OPEN List containing only the initial node.
    # 2. Set CLOSED to an empty List
    OPEN = [start]
    CLOSED = []


    #STEP2 Repeat until GOAL found.
    # 1. If no nodes in OPEN report failure
    while OPEN:

        #node equal first in OPEN
        node = OPEN.pop()
        print(node)
        #add node to Closed
        CLOSED.append(node.name)

        #if the node is final
        if node==goal:
            return node, len(CLOSED)

        #gather all neighbors to current node
        neighbors = node.get_neighbors()

        #View each successor of node
        for SUCCESSOR in neighbors:

            #Compute BESTNODE=g(SUCCESSOR)
            BESTNODE = node.add_g(SUCCESSOR)

            #See if its not currently in OPEN or CLOSED
            if (BESTNODE.name not in CLOSED) and (BESTNODE not in OPEN):

                #Add to OPEN if both are true
                OPEN.insert(0, BESTNODE)

            #If it is in OPEN then
            if (BESTNODE in OPEN):
                #Compare that nodes g to see if its the cheapest successor
                if OPEN[OPEN.index(BESTNODE)].g > BESTNODE.g:
                    #If so set it to the new path
                    OPEN[OPEN.index(BESTNODE)] = BESTNODE
        #Sort it to the order from start to finish and for each claculate
        #the h value
        OPEN.sort(key=lambda node: node.distance(goal, h), reverse=True)

        #print required output
        print("Expanding",node,"f=",node.f,", g=",node.g,", h=",node.g)
        print("Children are:(",*[x[0] for x in neighbors],")")
        print("OPEN:",*OPEN)
        print("CLOSED:",*CLOSED,'\n')



    return None
#Prints the A* path , path length, nodes expanded as long as solution found
def printAstar(result, visited):
    if result is not None:

        nodes = []
        while result.parent is not None:
            nodes.append(result)
            result = result.parent

        nodes.append(result)
        nodes.reverse()

        print("Path:",*nodes)
        print("Path length:",nodes[-1].g)
        print("" + str(visited) + " Nodes expanded.\n")
    else:
        print('solution not found')




if __name__ == "__main__":

    if len(sys.argv) !=3:
        print("Incorrect # of arguments")
        print("Correct: ./program startCity goalCity")

    else:
        start = sys.argv[1]
        goal = sys.argv[2]

        start=start.lower()
        goal=goal.lower()

        Node.store_longitudes();
        Node.store_roads();


        print("BFS")
        path = bfs(start, goal)
        print("Breath-first search solution:",*path)


        print("\nDFS\n")
        dfs_solution=list(dfs(start, goal))
        print("Depth-first search solution:",*dfs_solution,'\n')
        
        print("\nDFID\n")
        print(DFID(start, goal, 10))

        print("\nAstar with H=0\n")
        result = Astar(Node(start, 0), goal, 0)
        print("\n\nA-star-search solution with H=0")
        printAstar(result[0], result[1])

        print("\nAstar with H=EAST - WEST DISTANCE\n")
        result = Astar(Node(start, 0), goal, 1)
        print("\n\nA-star-search solution with H=EAST-WEST DISTANCE")
        printAstar(result[0], result[1])
