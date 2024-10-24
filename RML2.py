EL1 ={"LOVE", "LOYALTY", "PURITY"}
EL2 = {"PATIENCE", "BELIEF"}

TrueLOVE = EL1.union(EL2)
print(TrueLOVE)

amarDictionary ={
    "impossible" : "Osomvob",
    "sob" : "Somvob"
}
del amarDictionary["impossible"]
if "impossible" not in amarDictionary:
    print("amar dictionary te impossible bole kisu nai")

for x, y in amarDictionary.items():
    print(x,y)


if len(EL1) < 4:
    if len(EL1) == 3:
        print("purity")
    else:
        print("hipocrisy")    
i = 0
while i < len(EL2):
    print(EL2)
    i += 1

 
