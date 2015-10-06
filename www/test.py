from ORM import Model,StringField,IntegerField

class User(Model):
	"""docstring for User"""
	__table__='users'

	id=IntegerField(primary_key=True)
	name=StringField()

	# 
	user=User(id=123,name='bay')
	#
	user.insert()
	#
	users=User.findAll()