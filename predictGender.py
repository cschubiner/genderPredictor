import genderPredictor

gp = genderPredictor.genderPredictor()
gp.defaultTrain()

men = 0
women = 0

for name in open('toClassify.txt','r').readlines():
    name = name.strip().split()[0]
    gender = gp.classify(name)
    if gender == 'M': men+=1
    if gender == 'F': women+=1

print '------------------\n'
print men,'M', women,'F'
