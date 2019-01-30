from multiprocessing import Process
import os
def run_process(name):
    print("Run child process %s (%s)..."%(name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s' %(os.getpid()))
    p=Process(target=run_process,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print("Child process end")
