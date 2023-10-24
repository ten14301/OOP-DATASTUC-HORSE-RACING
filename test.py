from My_tree import BinarySearchTree

binary_tree = BinarySearchTree()

for i in range(100):
    binary_tree.insert(i,"Horse","Win")

print(binary_tree.find_bet(50,"Horse"))

