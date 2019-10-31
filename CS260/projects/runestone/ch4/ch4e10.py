from random import randint


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# main number bin
numbers = Queue()

# sorting bins
bin0, bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9 = \
Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue()

# list to hold each bin to allow using index to sort digits
diglist = [bin0, bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9]

# fill main number bin with 3 digit random values
for i in range(100):
    numbers.enqueue(str(randint(100, 999)))

for i in range(0, 4):  # one loop for each digit

    while not numbers.isEmpty():  # while loops runs until main bin is empty
        number = numbers.dequeue()
        digit = number[-i]
        for n in range(0, 10):  # loop for each potential int and sort appropriately
            if digit == str(n):
                diglist[n].enqueue(number)

    for n in range(0, 10):  # loops over each digit bin and enqueues back to main bin in order
        while not diglist[n].isEmpty():
            numbers.enqueue(diglist[n].dequeue())

print(numbers)
