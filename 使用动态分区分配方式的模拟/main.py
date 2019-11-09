from prettytable import PrettyTable
from copy import copy

memory_blocks = []

class memory_block():
  def __init__(self, start, end, id, size, state):
    self.start = start
    self.end = end
    self.id = id # 如果没有为‘none’
    self.size = size
    self.state = state
  
  def return_list(self):
    return [self.start, self.end, self.id, self.size, self.state]

def print_table():
  global memory_blocks
  table = PrettyTable(["起始地址", "终止地址", "作业id", "分配大小", "状态"])
  for mb in memory_blocks:
    table.add_row(mb.return_list())
  print(table)

def get_choice(type, size):
  global memory_blocks
  free_block = []
  for i, mb in enumerate(memory_blocks):
    if mb.size >= size and mb.state == 'free':
      free_block.append((mb.size, i))
  
  if not free_block:
    return None

  if type == 'best':
    free_block.sort(key=lambda x:x[0])

  return free_block[0][1]

def alloc(id, size, type):
  global memory_blocks
  num = get_choice(type, size)
  if num == None:
    print("内存空间不足")
    return "ERROR"

  tmp = memory_blocks[num]
  occupied = memory_block(tmp.start, tmp.start+size, id, size, 'occupied')
  freed = memory_block(tmp.start+size, tmp.end, 'none', tmp.size - size, 'free')
  memory_blocks = memory_blocks[0:num] + [occupied, freed] + memory_blocks[num+1:]
  merge()

def free(id, type):
  global memory_blocks
  num = None
  for i, mb in enumerate(memory_blocks):
    if mb.id == id:
      num = i 
  
  if num == None:
    print("没有这样的进程")
    return "ERROR"

  memory_blocks[num].id = 'none'
  memory_blocks[num].state = 'free'
  merge()

def merge():
  global memory_blocks
  blocks = [memory_blocks[0]]
  for i, mb in enumerate(memory_blocks[1:]):
    last = memory_blocks[i]
    if mb.state == last.state and mb.id == last.id: # 碰上两个相同的状态
      mb = memory_block(last.start, mb.end, mb.id, last.size+mb.size, mb.state)
      blocks.pop()
      blocks.append(mb)
    else:
      blocks.append(mb)
  memory_blocks = blocks

def agent(id, action, size, type):
  '''
  id 作业id，action in ["alloc", "free"], 
  size 如果是 free 为0
  type = [first, best]
  '''
  global memory_blocks
  print(f"\n{action}(process[{id}]), size={size}")
  if action == 'alloc':
    alloc(id, size, type)
  if action == 'free':
    free(id, type)
  print_table()

def inititate():
  global memory_blocks
  memory_blocks.append(memory_block(0, 640, 'none', 640, 'free'))

if __name__ == '__main__':
  works = eval(open('input').read())
  choice = input("\
    1. 首次适应算法\n\
    2. 最佳适应算法\n\
    输入你想要使用的算法：\
  ")
  type = ['first', 'best'][int(choice)-1]
  inititate()
  for work in works:
    agent(work['id'], work['action'], work['size'], type)
