import pymongo
from pymongo import MongoClient

class seniorSaver:
    """Application for querying an order database"""

    def connect(self):
        """Makes a connection to the database and returns connection to caller"""
        try:
            print("Connecting to database.")
            cluster = MongoClient("mongodb+srv://admin:SFKRaVaUVZU0Ojvw@seniorsaverdb-hpeul.gcp.mongodb.net/test?retryWrites=true&w=majority")
            print('Connection Successful')
            self.db = cluster['database']

            return self.db
        except:
            print("Exception, IDK why...")

    def init(self):
        print('Intializing Database.')
        Contact = self.db['Contact']
        Contact.delete_many({})
        c1 = {'_id': 'user0001', 'cName': 'Griffin', 'number': '+12503283164'}
        c2 = {'_id': 'user0002', 'cName': 'Nate', 'number': '+17788793964'}
        c3 = {'_id': 'user0003', 'cName': 'Patrick', 'number': '+17809317106'}
        c4 = {'_id': 'user0004', 'cName': 'Daulton', 'number': '+12504917700'}
        Contact.insert_many([c1, c2, c3, c4])
        print('Contacts inserted')
        Person = self.db['Person']
        Person.delete_many({})
        p1 = {'_id': 'User0001', 'pName': 'Bertha', 'gender': 'Female', 'dob': '1920-02-21',
              'health': 'Type 2 Diabetic'}
        p2 = {'_id': 'User0002', 'pName': 'Donald', 'gender': 'Male', 'dob': '1922-11-22', 'health': 'Hearing Loss'}
        p3 = {'_id': 'User0003', 'pName': 'Doreen', 'gender': 'Female', 'dob': '1926-03-09',
              'health': 'Broken Hip (Wheelchair)'}
        p4 = {'_id': 'User0004', 'pName': 'Mortimer', 'gender': 'Male', 'dob': '1928-09-30',
              'health': 'Partially Blind'}
        Person.insert_many([p1, p2, p3, p4])
        print('People inserted')
        Incident = self.db['Incident']
        Incident.delete_many({})
        i1 = {'_id': '0001', 'userId': 'user0001', 'latitude': 49.940313, 'longitude': -119.395310, 'datetime': '2020-01-18 22:53:05', 'Emergency': 0}
        i2 = {'_id': '0002', 'userId': 'user0001', 'latitude': 49.940313, 'longitude': -119.395310, 'datetime': '2020-01-18 23:00:14', 'Emergency': 0}
        i3 = {'_id': '0003', 'userId': 'user0001', 'latitude': 49.940313, 'longitude': -119.395310, 'datetime': '2020-01-19 00:00:00', 'Emergency': 1}
        i4 = {'_id': '0004', 'userId': 'user0002', 'latitude': 49.261749, 'longitude': -123.245867, 'datetime': '2020-01-18 22:53:05', 'Emergency': 0}
        i5 = {'_id': '0005', 'userId': 'user0003', 'latitude': 49.261749, 'longitude': -123.245867, 'datetime': '2020-01-16 22:53:05', 'Emergency': 0}
        i6 = {'_id': '0006', 'userId': 'user0004', 'latitude': 49.261749, 'longitude': -123.245867, 'datetime': '2019-11-01 22:53:05', 'Emergency': 1}
        Incident.insert_one(i1)
        Incident.insert_one(i2)
        Incident.insert_many([i3, i4, i5, i6])
        print('Incidents inserted')

    def listPeople(self):
        output = 'Listing all People: \n'+'userID, Name, Gender, DOB, Health'
        Person = self.db['Person']
        results = Person.find({})
        for result in results:
            output += '\n' + str(result)
        return output

    def listIncidents(self, userId):
        output = f'Listing all Incidents for User:{userId}: \n'+'IncidentId, UserId, longitude, latitude, datetime, emergency'
        Incident = self.db['Incident']
        results = Incident.find({'userId': userId})
        for result in results:
            output += '\n' + str(result)
        return output

    def listContact(self, userId):
        output = f'Listing Contact for User:{userId}: \n'+'UserID, Contact Name, Contact Number'
        Contact = self.db['Contact']
        results = Contact.find({'_id': userId})
        for result in results:
            output += '\n' + str(result)
        return output

    def addPerson(self, userId, name, gender, dob, health):
        newPerson = {'_id': userId, 'pName': name, 'gender': gender, 'dob': dob, 'health': health}
        Person = self.db['Person']
        Person.insert_one(newPerson)
        return

    def addContact(self, userId, cName, number):
        newContact = {'_id': userId, 'cName': cName, 'number': number}
        Contact = self.db['Contact']
        Contact.insert_one(newContact)
        return


    def addIncident(self, incidentId, userId, latitude, longitude, datetime, emergency):
        newIncident = {'_id': incidentId, 'userId': userId, 'latitude': latitude, 'longitude': longitude,
                       'datetime': datetime, 'emergency': emergency}
        Incident = self.db['Incident']
        Incident.insert_one(newIncident)
        return

    def deletePerson(self, userId):
        # Manually implements cascading delete
        Person = self.db['Person']
        Incident = self.db['Incident']
        Contact = self.db['Contact']
        Person.delete_one({'_id': userId})
        Incident.delete_many({'userId': userId})
        Contact.delete_one({'_id': userId})
        return

    def deleteContact(self, userId):
        Contact = self.db['Contact']
        Contact.delete_one({'_id': userId})
        return

    def deleteIncident(self, incidentId):
        Incident = self.db['Incident']
        Incident.delete_one({'_id': incidentId})
        return

    def updatePerson(self, userId, pName, gender, dob, health):
        query = {'_id': userId}
        update = {'$set': {'pName': pName, 'gender': gender, 'dob': dob, 'health': health}}
        Person = self.db['Person']
        Person.update_one(query, update)
        return

    def updateContact(self, userId, cName, number):
        query = {'_id': userId}
        update = {'$set': {'cName': cName, 'number': number}}
        Contact = self.db['Contact']
        Contact.update_one(query, update)
        return

    def updateIncident(self, incidentId, userId, latitude, longitude, datetime, emergency):
        query = {'_id': incidentId, }
        update = {'$set': {'userId': userId, 'latitude': latitude, 'longitude': longitude, 'datetime': datetime,
                           'emergency': emergency}}
        Incident = self.db['Incident']
        Incident.update_one(query, update)
        return

def setUp():
    self = seniorSaver()
    seniorSaver.connect(self)
    # This resets database
    # seniorSaver.init(self)
    userId = 'user0005'
    '''
    Tests for queries
    print(seniorSaver.listPeople(self))
    
    print(seniorSaver.listContact(self, userId))
    print(seniorSaver.listIncidents(self, userId))
    '''
    '''
    # Test for Add/Delete Person
    print('Listing all People: \n' + seniorSaver.listPeople(self))
    seniorSaver.addPerson(self, userId, 'Tester', 'NonBinary', '2020-01-19', 'Healthy')
    print('Listing all People: \n' + seniorSaver.listPeople(self))
    seniorSaver.deletePerson(self, userId)
    print('Listing all People: \n' + seniorSaver.listPeople(self))
    '''
    '''
    # Test for Add/ Delete Contact
    print(seniorSaver.listContact(self, userId))
    seniorSaver.addContact(self, userId, 'Test Contact', '+12345678912')
    print(seniorSaver.listContact(self, userId))
    seniorSaver.deleteContact(self, userId)
    print(seniorSaver.listContact(self, userId))
    '''
    '''
    # Test for Add/Delete Incident
    print(seniorSaver.listIncidents(self, userId))
    seniorSaver.addIncident(self, '0007', userId, 0.000000, 0.000000, '2020-01-19 00:00:00', 1)
    print(seniorSaver.listIncidents(self, userId))
    seniorSaver.deleteIncident(self, '0007')
    print(seniorSaver.listIncidents(self, userId))
    '''


if __name__ == '__main__':
    setUp()
