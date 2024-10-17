# 1 Oktober
## Planering
Today I've written a plan for the team. This plan included what each person is supposed to do. We haven't planed when things are supposed to be done. Everyone has their own main objectives, we have decided that you can do other things to so you don't have to work on only the main objective.
## MenuStore
We decided that my main objective is to work with MenuStore. I've decided to work with MySQL. I sadly missed yesterdays lecture so I read the pdf and have been trying to understand how SQL and RDBMS works. Haven't really understood evertyhing yet, I will use the internet to understand more about SQL and Database Management. 

**Information about our planing and To-DO list is in our repository. BurgerOrderer/Planering/planering.md**

# 11 Oktober
Yesterday I forgot to write in my engineer-diary. Yesterday I was trying to get our MenuStore container to work correctly and understand how to code SQL and how the database works, wasn't very succsesfull. Today I'm gonna watch videos from the YouTube channel freeCodeCamp.org so I can really understand how databases and SQL work because right now I don't understand much of what I'm supposed to do.

# 12 Oktober
I now know hot make the tabels on a basic level. I've realized that I don't need to code in SQL strictly and that SQLAlchemy is enough, which makes this alot easier. Connacted a friend in another group to understand this.

# 17 Oktober
I've completed MenuStore and now it works but we don't really know if works as it is supposed do. I've also done my debug session and here is how it went:
I'm pressing F5 while I'm running the app.py in MenuStore. I can see that variables like Flask.__init__ = None and SQLAlchemy.__init__ = None has been created. I'm pressing F11 to "Step into" the code so I can see what happens each line. I know a bit about how debuging works already from using Thonny while coding python. I now realize that I could just use the Python Debugger exention for future projects, this will make coding alot easier. I'm looking inside different functions and methods to see what they do more precisely. For example in burger_id I can look at the inside and I find things like special variables, function variables and class variables. When I go into functions and hover my mouse over it's name I can see what the function expects to receive. I will be honest and say that I don't understand everything ofcourse, but the basics. When I'm in a class and press "Step out" I get back to the line where the class is created. Pressing the "Restart" button gets me back to the first breakpoint. If I press "Continue" it skips to the next breakpoint. If I'm on a line where a class is created and press "Step over", it skips all the content in that class. Overall seems like debugging is a great tool for when programming in the future.
