import  pickle

shoplistfile = 'shoplist.data'

shoplist = ['яблоки', 'манго', 'морковь']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
stordelist = pickle.load(f)
print(stordelist)

