# DYNAMICALLY FORMAT AND OUTPUT TEXT RESUME ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import json
from collections import namedtuple
from datetime import date as d

resume = open('data.json')
date = d.today().strftime('%Y.%m.%d')
nl = '\n'
text = ''
dat = json.load(resume,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
info = dat[0]
ed = dat[1]
work = dat[2]
craft = dat[3]
skl = craft.name
dev = craft.dev
cl = 31
gut = 5
cr = 75
t = 2
full = cl + gut + cr

# DISPLAY NAME IN LARGE ASCII FONT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def display(l,s=''):
  for i in range(len(l)):
    ((s := f'''{s}{l[i]*'/'}''') if i%2 else (s := f'''{s}{l[i]*' '}''')) # alternate spaces and numbers
  return s

# VALUES FOR DISPLAY FONT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
_1 = [5,5,3,3,5,4,4,4,3,3,3,2,4,6,3,2,2,5,2,2,3,2,1,3,4,3,3,4,3,3,3,2,1,5]
_2 = [7,2,2,2,1,2,2,2,6,2,4,2,1,4,2,2,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,4,2,4,1,2,4,2,1,4,2,2,1,2,2,2]
_3 = [6,2,1,2,3,2,3,3,3,2,4,2,1,2,1,5,4,6,3,2,1,2,6,7,1,2,1,4,1,2,1,2,4,2,1,2,1,5,1,2,3,2]
_4 = [0,2,3,2,1,7,6,2,1,2,4,2,1,2,3,3,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,2,2,2,2,2,1,2,4,2,1,2,3,3,1,2,3,2]
_5 = [0,5,2,2,3,2,1,6,4,4,3,2,4,2,4,2,4,2,1,2,2,5,2,2,3,2,1,2,6,2,3,4,3,2,4,2,1,6]

# GENERATE BULLET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def bullet(s,mx,dent):
  a = []; i = 0
  s = ' '*dent+'* '+s
  while (len(s) > mx):
    i = mx
    while (s[i] != ' '): i -= 1
    a.append(s[:i])
    s = ' '*dent+' '+s[i:]
  a.append(s)
  return a

# GENERATE BULLETS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def bullets(arr,mx,dent):
  a = []
  for s in arr:
    a.extend(bullet(s,mx,dent))
  return a

# CONTACT INFORMATION AND AIM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
info_fields = f'EMAIL: {info.email} ~ TEXT: {info.phone} ~ SITE: {info.site} ~ DATE: {date}'
full_column = [nl,display(_1),display(_2),display(_3),display(_4),display(_5),nl,
f'''{(full-len(info_fields)-7)*' '}{info_fields}\n\n*{(full-2)*'~'}*'''] + bullets(info.text,103,8)
full_column += [f'''\n*{(full-2)*'~'}*''']

# ITERATE OVER SKILLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def skills(obj):
  a = []
  a.append(f'''{obj.title.upper()+':'+(cl-len(obj.title)+1-t)*' '}{gut*' '}''') 
  for n in obj.names:
    a.append(f'''{t*' '}{n+(cl-len(n)-t)*' '}{gut*' '}''')
  a.append(cl*' '+gut*' ')
  return a

# DEV SKILLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
left_column = [f'''{skl.upper()}{(cl-len(skl))*' '}{gut*' '}''',f'''*{(cl-2)*'~'}*{(gut)*' '}''']
left_column += skills(dev.prog)+skills(dev.lang)+skills(dev.meth)+skills(dev.tool)+skills(dev.doms)

# GENERATE WORK TEXT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def jobs(emp,sub=False):
  a = [f'''*{(cr-2)*'~'}*''']; subject = f'''{emp.role.upper()}{' ~ '+emp.sub if sub else ''}'''
  a.append(f'''{subject}{(cr-len(subject)-len(yrs := f'{emp.start} ~ {emp.end}'))*' '}{yrs}''')
  a.extend([f'''  {emp.name.title()}'''] + bullets(emp.text,71,2))
  return a

# WORK EXPERIENCE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
right_column = [f'''{(cr-len(f'{work.name}'))*' '}{work.name.upper()}''']
right_column += jobs(work.aun) + jobs(work.sbcs) + jobs(work.ace,True)

# ACADEMIC EXPERIENCE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
deg = f'{ed.grad.degree.upper()} ~ {ed.grad.major.title()}'; g = 'gpa: '
right_column += ['',f'''{(cr-len(f'{ed.name}'))*' '}{ed.name.upper()}''',f'''*{(cr-2)*'~'}*''',
f'''{deg}{(cr-len(deg)-len(ed.grad.year))*' '}{ed.grad.year}''', 
f'''  {ed.grad.school.title()}{(cr-len(ed.grad.school)-len(g)-len(str(ed.grad.gpa))-2)*' '}''' +\
f'''{g.upper()}{ed.grad.gpa}'''] + bullets(ed.grad.text,71,2)

# PRINT TEXT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
for line in full_column:
  text += line + '\n'
leftright = zip(left_column,right_column)
for line in leftright:
  text += line[0] + line[1] + '\n'
text += f'''\n\n{(full//2-len('~ * ~')//2)*' '}~ * ~{(full//2-len('~ * ~')//2)*' '}\n\n\n'''
                                                    
# WRITE TO TEXT FILE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
open('seeking.txt', 'w').write(text)