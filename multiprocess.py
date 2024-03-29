"""基于进程的并行"""

'Process类'
# from multiprocessing import Process
# import os

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info('function f')
#     print('hello', name)
    
# if __name__ == "__main__":
#     info('main line')
#     p = Process(target = f, args = ('bob',))
#     # 生成进程
#     p.start()    
#     p.join()
    
'上下文和启动方法'
# import multiprocessing as mp

# def foo(q):
#     q.put('hello')
    
# if __name__ == "__main__":
#     # 设置启动方法
#     # mp.set_start_method('spawn')
#     # q = mp.Queue()
#     # p = mp.Process(target = foo, args = (q,))
#     ctx = mp.get_context('spawn')
#     q = ctx.Queue()
#     p = ctx.Process(target = foo, args = (q,))
#     p.start()
#     print(q.get())
#     p.join()
    
'在进程之间交换对象'
###队列：put(), get()###
# from multiprocessing import Process, Queue

# def f(q):
#     q.put([42, None, 'hello'])
    
# if __name__ == "__main__":
#     q = Queue()
#     p = Process(target = f, args = (q,))
#     p.start()
#     print(q.get())
#     p.join()
    
###管道：send(), recv()###
# from multiprocessing import Process, Pipe

# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
    
# if __name__ == "__main__":
#     # 连接管道的两端
#     parent_conn, child_conn = Pipe()
#     p = Process(target = f, args = (child_conn,))
#     p.start()
#     print(parent_conn.recv())
#     p.join()

'进程间同步'
# from multiprocessing import Process, Lock

# def f(l, i):
#     # 锁机制
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()

# if __name__ == "__main__":
#     lock = Lock()
#     for num in range(10):
#         p = Process(target = f, args = (lock, num))
#         p.start()
#         p.join()

'进程间共享状态'
###共享内存: Value, Array###
# from multiprocessing import Process, Value, Array

# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]
        
# if __name__ == "__main__":
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))
#     p = Process(target = f, args = (num, arr))
#     p.start()
#     p.join()
#     print(num.value)
#     print(arr[:])
    
###服务进程: Manager()###
# from multiprocessing import Process, Manager

# def f(d, i):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     i.reverse()
    
# if __name__ == "__main__":
#     # Manager返回的管理器对象控制着服务进程
#     # 该进程保存对象并允许其他进程来代理操作
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list(range(10))
#         p = Process(target = f, args = (d, l))
#         p.start()
#         p.join()
#         print(d)
#         print(l)

'使用工作进程'
     
