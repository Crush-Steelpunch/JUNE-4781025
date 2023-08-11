import myapp.leonfunctions

def test_something():
    assert myapp.leonfunctions.reverseaword('bees') == 'seeb'

def test_seehearno():
    assert myapp.leonfunctions.seenohearno('pies') == ["Hear No Seip","See No Pies", "Speak No Pies"]