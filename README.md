# fibonacci-web : Fibonacci number generation with a web service

Description
~~~~~~~~~~~
Simple program to generte fibonacci numbers using python backend
  - A running sample available at : http://ec2-52-25-171-250.us-west-2.compute.amazonaws.com:8081/
  - Author : Rajat Jain (rjain@us.ibm.com)
  - Licensing : None


File List
~~~~~~~~~~~
fibonacci_web.py
templates/fibonacci_web.html

Instructions to build and deploy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. On any generic Linux, have python packages (>=2.7)  and web.py (easy_install web.py) installed
2. Run and test as follows :
      python fibonacci_web.py 8081  
      http://localhost:8081
      Note : A running instance is vailable at : http://ec2-52-25-171-250.us-west-2.compute.amazonaws.com:8081/

Unit test details
~~~~~~~~~~~~~~~~~
1. Web Input test - PASS
   Basic input validation on http forms
2. Web Refresh test - FAIL
   Refresh , Reload not working. URL has to be posted each time in a new instance 
3. Server stability - NOT PERFORMED
   If backend python crashes, it is not monitored
   Python code needs code analysis to determine possible runtime crashes
4. Optimization test - PASS
   Recursive python function is not being called multiple times for same number
5. Multiple client test - NOT PERFORMED
6. Browser test - PASS
   Only tested with FF 38.5.2 and Chrome 47.0.2526

Known issues
~~~~~~~~~~~~
1. Code needs comments (yeah, I am lazy..., but when this is a real project, I'll not skip it....)
2. Refresh , Reload not working. URL has to be posted each time in a new instance 


Future solutions / changes considered (but not implemented)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Fix known issues
2. DB caching for multiple clients and instances can be used, as fibonacci sequence is deterministic. Db/network latency to retrieve previously genrted numbers should be considered over compute bottlenecks.
3. Backend web.py web hosting may not scale well for enterprise solutions, so it may need to be replaced. (The actual fibonacci generation algorithm seems optimized though)
