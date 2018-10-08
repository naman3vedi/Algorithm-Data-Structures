class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def print_node(self):
        while self.next!=None:
            print(self.data)
            self=self.next
l=node(23)
node.left=node(20)
node.next=node(30)
node.next.next=node(18)
print_node(l)