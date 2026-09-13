import matplotlib.pyplot as plt
def dis(x,y):
    return (x**2+y**2)**0.5

a = []
for i in range(-100,101):
    for j in range(-100,101):
        if dis(i,j) >= 2 and dis(i,j) < 3:
            a.append([i,j])
b = ''
for i in a:
    b += f'particle minecraft:basic_flame_particle ~{i[0]/2} ~8 ~{i[1]/2}\n'
with open('e.mcfunction','w') as f:
    f.write(b)