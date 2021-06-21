from projectname.cli import main
from projectname.const import EXIT_OK


def test_main():
    assert main.main() == EXIT_OK
