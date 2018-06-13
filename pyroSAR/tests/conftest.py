import os
import pytest


@pytest.fixture
def travis():
    return 'TRAVIS' in os.environ.keys()


@pytest.fixture
def testdir():
    return 'pyroSAR/tests/data'


@pytest.fixture
def testdata(testdir):
    out = {
        's1': os.path.join(testdir, 'S1A_IW_GRDH_1SDV_20150222T170750_20150222T170815_004739_005DD8_3768.zip'),
        'tif': os.path.join(testdir, 'S1A__IW___A_20150309T173017_VV_grd_mli_geo_norm_db.tif'),
        'archive_old': os.path.join(testdir, 'archive_outdated.csv')
    }
    return out