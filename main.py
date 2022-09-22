from layer2 import SimulationStep
import node as nd

LINKCHANGES = 1
FROM_LAYER2 = 2
LINK_CHANGE = 10



'''
Programming assignment 3: implementing distributed, asynchronous,
                          distance vector routing.

THIS IS THE MAIN ROUTINE.  IT SHOULD NOT BE MODIFIED AT ALL BY STUDENTS!
'''

'''
NETWORK EMULATION CODE STARTS BELOW.
The code below emulates the layer 2 and below network environment:
  - emulates the tranmission and delivery (with no loss and no
    corruption) between two physically connected nodes
  - calls the initializations routines rtinit0, etc., once before
    beginning emulation

'''

def creatertpkt(initrtpkt, srcid, destid, mincosts):
    initrtpkt.sourceid = srcid
    initrtpkt.destid = destid
    initrtpkt.mincost = [i for i in mincosts]


def printevlist(evlist):
    print("--------------\nEvent List Follows:\n")
    for ev in evlist:
        print(f"Event {ev}")
    print("--------------\n")

def main():
    # Initialize the global variables
    TRACE = 0
    clocktime = 0.0
    evlist = []

    print("Enter TRACE")
    TRACE = int(input())

    # Creating objects for all nodes
    node0 = nd.Node0()
    node1 = nd.Node1()
    node2 = nd.Node2()
    node3 = nd.Node3()
    nodes = [node0, node1, node2, node3]

    ss = SimulationStep(evlist, TRACE, clocktime)
    ss.init(nodes)
    evlist = ss.evlist
    
    while True:
        eventptr = evlist
        if len(eventptr) == 0:
            print(f"Simulator terminated at {clocktime}, no packets in medium")
            break
        
        eventptr = evlist.pop(0)
        if TRACE > 1:
            print(f"MAIN: rcv event, {eventptr}")
        clocktime = eventptr.evtime
        if eventptr.evtype == FROM_LAYER2:
            assert eventptr.eventity < len(nodes), "Panic: unknown event entity"
            ly2 = SimulationStep(evlist, TRACE, clocktime)
            nodes[eventptr.eventity].rtupdate(eventptr.packetObj, TRACE, ly2.tolayer2)
            evlist = ly2.evlist
        elif eventptr.evtype == LINK_CHANGE:
            if clocktime < 10001.0:
                nodes[0].linkhandler(1, 20)
                nodes[1].linkhandler(0, 20)
            else:
                nodes[0].linkhandler(1, 1)
                nodes[1].linkhandler(0, 1)

        else:
            print("Panic: unknown event type")
            exit(0)
        
if __name__ == '__main__':
    main()