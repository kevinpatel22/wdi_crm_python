from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField()
  note = TextField()

  class Meta:
    database = db
  
  def full_name(self):
    return f'{self.first_name} {self.last_name}'

db.connect()
db.create_tables([Contact])

# contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')
# print(len(Contact.contacts))
# print(contact1.id)
# print(contact2.id)

# print(Contact.find(1))
# print(Contact.all())
# print(contact1.full_name())
# # Contact.delete_all()
# contact1.delete()
# print(len(Contact.contacts))
# print(Contact.find_by('first_name', 'Bit'))
# print(contact1.update('first_name','Bitty'))
