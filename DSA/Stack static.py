class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    def is_full(self):
        return self.top == self.max_size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print("Stack Overflow! Cannot push", value)
            return
        self.top += 1
        self.stack[self.top] = value
        print(f"{value} pushed to stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop")
            return
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        print(f"{value} popped from stack")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print(f"Top element is {self.stack[self.top]}")

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack elements:", [self.stack[i] for i in range(self.top, -1, -1)])


# ---- Menu-driven driver code ----
def main():
    size = int(input("Enter the size of the stack: "))
    s = Stack(size)

    while True:
        print("\n----- STACK MENU -----")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter value to push: "))
            s.push(value)
        elif choice == '2':
            s.pop()
        elif choice == '3':
            s.peek()
        elif choice == '4':
            s.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()