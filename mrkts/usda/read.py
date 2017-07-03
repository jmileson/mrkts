import requests
import csv
from collections import namedtuple
from io import StringIO

_COLS = [
    'id',
    'name',
    'website',
    'facebook',
    'twitter',
    'youtube',
    'other_media',
    'street',
    'city',
    'country',
    'state',
    'zip',
    'season1_date',
    'season1_time',
    'season2_date',
    'season2_time',
    'season3_date',
    'season3_time',
    'season4_date',
    'season4_time',
    'x',
    'y',
    'location',
    'credit',
    'wic',
    'wic_cash',
    'sfmnp',
    'snap',
    'organic',
    'baked_goods',
    'cheese',
    'crafts',
    'flowers',
    'eggs',
    'seafood',
    'herbs',
    'vegetables',
    'honey',
    'jams',
    'maple',
    'meat',
    'nursery',
    'nuts',
    'plants',
    'poultry',
    'prepared',
    'soap',
    'trees',
    'wine',
    'coffee',
    'beans',
    'fruits',
    'grains',
    'juices',
    'mushrooms',
    'pet_food',
    'tofu',
    'wild_harvested',
    'update_time'
]
FarmersMarket = namedtuple('FarmersMarket', _COLS)


def load_data(url):
    resp = requests.get(url)
    return resp.text


def read_data(url):
    """read the remote data as a csv, dropping the header"""
    io = StringIO(load_data(url))
    reader = csv.reader(io)
    _, *data = (line for line in reader if line)
    return data


def read(url):
    data = read_data(url)
    return [FarmersMarket(*r) for r in data]
