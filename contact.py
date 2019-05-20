class Contact:
  
  contacts = []
  next_id = 1 
  
  def __init__(self, first_name, last_name, email, note):

    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note
    self.id = Contact.next_id
    Contact.next_id += 1

  def __repr__(self):
    return f'{self.id} {self.first_name} {self.last_name} {self.email} {self.note}'

  @classmethod
  def create(cls, first_name, last_name, email, note):
    new_entry = Contact(first_name, last_name, email, note)
    cls.contacts.append(new_entry)
    return new_entry

  @classmethod
  def all(cls):
    for each in cls.contacts:
      return each

  @classmethod
  def find(cls, id):
    for entry in cls.contacts:
      if id == entry.id:
        return entry 

  def update(self, name, value):
    setattr(self, name, value)
    return self

  @classmethod
  def find_by(cls, name, value):
    for entry in cls.contacts:
      if getattr(entry, name) == value:
        return entry

  @classmethod
  def delete_all(cls):
    del cls.contacts[0: len(cls.contacts)]

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  def delete(self):
    Contact.contacts.remove(self)


contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')
print(len(Contact.contacts))
print(contact1.id)
print(contact2.id)

print(Contact.find(1))
print(Contact.all())
print(contact1.full_name())
# Contact.delete_all()
contact1.delete()
print(len(Contact.contacts))
print(Contact.find_by('first_name', 'Bit'))
print(contact1.update('first_name','Bitty'))
