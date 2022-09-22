'''
THERE IS NO REASON THAT ANY STUDENT SHOULD MODIFY THE CODE BELOW THIS LINE.
'''

class RtPkt:
    def __init__(self, sourceid, destid, mincost):
        self.sourceid = sourceid
        self.destid = destid
        self.mincost = mincost
    
    def __str__(self):
        ret =  f"source:{self.sourceid}, dest:{self.destid}, cost:"
        for i in self.mincost:
            ret += f"{i:3d} " 
        ret += "\n"
        return ret