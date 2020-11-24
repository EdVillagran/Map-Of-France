
class Node(object):
    position = {}
    connection = {}

    def __init__(self, name, g, parent=None):
        self.name = name
        self.parent = parent
        self.g = g
        self.f = None

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):

        return str(self).__hash__()

    def __repr__(self):

       return str(self)

    #H=0
    def h0(self, final_values):
        return 0

    #H= EAST-WEST DISTANCE
    def h1(self, final_values):
        return abs(int(self.position[final_values]) - int(self.position[self.name]))

    h = {
        0: h0,
        1: h1,

    }

    def get_neighbors(self):
        ops = []
        for city, cost in Node.connection[self.name].items():
            ops.append((city, cost))

        return ops

    def add_g(self, op):
        return Node(op[0], int(op[1]) + self.g, self)

    def distance(self, final_values, methode):
        self.f = self.h[methode](self, final_values) + self.g
        return self.f


    @staticmethod
    def store_roads():
        fd = open('france-roads1.txt', 'r')
        file = fd.read()
        fd.close()
        # Empty dict to hold cities
        Node.connection = {}
        for line in file.splitlines():
            if (line == ''):
                continue
            elif (line[0] == '#'):
                continue
            else:
                if (line.isupper()):
                    city = line
                    city = city.lower()
                    s = len(city)
                    city = city[:s - 1]
                else:
                    attatched_city = line.split()[0]
                    attatched_city = attatched_city.lower()
                    distance = line.split()[1]

                    # If the city is already in france map
                    # Avoid replacing current and append
                    if (city in Node.connection.keys()):
                        Node.connection[city].update({attatched_city: distance})

                    # It currently does not exist
                    else:
                        Node.connection[city] = {attatched_city: distance}


    @staticmethod
    def store_longitudes():
        fd = open('france-long1.txt', 'r')
        file = fd.read()
        fd.close()
        # Empty dict to hold longitudes

        Node.position = {}

        for line in file.splitlines():

            if (line == ''):
                continue
            elif (line[0] == '#'):
                continue
            else:
                city = line.split()[0]
                city = city.lower()
                long = line.split()[1]

                Node.position.update({city: long})
