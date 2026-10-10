class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def size(self):
        return len(self._items)


def is_balanced(brackets):
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())

    stack = Stack()
    for char in brackets:
        if char in opening:
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    line = input("Введите строку со скобками: ").strip()
    if is_balanced(line):
        print("Сбалансированно")
    else:
        print("Несбалансированно")