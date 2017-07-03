import pretend
import requests


def test_load_data(monkeypatch, data):
    from mrkts.usda.read import load_data

    resp = pretend.stub(text=data)
    get = pretend.call_recorder(lambda u: resp)
    monkeypatch.setattr(requests, 'get', get)

    assert load_data(pretend.stub()) == data


def test_read_data(monkeypatch, data):
    import mrkts.usda.read

    load_data = pretend.call_recorder(lambda u: data)
    monkeypatch.setattr(mrkts.usda.read, 'load_data', load_data)

    result = mrkts.usda.read.read_data(pretend.stub())

    assert len(result) == 9 # test data count


def test_read(monkeypatch, data):
    import mrkts.usda.read

    load_data = pretend.call_recorder(lambda u: data)
    monkeypatch.setattr(mrkts.usda.read, 'load_data', load_data)

    result = mrkts.usda.read.read(pretend.stub())

    # no cleansing occurs here
    assert result[0].name == ' Caledonia Farmers Market Association - Danville'