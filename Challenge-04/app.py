class Node:

    value = None

    next = None

    def __init__( self, value, next = None ):

        self.value = value
        self.next = next

def reverse( node, next = None ):

    nextNode = node.next

    node.next = next

    if not nextNode:
        return node

    return reverse( nextNode, node )


def showNodes( node ):

    print(node.value)

    if not node.next: return


    showNodes(node.next)

    return

node1 = Node( 1 )
node2 = Node( 2 )
node1.next = node2
node3 = Node( 3 )
node2.next = node3
node4 = Node( 4 )
node3.next = node4
node5 = Node( 5 )
node4.next = node5


node1 = reverse( node1 )


showNodes( node1 )


