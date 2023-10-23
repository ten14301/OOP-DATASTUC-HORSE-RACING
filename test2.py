class BettingNode:
    def __init__(self, result, horse, status):
        self.result = result
        self.horse = horse
        self.status = status
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, result, horse, status):
        self.root = self._insert(self.root, result, horse, status)

    #insert by result
    def _insert(self, root, result, horse, status):
        if root is None:
            return BettingNode(result, horse, status)
        if result < root.result:
            root.left = self._insert(root.left, result, horse, status)
        else:
            root.right = self._insert(root.right, result, horse, status)
        return root

    #in-order traverse
    def find_bet(self, result, horse):
        return self._find_bet(self.root, result, horse)

    def _find_bet(self, root, result, horse):
        if root is None:
            return "Bet not found"
        if result == root.result and horse == root.horse:
            return root.status
        elif result < root.result:
            return self._find_bet(root.left, result, horse)
        else:
            return self._find_bet(root.right, result, horse)
        

# สร้างอ็อบเจ็กต์ BettingTree
betting_tree = BinarySearchTree()

# สร้างการเดิมพัน
betting_tree.insert(1, "Horse White", "Win")
betting_tree.insert(2, "Horse Brown", "Lose")
betting_tree.insert(3, "Horse Black", "Win")

# ค้นหาการเดิมพัน
bet1 = betting_tree.find_bet(1, "Horse White")
bet2 = betting_tree.find_bet(2, "Horse Brown")
bet3 = betting_tree.find_bet(3, "Horse Black")
bet4 = betting_tree.find_bet(1, "Horse Black")

print(bet1)  # ผลลัพธ์: "Win"
print(bet2)  # ผลลัพธ์: "Lose"
print(bet3)  # ผลลัพธ์: "Win"
print(bet4)  # ผลลัพธ์: "Bet not found"
