import random
from rtpacket import RtPkt
from event import Event

LINKCHANGES = 1
FROM_LAYER2 = 2
LINK_CHANGE = 10

'''
THERE IS NO REASON THAT ANY STUDENT SHOULD MODIFY THE CODE BELOW THIS LINE.
'''

class SimulationStep:

    def __init__(self, evlist, TRACE, clocktime):
        self.evlist = evlist
        self.TRACE = TRACE
        self.clocktime = clocktime

    def creatertpkt(initrtpkt, srcid, destid, mincosts):
        initrtpkt.sourceid = srcid
        initrtpkt.destid = destid
        initrtpkt.mincost = [i for i in mincosts]


    def printevlist(self):
        print("--------------\nEvent List Follows:\n")
        for ev in self.evlist:
            print(f"Event {ev}")
        print("--------------\n")

    def jimsrand(self):
        return random.uniform(0,1)

    def init(self, nodes):
        random.seed(9999)
        sum = 0.0
        for _ in range(1000):
            sum += self.jimsrand()
        avg = sum / 1000.0
        
        if avg < 0.25 or avg > 0.75:
            print("It is likely that random number generation on your machine")
            print("is different from what this emulator expects.  Please take")
            print("a look at the routine jimsrand() in the emulator code. Sorry.")
            exit(0)
         
        for node in nodes:
            node.rtinit(self.TRACE, self.clocktime, self.tolayer2)

        # Initialize future link changes
        if LINKCHANGES == 1:
            evptr = Event(10000.0, LINK_CHANGE, -1, None)
            self.insertevent(evptr)
            evptr = Event(20000.0, LINK_CHANGE, 0, None)
            self.insertevent(evptr)


    # TOLAYER2
    def tolayer2(self, packet):
        evptr = Event()

        connectcosts = [[0, 1, 3, 7],
                    [1, 0, 1, 999],
                    [3, 1, 0, 2],
                    [7, 999, 2, 0]]
        
        # Check if the source and the destination ids are reasonable
        if packet.sourceid < 0 or packet.sourceid > 3:
            print("WARNING: illegal source id in your packet, ignoring packet")
            return
        if packet.destid < 0 or packet.destid > 3:
            print("WARNING: illegal destination id in your packet, ignoring packet")
            return
        if packet.sourceid == packet.destid:
            print("WARNING: source and destination ids are the same, ignoring packet")
            return
        if connectcosts[packet.sourceid][packet.destid] == 999:
            print("WARNING: no link between source and destination, ignoring packet")
            return
        
        # Create a copy of the packet given by the student
        mypktptr = RtPkt(packet.sourceid, packet.destid, packet.mincost)

        if self.TRACE > 2:
            print(f"TOLAYER2: {mypktptr}")

        # Create future event for arrival of packet at the other side
        # finally, compute the arrival time of packet at the other end.
        # medium can not reorder, so make sure packet arrives between 1 and 10
        # time units after the latest arrival time of packets
        # currently in the medium on their way to the destination
        lasttime = self.clocktime
        for ev in self.evlist:
            if ev.evtype == FROM_LAYER2 and ev.eventity == evptr.eventity:
                lasttime = max(lasttime, ev.evtime)
        evptr = Event(lasttime + 2*self.jimsrand(), FROM_LAYER2, packet.destid, mypktptr)

        if self.TRACE > 2:
            print("TOLAYER2: scheduling arrival on other side")
        self.insertevent(evptr)


    def insertevent(self, p):
        if self.TRACE > 3:
            print(f"INSERTEVENT: time is {self.clocktime}")
            print(f"INSERTEVENT: future time will be {p.evtime}")
        if len(self.evlist) == 0:
            self.evlist = [p]
        else:
            for i in range(0, len(self.evlist)):
                if self.evlist[i].evtime > p.evtime:
                    self.evlist.insert(i, p)
                    return
                if i == len(self.evlist) - 1:
                    self.evlist.append(p)
                    return
        