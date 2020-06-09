
                            #                     1
                            #         2                                 3
                            #     4            5               6                7
                            # 8       9   10      11      12        13      14      15


class Heap():
    def __init__ (self,array = []):
        self.array = array
        for i in range(int((len(array)/2)-1),-1,-1):
            self.bubbledown(i)

    def __str__ (self):
        return str(self.array)

    def __sizeof__(self):
        return len(self.array)
    
    def removeMin(self):
        heapMin = self.array.pop(0)
        self.array.insert(0,self.array.pop())
        self.bubbledown()
        return heapMin

    def insert(self,item):
        self.array.append(item)
        self.bubbleup(len(self.array)-1)

    def bubbleup(self,index = -1 ):
        parentIndex = int((index - 1 )/ 2 )
        if parentIndex < 0:
            return
        parent = self.array[parentIndex]
        cur = self.array[index]
        
        if parent > cur: 
            self.swap(parentIndex,index)
            if parentIndex >0:
                self.bubbleup(parentIndex)





    
    def bubbledown(self,index = 0):
        width = len(self.array)
        cur =  self.array[(index)]

        leftchild = self.array[(index)*2 + 1] if (index)*2 + 1 < width else None
        rightchild = self.array[(index)*2 + 2] if (index)*2 + 2 < width else None

        if leftchild and rightchild and (cur > leftchild or cur > rightchild):
            if leftchild < rightchild:
                self.swap(index,(index)*2 + 1)
                self.bubbledown((index)*2 + 1)
            else:
                self.swap(index,(index)*2 + 2)
                self.bubbledown((index)*2 + 2)
        elif leftchild and leftchild < cur:
            self.swap(index,(index)*2 + 1)
            self.bubbledown((index)*2 + 1)
        elif rightchild and rightchild < cur:
            self.swap(index,(index)*2 + 2)
            self.bubbledown((index)*2 + 2)
    
    def swap(self,index1,index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp






