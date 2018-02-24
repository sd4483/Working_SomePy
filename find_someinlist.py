emails=['sudheer@gmail.com', 'swathi@gmail.com', 'rajani@gmail.com', 'purna@gmail.com']
for i in emails:
    if 'some' in i:
        print(len(i))

a="Tricky"
for j in a[:3]:
    print(j)

names = ['sudheer', 'swathi', 'Rajani', 'Purna ChandraRao']

for i,j in zip(names,emails):
        print("Name:"+ i,", Email:"+j)
