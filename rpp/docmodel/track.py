from .item import Item 

class Track:
    
    def __init__(self, rppxml):
        """
        Create a track object for the given rppxml
        """
        self.rppxml = rppxml

    @property
    def uuid(self):
        """
        The Track UUID.
        """
        return self.rppxml.attrib[0]

    @property
    def name(self):
        """
        The Track name.
        """
        return self.rppxml.find('NAME')[1]

    @property
    def solo(self):
        """
        Solo state, True or False.
        """
        value = self.rppxml.find('MUTESOLO')[2]
        return value == '2'

    @property
    def mute(self):
        """
        Muted state, True or False.
        """
        value = self.rppxml.find('MUTESOLO')[1]
        return value == '1'

    @property
    def items(self):
        """
        Iterate through each media item on this track.
        """
        for item in self.rppxml.findall('ITEM'):
            yield Item(item)

