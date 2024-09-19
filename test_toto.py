def toto(x,y,z):
    return (x*y)**z

def test_toto():
    assert toto(1, 2, 3) == 8
