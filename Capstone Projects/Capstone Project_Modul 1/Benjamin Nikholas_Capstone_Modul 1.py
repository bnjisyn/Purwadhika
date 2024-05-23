contact_db = {
    0: {'Name': 'Alice', 'Phone Number': '08123456789', 'Email': 'alice@example.com', 'Job': 'Manager'},
    1: {'Name': 'Bob', 'Phone Number': '08234567890', 'Email': 'bob@gmail.com', 'Job': 'Security'},
    2: {'Name': 'Charles', 'Phone Number': '08345678901', 'Email': 'charles@example.com', 'Job': 'Developer'},
    3: {'Name': 'James', 'Phone Number': '08456789012', 'Email': 'james@example.com', 'Job': 'Analyst'},
    4: {'Name': 'Jack', 'Phone Number': '08567890123', 'Email': 'jack@example.com', 'Job': 'Designer'},
    5: {'Name': 'Charly', 'Phone Number': '08678901234', 'Email': 'charly@example.com', 'Job': 'Tester'},
    6: {'Name': 'Harold', 'Phone Number': '08789012345', 'Email': 'harold@example.com', 'Job': 'Manager'},
    7: {'Name': 'Andy', 'Phone Number': '08890123456', 'Email': 'andy@example.com', 'Job': 'Engineer'}
}

id = len(contact_db)

# Table Format Function
def DataFrame(data, headers):
  
    # Column width count
    col_widths = [
        max(len(str(row[i])) for row in ([headers] + data))
        for i in range(len(headers))
    ]
    
    # String Format
    format_str = ' | '.join(f"{{:<{width}}}" for width in col_widths)
    separator = '-+-'.join('-' * width for width in col_widths)
    
    # Making Table String
    table_str = format_str.format(*headers) + '\n' + separator + '\n'
    for row in data:
        formatted_row = [str(cell) if cell is not None else 'None' for cell in row]
        table_str += format_str.format(*formatted_row) + '\n'
    
    return table_str

# Reordering Indexes on Deleting a Data
def reorder_ids():
    global contact_db
    global id

    new_db = {}
    for new_id, old_id in enumerate(sorted(contact_db.keys())):
       new_db[new_id] = contact_db[old_id]

    contact_db = new_db
    id = len(contact_db)

####### CREATE/POST #######
def PostById():
    global id
    
    while True:
      name = input('Name : ')
      
      if all(char.isalpha() or char.isspace() for char in name):
        break
      elif name == '':
        print('400 Bad Request: Name Must be Filled\n')
      else:
        print('400 Bad Request: Name Input Should be Character Only.\n')
      
    while True:
      phone_num = input('Phone Number : ')
      if not phone_num.isdigit():
        print('400 Bad Request: Phone Number Must be Integer Only\n')
      elif not (11 <= len(phone_num) <= 13):
        print('400 Bad Request: Phone Number Length Should be Between 11 and 13 Characters\n')
      else:
        phone_num_valid = False
        for key, value in contact_db.items():
          if value['Phone Number'] == phone_num:
            phone_num_valid = True
            break
        if phone_num_valid:
          print('400 Bad Request: Phone Number is Already in the Database')
        else:
          break
      
    while True:
      email = input('Email : ')
      
      if '@' in email and '.' in email:
        break
      else: 
        print('400 Bad Request: Not a Valid Email Format (should have @ and .)\n')
    
    while True:
      job = input('Job : ')
      
      if not job.isalpha():
        print('400 Bad Request: Job input Should Be Character Only.\n')
      else: 
        break

    new_contact = {'Name': name, 'Phone Number': phone_num, 'Email': email, 'Job': job}
    headers = ['Id', 'Name', 'Phone Number', 'Email', 'Job']
    contact_db[id] = new_contact
    print(f'201 Created: New Contact Has Been Added with Id {id}')
    id += 1
    
    data = [[id-1, name, phone_num, email, job]]
    print(DataFrame(data, headers))

    return contact_db

####### READ/GET #######

# GET ALL
def GetAll():
  if not contact_db:
    print('404 Not Found: No Contact Found\n')
  else:
    headers = ['Id', 'Name', 'Phone Number', 'Email', 'Job']

    data = [
        [id,
         details['Name'],
         details['Phone Number'],
         details['Email'],
         details['Job']]
        for id, details in contact_db.items()
    ]
    print('200 OK: All Contacts Retrieved Successfully\n')
    print(DataFrame(data, headers))

# GET BY ID
def GetById():
  while True:
    try:
      id = int(input('Input Id : '))
    except ValueError:
      print('400 Bad Request: Id Should be Integer Only.\n')
    
    if id in contact_db.keys():
      headers = ['Id', 'Name', 'Phone Number', 'Email', 'Job']
      details = contact_db[id]
      data = [
          [id,
           details['Name'],
           details['Phone Number'],
           details['Email'],
           details['Job']]
      ]
      print(DataFrame(data, headers))
      break
    
    else:
      print(f'404 Not Found: Id {id} not found\n')

# GET BY NAME
def GetByName():
    search_string = input('Input Name : ').lower()
    results = [
        [id,
         details.get('Name'),
         details.get('Phone Number'),
         details.get('Email'),
         details.get('Job')]
        for id, details in contact_db.items()
        if details.get('Name').lower().startswith(search_string)
    ]
    
    if not results:
        print(f'404 Not Found: No Contact Found with Name Starts From "{search_string}".\n')
    else:
        headers = ['Id', 'Name', 'Phone Number', 'Email', 'Job']
        print('200 OK: Successfully Retrieved Contacts by Name\n')
        print(DataFrame(results, headers))

####### UPDATE/PUT #######
def UpdateById():
  while True:
    id = input('Input Id : ')
    
    if not id.isdigit():
      print('400 Bad Request: Id Should be Integer Only.\n')
    elif int(id) not in contact_db:
      print(f'404 Not Found: Contact with id {id} Not Found\n')
      return
    else:
      id = int(id)
      break
  
  while True:
    name = input('Input Name Change : ')
    
    if name == '':
        name = None
        break
    elif all(char.isalpha() or char.isspace() for char in name):
        break
    else:
        print('400 Bad Request: Name Input Should be Character Only.\n')
  
  while True:
      phone_num = input('Phone Number : ')
      if phone_num == '':
        phone_num = None
        break
      elif not phone_num.isdigit():
        print('400 Bad Request: Phone Number Must be Integer Only\n')
      elif not (11 <= len(phone_num) <= 13):
        print('400 Bad Request: Phone Number Length Should be Between 11 and 13 Characters\n')
      else:
        phone_num_valid = False
        for key, value in contact_db.items():
          if value['Phone Number'] == phone_num:
            phone_num_valid = True
            break
        if phone_num_valid:
          print('400 Bad Request: Phone Number is Already in the Database')
        else:
          break    
  
  while True:
    email = input('Input Email Change : ')
    
    if email == '':
      email = None
      break
    elif '@' in email and '.' in email:
      break
    else: 
      print('400 Bad Request: Not a Valid Email Format (should have @ and .)\n')
  
  while True:
    job = input('Input Job Change :')
    
    if job == '':
      job = None
      break
    
    if not job.isalpha(): 
      print('400 Bad Request: Job input Should Be Character Only.\n')
    else:
      break
    
  if id in contact_db.keys():
    details = contact_db[id]
    old_data = [
      [
        id, 
        details['Name'], 
        details['Phone Number'], 
        details['Email'], 
        details['Job']
      ]
    ]
    headers = ['Id', 'Name', 'Phone Number', 'Email', 'Job']

    if name is None and phone_num is None and email is None and job is None:
      print('No Changes Made')
      print(DataFrame(old_data, headers))
      return

    else:

      # Old Data
      details = contact_db[id]

      print('\nData Before Change')
      print(DataFrame(old_data, headers))

      if name is not None:
        contact_db[id]['Name'] = name
      if phone_num is not None:
        contact_db[id]['Phone Number'] = phone_num
      if email is not None:
        contact_db[id]['Email'] = email
      if job is not None:
        contact_db[id]['Job'] = job

      # New Data
      new_data = [
          [id, 
           details['Name'], 
           details['Phone Number'], 
           details['Email'], 
           details['Job']]
      ]

      print('\nData After Change')
      print(DataFrame(new_data, headers))
  
  else:
    print(f'Contact with id {id} Not Found')

####### DELETE #######
def DeleteById():
  while True:
    try:
      id = int(input('Input Id to Delete : '))
    except ValueError:
      print('400 Bad Request: Id should be integer only\n')
  
    if id in contact_db:
      del contact_db[id]
      reorder_ids()
      print(f'200 OK: Contact with id {id} has been deleted\n')
      break
  
    else:
      print(f'404 Not Found: Contact with id {id} Not Found\n')
      break
  
  return GetAll()

def DeleteAll():
  global id
  contact_db.clear()
  id = len(contact_db)
  print('200 OK: All contacts have been deleted\n')
  
# Menu

def Menu():
    while True:
        print('------ Phone Number Dashboard ------')
        print('1. Add New Phone Number Data Option\n2. Change Phone Number Data Option\n3. Delete Phone Number Data Option\n4. Phone Number Database Option\n5. Exit')

        try:
          user_input = int(input('Choose Menu [1-5] : '))
        except ValueError:
          print('Choose Valid Input\n')
          continue

        if user_input == 1:
          CreateMenu()
        elif user_input == 2:
          UpdateMenu()
        elif user_input == 3:
          DeleteMenu()
        elif user_input == 4:
           GetMenu()
        elif user_input == 5:
          break
        else:
          print('Choose Valid Input\n')

def CreateMenu():
    while True:
      print("------ Add New Phone Number ------")
      print('1. Add Phone Number\n2. Exit')

      try:
        user_input = int(input('Choose Menu [1-2] : '))
      except ValueError:
        print('Choose Valid Input\n')
      
      if user_input == 1:
        PostById()
      elif user_input == 2:
        break
      else:
        print('Choose Valid Input\n')

def GetMenu():
    while True:
      print("------ Phone Number Database ------")
      print('1. All Phone Number\n2. Choose a Phone Number\n3. Search by Name\n4. Exit')
      try:
        user_input = int(input('Choose Menu [1-4] : '))
      except ValueError:
        print('Choose Valid Input\n')
      
      if user_input == 1:
        GetAll()
      elif user_input == 2:
        GetById()
      elif user_input == 3:
        GetByName()
      elif user_input == 4:
        break
      else:
        print('Choose Valid Input\n')

def UpdateMenu():
    while True:
      print('------ Change Phone Number ------')
      print('1. Change a Phone Number\n2. Exit')

      try:
        user_input = int(input('Choose Menu [1-2] : '))
      except ValueError:
        print('Choose Valid Input\n')
      
      if user_input == 1:
        UpdateById()
      elif user_input == 2:
        break
      else:
        print('Choose Valid Input\n')

def DeleteMenu():
    while True:
      print('------ Delete Phone Number ------')
      print('1. Delete a Phone Number\n2. Delete All Phone Number\n3. Exit')
    
      try:
        user_input = int(input('Choose Menu [1-3] : '))
      except ValueError:
        print('Choose Valid Input\n')
      
      if user_input == 1:
        DeleteById()
      elif user_input == 2:
        DeleteAll()
      elif user_input == 3:
        break
      else:
        print('Choose Valid Input\n')
        
Menu()