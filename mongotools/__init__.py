import datetime

IMPORTFAILS = {} #global variable for function checks

try:
    #Attempt to import bson from python bson.
    from bson.objectid import ObjectId
except ImportError:
    #If it fails to import, some functions are still available
    IMPORTFAILS['bson'] = None #Store as a dict for quick check using "in" 

try:
    from dateutil.parser import parse
except ImportError:
    #If it fails to import, some functions are still available
    IMPORTFAILS['parser'] = None #Store as a dict for quick check using "in"





def objectId_to_datetime(input):
    '''
    Input  -- input <basestring> or <ObjectId>
              if input is ObjectId, convert it to a string first

    Output -- response_datetime <datetime>

    
    reference: http://docs.mongodb.org/manual/reference/object-id/#objectid
               http://api.mongodb.org/python/1.5.2/api/pymongo/objectid.html
    
    this was written prior to pymongo 1.2
        alternate function to pymongo's ObjectId.generation_time post pymongo 1.2
    
    procedure:
        cast input to string
        get only first 8 characters (from ref: a 4-byte value representing the seconds since the Unix epoch)
        cast to integer from hex string
        cast to datetime object using fromtimestamp function 
        
    '''
    return datetime.datetime.fromtimestamp(int(str(input)[:8], 16))



def datetime_to_objectId(input="", year=0, month=1, day=1, hour=0):
    '''
    Input  -- input <datetime.datetime> <basestring> 
              year <int>
              month <int>
              day <int>
              hour <int>
    
    Output --  <ObjectId> or None or <basestring> if bson.objectid module does not exist
    
    
    reference: http://api.mongodb.org/python/1.5.2/api/pymongo/objectid.html
    
    '''
    response_objectid = None #default to None to enable 'if' check
    if "bson" not in IMPORTFAILS:
        if input:
            if isinstance(input, basestring): #need to parse
                response_objectid =  ObjectId.from_datetime(_parse_input(input))
            else: #should only be a string or datetime, all else will fail here
                response_objectid = ObjectId.from_datetime(input)
        elif year:
            response_objectid = ObjectId.from_datetime(datetime.datetime(int(year), int(month), int(day), int(hour)))
    else:
        pass
        #TODO: build object ID without objectID library
    return response_objectid # should be of ObjectID or None
  
def _parse_input(input):
    '''
    Input  -- input <basestring>

    Output --  <datetime.datetime> 
    
    reference: http://labix.org/python-dateutil#head-c0e81a473b647dfa787dc11e8c69557ec2c3ecd2
    '''
    if 'parser' not in IMPORTFAILS:
        return parse(input)
    else:
        return None

