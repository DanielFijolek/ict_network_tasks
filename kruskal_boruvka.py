class Graph:

    def __init__(self, no_of_points):
        self.no = no_of_points
        self.array = []

    def addEdge(self, u, v, weight):
        self.array.append([u, v, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot

        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):

        result = []
        i = 0
        e = 0
        self.array = sorted(self.array, key=lambda item: item[2])

        parent = []
        rank = []
        for node in range(self.no):
            parent.append(node)
            rank.append(0)

        while e < self.no - 1:
            u, v, weight = self.array[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, weight])
                self.union(parent, rank, x, y)

        for u, v, weight in result:
            print("%d -- %d == %d" % (u+1, v+1, weight))

    def boruvkaMST(self):
        parent = []
        rank = []
        cheapest = []

        numTrees = self.no
        MSTweight = 0

        for node in range(self.no):
            parent.append(node)
            rank.append(0)
            cheapest = [-1] * self.no

        while numTrees > 1:

            for i in range(len(self.array)):

                u, v, weight = self.array[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:

                    if cheapest[set1] == -1 or cheapest[set1][2] > weight:
                        cheapest[set1] = [u, v, weight]

                    if cheapest[set2] == -1 or cheapest[set2][2] > weight:
                        cheapest[set2] = [u, v, weight]

            for node in range(self.no):

                if cheapest[node] != -1:
                    u, v, weight = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        MSTweight += weight
                        self.union(parent, rank, set1, set2)
                        print("Edge %d-%d with weight %d included in MST" %
                              (u+1, v+1, weight))
                        numTrees = numTrees - 1

            cheapest = [-1] * self.no

            print("Weight of MST is %d" % MSTweight)


g = Graph(5)
g.addEdge(0, 1, 1)
g.addEdge(0, 2, 2)
g.addEdge(0, 3, 2)
g.addEdge(0, 4, 6)
g.addEdge(1, 3, 4)
g.addEdge(1, 4, 5)
g.addEdge(2, 3, 3)
g.addEdge(3, 4, 3)

g.KruskalMST()
g.boruvkaMST()
