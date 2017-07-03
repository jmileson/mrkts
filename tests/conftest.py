import pytest
import pretend


@pytest.fixture()
def data():
    with open('./tests/test_data.csv') as f:
        return f.read()


@pytest.fixture()
def converted_data(monkeypatch, data):
    import mrkts.usda.read

    load_data = pretend.call_recorder(lambda u: data)
    monkeypatch.setattr(mrkts.usda.read, 'load_data', load_data)

    return mrkts.usda.read.read(pretend.stub())
