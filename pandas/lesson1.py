import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

#### series in pandas
a=[1,2,3]
a1=pd.Series(a)
# convert index to labels
a2=pd.Series(a,index=['one','two','three'])
print(a1)
# when you create labels
print(a2['one'])
# key/value
calories = {"day1": 420, "day2": 380, "day3": 390}

test = pd.Series(calories)
print(test)

#############
