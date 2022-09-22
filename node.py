from rtpacket import RtPkt

class Node0:
    def __init__(self):
        self.costs = [[-1 for _ in range(4)] for _ in range(4)]

    # The following two functions must be completed by the students and if required some others as well
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    
    def rtinit(self, TRACE: int, clocktime: float, tolayer2: callable(RtPkt)):
        return "To be Completed"
    
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtupdate(self, rcvdpkt: RtPkt, TRACE: int, tolayer2: callable(RtPkt)):
        return "To be Completed"

    def printdt(self):
        print("                via     ")
        print("   D0 |    1     2    3 ")
        print("  ----|-----------------")
        print("     1|  {:3d}   {:3d}   {:3d}".format(self.costs[1][1], self.costs[1][2], self.costs[1][3]))
        print("dest 2|  {:3d}   {:3d}   {:3d}".format(self.costs[2][1], self.costs[2][2], self.costs[2][3]))
        print("     3|  {:3d}   {:3d}   {:3d}".format(self.costs[3][1], self.costs[3][2], self.costs[3][3]))

    """
    Called when cost from 0 to linkid changesfrom current value to newcost.
    You can leave this routine empty if you are an undergrad.
    If you want to use the routine, change the LINKCHANGE constant from 0 to 1.
    """
    def linkhandler(self, linkid: int, newcost: int):
        return "To be Completed"

class Node1:
    def __init__(self):
        self.connectcosts1 = [1, 0, 1, 999]
        self.costs = [[-1 for _ in range(4)] for _ in range(4)]

    # The following two functions and maybe more must be written by the students
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtinit(self, TRACE: int, clocktime: float, tolayer2: callable(RtPkt)):
        return "To be completed"
    
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtupdate(self, rcvdpkt: RtPkt, TRACE: int, tolayer2: callable(RtPkt)):
        return "To be Completed"
    
    def printdt(self):  
        print("             via   ")
        print("   D1 |    0     2 ")
        print("  ----|------------")
        print("     0|  {:3d}   {:3d}".format(self.costs[0][0], self.costs[0][2]))
        print("dest 2|  {:3d}   {:3d}".format(self.costs[2][0], self.costs[2][2]))
        print("     3|  {:3d}   {:3d}".format(self.costs[3][0], self.costs[3][2]))

    """
    Called whne cost from 0 to linkid changesfrom current value to newcost.
    You can leave this routine empty if you are an undergrad.
    If you want to use the routine, change the LINKCHANGE constant from 0 to 1.
    """
    def linkhandler(self, linkid: int, newcost: int):
        return "To be Completed"

class Node2:
    def __init__(self):
        self.costs = [[-1 for _ in range(4)] for _ in range(4)]

    # The following two functions and maybe more must be written by the students
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtinit(self, TRACE: int, clocktime: float, tolayer2: callable(RtPkt)):
        return "To be completed"

    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtupdate(self, rcvdpkt: RtPkt, TRACE: int, tolayer2: callable(RtPkt)):
        return "To be Completed"
    
    def printdt(self):  
        print("                via     ")
        print("   D2 |    0     1    3 ")
        print("  ----|-----------------")
        print("     0|  {:3d}   {:3d}   {:3d}".format(self.costs[0][0], self.costs[0][1], self.costs[0][3]))
        print("dest 1|  {:3d}   {:3d}   {:3d}".format(self.costs[1][0], self.costs[1][1], self.costs[1][3]))
        print("     3|  {:3d}   {:3d}   {:3d}".format(self.costs[3][0], self.costs[3][1], self.costs[3][3]))

class Node3:
    def __init__(self):
        self.costs = [[-1 for _ in range(4)] for _ in range(4)]

    # The following two functions and maybe more must be written by the students
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtinit(self, TRACE, clocktime, tolayer2):
        return "To be completed"
    
    # NOTE: tolayer2 is a function that sends a packet to layer 2
    #       input for tolayer2 is a packet object of type RtPkt
    def rtupdate(self, rcvdpkt: RtPkt, TRACE: int, tolayer2: callable(RtPkt)):
        return "To be Completed"

    def printdt(self):
        print("             via  ")
        print("   D3 |    0     2")
        print("  ----|-----------")
        print("     0|  {:3d}   {:3d}".format(self.costs[0][0], self.costs[0][2]))
        print("dest 1|  {:3d}   {:3d}".format(self.costs[1][0], self.costs[1][2]))
        print("     2|  {:3d}   {:3d}".format(self.costs[2][0], self.costs[2][2]))


