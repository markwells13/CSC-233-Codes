class Node:
    def __init__(self, data):
        self.data = data      # Holds the song name and info
        self.next = None      # Points to the next node

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Starts the list

    def append(self, data):
        """Add a new node to the end of the list"""
        new_node = Node(data)  # Create a new node with the given data

        if not self.head:
            # If the list is empty, make the new node the head
            self.head = new_node
            return

        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next

        # Link the last node to the new node
        current.next = new_node

    def prepend(self, data):
        #Data holds the value to be stored in the current node.
        #Add a new node at the beginning of the list
        new_node = Node(data)  # Create the new node

        # Point the new node's next to the current head
        #Next is responsible for containing a link to the next node in the list.
        new_node.next = self.head

        # Update head to the new node
        self.head = new_node

    def display(self):
        #Print the list from head to tail
        current = self.head

        print("Playlist:", end=" ")

        # Traverse the list in forward direction
        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

# Usage example:

# Create a new singly linked list for a playlist
playlist = SinglyLinkedList()

# Append songs to the playlist
playlist.append("Uptown Funk")
playlist.append("Last Friday Night")
playlist.append("Hot and Cold")

# Add an intro song at the beginning
playlist.prepend("Intro")

# Show playlist in forward direction (from first to last song)
playlist.display()

