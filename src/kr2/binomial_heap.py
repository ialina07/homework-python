import heapq

priority_queue = []
heapq.heappush(priority_queue, (2, "One"))
heapq.heappush(priority_queue, (1, "Two"))
heapq.heappush(priority_queue, (3, "Three"))
while priority_queue:
    priority, task = heapq.heappop(priority_queue)

class Node:
    def __init__(self):
        self.data = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.parent = None
        self.sibling = None

        # соединение двух биномиальных куч
        def mergeBinomialTrees(b1, b2):
            if b1.data > b2.data:
                b1, b2 = b2, b1
                b2.parent = b1
                b2.sibling = b1.child
                b1.child = b2
                b1.degree += 1

                return b1

        def unionBinomialHeap(l1, l2):
            _new = []
            it = ot = 0
            while (it < len(l1)) and (ot < len(l2)):
                if l1[it].degree <= l2[ot].degree:
                    _new.append(l1[it])
                    it+=1
                else:
                    _new.append(l2[ot])
                    ot += 1

            while it < len(l1):
                _new.append(l1[it])
                it += 1
            while ot < len(l2):
                _new.append(l2[ot])
                ot += 1

            return _new

    def adjust(_heap):
        if len(_heap) <= 1:
            return _heap
        new_heap = []
        it1 = it2 = it3 = 0
        if len(_heap) == 2:
            it2 = 1
            it3 = len(_heap)
        else:
            it2 = 1
            it3 = 2

        while it1 < len(_heap):
            if it2 == len(_heap):
                it1 += 1

            elif _heap[it1].degree < _heap[it2].degree:
                it1 += 1
                it2 += 1
                if it3 < len(_heap):
                    it3 += 1

            elif it3 < len(_heap) and _heap[it1].degree == _heap[it2].degree == _heap[it3].degree:
                it1 += 1
                it2 += 1
                it3 += 1

            elif _heap[it1].degree == _heap[it2].degree:
                _heap[it1] = mergeBinomialTrees(_heap[it1], _heap[it2])
                del _heap[it2]
                if it3 < len(_heap):
                    it3 += 1
        return _heap

    def InsertATreeInHeap(_heap, tree):
        temp = tree
        temp = unionBinomialHeap(_heap, tree)
        return adjust(_heap)


    def removeMinFromTreeReturnBHeap(tree):
        heap = []
        temp = tree.child

        # создаем кучу детей минимального элемента
        while temp:
            lo = temp
            temp = temp.sibling
            lo.sibling = None
            heap.insert(0, lo)

        return heap


    # добавляем в биномиальную кучу
    def insert(_head, key):
        temp = Node(key)
        return insertATreeInHeap(_head, temp)


    def getMin(_heap):
        temp = _heap[0]

        # ищем минимальный элемент в куче
        for node in _heap:
            if node.data < temp.data:
                temp = node

        return temp

    def extractMin(_heap):
        new_heap = []
        lo = []

        temp = getMin(_heap)

        # удаляем минимальный элемент кучи
        for node in _heap:
            if node != temp:
                new_heap.append(node)

        # соединяем кучу с детьми минимального элемента
        lo = removeMinFromTreeReturnBHeap(temp)
        new_heap = unionBionomialHeap(new_heap, lo)
        new_heap = adjust(new_heap)

        return new_heap











