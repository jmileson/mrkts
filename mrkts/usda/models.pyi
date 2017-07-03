import mrkts.usda.read


class FarmersMarket(object):
    pass


class FarmersMarketFactory(object):
    @classmethod
    def from_converted(cls, conv: mrkts.usda.read.FarmersMarket) -> FarmersMarket:
        ...
