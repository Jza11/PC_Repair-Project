class myHeap:
    def extractMax(self, arr):
        max = arr[0]
        n = len(arr)
        arr[0] = arr[n-1]
        n = n-1
        self.heapify(A, 0, n-1)
        return max

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def heapify(self, arr, i):
        largest = i
        n = len(arr)
        if ((2*i + 1) <= n and (arr[2*i + 1] > arr[i])):
            largest = 2*i + 1

        if ((2*i + 2 <= n) and (arr[2*i + 2] > arr[largest])):
            largest = 2*i + 2

        if (largest != i):
            self.swap(arr, i, largest)
            self.heapify(arr, largest, n)

    def printHeap(self, arr):
        n = len(arr)
        for i in range(n):
            print(i + " " + arr[i])

    def buildHeap(self, arr):
        n = len(arr)
        for i in reversed(range(n)):
            self.heapify(arr, i, n)