class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def address(self):
        # id() returns the object's real memory address (as an int) in CPython
        return hex(id(self))


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # tail.next always points back to head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head   # single node points to itself
            return
        new_node.next = self.head       # new node closes the loop
        self.tail.next = new_node
        self.tail = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head
            return
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head      # tail must re-link to new head

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
        temp.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == value:
            if self.head == self.tail:
                self.head = self.tail = None    # only node in the list
            else:
                self.head = self.head.next
                self.tail.next = self.head       # re-close the loop
            print(f"{value} deleted.")
            return
        prev = self.head
        curr = self.head.next
        while curr != self.head:
            if curr.data == value:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev              # deleted node was the tail
                print(f"{value} deleted.")
                return
            prev = curr
            curr = curr.next
        print(f"{value} not found in the list.")

    def display(self):
        # Must stop manually after one full loop back to head,
        # otherwise this would print forever
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
        print(" -> ".join(elements) + " -> (back to head)")

    def display_with_addresses(self):
        # Mirrors the diagram: shows each node's own address and the
        # address stored in its next pointer. The tail's next shows
        # head's address instead of NULL, closing the loop.
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print(f"{'ADDRESS':<14}{'DATA':<8}{'NEXT':<14}")
        while True:
            print(f"{temp.address():<14}{str(temp.data):<8}{temp.next.address():<14}")
            temp = temp.next
            if temp == self.head:
                break
        print("(next node's NEXT loops back to the first ADDRESS above)")


# Program entry point: no main() or __name__ guard, so this runs immediately
cll = CircularLinkedList()

while True:
    print("\n--- Circular Singly Linked List Menu ---")
    print("1. Insert at end")
    print("2. Insert at beginning")
    print("3. Insert at position")
    print("4. Delete by value")
    print("5. Display list")
    print("6. Display with addresses")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == '1':
        value = input("Enter value to insert at end: ")
        cll.insert_at_end(value)

    elif choice == '2':
        value = input("Enter value to insert at beginning: ")
        cll.insert_at_beginning(value)

    elif choice == '3':
        value = input("Enter value to insert: ")
        pos = int(input("Enter position (0-based index): "))
        cll.insert_at_position(value, pos)

    elif choice == '4':
        value = input("Enter value to delete: ")
        cll.delete_by_value(value)

    elif choice == '5':
        cll.display()

    elif choice == '6':
        cll.display_with_addresses()

    elif choice == '7':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")