import myapp.myfunctions

def test_myfunctions():
    assert myapp.myfunctions.maxthreenumbers(2,4,6) == 6
    assert myapp.myfunctions.maxthreenumbers(6,4,2) == 6
    assert myapp.myfunctions.maxthreenumbers(2,6,4) == 6
    assert myapp.myfunctions.maxthreenumbers(4,2,6) == 6