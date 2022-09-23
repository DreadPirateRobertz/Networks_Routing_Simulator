from rtpacket import RtPkt

class Node0:
    def __init__(self):
        # Changed -1 to 999, because of connectcosts in layer2.py because 999 indicates no connection
        self.costs = [[999 for _ in range(4)] for _ in range(4)]
        self.minCost = []

    # The following two functions must be completed by the students and if required some others as well
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt

    def getMinCosts(self):
        minCost = [999 for i in range(4)]

        for i in range(4):
            for j in range(4):
                if(minCost[i] > self.costs[i][j]):
                    minCost[i] = self.costs[i][j]
        
        return minCost

    
    def rtinit(self, TRACE: int, clocktime: float, tolayer2: callable(RtPkt)):
        # Initalize the distance table (i.e., the costs matrix)
        self.costs[0][0] = 0
        self.costs[1][1] = 1
        self.costs[2][2] = 3
        self.costs[3][3] = 7

        # Get mincost list
        self.minCost = self.getMinCosts()
        

        # Send packets to 1,2,3 with mincost.
        for i in range(3):
            rtPkt = RtPkt(sourceid=0, destid=i+1, mincost=self.minCost)
            tolayer2(rtPkt)

        # Print the table w/ what is happening
        print("Node 0 Initalization")
        self.printdt()
    
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtupdate(self, rcvdpkt: RtPkt, TRACE: int, tolayer2: callable(RtPkt)):
        # Get ID of which packet this came from
        srcId = rcvdpkt.sourceid
        for i in range(4):
            # Update columns with formula from textbook
            self.costs[i][srcId] = rcvdpkt.mincost[i] + self.minCost[srcId]
        
        # Array to store smallest value in each row from updated distance table
        p0MinCosts = [999 for i in range(4)]
        for x in range(4):
            for y in range(4):
                if(self.costs[x][y] < p0MinCosts[x]):
                    p0MinCosts[x] = self.costs[x][y]
        
        # Check if updated packets need to be sent
        needUpdate = False
        for i in range(4):
            if p0MinCosts[i] < self.minCost[i]:
                # Min cost array has changed so send
                self.minCost[i]=p0MinCosts[i] 
                needUpdate = True

        # Send updated packet to 1,2,3 with new mincost
        if needUpdate:
            for i in range(3):
                rtP = RtPkt(sourceid=0, destid=i+1, mincost=self.minCost)
                tolayer2(rtP)
            print(f"Sending Node {rcvdpkt.destid} updates with Mincost of = ", self.minCost)
        self.printdt()

    def printdt(self):
        print("                via     ")
        print("   D0 |    1     2    3 ")
        print("  ----|-----------------")
        print("     1|  {:3d}   {:3d}   {:3d}".format(self.costs[1][1], self.costs[1][2], self.costs[1][3]))
        print("dest 2|  {:3d}   {:3d}   {:3d}".format(self.costs[2][1], self.costs[2][2], self.costs[2][3]))
        print("     3|  {:3d}   {:3d}   {:3d}".format(self.costs[3][1], self.costs[3][2], self.costs[3][3]))
        print()

    """
    Called when cost from 0 to linkid changesfrom current value to newcost.
    You can leave this routine empty if you are an undergrad.
    If you want to use the routine, change the LINKCHANGE constant from 0 to 1.
    """
    def linkhandler(self, linkid: int, newcost: int):
        # lol no
        return "To be Completed"

class Node1:
    def __init__(self):
        self.connectcosts1 = [1, 0, 1, 999]
        # Changed -1 to 999, because of connectcosts in layer2.py because 999 indicates no connection
        self.costs = [[999 for _ in range(4)] for _ in range(4)]
        self.minCost = []
    
    def getMinCosts(self):
        minCost = [999 for i in range(4)]

        for i in range(4):
            for j in range(4):
                if(minCost[i] > self.costs[i][j]):
                    minCost[i] = self.costs[i][j]
        
        return minCost

    # The following two functions and maybe more must be written by the students
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtinit(self, TRACE: int, clocktime: float, tolayer2: callable(RtPkt)):
        # Initalize the distance table (i.e., the costs matrix)
        self.costs[0][0] = self.connectcosts1[0]
        self.costs[1][1] = self.connectcosts1[1]
        self.costs[2][2] = self.connectcosts1[2]
        self.costs[3][3] = self.connectcosts1[3]

        # Get mincost list
        self.minCost = self.getMinCosts()

        # Send packets to 0 and 2 with mincost.
        for i in range(4):
            if i == 1 or i == 3:
                continue
            rtPkt = RtPkt(sourceid=1, destid=i, mincost=self.minCost)
            tolayer2(rtPkt)

        # Print the table w/ what is happening
        print("Node 1 Initalization")
        self.printdt()




    
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtupdate(self, rcvdpkt: RtPkt, TRACE: int, tolayer2: callable(RtPkt)):
         # Get ID of which packet this came from
        srcId = rcvdpkt.sourceid
        for i in range(4):
            # Update columns with formula from textbook
            self.costs[i][srcId] = rcvdpkt.mincost[i] + self.minCost[srcId]
        

        # Array to store smallest value in each row from updated distance table
        p1MinCosts = [999 for i in range(4)]
        for x in range(4):
            for y in range(4):
                if(self.costs[x][y] < p1MinCosts[x]):
                    p1MinCosts[x] = self.costs[x][y]
        
        # Check if updated packets need to be sent
        needUpdate = False
        for i in range(4):
            if p1MinCosts[i] < self.minCost[i]:
                self.minCost[i]=p1MinCosts[i] 
                needUpdate = True

        # Send updated packet to 1,2,3 with new mincost
        if needUpdate:
            # Send packets to 0 and 2 with mincost.
            for i in range(4):
                if i == 1 or i == 3:
                    continue
                rtP = RtPkt(sourceid=1, destid=i, mincost=self.minCost)
                tolayer2(rtP)
            print(f"Sending Node {rcvdpkt.destid} updates with Mincost of = ", self.minCost)
        self.printdt()
    
    def printdt(self):  
        print("             via   ")
        print("   D1 |    0     2 ")
        print("  ----|------------")
        print("     0|  {:3d}   {:3d}".format(self.costs[0][0], self.costs[0][2]))
        print("dest 2|  {:3d}   {:3d}".format(self.costs[2][0], self.costs[2][2]))
        print("     3|  {:3d}   {:3d}".format(self.costs[3][0], self.costs[3][2]))
        print()

    """
    Called whne cost from 0 to linkid changesfrom current value to newcost.
    You can leave this routine empty if you are an undergrad.
    If you want to use the routine, change the LINKCHANGE constant from 0 to 1.
    """
    def linkhandler(self, linkid: int, newcost: int):
        return "To be Completed"

class Node2:
    def __init__(self):
        # Changed -1 to 999, because of connectcosts in layer2.py because 999 indicates no connection
        self.costs = [[999 for _ in range(4)] for _ in range(4)]
        self.minCost = []
    
    def getMinCosts(self):
        minCost = [999 for i in range(4)]

        for i in range(4):
            for j in range(4):
                if(minCost[i] > self.costs[i][j]):
                    minCost[i] = self.costs[i][j]
        
        return minCost

    # The following two functions and maybe more must be written by the students
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtinit(self, TRACE: int, clocktime: float, tolayer2: callable(RtPkt)):
        # Initalize the distance table (i.e., the costs matrix)
        self.costs[0][0] = 3
        self.costs[1][1] = 1
        self.costs[2][2] = 0
        self.costs[3][3] = 2

        # Get mincost list
        self.minCost = self.getMinCosts()

        

        # Send packets to 0,1,3 with mincost.
        for i in range(4):
            if i == 2:
                continue
            rtPkt = RtPkt(sourceid=2, destid=i, mincost=self.minCost)
            tolayer2(rtPkt)

        # Print the table w/ what is happening
        print("Node 2 Initalization")
        self.printdt()

    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtupdate(self, rcvdpkt: RtPkt, TRACE: int, tolayer2: callable(RtPkt)):
        # Get ID of which packet this came from
        srcId = rcvdpkt.sourceid
        for i in range(4):
            # Update columns with formula from textbook
            self.costs[i][srcId] = rcvdpkt.mincost[i] + self.minCost[srcId]
        
        # Array to store smallest value in each row from updated distance table       
        p2MinCosts = [999 for i in range(4)]
        for x in range(4):
            for y in range(4):
                if(self.costs[x][y] < p2MinCosts[x]):
                    p2MinCosts[x] = self.costs[x][y]
        
        # Check if updated packets need to be sent
        needUpdate = False
        for i in range(4):
            if p2MinCosts[i] < self.minCost[i]:
                self.minCost[i]=p2MinCosts[i] 
                needUpdate = True

        # Send updated packet to 0,1,3 with new mincost
        if needUpdate:
            for i in range(4):
                if i == 2:
                    continue
                rtP = RtPkt(sourceid=2, destid=i, mincost=self.minCost)
                tolayer2(rtP)
            print(f"Sending Node {rcvdpkt.destid} updates with Mincost of = ", self.minCost)
        self.printdt()
        
    
    def printdt(self):  
        print("                via     ")
        print("   D2 |    0     1    3 ")
        print("  ----|-----------------")
        print("     0|  {:3d}   {:3d}   {:3d}".format(self.costs[0][0], self.costs[0][1], self.costs[0][3]))
        print("dest 1|  {:3d}   {:3d}   {:3d}".format(self.costs[1][0], self.costs[1][1], self.costs[1][3]))
        print("     3|  {:3d}   {:3d}   {:3d}".format(self.costs[3][0], self.costs[3][1], self.costs[3][3]))
        print()

class Node3:
    def __init__(self):
        # Changed -1 to 999, because of connectcosts in layer2.py because 999 indicates no connection
        self.costs = [[999 for _ in range(4)] for _ in range(4)]
        self.minCost = []
    
    def getMinCosts(self):
        minCost = [999 for i in range(4)]

        for i in range(4):
            for j in range(4):
                if(minCost[i] > self.costs[i][j]):
                    minCost[i] = self.costs[i][j]
        
        return minCost

    # The following two functions and maybe more must be written by the students
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtinit(self, TRACE, clocktime, tolayer2):
        # Initalize the distance table (i.e., the costs matrix)
        self.costs[0][0] = 7
        self.costs[1][1] = 999
        self.costs[2][2] = 2
        self.costs[3][3] = 0

        # Get mincost list
        self.minCost = self.getMinCosts()

        
        # Send packets to 0,2 with mincost.
        for i in range(3):
            if i == 1:
                continue
            rtPkt = RtPkt(sourceid=3, destid=i, mincost=self.minCost)
            tolayer2(rtPkt)

        # Print the table w/ what is happening
        print("Node 3 Initalization")
        self.printdt()
    
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtupdate(self, rcvdpkt: RtPkt, TRACE: int, tolayer2: callable(RtPkt)):
        # Get ID of which packet this came from
        srcId = rcvdpkt.sourceid
        for i in range(4):
            # Update columns with formula from textbook
            self.costs[i][srcId] = rcvdpkt.mincost[i] + self.minCost[srcId]
        
        # Array to store smallest value in each row from updated distance table
        p3MinCosts = [999 for i in range(4)]
        for x in range(4):
            for y in range(4):
                if(self.costs[x][y] < p3MinCosts[x]):
                    p3MinCosts[x] = self.costs[x][y]
        # Check if updated packets need to be sent
        needUpdate = False
        for i in range(4):
            if p3MinCosts[i] < self.minCost[i]:
                # Min cost array has changed so send
                self.minCost[i]=p3MinCosts[i] 
                needUpdate = True
    
        # Send updated packet to 0,2 with new mincost
        if needUpdate:
            for i in range(3):
                if i == 1:
                    continue
                rtP = RtPkt(sourceid=3, destid=i, mincost=self.minCost)
                tolayer2(rtP)
            print(f"Sending Node {rcvdpkt.destid} updates with Mincost of = ", self.minCost)
        self.printdt()

    def printdt(self):
        print("             via  ")
        print("   D3 |    0     2")
        print("  ----|-----------")
        print("     0|  {:3d}   {:3d}".format(self.costs[0][0], self.costs[0][2]))
        print("dest 1|  {:3d}   {:3d}".format(self.costs[1][0], self.costs[1][2]))
        print("     2|  {:3d}   {:3d}".format(self.costs[2][0], self.costs[2][2]))
        print()


