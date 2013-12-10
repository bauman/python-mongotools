from mongotools import datetime_to_objectId
from mongotools import objectId_to_datetime
import datetime


example1 = datetime_to_objectId("2011-12-10")
example2 = datetime_to_objectId(year=2011, month=12, day=10)
example3 = datetime_to_objectId(datetime.datetime(2011, 12, 10, 0))


example1_a = objectId_to_datetime(example1)
example2_a = objectId_to_datetime(example2)


assert str(example1) == str(example2)
assert str(example1) == str(example3)
assert example1_a.isoformat() == example2_a.isoformat()

