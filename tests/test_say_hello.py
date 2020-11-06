import trongPackage

def test_say_hello():
    try:
        trongPackage.main.say_hello()
        assert True
    except:
        assert False    