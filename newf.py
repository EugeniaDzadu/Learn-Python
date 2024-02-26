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
        def add_title(todo_database):
         user_title=(input('Enter title: \n'))
         if todo_database.count(user_title) < 1:
          todo_database.append(user_title)
          print('Todo saved successfully')
         else :
          print('Todo already exists')
        add_title(todo_database)
          
    elif user_input == 2:
        def remove_title(todo_database):
          user_remove=(input('Enter title to remove: \n'))
          if len(todo_database)!=0:
           if user_remove in todo_database:
            todo_database.remove(user_remove)
            print('Todo removed successfully')
           else:
            print('Title does not exist in the database')
          else:
           print('Database is empty')
          remove_title(todo_database)  
        
    elif user_input == 3:
        def update(todo_database):
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
            update(todo_database)
            
    elif user_input == 4:
       def viewtab(todo_database):
            if len(todo_database)!=0:   
             for i in todo_database:
              print(i)
            else:
              print('You do not have any data in the database')
            viewtab(todo_database)
            
    elif user_input == 5:
       exit(0)
    else:
       print('Invalid user input')
              
option = start_todo()
user_option(option)