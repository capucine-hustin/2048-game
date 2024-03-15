

from textual_2048 import adding, double, read_player_command
from io import StringIO


def test_double(monkeypatch):
    number_inputs = StringIO('10\n')
    monkeypatch.setattr('sys.stdin', number_inputs) # Instead of reading from the standard input we read from
                                                    # number_inputs
    assert double() == 20


def test_adding(monkeypatch):
    number_inputs = StringIO('20\n3\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert adding() == 23

def test_read_player_command(monkeypatch):
    test_inputs = StringIO('d')
    monkeypatch.setattr('sys.stdin', test_inputs)
    assert read_player_command() == 'd'