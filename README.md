# E-Commerce ![Django](https://github.com/ESWZY/cs50web-final-project/workflows/Django%20CI/badge.svg)

  ## An e-commerce Mobile Responsive Website powered by [Django](https://www.djangoproject.com/) using [Python](https://www.python.org/) ,in which a user can view 
  a watch list , craete & upload new item and delete it  as well as some other features :
   - add item to favourites 
   - remove item from favourites
   - place bids
   - end bids
   - add comments
   - view favourites list
   

# Project Structure


## HTML Files
      
 - index.html
   - this page dispalys the active listing (available items could be bet on)
    
 - login.html
   - user has to login in order to participate in  any class 
 
 - Register.html
   - a page in which a user with no previous interaction with this site has to register to be able to use this website
   
 - listing.html 
   - displays item details where a user can place a bet , add a comment and rate items 
   
 - create.html 
   - a page in which a user can create new item
    
 - watchlist.html 
   - displays favourites list (liked items )
   

## JS Files
 -  main.js (include all the functions to handle and manipulate the DOM, using json and Ajax)



# Backend


## Python Files
 - models.py(includes 4 models (user,classes,membership,user_class)
   - it includes 4 models
      - User model (saves user logging data )
      - Email model(handles all the data including sender, reciever,body,date,read or not and archived ones )
      
 - views.py (include different functions such as class_capacity , user,membershipinfo ,join,add)
     - it includes functions
         - listing  
         - create
         - remove
         - comments
         - close
 - urls.py (include routes(add,user,membershipinfo) as well as API routes(join, class_capacity)
   - routes(Paths):-
      - /
      - /register
      - /logout
      - /login
     
   - API routes:-
      - /listing 
      - /watchlist
      - /create
      - /remove
      - close



# Setup
   ```shell script
git clone https://github.com/oi19/e-commerce
cd e-commerce
```
Run the following command to run your server.


```shell script
python manage.py runserver
```

Run those following commands to migrate database.

```shell script
python manage.py makemigrations
python manage.py migrate
```

