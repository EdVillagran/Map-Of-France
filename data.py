
class Map_Info(object):
    #store france_map, france_long, france_roads_no_weight
    def _init_(self):
        self.france_map=store_roads()
        self.france_long=store_longitudes()
        self.france_map_weightless=store_roads_without_weight()

    @staticmethod
    def store_roads_without_weight():
        fd = open('france-roads1.txt', 'r')
        file = fd.read()
        fd.close()
        #Empty dict to hold cities
        france_map={}
        for line in file.splitlines():
            if(line==''):
                continue
            elif(line[0]=='#'):
                continue
            else:
                if(line.isupper()):
                    city=line
                    city=city.lower()
                    s=len(city)
                    city=city[:s-1]
                else:
                    attatched_city=line.split()[0]
                    attatched_city=attatched_city.lower()
                
                    #If the city is already in france map
                    #Avoid replacing current and append
                    if (city in france_map.keys()):
                        france_map[city].add(attatched_city)

                    #It currently does not exist
                    else:
                        france_map[city]=set([attatched_city])
        return france_map

