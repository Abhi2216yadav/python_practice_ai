from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Yadav ji", "Abhi", "harry"]:
        assert hello(name) == f"hello, {name}"
    assert hello("Abhay") == "hello, Abhay"
