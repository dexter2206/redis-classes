## Suggested exercises
1. Write a program that prints how many times it has been run.

2. Suppose you are writing computation-heavy function (accepting one argument) that will be used
   multiple times, possibly with the same argument. Unfortunately, different
   invocations may occur during different program runs, and therefore you
   cannot use built-in lru_cache decorator. Can you implement similar cache using
   Redis? Mock this behaviour for some simple function and test it by logging 
   actual function invocations and cache hits.

2. Implement a simple microblog using Redis lists

   Pick your usser name. We will publish to the list  named <user_name>:blog.
   Suppose our microblog will hold at most 10 entries for every user (at most).
   
   Write an app that allows you to add new wntries to the list with the
   name specified above. Make sure that the list is never longer than 10
   elements.
   
   Write a second app that allows you to view entries published by
   other user, specified as an input to the program.
   
 3. Write a mock of a simple voting app using Redis sets and strings. 
    Suppose we can vote for three options: black, red, blue. The app should accept
    user name and his/her vote, then display current state of the scoreboard.
    However, the vote should not be accepted if the given user has already voted.
    
 4. Reimplement exercise 3. using sorted sets.
 
 5. Think of the following problem of simplified throttling. Suppose that
    you are writing a web application that performs some computational intensive
    task. For that reason, you would like to allow only limited number of
    requests in given time time window (say 5 every minute). Can we use Redis
    to implement such a mechanism?
    
    Note: in this exercise we consider only time windows that start at full minute
    , i.e. you don't
    want more than 5 requests between 21:37:00 and 21:37:59 or between
    6:15:00 and 6:15:59. However, you are not required to enforce this limit
    for windows like 8:30:27-8:31:27.
    
 