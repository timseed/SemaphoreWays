#Semaphore Tests

Background: Due to work-flow processing I do not want to have two processes running, both using the same code. I essentially need to create a Semaphore to ensure that I only have 1 process running at the same time.


However as this process is created bya crontab event, it needs to be robust.


I initially got a model that was working with Threads working. This was nice and clean, however when I moved the code into Two seperate Python Files, becuase each Python thread was independant - they both run.

This code can be found in **main.py**.


##Independent Processes

Using a test script called **test.sh**, I start 2 processes. There are 3 pieces to this


  - Lock.py
  
    A simple class to handle the Synchronisation. 
    Please note: At the moment this will only work on 1 Machine and not in a distrubuted enviroment. 
    
  - ipc1.py
  
     Process 1 - which starts work, and then finishes.
     
  - ipc2.py
  
      Process 2 - which tries to start work, but finds process 1 is already underway. So it has to wait, then it starts work.
      
#Versions

I have tested this on Python 3.6, Ubuntu 14, and Mac OS 11.3.

     