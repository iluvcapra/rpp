class Source:
    def __init__(self, rppxml):
        pass

    @property
    def kind(self):
        return self.attrib[0]

    @property
    def file(self):
        return self.rppxml.find('FILE')[1]
