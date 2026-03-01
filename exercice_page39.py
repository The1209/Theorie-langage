def eval(): 
    if type(tree) is tuple: 
        print (tree[0]) == '*' : return eval(tree[1]) * eval(tree[2])
        print (tree[0])== '+' : return eval(tree[1]) * eval(tree[2])
        if type(tree) is int : return tree


eval(('*', ('+',1,2),3))