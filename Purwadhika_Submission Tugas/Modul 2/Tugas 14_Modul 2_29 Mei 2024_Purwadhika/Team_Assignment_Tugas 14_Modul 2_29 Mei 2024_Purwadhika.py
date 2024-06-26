import mysql.connector
from mysql.connector import Error

def Menu(connection):
    while True:
        print('------ Phone Number Dashboard ------')
        print('1. Add New Phone Number Data Option\n2. Change Phone Number Data Option\n3. Delete Phone Number Data Option\n4. Phone Number Database Option\n5. Exit')

        try:
            user_input = int(input('Choose Menu [1-5] : '))
        except ValueError:
            print('Choose a Valid Input\n')
            continue

        if user_input == 1:
            PostMenu(connection)
        elif user_input == 2:
            UpdateMenu(connection)
        elif user_input == 3:
            DeleteMenu(connection)
        elif user_input == 4:
            GetMenu(connection)
        elif user_input == 5:
            print('Exiting and closing the connection...')
            connection.close()
            break
        else:
            print('Choose a Valid Input\n')

def PostMenu(connection):
    while True:
        print('------ Add New Phone Number ------')
        print('1. Add Phone Number\n2. Exit')

        try:
            user_input = int(input('Choose Menu [1-2] : '))
        except ValueError:
            print('Choose a Valid Input\n')
            continue
        
        if user_input == 1:
            # Name Validation
            while True:
                name = input('Name : ')
                if all(char.isalpha() or char.isspace() for char in name): 
                    break
                elif name == '':
                    print('400 Bad Request: Name Must be Filled\n')
                else: 
                    print('400 Bad Request: Name Input Should be Character Only.\n')
            
            # Phone Number Validation
            while True:
                phone_number = input('Phone Number : ')
                if not phone_number.isdigit():
                    print('400 Bad Request: Phone Number Must be Integer Only\n')
                elif not (11 <= len(phone_number) <= 13):
                    print('400 Bad Request: Phone Number Length Should be Between 11 and 13 Characters\n')
                else: 
                    break
            
            # Email Validation
            while True:
                email = input('Email : ')
                if '@' in email and '.' in email:
                    break
                else: 
                    print('400 Bad Request: Not a Valid Email Format (should have @ and .)\n')
            
            job = input('Job : ')
            
            PostUser(connection, name, phone_number, email, job)
        elif user_input == 2:
            break
        else:
            print('Choose a Valid Input\n')

def GetMenu(connection):
    while True:
        print('------ Phone Number Database ------')
        print('1. All Phone Number\n2. Choose a Phone Number\n3. Search by Name\n4. Exit')
        try:
            user_input = int(input('Choose Menu [1-4] : '))
        except ValueError:
            print('Choose a Valid Input\n')
            continue
        
        if user_input == 1:
            GetAll(connection)
        elif user_input == 2:
            user_id = int(input('Input Id : '))
            GetById(connection, user_id)
        elif user_input == 3:
            name = input('Input Name : ').lower()
            GetByName(connection, name)
        elif user_input == 4:
            break
        else:
            print('Choose a Valid Input\n')

def UpdateMenu(connection):
    while True:
        print('------ Change Phone Number ------')
        print('1. Change Phone Number\n2. Exit')
        
        try:
            user_input = int(input('Choose Menu [1-2] : '))
        except ValueError:
            print('Choose a Valid Input\n')
            continue
        
        if user_input == 1:
            user_id = int(input('Input Id : '))
            name = input('New Name (leave blank if no change) : ')
            phone_number = input('New Phone Number (leave blank if no change) : ')
            email = input('New Email (leave blank if no change) : ')
            job = input('New Job (leave blank if no change) : ')
            UpdateById(connection, user_id, name if name else None, phone_number if phone_number else None, email if email else None, job if job else None)
        elif user_input == 2:
            break
        else:
            print('Choose a Valid Input\n')

def DeleteMenu(connection):
    while True:
        print('------ Delete Phone Number ------')
        print('1. Delete One Phone Number\n2. Delete All Phone Number\n3. Exit')
        
        try:
            user_input = int(input('Choose Menu [1-3] : '))
        except ValueError:
            print('Choose a Valid Input\n')
            continue
        
        if user_input == 1:
            user_id = int(input('Input Id : '))
            DeleteById(connection, user_id)
        elif user_input == 2:
            confirm = input('Delete All Users? (y/n) : ')
            if confirm.lower() == 'y':
                DeleteAll(connection)
        elif user_input == 3:
            break
        else:
            print('Choose a Valid Input\n')

####### CREATE/POST #######
def PostUser(connection, name, phone_number, email, job):
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO tb_kel7 (name, phone_number, email, job) VALUES (%s, %s, %s, %s)', 
                       (name, phone_number, email, job))
        connection.commit()
        print('User berhasil dibuat.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        cursor.close()

######## READ/GET ########
def GetAll(connection):
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM tb_kel7')
        result = cursor.fetchall()
        if not result:
            print('404 Not Found: No Contact Found\n')
        else:
            headers = ['Id', 'Name', 'Phone Number', 'Email', 'Job']
            print('200 OK: All Contacts Retrieved Successfully\n')
            print(DataFrame(result, headers))
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        cursor.close()

def GetById(connection, user_id):
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM tb_kel7 WHERE id = %s', (user_id))
        result = cursor.fetchone()
        if not result:
            print(f'404 Not Found: Id {user_id} not found\n')
        else:
            headers = ['Id', 'Name', 'Phone Number', 'Email', 'Job']
            print(DataFrame([result], headers))
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        cursor.close()

def GetByName(connection, name):
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM tb_kel7 WHERE name LIKE %s)', ('%' + name + '%'))
        result = cursor.fetchall()
        if not result:
            print(f'404 Not Found: No Contact Found with Name Starts From {name}.\n')
        else:
            headers = ['Id', 'Name', 'Phone Number', 'Email', 'Job']
            print('200 OK: Successfully Retrieved Contacts by Name\n')
            print(DataFrame(result, headers))
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        cursor.close()

####### UPDATE/PUT #######
def UpdateById(connection, user_id, name = None, phone_number = None, email = None, job = None):
    cursor = connection.cursor()
    try:
        update_fields = []
        update_values = []
        if name:
            update_fields.append('name = %s')
            update_values.append(name)
        if phone_number:
            update_fields.append('phone_number = %s')
            update_values.append(phone_number)
        if email:
            update_fields.append('email = %s')
            update_values.append(email)
        if job:
            update_fields.append('job = %s')
            update_values.append(job)
        
        update_values.append(user_id)
        update_query = f"UPDATE tb_kel7 SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(update_query, tuple(update_values))
        connection.commit()
        print('User berhasil diperbarui.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        cursor.close()

######## DELETE ########
def DeleteById(connection, user_id):
    cursor = connection.cursor()
    try:
        cursor.execute('DELETE FROM tb_kel7 WHERE id = %s', (user_id))
        connection.commit()
        print(f'200 OK: Contact with id {user_id} has been deleted\n')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        cursor.close()

def DeleteAll(connection):
    cursor = connection.cursor()
    try:
        cursor.execute('DELETE FROM tb_kel7')
        connection.commit()
        print('200 OK: All contacts have been deleted\n')
        
        # Index Reordering
        try:
            cursor.execute("SET @count = 0;")
            cursor.execute("UPDATE tb_kel7 SET id = @count := @count + 1;")
            connection.commit()
            print('Index Reordered\n')
        except mysql.connector.Error as err:
            print(f'Error: {err}')
            
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        cursor.close()

def DataFrame(data, headers):
    col_widths = [
        max(len(str(row[i])) for row in ([headers] + data))
        for i in range(len(headers))
    ]
    
    format_str = ' | '.join(f"{{:<{width}}}" for width in col_widths)
    separator = '-+-'.join('-' * width for width in col_widths)
    
    table_str = format_str.format(*headers) + '\n' + separator + '\n'
    for row in data:
        formatted_row = [str(cell) if cell is not None else 'None' for cell in row]
        table_str += format_str.format(*formatted_row) + '\n'
    
    return table_str

def register(new_user, new_password, host='localhost'):
    try:
        # MySQL Connection using user with high privilige
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'db_kel7'
        )
        
        cursor = connection.cursor()

        # Create New User
        create_user_query = f'CREATE USER "{new_user}"@"{host}" IDENTIFIED BY "{new_password}";'
        cursor.execute(create_user_query)

        # Give DBManager Role (Database Management) to new user
        grant_privileges_query = f'GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON *.* TO "{new_user}"@"{host}";'
        cursor.execute(grant_privileges_query)

        # MSave Changes
        cursor.execute('FLUSH PRIVILEGES;')
        
        print(f'User "{new_user}" created successfully with DBManager privileges.')

        # Close Cursor and Connection
        cursor.close()
        connection.close()

        # Go to Main Menu with New Registered User
        connection = mysql.connector.connect(
            host = 'localhost',
            user = new_user,
            password = new_password,
            database = 'db_kel7'
        )
        Menu(connection)
    
    # Error Check
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)

def login(username, password):
    try:
        # Database Connection
        connection = mysql.connector.connect(
            host = 'localhost',
            user = username,
            password = password,
            database = 'db_kel7'
        )
        
        # Check Connection
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute('SELECT DATABASE();')
            database_name = cursor.fetchone()[0]
            print(f'Connection successful. Connected to database: {database_name}')
            Menu(connection)
            return True
    except Error as err:
        print(f'Error: {err}')
    
    print('Failed to connect to the database.')
    return False

register('kelompok7', 'kelompok7')
# login('kelompok7', 'kelompok7')