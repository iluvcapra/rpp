class Marker:
    def __init__(self, rppxml):
        self.rppxml = rppxml

class Region:
    def __init__(self, rppxml1, rppxml2):
        self.start_marker = Marker(rppxml1)
        self.finish_marker = Marker(rppxml2)


