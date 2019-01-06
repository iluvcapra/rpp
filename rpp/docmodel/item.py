class Item:
    
    def __init__(self, rppxml):
        """
        Create an Item object from rppxml.
        """

    @property
    def position(self):
        "Start of this clip, in seconds."
        return None

    @property
    def length(self):
        "Length of this clip, in seconds."
        return None

    def start_offset(self):
        "Start offset in source."
        return None

    @property
    def loop(self):
        "Looped option, True or False."
        return None

    @property
    def mute(self):
        "Mute state, True or False."
        return None

    @property
    def name(self):
        "Item name."
        return None

    @property
    def fade_in(self):
        "FadeDescriptor for clip's fade in."
        return None

    @property
    def fade_out(self):
        "FadeDescriptor for clip's fade out."
        return None

    @property
    def source(self):
        ":class:`rpp.docmodel.Source` of this item."
        return None
