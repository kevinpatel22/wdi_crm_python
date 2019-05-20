from contact import Contact

class CRM:

  def main_menu(self):
    while True:
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)

  def print_main_menu(self): 
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')

  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
        self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      exit()

  def add_new_contact(self):
    print('Enter First Name: ')
    first_name = input()
    print('Enter Last Name: ')
    last_name = input()
    print('Enter Email Address: ')
    email = input()
    print('Enter a Note: ')
    note = input()
    Contact.create(first_name, last_name, email, note)

  @classmethod
  def modify_existing_contact(self):
    id = input('Enter the ID of the contact to delete: ')
    find = Contact.find(int(id))
    attr_update = input('Enter the attribute you would like to change: ')
    Value_update = input('Enter the value you would like to change to: ')
    find.update(attr_update, Value_update)
    
  def delete_contact(self):
    id = input('Enter the ID of the contact to delete: ')
    remove = Contact.find(int(id))
    remove.delete()
  
  def display_all_contacts(self):
    print(Contact.all())
  
  def search_by_attribute(self):
    attr = input('Find contact by attribute: ')
    value = input('Now enter its value: ')
    found = Contact.find_by(attr, value)
    print({found})

a_crm_app = CRM()
a_crm_app.main_menu()