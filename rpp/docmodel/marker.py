class Marker:
    def __init__(self, rppxml):
        self.rppxml = rppxml

    @property
    def is_marker(self):
       return True

    @property
    def is_region(self):
       return False

class Region:
    def __init__(self, rppxml1, rppxml2):
        self.start_marker = Marker(rppxml1)
        self.finish_marker = Marker(rppxml2)

    @property
    def is_marker(self):
        return False

    @property
    def is_region(self):
        return True
