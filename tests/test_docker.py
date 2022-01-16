import pytest
from scripts.utils import read_var

def test_run_build():
    images_changed = read_var('IMAGES_CHANGED')
    if type(images_changed) == 'str':
        assert images_changed == "datascience-notebook"
    else:
        assert images_changed == ["datascience-notebook"]