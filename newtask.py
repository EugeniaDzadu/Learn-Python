# Create a simple todo list, which allows users to 
# *Add a todo
# *update a todo
# *remove a todo
# *Exit app

#NB
# * User's are allowed to store as many todo's they wish
# * User's should not be able to remove students, if the database is empty (  len   )
# * User's should not be able to add the same Todo's
todo_database = []
def start_todo():
   user_input = 0
   
   while user_input != 5:
     user_input = int(input('*****Todo list for Eugenia***** \n' 
             '1. Add Todo \n'
             '2. Remove Todo \n'
             '3. Update Todo \n'
             '4. View Todos \n'
             '5. Exit app \n\n'
             'Provide option: '))
     return user_input


def user_option(user_input):
    if user_input == 1:
       add_title()

    elif user_input == 2:
       remove_title()
       
    elif user_input == 3:
       update()
        
    elif user_input == 4:
       viewtab()
       
    elif user_input == 5:
       exit(0)
    else:
       print('Invalid user option, try again')
      
    user_option( start_todo()   )
 
 
def add_title():
       user_title=(input('Enter title: \n'))
       if todo_database.count(user_title) < 1:
         todo_database.append(user_title)
         print('Todo saved successfully')
       else :
         print('Todo already exists')
         
         
def remove_title():
       user_remove=(input('Enter title to remove: \n'))
       if len(todo_database)!=0:
        if user_remove in todo_database:
            todo_database.remove(user_remove)
            print('Todo removed successfully')
        else:
           print('Title does not exist in the database')
       else:
          print('Database is empty')
          
def update():
       if len(todo_database) == 0:
          print('Database is empty, enter Todo')
       current_title = input('Enter title : ')
       if current_title in todo_database:
          user_update=input('Enter title to update: ')
          todo_database.remove(current_title)
          todo_database.append(user_update)
          print('Todo updated successfully')
       else:
          print('invalid title')
          
def viewtab():
       if len(todo_database)!=0:   
        for i in todo_database:
         print(i)
       else:
          print('You do not have any data in the database')
          

   
option = start_todo()
user_option(option)