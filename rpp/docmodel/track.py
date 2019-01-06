class Track:
    
    def __init__(self, rppxml):
        """
        Create a track object for the given rppxml
        """
        pass

    @property
    def uuid(self):
        """
        The Track UUID.
        """
        return None

    @property
    def name(self):
        """
        The Track name.
        """
        return None

    @property
    def solo(self):
        """
        Solo state, True or False.
        """
        return None

    @property
    def mute(self):
        """
        Muted state, True or False.
        """
        return None

    @property
    def items(self):
        """
        Iterate through each media item on this track.
        """
        yield None

