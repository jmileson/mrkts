from mrkts.usda.models import FarmersMarketFactory


def test_farmers_market_from_converted(converted_data):
    sut = FarmersMarketFactory.from_converted(converted_data[0])
    
