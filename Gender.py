from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [height, weight, ShoeSize]
x  = [[180, 75, 28],[178, 72, 26], [154, 52, 23], [172, 61, 26], [185, 84, 29], [174, 71, 28], [162, 55, 24], [155, 50, 22], [192, 95, 30], [165, 58, 26]]

y = ['male', "male", "female", "male", "male", "male", "female", "female", "male", "female"]

clf = clf.fit(x,y)

prediction = clf.predict([[153, 48, 22]])

print(prediction)