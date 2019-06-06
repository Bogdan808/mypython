import os
import time
import zipfile

sources = ['H:\\My Code', 'H:\\MyDoc']

target_dir = 'H:\\MyBackup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')


comment = input('Введите комментарий --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ','_') + '.zip'



if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог {0} успешно создан'.format(today))

listfiles = []
for source in sources:
    print('source::', source)
    for root, dirs, files in os.walk(source):
        for file in files:
            print('files::',file)
            listfiles.append(root + os.sep + file)


###

zfile = zipfile.ZipFile(target, 'w')
for file in listfiles:
    zfile.write(file)

zfile.close()
###

# print('today::', today)
# print('now::', now)
# print('os.path ({0})::'.format(today), os.path.exists(today))