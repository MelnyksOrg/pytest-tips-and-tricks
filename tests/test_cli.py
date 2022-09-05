from click.testing import CliRunner
from cli import make_change
from mlib.mchange import change

import pytest


@pytest.fixture
def amount():
    return [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}]


@pytest.fixture
def runner():
    my_runner = CliRunner()
    return my_runner


def test_change(amount):
    assert amount == change(1.34)


def test_cli_help(runner):
    result = runner.invoke(make_change, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_cli_change(runner):
    result = runner.invoke(make_change, ["--amount", "1.34"])
    assert result.exit_code == 0
    assert "5\nnickels" in result.output
