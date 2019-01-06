import attr
from os import path
from rpp import Project, load

test_project_path = path.join(path.dirname(__file__),'data','docmodel.RPP')

def project_helper():
    with open(test_project_path,'r') as f:
        rppxml = load(f)
        return Project(rppxml)


def test_project():
    proj = project_helper()
    assert(proj.originator == '5.965/OSX64')
    assert(proj.sample_rate == '48000')

def test_markers():
    proj = project_helper()
    count = 0
    for index, marker in enumerate(proj.markers):
        count += 1
        if index == 0:
            assert(marker.is_region)
        elif index == 1:
            assert(marker.is_marker)
        
