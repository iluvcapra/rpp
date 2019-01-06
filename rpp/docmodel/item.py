class Item:

    def __init__(self, rppxml):
        """
        Create an Item object from rppxml.
        """
        self.rppxml = rppxml

    @property
    def position(self):
        "Start of this clip, in seconds."
        return float(self.rppxml.find('POSITION')[1])

    @property
    def length(self):
        "Length of this clip, in seconds."
        return float(self.rppxml.find('LENGTH')[1])

    @property
    def start_offset(self):
        "Start offset in source."
        return float(self.rppxml.find('SOFFS')[1])

    @property
    def loop(self):
        "Looped option, True or False."
        return self.rppxml.find('LOOP')[1] == '1'

    @property
    def mute(self):
        "Mute state, True or False."
        return self.rppxml.find('MUTE')[1] == '1'

    @property
    def name(self):
        "Item name."
        return self.rppxml.find('NAME')[1]

    @property
    def fade_in(self):
        ":class:`rpp.docmodel.fade_descriptor.FadeDescriptor` for clip's fade in."
        return FadeDescriptor(self.rppxml.find('FADEIN'))

    @property
    def fade_out(self):
        ":class:`rpp.docmodel.fade_descriptor.FadeDescriptor` for clip's fade out."
        return FadeDescriptor(self.rppxml.find('FADEOUT'))

    @property
    def gain(self):
        """
        Overall gain.
        """
        return float(self.rppxml.find('VOLPAN')[3])

    @property
    def source(self):
        ":class:`rpp.docmodel.Source` of this item."
        return None
