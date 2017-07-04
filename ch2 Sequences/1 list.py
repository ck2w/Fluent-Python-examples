# -*- coding:utf-8 -*-

# map, filter
symbols = '$￠￡￥€¤'
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print beyond_ascii

# catesian product
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]


print 'end'


