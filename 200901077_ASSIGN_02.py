#           <<<<SYNTAX TREE>>>>>
#Muhammad Ahmad Siddique
#200901077

import ast

def SyntaxTree(Expression): #PascalCase
    tree = ast.parse(Expression)
    root_node = tree.body[0] #snake_case

    print(root_node._fields) # gives [target and values]
    print(ast.dump(tree)) #format string returns
    return root_node

Expression = input("Enter any expression: ")
root_node = SyntaxTree(Expression)
print(root_node)
