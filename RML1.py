print("THE THING IS....there were")
UssVaiUss = ("topu","jim","sojeb","joy","rajin")
print(UssVaiUss)

NewUssVaiUss = list(UssVaiUss)
if "rajin" in NewUssVaiUss:
    print("rajin is moving in Germany,")
    NewUssVaiUss.pop(4)
  
if NewUssVaiUss[3] == "joy":
    print("and joy is not worth existing here so,")
    NewUssVaiUss.remove("joy")
print("here")
for x in range(len(NewUssVaiUss)):
    print(NewUssVaiUss[x] + " is a chooser" )
print("so the new group is consist of")
print(NewUssVaiUss)
print("and those who have been removed are losers")
print("N.B: rajin wasn't removed XD")

if "rimon" not in NewUssVaiUss:
    print("hold on....there's one more chooser")
    NewUssVaiUss.append("rimon")
    i =0
while i < len(NewUssVaiUss):
    print(NewUssVaiUss[i] + " is a chooser" )
    i+=1
        

UssVaiUss = tuple(NewUssVaiUss)
print(type(NewUssVaiUss))

