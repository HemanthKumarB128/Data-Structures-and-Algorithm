class Node:
    # Each node stores data plus links to BOTH neighbors
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # tail lets us insert/traverse backward in O(1)

    def insert_at_end(self, data):
        # Attach new node after tail, then update tail
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_at_beginning(self, data):
        # Attach new node before head, then update head
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_position(self, data, position):
        # Walk to the target index, then relink prev/next on both sides
        if position <= 0 or self.head is None:
            self.insert_at_beginning(data)
            return
        temp = self.head
        count = 0
        while count < position - 1 and temp.next:
            temp = temp.next
            count += 1
        if temp.next is None:
            self.insert_at_end(data)
            return
        new_node = Node(data)
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node

    def delete_by_value(self, value):
        # Find the node, then bypass it from both directions
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next   # deleting the head
                if temp.next:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev   # deleting the tail
                print(f"{value} deleted.")
                return
            temp = temp.next
        print(f"{value} not found in the list.")

    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print("None <- " + " <-> ".join(elements) + " -> None")

    def display_backward(self):
        # Same list, walked from tail using .prev
        if self.tail is None:
            print("List is empty.")
            return
        temp = self.tail
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.prev
        print("None <- " + " <-> ".join(elements) + " -> None")


# Program entry point: no main() or __name__ guard, so this runs immediately
dll = DoublyLinkedList()

while True:
    print("\n--- Doubly Linked List Menu ---")
    print("1. Insert at end")
    print("2. Insert at beginning")
    print("3. Insert at position")
    print("4. Delete by value")
    print("5. Display forward")
    print("6. Display backward")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == '1':
        value = input("Enter value to insert at end: ")
        dll.insert_at_end(value)

    elif choice == '2':
        value = input("Enter value to insert at beginning: ")
        dll.insert_at_beginning(value)

    elif choice == '3':
        value = input("Enter value to insert: ")
        pos = int(input("Enter position (0-based index): "))
        dll.insert_at_position(value, pos)

    elif choice == '4':
        value = input("Enter value to delete: ")
        dll.delete_by_value(value)

    elif choice == '5':
        dll.display_forward()

    elif choice == '6':
        dll.display_backward()

    elif choice == '7':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")