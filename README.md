# Map of France

Map_of_France takes two cities as command line arguments and uses various search algorithms to find best path.<br>
Search Algorithms used: A*, BFS, DFS, DFID.<br>
Program is ran by ./france_map.py start goal


## Purpose

I wanted to explore how various algorithims work compared to each other. My main focus on this was A*, and getting to learn more about informed search algorithms and the use of heuristic functions. I wanted to use this as an introduction to expanding my knowledge in python and start to dive more into AI related topics.

## File Descriptions
Node.py:          Contains the Node class used to represent each city for A*.<br>
data.py           Stores the cities into a dictionary without the distances.<br>
france-long1.txt 	Contains the longitudes for each city. <br>
france-roads1.txt Contains each city, its connections, and distances to each one.<br>
france2.pdf 	    PDF of the map with cities and distances I used.<br>
france_map.py     Program ran to calculate best path using various search methods.<br>
