'''
 THERE IS NO REASON THAT ANY STUDENT SHOULD MODIFY THE CODE BELOW THIS LINE.
'''

FROM_LAYER2 = 2

class Event:
    def __init__(self, evtime= 0.0, evtype= 0, eventity = 0, packetObj = None):
        self.evtime = evtime
        self.evtype = evtype
        self.eventity = eventity
        self.packetObj = packetObj
    
    def __str__(self):
        ret =  f"t: {self.evtime:.3f}, at {self.eventity}"
        if self.evtype == FROM_LAYER2:
            ret += f" source {self.packetObj.sourceid:2d}"  
            ret += f" dest {self.packetObj.destid:2d}"
            ret += f" contents: "    
            for i in self.packetObj.mincost:
                ret += f"{i:3d} "
            ret += "\n"
        return ret