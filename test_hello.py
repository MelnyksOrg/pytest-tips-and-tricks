from hello import more_goodbye, more_hello


def test_more_hello():
    assert more_hello() == "hi"


def test_more_hello_2():
    assert more_goodbye() == "bye"
