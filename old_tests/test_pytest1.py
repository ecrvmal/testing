import pytest
import sys
from pathlib import Path
sys.path.append(str(Path('').absolute().parent))
from main import Digit, Teacher


class TestSuit:
    def setup_module(self):
        self.t = Teacher("Ivan", 33, 'Math')
        self.t.name = 'Vano'


    # t = setup_module()

    def teardown_module(self):
        # teardown_something()
        pass

    def test_upper(self):
        # assert 'foo'.upper() == 'FOO'
        assert self.t.name == 'Vano'

    def test_isupper(self):
        # assert 'FOO'.isupper()
        assert self.t.age == 33

    def test_failed_upper(self):
        # assert 'foo'.upper() == 'FOo'
        assert t.subject == 'Math'