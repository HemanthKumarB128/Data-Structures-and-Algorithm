class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def address(self):
        # id() returns the object's real memory address (as an int) in CPython
        return hex(id(self))


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # tail.next == head, and head.prev == tail

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node   # points to itself
            return
        new_node.prev = self.tail
        new_node.next = self.head
        self.tail.next = new_node
        self.head.prev = new_node
        self.tail = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
            return
        new_node.next = self.head
        new_node.prev = self.tail
        self.head.prev = new_node
        self.tail.next = new_node
        self.head = new_node

    def insert_at_position(self, data, position):
        if position <= 0 or self.head is None:
            self.insert_at_beginning(data)
            return
        temp = self.head
        count = 0
        while count < position - 1 and temp.next != self.head:
            temp = temp.next
            count += 1
        if temp == self.tail:
            self.insert_at_end(data)
            return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while True:
            if temp.data == value:
                if temp.next == temp:
                    # only node in the list
                    self.head = self.tail = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    if temp == self.head:
                        self.head = temp.next
                    if temp == self.tail:
                        self.tail = temp.prev
                print(f"{value} deleted.")
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"{value} not found in the list.")

    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        elements = []
        while True:
            elements.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" <-> ".join(elements) + " -> (back to head)")

    def display_backward(self):
        if self.tail is None:
            print("List is empty.")
            return
        temp = self.tail
        elements = []
        while True:
            elements.append(str(temp.data))
            temp = temp.prev
            if temp == self.tail:
                break
        print(" <-> ".join(elements) + " -> (back to tail)")

    def display_with_addresses(self):
        # Mirrors the diagram: shows each node's own address plus the
        # addresses stored in its prev/next pointers. head's PREV shows
        # tail's address and tail's NEXT shows head's address - no NULL
        # anywhere, since the ring is closed in both directions.
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print(f"{'ADDRESS':<14}{'PREV':<14}{'DATA':<8}{'NEXT':<14}")
        while True:
            print(f"{temp.address():<14}{temp.prev.address():<14}{str(temp.data):<8}{temp.next.address():<14}")
            temp = temp.next
            if temp == self.head:
                break
        print("(PREV/NEXT always resolve to a real address - the ring never hits NULL)")


# Program entry point: no main() or __name__ guard, so this runs immediately
cdll = CircularDoublyLinkedList()

while True:
    print("\n--- Circular Doubly Linked List Menu ---")
    print("1. Insert at end")
    print("2. Insert at beginning")
    print("3. Insert at position")
    print("4. Delete by value")
    print("5. Display forward")
    print("6. Display backward")
    print("7. Display with addresses")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == '1':
        value = input("Enter value to insert at end: ")
        cdll.insert_at_end(value)

    elif choice == '2':
        value = input("Enter value to insert at beginning: ")
        cdll.insert_at_beginning(value)

    elif choice == '3':
        value = input("Enter value to insert: ")
        pos = int(input("Enter position (0-based index): "))
        cdll.insert_at_position(value, pos)

    elif choice == '4':
        value = input("Enter value to delete: ")
        cdll.delete_by_value(value)

    elif choice == '5':
        cdll.display_forward()

    elif choice == '6':
        cdll.display_backward()

    elif choice == '7':
        cdll.display_with_addresses()

    elif choice == '8':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")