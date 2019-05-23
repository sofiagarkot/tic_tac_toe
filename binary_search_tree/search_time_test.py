from linkedbst import LinkedBST
import time
import random

words_list = []
f = open("words.txt")
for l in f.readlines():
    words_list.append(l.split()[0])

# random.shuffle(words_list)
words_to_find = list(random.choice(words_list) for i in range(10000))
start_list = time.time()
n = 0
for el in words_to_find:
    found = words_list.index(el)
end_list = time. time()
print("List :",end_list - start_list)

random.shuffle(words_list)
bstree = LinkedBST()
for i in words_list:
    bstree.add(i)

start_tree = time.time()
for el in words_to_find:
    found = bstree.find(el)
end_tree = time.time()

print("Tree :",end_tree - start_tree)

balanced_bst = bstree.rebalance()

start_balanced = time.time()
for el in words_to_find:
    found = balanced_bst.find(el)
end_balanced = time.time()

print("Balanced :", end_balanced - start_balanced)