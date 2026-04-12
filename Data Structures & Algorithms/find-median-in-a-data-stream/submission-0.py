class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        #even case
        if len(self.data) % 2 == 0:
            mid1 = len(self.data) // 2
            mid2 = ((len(self.data) // 2) - 1) 
            return (self.data[mid1] + self.data[mid2]) / 2
        else:
            mid = len(self.data) // 2
            return self.data[mid]
        #odd case
        