bri = set(['Brassil', 'Russion', 'India'])
sitys = {}
print('India' in bri)
print('USA' in bri)

bric = bri.copy()
bric.add('China')

print(bric.issuperset(bri))
bri.remove('Russion')

