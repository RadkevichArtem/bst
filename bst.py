class Node:
    def __init__(self, rootObj):
        self.root = rootObj
        self.left = None
        self.right = None
        self.status = {'min':rootObj, 'max':rootObj}

    def insert(self, elem):
        """метод рекурсивно добаляет новый элемент в дерево и обновляет статус (мин и макс)"""
        if self.root:
            if elem < self.root:
                if self.left is None:
                    self.left = Node(elem)
                    self.status['min'] = elem
                else:
                    self.left.insert(elem)
            elif elem > self.root:
                self.status['max'] = elem
                if self.right is None:
                    self.right = Node(elem)
                    
                else:
                    self.right.insert(elem)
        else:
            self.root = elem


def createTree(data:list) -> Node:
    """функция создает дерево из списка"""
    data.sort()  
    mid = data[len(data) // 2]
    tree = Node(mid)
    if len(data) > 1:
        for value in data:
            tree.insert(value)
    
    return tree

data_in = [17, 6, 8, 20 , 13, 11, 4, 7, 19, 100, 1 ,27, 5]
myTreeStatus = createTree(data_in).status
print('Минимальный лист: {}\nМаксимальный лист: {}'.format(myTreeStatus['min'], myTreeStatus['max']))

