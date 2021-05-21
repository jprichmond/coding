import json; from collections import namedtuple; from datetime import date as d
##############################################################################################################
resume = open('../data.json')
dat = json.load(resume,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
info = dat[0]; ed = dat[1]; work = dat[2]; craft = dat[3]; web = craft.skills.web; data = craft.skills.data
date = d.today().strftime('%Y.%m.%d'); 
coll = 31; gut = 5; colr = 75; bs = '\\'; tab = 2; indent = 8; full = coll + gut + colr; nl = '\n'
##############################################################################################################
def display(l,s=''):
  for i in range(len(l)):
    ((s := f'''{s}{l[i]*'/'}''') if i%2 else (s := f'''{s}{l[i]*' '}'''))
  return s
##############################################################################################################
a = [5,5,3,3,5,4,4,4,3,3,3,2,4,6,3,2,2,5,2,2,3,2,1,3,4,3,3,4,3,3,3,2,1,5]
b = [7,2,2,2,1,2,2,2,6,2,4,2,1,4,2,2,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,4,2,4,1,2,4,2,1,4,2,2,1,2,2,2]
c = [6,2,1,2,3,2,3,3,3,2,4,2,1,2,1,5,4,6,3,2,1,2,6,7,1,2,1,4,1,2,1,2,4,2,1,2,1,5,1,2,3,2]
d = [0,2,3,2,1,7,6,2,1,2,4,2,1,2,3,3,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,2,2,2,2,2,1,2,4,2,1,2,3,2,1,2,3,2]
e = [0,5,2,2,3,2,1,6,4,4,3,2,4,2,4,2,4,2,1,2,2,5,2,2,3,2,1,2,6,2,3,4,3,2,3,2,1,6]
##############################################################################################################
info_fields = f'EMAIL: {info.email} ~ TEXT: {info.phone} ~ SITE: {info.site}'
full_column = [nl,display(a),display(b),display(c),display(d),display(e),nl,
f'''{(full-len(info_fields)-7)*' '}{info_fields}\n\n*{(full-2)*'~'}*''',
f'''{indent*' '}* {info.text[0][:91]}\n{indent*' '}  {info.text[0][92:]}''',
f'''{indent*' '}* {info.text[1][:86]}\n{indent*' '}  {info.text[1][87:]}''',
f'''{indent*' '}* {info.text[2][:89]}\n{indent*' '}  {info.text[2][90:180]}''',
f'''{indent*' '}* {info.text[3][:91]}\n*{(full-2)*'~'}*''']
wds = 'web dev skills'; lvl = 'acquiring'; w = web.acquiring; 
left_column = [f'''{f'{wds.upper()}'+(coll-len(f'{wds}'))*' '}{gut*' '}''',f'''*{(coll-2)*'~'}*{(gut)*' '}''',
f'''{lvl.upper()}:{(coll-len(lvl+':'))*' '}{gut*' '}''',
f'''{tab*' '}{w[0]+(coll-len(w[0])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[1]+(coll-len(w[1])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[2]+(coll-len(w[2])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[3]+(coll-len(w[3])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[4]+(coll-len(w[4])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[5]+(coll-len(w[5])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[6]+(coll-len(w[6])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[7]+(coll-len(w[7])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[8]+(coll-len(w[8])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[9]+(coll-len(w[9])-tab)*' '}{gut*' '}''']
lvl = 'employing'; w = web.employing
left_column += [f'''{lvl.upper()}:{(coll-len(lvl+':'))*' '}{gut*' '}''',
f'''{tab*' '}{w[0]+(coll-len(w[0])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[1]+(coll-len(w[1])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[2]+(coll-len(w[2])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[3]+(coll-len(w[3])-tab)*' '}{gut*' '}''']
lvl = 'mastering'; w = web.mastering
left_column += [f'''{lvl.upper()}:{(coll-len(lvl+':'))*' '}{gut*' '}''',
f'''{tab*' '}{w[0]+(coll-len(w[0])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[1]+(coll-len(w[1])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[2]+(coll-len(w[2])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[3]+(coll-len(w[3])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{w[4]+(coll-len(w[4])-tab)*' '}{gut*' '}''']
lvl = 'acquiring'; d = data.acquiring
left_column += [f'''{f'{wds.upper()}'+(coll-len(f'{wds}'))*' '}{gut*' '}''',
f'''*{(coll-2)*'~'}*{(gut)*' '}''',
f'''{lvl.upper()}:{(coll-len(lvl+':'))*' '}{gut*' '}''',
f'''{tab*' '}{d[0]+(coll-len(d[0])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[1]+(coll-len(d[1])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[2]+(coll-len(d[2])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[3]+(coll-len(d[3])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[4]+(coll-len(d[4])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[5]+(coll-len(d[5])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[6]+(coll-len(d[6])-tab)*' '}{gut*' '}''',]
lvl = 'employing'; d = web.employing
left_column += [f'''{lvl.upper()}:{(coll-len(lvl+':'))*' '}{gut*' '}''',
f'''{tab*' '}{d[0]+(coll-len(d[0])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[1]+(coll-len(d[1])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[2]+(coll-len(d[2])-tab)*' '}{gut*' '}''',
f'''{tab*' '}{d[3]+(coll-len(d[3])-tab)*' '}{gut*' '}''']
f'''{tab*' '}{d[4]+(coll-len(d[4])-tab)*' '}{gut*' '}''']
lvl = 'mastering'; d = web.mastering
left_column += [f'''{lvl.upper()}:{(coll-len(lvl+':'))*' '}{gut*' '}''',
f'''{tab*' '}{d[0]+(coll-len(d[0])-tab)*' '}{gut*' '}''']
wex = 'work experience'; sbcs = work.sbcs; yrs = f'{sbcs.start} ~ {sbcs.end}'
right_column = [f'''{(colr-len(f'{wex}'))*' '}{wex.upper()}''',
f'''*{(colr-2)*'-'}*''',
f'''{sbcs.role.upper()}{(colr-len(sbcs.role)-len(yrs))*' '}{yrs}''',
f'''  {sbcs.name.upper()}''',
f'''  * {sbcs.text[0][:71]}''',
f'''    {sbcs.text[0][72:142]}''',
f'''    {sbcs.text[0][142:]}''',
f'''  * {sbcs.text[1][:71]}''',
f'''    {sbcs.text[1][72:143]}''',
f'''    {sbcs.text[1][143:]}''',
f'''  * {sbcs.text[2][:71]}''',
f'''    {sbcs.text[2][72:]}''',
f'''  * {sbcs.text[3][:68]}''','',
f'''*{(colr-2)*'~'}*''']

ace = work.ace; yrs = f'{ace.start} ~ {ace.end}'
right_column += [f'''{ace.role.upper()}{(colr-len(ace.role)-len(yrs))*' '}{yrs}''',
f'''  {ace.name.upper()}''',
f'''  * {ace.text[0][:68]}''',
f'''    {ace.text[0][69:138]}''',
f'''    {ace.text[0][139:]}''',
f'''  * {ace.text[1][:65]}''',
f'''    {ace.text[1][66:]}''',
f'''  * {ace.text[2][:71]}''',
f'''    {ace.text[2][72:]}''',
f'''  * {ace.text[3][:71]}''',
f'''    {ace.text[3][72:140]}''','',
f'''*{(colr-2)*'~'}*'''
]

edu = 'education'; grad = ed.grad; deg = f'{grad.degree} ~ {grad.major}'; gpa = str(grad.gpa); g = 'gpa: '
right_column += [f'''{(colr-len(f'{edu}'))*' '}{edu.upper()}''',
f'''*{(colr-2)*'~'}*''',
f'''{deg.upper()}{(colr-len(deg)-len(grad.year))*' '}{grad.year}''',
f'''  {grad.school.upper()}{(colr-len(grad.school)-len(g)-len(gpa)-2)*' '}{g.upper()}{grad.gpa}''',
f'''  * {grad.text[0][:71]}''',
f'''    {grad.text[0][72:142]}''',
f'''    {grad.text[0][143:]}''',
]

text = ''
for line in full_column:
  text += line + '\n'
leftright = zip(left_column,right_column)
for line in leftright:
  text += line[0] + line[1] + '\n'

# text += f'''{col.left[0]}{(colr-len(f'{wex}'))*' '}{wex}
# {col.left[1]}*{(colr-2)*'~'}*
# '''; sbcs = work.sbcs; role = sbcs.role.upper(); yrs = f'{sbcs.start} ~ {sbcs.end}'; w = web.acquiring
# text += f'''{role}{(colr-len(role)-len(yrs))*' '}{yrs}
# {tab*' '}{w[0]+(coll-len(w[0])-tab)*' '}{gut*' '}  {sbcs.name.upper()}
# {tab*' '}{w[1]+(coll-len(f'{w[1]}')-tab)*' '}{gut*' '}  * {sbcs.text[0][:71]}
# {tab*' '}{w[2]+(coll-len(f'{w[2]}')-tab)*' '}{gut*' '}    {sbcs.text[0][72:142]}
# {tab*' '}{w[3]+(coll-len(f'{w[3]}')-tab)*' '}{gut*' '}    {sbcs.text[0][142:]}
# {tab*' '}{w[4]+(coll-len(f'{w[4]}')-tab)*' '}{gut*' '}  * {sbcs.text[1][:71]}
# {tab*' '}{w[5]+(coll-len(f'{w[5]}')-tab)*' '}{gut*' '}    {sbcs.text[1][72:143]}
# {tab*' '}{w[6]+(coll-len(f'{w[6]}')-tab)*' '}{gut*' '}    {sbcs.text[1][143:]}
# {tab*' '}{w[7]+(coll-len(f'{w[7]}')-tab)*' '}{gut*' '}  * {sbcs.text[2][:71]}
# {tab*' '}{w[8]+(coll-len(f'{w[8]}')-tab)*' '}{gut*' '}    {sbcs.text[2][72:]}
# {tab*' '}{w[9]+(coll-len(f'{w[9]}')-tab)*' '}{gut*' '}  * {sbcs.text[3][:68]}
# '''; w = web.employing; ace = work.ace
# text += f'''EMPLOYING:{(coll-len('EMPLOYING:'))*' '}{gut*' '}    {sbcs.text[3][68:134]}
# {tab*' '}{w[0]+(coll-len(f'{w[0]}')-tab)*' '}{gut*' '}    {sbcs.text[3][135:]}
# {tab*' '}{w[1]+(coll-len(f'{w[1]}')-tab)*' '}
# {tab*' '}{w[2]+(coll-len(f'{w[2]}')-tab)*' '}{gut*' '}*{(colr-2)*'~'}*
# '''; role = ace.role.upper(); yrs = f'{ace.start} ~ {ace.end}'
# text += f'''{tab*' '}{w[3]+(coll-len(f'{w[3]}')-tab)*' '}{gut*' '}{role}{(colr-len(role)-len(yrs))*' '}{yrs}
# '''; w = web.mastering
# text += f'''MASTERING:{(coll-len('MASTERING:'))*' '}{gut*' '}  {ace.name.upper()} ~ {ace.cs.upper()}
# {tab*' '}{w[0]+(coll-len(f'{w[0]}')-tab)*' '}{gut*' '}  * {ace.text[0][:68]}
# {tab*' '}{w[1]+(coll-len(f'{w[1]}')-tab)*' '}{gut*' '}    {ace.text[0][69:138]}
# {tab*' '}{w[2]+(coll-len(f'{w[2]}')-tab)*' '}{gut*' '}    {ace.text[0][139:]}
# {tab*' '}{w[3]+(coll-len(f'{w[3]}')-tab)*' '}{gut*' '}  * {ace.text[1][:65]}

# '''
output = open('resume.txt', 'w')
output.write(text)
print('file should have been written')




