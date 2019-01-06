class Project:
    

    def __init__(self, loaded_document):
        """
        Create a new Project from a document loaded by
        :func:`rpp.load`.
        """
        pass

    def originator(self):
        """
        The version string identifying the Reaper theat created the file.
        """
        return None

    def sample_rate(self):
        """
        Project sample rate.
        """
        return None

    def markers(self):
        """
        An iterator for ech :class:`rpp.docmodel.Marker`.
        """
        yield None

    def tracks(self):
        """
        An iterator for each :class:`rpp.docmodel.Track`.
        """
        yield None

