# Speed It Up
# Parallelize It
# Life of a Thread
# Synchronization between Threads
# Communication between Threads
# Debug and Benchmark
# Executors and Pools
# Multiprocessing
# Event-Driven Programming
# Reactive Programming
# Using the GPU
# Choosing a solution

# W'LL USE THESE LIBRARIES/TOOLS/SOFTWARES:
#   Beautiful Soup          // $ pip install beautifulsoup4
#   RxPy                    // $ pip install rx
#   Anaconda                // https://www.anaconda.com/download/
#   Theano                  // $ pip install Theano
#   PyOpenCL                // https://wiki.tiker.net/PyOpenCL/Installation/Windows

# Getting the most out of your software is something all developers strive for, and concurrency, 
# and the art of concurrent programming, happens to be one of the best ways in order for you to 
# improve the performance of your applications. 

# Gone are the days of unresponsive programs that give you no indication as to whether they’ve 
# crashed or are still silently working.

# By choosing to implement systems in a concurrent fashion, we typically see an increase in the
# overall complexity of our code, and a heightened risk for bugs to appear within this new code.
#
# Dijkstra then went on to define fundamental concurrency concepts, such as semaphores, mutual
# exclusions, and deadlocks as well as the famous Dijkstra’s Shortest Path Algorithm.
#
# The introduction of high-level concurrency primitives and better native language support have
# really improved the way in which we, as software architects, implement concurrent solutions.
#
#
#
# WHAT IS A THREAD?
#   - A thread can be defined as an ordered stream of instructions that can be scheduled to run as
#     such by operating systems.
#   - These threads, typically, live within processes, and
#   - Consist of a program counter, a stack, and a set of registers as well as an identifier.
#   - These threads are the smallest unit of execution to which a processor can allocate time.
#
# Threads are able to interact with shared resources, and communication is possible between
# multiple threads.
# They are also able to share memory, and read and write different memory addresses.
#
# When two threads start sharing memory, and you have no way to guarantee the order of a thread's
# execution, you could start seeing issues or minor bugs.
#
# These issues are, primary, caused by race conditions.
#
# Within a typical operating system, we, typically, have two different types of threads:
#   - User-level threads
#   - Kernel-level threads
#
# Python works at the user-level.
#
# - In a single-threaded program, there would only be one person working in this office at all
# times, handling all of the work in a sequential manner.
#
# - With multithreading, our single solitary worker becomes an excellent multitasker, and is able
# to work on multiple things at different times. (By being able to switch context when something is
# blocking them, they are able to do far more work in a shorter period of time, and thus make our
# business more money.)
#
#
# ADVANTAGES OF THREADING:
#   - Multiple threads are excellent for speeding up blocking I/O bound programs.
#   - They're lightweight in terms of memory footprint when comared to processes.
#   - Threads share resources, and thus communication between them is easier
#
# DISADVANTAGES:
#   - CPython threads are hamstrung by the limitations of the global interpreter lock (GIL).
#   - While comminucation between threads may be easier, you must be very careful not to implement
#     code that is subject to race conditions.
#   - It's computationally expensive to switch context between multiple threads. By adding multiple
#     threads, you could see a degradation in your program's overall performance.
#
#
# PROCESSES
#   - they are not bound to a singular CPU core.
# if we had a four core CPU, then we can hire two dedicated sales team members and two workers, and
# all four of them would be able to execute work in parallel.
#
# These processes contain one main primary thread, but can spawn multiple sub-threads that each
# contain their own set of registers and a stack.
#
