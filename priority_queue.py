class MaxPriorityQueue:
  # Do whatever setup you need here (this is not directly autograded)
  def __init__(self):
    self.pq = list()
    self.len = 0
 
  # Insert the given key into the priority queue
  #   This isn't directly autograded, but will vary depending on your implementation
  #   Does not need to return anything
  #   You may assume key is always an integer 
  def insert(self, key):
    self.len += 1
    key_index = self.len-1
    self.pq.append(key)
    parent_index = (key_index-1)//2
    while key_index > 0:
        if self.pq[parent_index] < key:
            self.pq[key_index], self.pq[parent_index] = self.pq[parent_index], self.pq[key_index]
            key_index = parent_index
            parent_index = (key_index-1)//2
        else:
            break
        

  # Return the value of the largest item in the PQ
    # However, do NOT remove this item. Peek should not modify your PQ at all, it is readonly
    # If your PQ is empty, return None
  def peek_max(self):
    return self.pq[0] if self.pq else None

  # Return the value of the largest item in the PQ AND remove it
    # If your PQ is empty, return None
  def pop_max(self):
    if not self.pq:
        return None
    if len(self.pq) == 1:
        popped = self.pq.pop()
        self.len -= 1
        return popped
    self.len -= 1
    self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
    maximum = self.pq.pop()
    cur_index = 0
    while cur_index < self.len:
        left = cur_index * 2 + 1
        right = cur_index * 2 + 2
        largest_index = cur_index
        if left < self.len and self.pq[left] > self.pq[largest_index]:
            largest_index = left
        if right < self.len and self.pq[right] > self.pq[largest_index]:
            largest_index = right
        if cur_index == largest_index:
            return maximum
        self.pq[cur_index], self.pq[largest_index] = self.pq[largest_index], self.pq[cur_index]
        cur_index = largest_index
    

  # Should return the number of items in the PQ as an integer
  def __len__(self):
    return self.len
