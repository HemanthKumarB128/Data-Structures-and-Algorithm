class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position <= 0 or self.head is None:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        count = 0
        while count < position - 1 and temp.next:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == value:
            self.head = self.head.next
            print(f"{value} deleted.")
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == value:
                prev.next = curr.next
                print(f"{value} deleted.")
                return
            prev = curr
            curr = curr.next
        print(f"{value} not found in the list.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) + " -> None")


def main():
    ll = LinkedList()

    while True:
        print("\n--- Singly Linked List Menu ---")
        print("1. Insert at end")
        print("2. Insert at beginning")
        print("3. Insert at position")
        print("4. Delete by value")
        print("5. Display list")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            value = input("Enter value to insert at end: ")
            ll.insert_at_end(value)

        elif choice == '2':
            value = input("Enter value to insert at beginning: ")
            ll.insert_at_beginning(value)

        elif choice == '3':
            value = input("Enter value to insert: ")
            pos = int(input("Enter position (0-based index): "))
            ll.insert_at_position(value, pos)

        elif choice == '4':
            value = input("Enter value to delete: ")
            ll.delete_by_value(value)

        elif choice == '5':
            ll.display()

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()