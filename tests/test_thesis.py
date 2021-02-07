import pyexlatex as pl

from tests.config import INPUT_FILES_DIR
from tests.utils.doc import compare_doc
from tests.fixtures.thesis import thesis



def test_create_thesis(thesis):
    name = 'thesis'
    thesis_path = INPUT_FILES_DIR / f'{name}.tex'
    assert str(thesis) == thesis_path.read_text()


def test_create_thesis_document(thesis):
    compare_doc(thesis, 'thesis')