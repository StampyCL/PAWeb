
countriesOCE = ['Fiji', 'Kiribati', 'Marshall Islands', 'Australia', 'Federated States of Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

def check(l):
  for c in countriesOCE:
    if c in l:
      return True
  return False

file = open('shapesCountries.js', 'r')

txt = file.read()

file.close()

lines = txt.split('\n')

newTxt = ''

for l in lines:
  if check(l):
    words = l.split(' ')
    changeNext = False
    for k in range(len(words)):
      if changeNext and words[k] != '[':
        words[k] = str(float(words[k].replace(',', ''))-360)+','
        changeNext = False
      if words[k] == '[':
        changeNext = True
    
    newLine = ' '.join(words)
    newTxt += newLine
  else:
    newTxt += l
  newTxt += '\n'


file = open('newShapesCountries.js', 'w')

file.write(newTxt)
file.close()

