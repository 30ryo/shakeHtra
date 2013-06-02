from neomodel import (StructuredNode, StringProperty, IntegerProperty,
                      RelationshipTo, RelationshipFrom, Relationship)

from py2neo import neo4j
from django.utils import simplejson



class NodeManagement(object):
    def __init__(self):
        self.neo4j_db = neo4j.GraphDatabaseService(neo4j.DEFAULT_URI)
        
    



class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)    
    inhabitant = RelationshipFrom('Person', 'IS_FROM')
    
    
class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    
    country = RelationshipTo('Country', 'IS_FROM')
    friends = Relationship('Person','FRIEND')

    
class VirtualPerson(Person):
    virtualname = StringProperty(unique_index=True)
    sex = IntegerProperty(index=True, default=0)
    real = RelationshipFrom('Person','VIRTUAL')

class VirtualWorker(VirtualPerson):
    job = StringProperty(index=True)
    account = RelationshipFrom('VirtualPerson','JOB')

class Place(StructuredNode):
    address = StringProperty(index=True,default='hogehoge')
    phone = StringProperty(index=True,default='000-000-000')

class VirtuarWorkplace(Place):
    server = StringProperty(index=True,default='hogeserver')
    

