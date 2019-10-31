# 使用动态优先权的进程调度算法模拟

1、实验目的

通过动态优先权算法的模拟加深对进程概念进程调度过程的理解。

2、实验内容

（1）用C语言来实现对N个进程采用动态优先权优先算法的进程调度。

（2）每个用来标识进程的进程控制块PCB用结构来描述，包括以下字段：

- 进程标识数 ID。

- 进程优先数 PRIORITY，并规定优先数越大的进程，其优先权越高。

- 进程已占用的CPU时间CPUTIME。

- 进程还需占用的CPU时间ALLTIME。当进程运行完毕时，ALLTIME变为0。- 进程的阻塞时间STARTBLOCK，表示当进程再运行STARTBLOCK个时间片后，将进入阻塞状态。

- 进程被阻塞的时间BLOCKTIME，表示已足赛的进程再等待BLOCKTIME个时间片后，将转换成就绪状态。

- 进程状态START。

- 队列指针NEXT，用来将PCB排成队列。

（3）优先数改变的原则：

- 进程在就绪队列中呆一个时间片，优先数加1。

- 进程每运行一个时间片，优先数减3。

（4）假设在调度前，系统中有5个进程，它们的初始状态如下：

| ID         | 0     | 1     | 2     | 3     | 4     |
| ---------- | ----- | ----- | ----- | ----- | ----- |
| PRIORITY   | 9     | 38    | 30    | 29    | 0     |
| CPUTIME    | 0     | 0     | 0     | 0     | 0     |
| ALLTIME    | 3     | 3     | 6     | 3     | 4     |
| STARTBLOCK | 2     | -1    | -1    | -1    | -1    |
| BLOCKTIME  | 3     | 0     | 0     | 0     | 0     |
| STATE      | READY | READY | READY | READY | READY |

（3）  为了清楚的观察各进程的调度过程，程序应将每个时间片内的情况显示出来，参照的具体格式如下：

```
RUNNING PROG：i
READY-QUEUE：-〉id1-〉id2
BLOCK-QUEUE：-〉id3-〉id4
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = == = =
ID                       	0      1      2      3      4

PRIORITY                	P0     P1     P2     P3     P4

CUPTIME                		C0     C1     C2     C3     C4

ALLTIME                		A0     A1     A2     A3     A4

STARTBLOCK            		T0     T1     T2     T3     T4

BLOCKTIME             		B0     B1     B2     B3     B4

STATE                   	S0     S1     S2     S3     S4
```

