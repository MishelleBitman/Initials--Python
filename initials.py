first_names= ['Michelle','Lior', 'Eli', 'Adam', 'Anna', 'Ayllon', 'Jonah', 'Patric', 'Ari']
last_name= ['Landsman', 'Rosen', 'Offman', 'Pressman', 'Segal', 'Rubin', 'Shulman', 'Wagman', 'Amado', 'Rosenberg']
initials=[]
for i in first_names:
    for j in last_name:
        initials.append(i[0]+j[0])
print(initials)
for i in range(len(initials)-1):
    if initials[i] in initials[i+1:]:
        for j in range(len(last_name)):
            last_name[j]+='aa'
        break
print(last_name)
