forbidden = ('.', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '...', '’', '“', '”', '/', ',')
text = 'ololo?'
newtext = ''

#
for char in text.lower():
    print(char)
    if not char in forbidden:
        newtext = newtext + char
#

newt = ''.join([x for x in text if not x in forbidden])

print(newt)
