class FadeDescriptor
    """
    The descriptor has six parameters:
       FADEIN | FADEOUT
    1: TYPE = 0 | 1 | 2 | 3 | 4 | 5 | 5.1
    2: LENGTH = float
    3: ?
    4: TYPE
    5:
    6: CURVE_XOVER = float (zero is the midpoint)
    
    Fade Types
    ----------
    0 seems to be equal gain
    1 seems to be equal power
    2 seems to be equal gain (but selecting it sets the XOVER to +1.0)
    3 seems to be equal gain (but selecting it sets the XOVER to -1.0)
    4 seems to be quadratic?
    5 seems to be cosine?
    5.1 seems to be square of cosine? 
    """
    def __init__(self, rppxml):
        "Create a FadeDescriptor"
        self.rppxml = rppxml

    @property 
    def fadein(self):
        return self.rppxml[0] == 'FADEIN'

    @property
    def fadeout(self):
        return self.rppxml[0] == 'FADEOUT'

    @property
    def fade_length(self):
        return float(self.rppxml[2]) 

    @property
    def fade_shape(self):
        return self.rppxml[1]

    @property
    def fade_crossover_point(self):
        return float(self.rppxml[6])
