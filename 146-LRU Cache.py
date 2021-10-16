class MemoryNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.volume = 0
        self.mapping = dict()
        self.memory_head = MemoryNode(None, None)
        self.memory_tail = MemoryNode(None, None)
        self.memory_head.next = self.memory_tail
        self.memory_tail.prev = self.memory_head
    
    def touch(self, key):
        # 将最新操作过的单元放在队列最前方
        cur_node = self.mapping[key]
        if cur_node.prev == self.memory_head:
            return
        
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
            
        cur_node.prev = self.memory_head
        cur_node.next = self.memory_head.next    
        self.memory_head.next.prev = cur_node
        self.memory_head.next = cur_node
        
    def get(self, key: int) -> int:
        if key in self.mapping:
            self.touch(key)
            return self.mapping[key].value
        else:
            return -1

    def free(self, free_node):
        free_node.prev.next = free_node.next
        free_node.next.prev = free_node.prev
        self.mapping.pop(free_node.key)
        self.volume -= 1
    
    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping[key].value = value
            self.touch(key)
        else:    
            if self.volume == self.capacity:
                self.free(self.memory_tail.prev)
            
            cur_node = MemoryNode(key, value)
            cur_node.prev = self.memory_head
            cur_node.next = self.memory_head.next
            self.memory_head.next.prev = cur_node
            self.memory_head.next = cur_node
            self.mapping[key] = cur_node
            self.volume += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)