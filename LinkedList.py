class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

class LinkedList(object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    # for sort method
    def add_node (self, n):
	    n.set_next(self.root)
	    self.root = n
	    self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    # Timsort
    def sort (self):
	    if self.size > 1:
		    newlist = []
		    current = self.root
		    newlist.append(self.root)
		    while current.has_next():
			    current = current.get_next()
			    newlist.append(current)
		    newlist = sorted(newlist, key = lambda node: node.get_data(), reverse = True)
		    newll = LinkedList()
		    for node in newlist:
			    newll.add_node(node)
		    return newll
	    return self

    def print_list(self):
        l = []
        current = self.root
        while current:
            l.append(current.get_data())
            current = current.get_next()
        print(l)

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.add(24)
myList.add(99)
myList.add(15)
myList.add(3)
myList.remove(8)
print(myList.remove(12))
print(myList.remove(13))
print(myList.find(5))
myList.print_list()
myList = myList.sort()
myList.print_list()