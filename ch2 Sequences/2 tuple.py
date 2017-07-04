
# used as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# sorted by city
for passport in sorted(traveler_ids):
    print '%s/%s' % passport

# _, dummy variable
for country, _ in traveler_ids:
    print country

# tuple unpacking
import os

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print filename

# Using * to grab excess items
# a, b, *rest = range(5)
# print rest

# named tuple
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print tokyo
print tokyo.population
print tokyo[1]
# print City._fileds

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

# _make(), initiate from an iterable
delhi = City._make(delhi_data)

# _asdict(), return OrderedDict built from named tuple
print delhi._asdict()
for key, value in delhi._asdict().items():
    print key + ':', value

print 'end'