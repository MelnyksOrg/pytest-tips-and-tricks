from re import sub
from smath import subtract

def setup_function(function):
    print(f" Running Setup: {function.__name__}");
    function.x = 10

def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x

def test_hello_subtract():
    f = test_hello_subtract.x
    assert subtract(9) == 8