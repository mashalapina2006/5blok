#1
print('starting to load recur1.py')
import recur2
def X():
    print('recur1.X')
recur2.Y()
print('finished loading recur1.py')

# 2
print('starting to load recur2.py')
import recur1
def Y():
    print('recur2.Y')
recur1.X()
print('finished loading recur2.py')
