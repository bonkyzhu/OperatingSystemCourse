'''
使用动态优先权的进程调度算法模拟.py
'''
from prettytable import PrettyTable 
from queue import PriorityQueue as PQ
from asyncio import sleep 

# 下面这个PCB
# 状态四种： READY, BLOCK, END, RUNING
Process0 = {'ID':0,'PRIORITY':9, 'CPUTIME':0, 'ALLTIME':3, 'STARTBLOCK':2, 'BLOCKTIME':3, 'STATE':'READY'}
Process1 = {'ID':1,'PRIORITY':38, 'CPUTIME':0, 'ALLTIME':3, 'STARTBLOCK':-1, 'BLOCKTIME':0, 'STATE':'READY'}
Process2 = {'ID':2,'PRIORITY':30, 'CPUTIME':0, 'ALLTIME':6, 'STARTBLOCK':-1, 'BLOCKTIME':0, 'STATE':'READY'}
Process3 = {'ID':3,'PRIORITY':29, 'CPUTIME':0, 'ALLTIME':3, 'STARTBLOCK':-1, 'BLOCKTIME':0, 'STATE':'READY'}
Process4 = {'ID':4,'PRIORITY':0, 'CPUTIME':0, 'ALLTIME':4, 'STARTBLOCK':-1, 'BLOCKTIME':0, 'STATE':'READY' }
All_Process = [ Process0,Process1,Process2,Process3,Process4 ]

class PriorityQueue(PQ):
  '''
  优先队列
  '''
  def __init__(self, *option):
    super().__init__(*option)
    self.record = []

  def put(self, Process):
    if Process['PRIORITY'] >= 0:
      item = (-Process['PRIORITY'], Process['ID'])
    # else:
    #   item = (F , Process['ID'])
    # if Process['ID'] not in self.record:
      super().put(item)
    #else:
     # self.record.append(Process['ID'])

  def get(self):
    item_id = super().get()[1]
    return All_Process[item_id]

  def allelem(self):
    ''' 
    获得所有的队列元素按照优先顺序, 返回elems
    '''
    size = self.qsize() 
    elems = []
    ans = []

    for i in range(size):
      elem = self.get() 
      elems.append(elem)

    for elem in elems:
      self.put(elem)

    for elem in elems:
      ans.append(elem['ID'])
    return ans

  def check(self, id):
    elem = self.allelem()
    for e in elem:
      if e == id:
        return True

def printTable(now_running):
  '''
  打印表格
  '''
  table = PrettyTable(list(Process0.keys()))
  for i in range(5):
    table.add_row(list(All_Process[i].values()))
  print(f"Running: Process {now_running['ID']}")
  print(f"Ready list: {Ready_Queue.allelem()}")
  print(f"Block list: {Block_Queue.allelem()}")
  print(table)

def compute_Priority(Process):
  '''
  进行优先级的加减
  '''
  if Process['STATE'] == 'READY':
    Process['PRIORITY'] += 1
  if Process['STATE'] == 'RUNNING':
    Process['PRIORITY'] -= 3

def to_END(Process):
  '''
  检查是否满足结束条件，满足即设置为END，否则ALLTIME减去1
  '''
  if Process['ALLTIME'] != 0 and Process['STATE'] == 'RUNNING':
    Process['ALLTIME'] -= 1
  return Process['ALLTIME'] == 0

def to_BLOCK(Process):
  '''
  检查是否满足阻塞条件，满足即设置为END，否则ALLTIME减去1
  '''
  if Process['STARTBLOCK'] == 0:
    return False
  if Process['STARTBLOCK'] != 0 and Process['STATE'] == 'RUNNING':
    if Process['STARTBLOCK'] != -1:
        Process['STARTBLOCK'] -= 1
  return Process['STARTBLOCK'] == 0 

def to_READY(Process):
  if Process['STATE'] == 'BLOCK' and Process['BLOCKTIME'] != 0:
    Process['BLOCKTIME'] -= 1
  return Process['BLOCKTIME'] == 0

def to_Finish():
  for i in range(5):
    if All_Process[i]['STATE'] != 'END':
      return False
  return True

Ready_Queue = PriorityQueue()
Block_Queue = PriorityQueue()

def initiate():
  for process in All_Process:
    Ready_Queue.put(process)
  # print(Ready_Queue.allelem())

def main():
  initiate()
  while(not to_Finish()):
    now_running = Ready_Queue.get()
    run_ID = now_running['ID']
    All_Process[run_ID]['STATE'] = 'RUNNING'
    printTable(now_running)

    for process in All_Process:
      compute_Priority(process)
      if process['STATE'] == 'RUNNING':
        process['CPUTIME'] += 1
        if to_BLOCK(process):
          Block_Queue.put(process)
          process['STATE'] = 'BLOCK'

        elif to_END(process):
          process['PRIORITY'] = 0
          process['STATE'] = 'END'

        else:
          process['STATE'] = 'READY'
          Ready_Queue.put(process)

      elif process['STATE'] == 'BLOCK':
        if to_READY(process):
          Ready_Queue.put(process)
          Block_Queue.get()
          process['STATE'] = 'READY'
      
  printTable(now_running)

if __name__ == '__main__':
  main()