import fb_checkin as fb
from Queue import PriorityQueue
class TreeNode():
     def __init__(self,name,initWeight):
        self.children = list()
        self.name=name
        self.weight = initWeight

     def addChild(self, name,weight):
        self.children.append(TreeNode(name,weight))
    
     def is_branch(self):
       return len(self.children) > 0
     

root = TreeNode("problem",1)
root.addChild("inc_num_of_samples",0.6)
root.addChild("randomize",0.1)
root.addChild("inc_num_of_features",0.3)
#print root.children[0].weight
root.children[0].addChild(7030,0.5)
root.children[0].addChild(8020,0.3) 
root.children[0].addChild(9010,0.2)
root.children[2].addChild("weekday",0.4) 
root.children[2].addChild("hour",0.3) 
root.children[2].addChild("year",0.2) 
root.children[2].addChild("month",0.1)   
#print root.children[0].children[0].weight
def search(root):
    frontier = PriorityQueue()
    frontier.put((1-root.weight, root))
    came_from = {}
    came_from[None] = root
    while not frontier.empty():
        i=0
        current = frontier.get()[1]
        if len(current.children) == 0:
            return current,came_from[current]
        else:
            for next in current.children:
                i=i+1
                frontier.put((1-next.weight, next))
                came_from[next] = (current,i)

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from ggplot import *
from sklearn import neighbors
from sklearn.cross_validation import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score,  recall_score
import csv

accuracy=0
counter=0
size=6040
feature='time'
df=pd.read_csv("new_train.csv",sep=",")
small_train = df[df['time'] < 7.3e5]
small_val = df[df['time'] >= 7.3e5] 
 
g1=ggplot(small_train, aes(x='x', y='y', color='place_id')) +\
    geom_point(aes(color='place_id')) +\
    scale_color_brewer(type='diverging', palette=4) +\
    xlab("x") + ylab("y")

#g1.draw()

group_data = df.groupby('place_id')
df = group_data.filter(lambda x: len(x)>300)

#print df


def validation(size=0.2,feature=5):
    X  =  df.iloc[:,[2,3,feature]]    # X includes columns 0,1,2,3
    y  =  df['place_id']   # Get last column
 
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X, y)
    Z = clf.predict(X)
    accuracy=clf.score(X,y)*100
    print ("Predicted model accuracy: "+ str(accuracy))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = size)
    clf1 = neighbors.KNeighborsClassifier()
    clf1 = clf1.fit(X_train,y_train)
    y_pred=clf1.predict(X_test)
    accuracy_score(y_test,  y_pred) * 100
    #print "###############################################################################"
    print
    y_true = y
    y_pred = clf1.predict(X)
    print "f1_score(macro) = ", f1_score(y_true, y_pred, average='macro')
    print 'Precision(macro) = ', precision_score(y_true, y_pred, average='macro') 
    print 'Recall(micro) =', recall_score(y_true, y_pred, average='macro') 
    #print 'Accuracy:', accuracy_score(y_true,  y_pred) * 100, "%"
    print
    #print "###############################################################################"
    return accuracy

#out = csv.writer(open("myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
#out.writerow(output)

print "===Accuracy====",validation(fb.fc_test(size),fb.fc_test1(feature))
threshold = fb.fc_test2()
print "===THRESHOLD===",threshold
while accuracy < threshold and counter<5:
    print "###############################################################################"
    print "===THRESHOLD===",threshold
    print "APPLYING SEARCH STRATEGY:",counter+1
    result = search(root)
    print (result[0].name),result[1][0].name,result[1][1]
    node = result[0].name
    parent = result[1][0]
    child_id = result[1][1]
    print "parent Name:",parent.name
    #making prob 0
    parent.children[child_id-1].weight=0
    if parent.name == "inc_num_of_samples":
        size = node
    elif parent.name == "inc_num_of_features":
        feature = node
    new_accuracy=validation(fb.fc_test(size),fb.fc_test1(feature))
    print "===New Accuracy====",new_accuracy
    if accuracy<new_accuracy:
            accuracy=new_accuracy
    print "NEW BEST ACCURACY SO FAR",accuracy
    counter=counter+1