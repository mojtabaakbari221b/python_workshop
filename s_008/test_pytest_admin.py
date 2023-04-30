from q_t import login

def test_admin():
    output = login(username="hasan", password="hasan")

    assert output == False