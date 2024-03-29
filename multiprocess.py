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
