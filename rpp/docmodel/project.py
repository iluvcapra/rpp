from .track import Track
from .marker import Marker, Region

class Project:
    
    def __init__(self, loaded_document):
        """
        Create a new Project from a document loaded by
        :func:`rpp.load`.
        """
        self.rppxml = loaded_document

    @property
    def originator(self):
        """
        The version string identifying the Reaper theat created the file.
        """
        return self.rppxml.attrib[1]

    @property
    def sample_rate(self):
        """
        Project sample rate.
        """
        return self.rppxml.find('./SAMPLERATE')[1]

    @property
    def markers(self):
        """
        An iterator for ech :class:`rpp.docmodel.Marker`.
        """
        markers = self.rppxml.findall('./MARKER')
        skip_next = False
        for marker1, marker2 in zip(markers, markers[1:] + [None]):
            if skip_next:
                skip_next = False
                continue

            if marker1[1] == marker2[1]:
                skip_next = True
                yield Region(marker1, marker2)
 
            else:
                yield Marker(marker1)
   
    @property
    def tracks(self):
        """
        An iterator for each :class:`rpp.docmodel.Track`.
        """
        for track in self.rppxml.findall('./TRACK'):
            yield Track(track)

