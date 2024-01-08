

import csv
import string 

class HybridNode:
    def __init__(self, key, element):
        self.key = key
        self.element = element
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.next_node = None
        self.color = "Red"

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color



class RedBlackTree:
    def __init__(self):
        self.root = None
        self.NIL_LEAF = HybridNode(None, None) 
        self.NIL_LEAF.set_color("Black")


    def get_sibling(self, node):
        if node.parent is None:
                return None
        parent = node.parent
        if node == parent.left_child:
                return parent.right_child
        else:
                return parent.left_child



    
    
    def rotate_right(self, y):
        if y is None or y.left_child is None:
            return

        x = y.left_child
        y.left_child = x.right_child
        if x.right_child is not self.NIL_LEAF:
            x.right_child.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y is y.parent.right_child:
            y.parent.right_child = x
        else:
            y.parent.left_child = x
        x.right_child = y
        y.parent = x

    def rotate_left(self, x):
        if x is None or x.right_child is None:
            return

        y = x.right_child
        x.right_child = y.left_child
        if y.left_child is not self.NIL_LEAF:
            y.left_child.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left_child:
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x
        x.parent = y

    def insert(self, key, element):
        new_node = HybridNode(key, element)
        new_node.right_child=self.NIL_LEAF
        new_node.left_child=self.NIL_LEAF
        if self.root is None:
            self.root = new_node
            self.root.set_color("Black")  # Ensure the root is black
        else:
            self._insert_helper(self.root, new_node)
            self.fix_up(new_node)
        
    def _insert_helper(self, current, new_node):
        
        if current.key and new_node.key < current.key:
            if current.left_child is self.NIL_LEAF:
                current.left_child = new_node
                new_node.parent = current
            else:
                self._insert_helper(current.left_child, new_node)
        else:
            if current.right_child is self.NIL_LEAF:
                current.right_child = new_node
                new_node.parent = current
            else:
     
                self._insert_helper(current.right_child, new_node)

    def minimum(self, node):
        while node.left_child is not self.NIL_LEAF:
            node = node.left_child
        return node

    def fix_up(self, node):
        while node != self.root and node.get_color() == "Red" and node.parent.get_color() == "Red":
            if node.parent == node.parent.parent.left_child:
                uncle = node.parent.parent.right_child
                if uncle and uncle.get_color() == "Red":
                    node.parent.set_color("Black")
                    uncle.set_color("Black")
                    node.parent.parent.set_color("Red")
                    node = node.parent.parent
                else:
                    if node == node.parent.right_child:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.set_color("Black")
                    node.parent.parent.set_color("Red")
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left_child
                if uncle and uncle.get_color() == "Red":
                    node.parent.set_color("Black")
                    uncle.set_color("Black")
                    node.parent.parent.set_color("Red")
                    node = node.parent.parent
                else:
                    if node == node.parent.left_child:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.set_color("Black")
                    node.parent.parent.set_color("Red")
                    self.rotate_left(node.parent.parent)

        self.root.set_color("Black")
    def traverse_up(self, node):
        
        result=[]
        current=node 
        while current is not None :
            result.append(current)

            current=current.parent
           
    
        return result 

    def traverse_down(self, node, bit_sequence):
        result=[]
        
        current=node
        print(bit_sequence)
        for i in bit_sequence:
            print(i)
            
            if i=='1':
                
                if current is not self.NIL_LEAF:
                    result.append(current)
                    current=current.left_child   
                else:
                    break    

                 
                      
                    
            elif i=='0':
                if current.right_child  is not self.NIL_LEAF:
                    result.append(current)
                    current=current.right_child
                else:
                    break            
        return result 
        

    def preorder_traversal(self, node, depth, result):
        def recursive_traversal(current, current_depth):
            if current is not self.NIL_LEAF and current_depth <=depth:
                result.append(current.element)
                if current_depth < depth:
                    recursive_traversal(current.left_child, current_depth + 1)
                    recursive_traversal(current.right_child, current_depth + 1)

        recursive_traversal(node, 0)
        return result 

 
         
    def black_height(self, node):
        if node is None:
            return 0
        if node is self.NIL_LEAF:
            return 0

        black_height = 0

        
        current = self.root
        while current is not self.NIL_LEAF:
            if current.get_color() == "Black":
                black_height += 1
            current = current.left_child

        return black_height

        


    def transfer(self, node1, node2):
        if node1.parent is None:
            self.root = node2
        elif node1 == node1.parent.left_child:
            node1.parent.left_child = node2
        else:
            node1.parent.right_child = node2

        if node2:
            node2.parent = node1.parent



    def search(self, key):
        if self.root is None:
            return None
        else:
            current=self.root
            while current is not self.NIL_LEAF:
                if key==current.key:
                    return current 
                elif key<=current.key:
                    current=current.left_child 
                else:
                    current=current.right_child 

        return None 

    def delete(self, key):
        # Find the node to delete
        node = self.search(key)
        if node is None:
            return

        # Perform the actual deletion and rebalancing
        self._delete_node(node)

    def _delete_node(self, node):
        # Perform the actual deletion
        y = node
        y_original_color = y.get_color()
        if node.left_child is self.NIL_LEAF:
            x = node.right_child
            self.transfer(node, node.right_child)
        elif node.right_child is self.NIL_LEAF:
            x = node.left_child
            self.transfer(node, node.left_child)
        else:
            y = self.minimum(node.right_child)
            y_original_color = y.get_color()
            x = y.right_child
            if y.parent is node:
                x.parent = y
            else:
                self.transfer(y, y.right_child)
                y.right_child = node.right_child
                y.right_child.parent = y
            self.transfer(node, y)
            y.left_child = node.left_child
            y.left_child.parent = y
            y.set_color(node.get_color())

        if y_original_color == "Black":
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while x is not self.root and x.get_color() == "Black":
            if x is x.parent.left_child:
                sibling = x.parent.right_child
                if sibling.get_color() == "Red":
                    sibling.set_color("Black")
                    x.parent.set_color("Red")
                    self.rotate_left(x.parent)
                    sibling = x.parent.right_child
                if sibling.left_child.get_color() == "Black" and sibling.right_child.get_color() == "Black":
                    sibling.set_color("Red")
                    x = x.parent
                else:
                    if sibling.right_child.get_color() == "Black":
                        sibling.left_child.set_color("Black")
                        sibling.set_color("Red")
                        self.rotate_right(sibling)
                        sibling = x.parent.right_child
                    sibling.set_color(x.parent.get_color())
                    x.parent.set_color("Black")
                    sibling.right_child.set_color("Black")
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left_child
                if sibling.get_color() == "Red":
                    sibling.set_color("Black")
                    x.parent.set_color("Red")
                    self.rotate_right(x.parent)
                    sibling = x.parent.left_child
                if sibling.right_child.get_color() == "Black" and sibling.left_child.get_color() == "Black":
                    sibling.set_color("Red")
                    x = x.parent
                else:
                    if sibling.left_child.get_color() == "Black":
                        sibling.right_child.set_color("Black")
                        sibling.set_color("Red")
                        self.rotate_left(sibling)
                        sibling = x.parent.left_child
                    sibling.set_color(x.parent.get_color())
                    x.parent.set_color("Black")
                    sibling.left_child.set_color("Black")
                    self.rotate_right(x.parent)
                    x = self.root
        x.set_color("Black")
    
    
class Lexicon:
    def __init__(self):
        self.red_black_tree = RedBlackTree()
        self.index = {}
        self.common_words_set = set()
        self.chapter_names=[]

    def update_common_words(self, word_counts):
        if not self.common_words_set:
            self.common_words_set = set(word_counts.keys())
        else:
            self.common_words_set &= set(word_counts.keys())

    def read_records_from_file(self, file):
        with open(file) as csv_file:
            word = []
            chapter_name = file.replace(".txt", "")
            for line in csv_file:
                words = line.strip().split()
                for wordy in words:
                    
                    
                    new_word = ''.join(char for char in wordy if char not in string.punctuation)
                    
                    word.append(new_word)
                
            self.word_processing(chapter_name, word)        

    def word_processing(self,chapter_name,words) :
        word_counts = {}

        for word in words:
            word=word.lower()
            
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        
        self.update_common_words(word_counts)
        
        for word, word_count in word_counts.items():
            if word in self.index:
                index_entry = self.index[word]
                index_entry.add_occurrence(chapter_name, word_count)
                
            else:
                self.red_black_tree.insert(word,chapter_name)
                index_entry = IndexEntry(word)
                index_entry.add_occurrence(chapter_name, word_count)
                
                self.index[word] = index_entry


    def read_chapters(self, chapter_names):
        for j in chapter_names:
            chapter_name = j.replace(".txt", "")
            self.chapter_names.append(chapter_name)

        
        
        for i in chapter_names:
            self.read_records_from_file(i)
        self.prune_common_words()   
       
        
       
            
   
    def prune_common_words(self):
        
            
        print(self.common_words_set)
       

        for word in self.common_words_set:
            self.red_black_tree.delete(word)


            
    def build_index(self):
        
        index = []
        temp_word_counts=[]

        for word, entry in self.index.items():
            
            index_entry = IndexEntry(word)
            
            
            if len(self.chapter_names)!=len(entry.chapter_word_counts):
                
                temp_word_counts=[]
                  
                           
                for i in self.chapter_names:
                    
                    
                    flag=0
                    for j in range(len(entry.chapter_word_counts)):
                       
                        
                        if i == entry.chapter_word_counts[j][0]:
                             
                            flag=1
                            
                        else:
                            continue     
                    if flag==0:
                        
                        temp_word_counts.append((i,0))
                     
                    elif flag==1:
                        
                        for k in range(len(entry.chapter_word_counts)):
                            if entry.chapter_word_counts[k][0]==i:
                                temp_word_counts.append(entry.chapter_word_counts[k])
                                
            else:
                
                temp_word_counts=entry.chapter_word_counts
                                
                    
            index_entry.chapter_word_counts = temp_word_counts
            index.append(index_entry)

        index.sort(key=lambda entry: entry.word)

        return index

        

class IndexEntry:
    def __init__(self, word):
        self.word = word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples

    def add_occurrence(self, chapter, word_count):
        self.chapter_word_counts.append((chapter, word_count))

    def get_word_count(self, chapter):
        for entry in self.chapter_word_counts:
            if entry[0] == chapter:
                return entry[1]
        return 0
    def __str__(self):
        # Return a string representation of the IndexEntry
        return f"Word: {self.word}, Occurrences: {self.chapter_word_counts}"

class MRU:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []

    def access(self, index_entry):
        if index_entry in self.items:
            self.items.remove(index_entry)
        elif len(self.items) >= self.max_size:
            self.items.pop()
        self.items.insert(0, index_entry)

    def get_most_recent(self):
        if self.items:
            return self.items[0]
        else:
            return None
