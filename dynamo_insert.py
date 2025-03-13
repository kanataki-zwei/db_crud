# import 
import boto3

!aws configure

# this will ask you for certain keys
#AWS Access Key ID []: 
#AWS Secret Access Key []: 
#Default region name []: 
#Default output format []: 


# type1
def db_put_item(db_name, data: dict):
    """
    - Ensure that data is bearing the applicable partition key feature or put will fail
    Insert new record or Update ENTIRE record. this happens by matching unique partition key data bears
    """
    if not is_dict(data):
        raise TypeError("data must be a dictionary")

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(db_name)
    data["created"] = now_now_str()
    data["updated"] = now_now_str()
    status = table.put_item(Item=data)

    if status["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return True
    return False

#db_name = ""
#result = db_put_item(db_name, converted_data)
#print("Success:", result)


# type2
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('')

table.put_item(
    Item= {
        'id': str(123),
        'age': Decimal('20.0'),
        'country': 'KE',
        'created': '2024-07-15 08:00:13.844512+01:00',
        'is_active': False,
        'name': 'John Smith'
    },
)

print("Item successfully inserted")

# insert multiple items
db_name = ""

# Iterate over DataFrame rows and insert each row into DynamoDB
for index, row in profiles.iterrows():
    item = row.to_dict()
    item['id'] = str(item['id'])  # Convert id to string
    item['age'] = Decimal(str(item['age']))

    success = db_put_item(db_name, item)
    if success:
        print(f"Inserted item with id {item['id']}")
    else:
        print(f"Failed to insert item with id {item['id']}")
