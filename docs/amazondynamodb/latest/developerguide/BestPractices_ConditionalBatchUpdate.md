# Conditional batch update

DynamoDB supports batch operations such as `BatchWriteItem` using which you can perform up to 25
`PutItem` and `DeleteItem` requests in a single batch. However, `BatchWriteItem` doesn't support `UpdateItem` operations
and doesn't support condition expressions. As a workaround, you can use other DynamoDB APIs such as
`TransactWriteItems` for batch size up to 100.

When more items are involved, and a major chunk of data needs to be changed, you can use services such as
AWS Glue, Amazon EMR, AWS Step Functions or use custom scripts and tools like DynamoDB-shell for efficient
bulk updates.

###### When to use this pattern

- DynamoDB-shell is not a supported for production use case.
- `TransactWriteItems` – up to 100 individual updates with or without conditions,
  executing as an all or nothing ACID bundle. `TransactWriteItems` calls can also be supplied with
  a `ClientRequestToken` if your application requires idempotency, meaning multiple identical calls
  have the same effect as one single call. This ensures you don't execute the same transaction
  multiple times and end up with an incorrect state of data.

Trade-off – Additional throughput is consumed. 2 WCUs per 1KB write instead of
the standard 1 WGU per 1 KB write.

- PartiQL `BatchExecuteStatement` – up to 25 updates with or without conditions.
  `BatchExecuteStatement` always returns a success response to the overall request, and also returns
  a list of individual operation responses that preserves order.

Trade-off – For larger batches, additional client-side logic is required to
distribute requests in batches of 25. Individual error responses need to be considered to
determine retry strategy.

## Code examples

These code examples use the boto3 library, which is the AWS SDK for
Python. The examples assume you have boto3 installed and configured with appropriate AWS
credentials.

Assume an inventory database for an electrical appliance vendor who has multiple warehouses
across European cities. Because it is end of summer, the vendor would like to clear out desk fans
to make room for other stock. The vendor wants to provide a price discount for all desk fans
supplied out of warehouses in Italy but only if they have a reserve stock of 20 desk fans.
The DynamoDB table is called **inventory**, it has a key schema of Partition key **sku** which is a
unique identifier for each product and a Sort key **warehouse** which is an identifier for a
warehouse.

The following Python code demonstrates how to perform this conditional batch update using
`BatchExecuteStatement` API call.

```
import boto3

client=boto3.client("dynamodb")

before_image=client.query(TableName='inventory', KeyConditionExpression='sku=:pk_val AND begins_with(warehouse, :sk_val)', ExpressionAttributeValues={':pk_val':{'S':'F123'},':sk_val':{'S':'WIT'}}, ProjectionExpression='sku,warehouse,quantity,price')
print("Before update: ", before_image['Items'])

response=client.batch_execute_statement(
        Statements=[
            {'Statement': 'UPDATE inventory SET price=price-5 WHERE sku=? AND warehouse=? AND quantity > 20', 'Parameters': [{'S':'F123'}, {'S':'WITTUR1'}], 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'},
            {'Statement': 'UPDATE inventory SET price=price-5 WHERE sku=? AND warehouse=? AND quantity > 20', 'Parameters': [{'S':'F123'}, {'S':'WITROM1'}], 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'},
            {'Statement': 'UPDATE inventory SET price=price-5 WHERE sku=? AND warehouse=? AND quantity > 20', 'Parameters': [{'S':'F123'}, {'S':'WITROM2'}], 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'},
            {'Statement': 'UPDATE inventory SET price=price-5 WHERE sku=? AND warehouse=? AND quantity > 20', 'Parameters': [{'S':'F123'}, {'S':'WITROM5'}], 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'},
            {'Statement': 'UPDATE inventory SET price=price-5 WHERE sku=? AND warehouse=? AND quantity > 20', 'Parameters': [{'S':'F123'}, {'S':'WITVEN1'}], 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'},
            {'Statement': 'UPDATE inventory SET price=price-5 WHERE sku=? AND warehouse=? AND quantity > 20', 'Parameters': [{'S':'F123'}, {'S':'WITVEN2'}], 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'},
            {'Statement': 'UPDATE inventory SET price=price-5 WHERE sku=? AND warehouse=? AND quantity > 20', 'Parameters': [{'S':'F123'}, {'S':'WITVEN3'}], 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'},
        ],
        ReturnConsumedCapacity='TOTAL'
    )

after_image=client.query(TableName='inventory', KeyConditionExpression='sku=:pk_val AND begins_with(warehouse, :sk_val)', ExpressionAttributeValues={':pk_val':{'S':'F123'},':sk_val':{'S':'WIT'}}, ProjectionExpression='sku,warehouse,quantity,price')
print("After update: ", after_image['Items'])

```

Execution produces the below output on sample data:

```
Before update:  [{'quantity': {'N': '20'}, 'warehouse': {'S': 'WITROM1'}, 'price': {'N': '40'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '25'}, 'warehouse': {'S': 'WITROM2'}, 'price': {'N': '40'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '28'}, 'warehouse': {'S': 'WITROM5'}, 'price': {'N': '38'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '26'}, 'warehouse': {'S': 'WITTUR1'}, 'price': {'N': '40'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '10'}, 'warehouse': {'S': 'WITVEN1'}, 'price': {'N': '38'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '20'}, 'warehouse': {'S': 'WITVEN2'}, 'price': {'N': '38'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '50'}, 'warehouse': {'S': 'WITVEN3'}, 'price': {'N': '35'}, 'sku': {'S': 'F123'}}]
After update:  [{'quantity': {'N': '20'}, 'warehouse': {'S': 'WITROM1'}, 'price': {'N': '40'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '25'}, 'warehouse': {'S': 'WITROM2'}, 'price': {'N': '35'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '28'}, 'warehouse': {'S': 'WITROM5'}, 'price': {'N': '33'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '26'}, 'warehouse': {'S': 'WITTUR1'}, 'price': {'N': '35'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '10'}, 'warehouse': {'S': 'WITVEN1'}, 'price': {'N': '38'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '20'}, 'warehouse': {'S': 'WITVEN2'}, 'price': {'N': '38'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '50'}, 'warehouse': {'S': 'WITVEN3'}, 'price': {'N': '30'}, 'sku': {'S': 'F123'}}]

```

Since this is a bounded operation for an internal system, idempotency requirements haven't
been considered. It's possible to place additional guardrails like price update should go through
only if price is greater than 35 and less than 40 to make the updates more robust.

Alternatively, we can perform the same batch update operation using `TransactWriteItems` in
case of stricter idempotency and ACID requirements. However, it is important to remember that
either all the operations in the transaction bundle go through or the entire bundle fails.

Let’s assume a case where there is a heatwave in Italy and the demand for desk fans has
increased sharply. The vendor wants to increase their desk fan cost going out of every warehouse
in Italy by 20 Euros but the regulatory body only allows this cost increase if the current cost is
less than 70 Euros across their entire inventory. It's essential that the price is updated
throughout the inventory at once and only once and only if the cost is less than 70 Euros in
each of their warehouse.

The following Python code demonstrates how to perform this batch update using
`TransactWriteItems` API call.

```

import boto3

client=boto3.client("dynamodb")

before_image=client.query(TableName='inventory', KeyConditionExpression='sku=:pk_val AND begins_with(warehouse, :sk_val)', ExpressionAttributeValues={':pk_val':{'S':'F123'},':sk_val':{'S':'WIT'}}, ProjectionExpression='sku,warehouse,quantity,price')
print("Before update: ", before_image['Items'])

response=client.transact_write_items(
        ClientRequestToken='UUIDAWS124',
        TransactItems=[
            {'Update': { 'Key': {'sku': {'S':'F123'}, 'warehouse': {'S':'WITTUR1'}}, 'UpdateExpression': 'SET price = price + :inc', 'ConditionExpression': 'price < :cap', 'ExpressionAttributeValues': { ':inc': {'N': '20'}, ':cap': {'N': '70'}}, 'TableName': 'inventory', 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'}},
            {'Update': { 'Key': {'sku': {'S':'F123'}, 'warehouse': {'S':'WITROM1'}}, 'UpdateExpression': 'SET price = price + :inc', 'ConditionExpression': 'price < :cap', 'ExpressionAttributeValues': { ':inc': {'N': '20'}, ':cap': {'N': '70'}}, 'TableName': 'inventory', 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'}},
            {'Update': { 'Key': {'sku': {'S':'F123'}, 'warehouse': {'S':'WITROM2'}}, 'UpdateExpression': 'SET price = price + :inc', 'ConditionExpression': 'price < :cap', 'ExpressionAttributeValues': { ':inc': {'N': '20'}, ':cap': {'N': '70'}}, 'TableName': 'inventory', 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'}},
            {'Update': { 'Key': {'sku': {'S':'F123'}, 'warehouse': {'S':'WITROM5'}}, 'UpdateExpression': 'SET price = price + :inc', 'ConditionExpression': 'price < :cap', 'ExpressionAttributeValues': { ':inc': {'N': '20'}, ':cap': {'N': '70'}}, 'TableName': 'inventory', 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'}},
            {'Update': { 'Key': {'sku': {'S':'F123'}, 'warehouse': {'S':'WITVEN1'}}, 'UpdateExpression': 'SET price = price + :inc', 'ConditionExpression': 'price < :cap', 'ExpressionAttributeValues': { ':inc': {'N': '20'}, ':cap': {'N': '70'}}, 'TableName': 'inventory', 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'}},
            {'Update': { 'Key': {'sku': {'S':'F123'}, 'warehouse': {'S':'WITVEN2'}}, 'UpdateExpression': 'SET price = price + :inc', 'ConditionExpression': 'price < :cap', 'ExpressionAttributeValues': { ':inc': {'N': '20'}, ':cap': {'N': '70'}}, 'TableName': 'inventory', 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'}},
            {'Update': { 'Key': {'sku': {'S':'F123'}, 'warehouse': {'S':'WITVEN3'}}, 'UpdateExpression': 'SET price = price + :inc', 'ConditionExpression': 'price < :cap', 'ExpressionAttributeValues': { ':inc': {'N': '20'}, ':cap': {'N': '70'}}, 'TableName': 'inventory', 'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'}},
        ],
        ReturnConsumedCapacity='TOTAL'
    )

after_image=client.query(TableName='inventory', KeyConditionExpression='sku=:pk_val AND begins_with(warehouse, :sk_val)', ExpressionAttributeValues={':pk_val':{'S':'F123'},':sk_val':{'S':'WIT'}}, ProjectionExpression='sku,warehouse,quantity,price')
print("After update: ", after_image['Items'])

```

Execution produces the below output on sample data:

```

Before update:  [{'quantity': {'N': '20'}, 'warehouse': {'S': 'WITROM1'}, 'price': {'N': '60'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '25'}, 'warehouse': {'S': 'WITROM2'}, 'price': {'N': '55'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '28'}, 'warehouse': {'S': 'WITROM5'}, 'price': {'N': '53'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '26'}, 'warehouse': {'S': 'WITTUR1'}, 'price': {'N': '55'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '10'}, 'warehouse': {'S': 'WITVEN1'}, 'price': {'N': '58'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '20'}, 'warehouse': {'S': 'WITVEN2'}, 'price': {'N': '58'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '50'}, 'warehouse': {'S': 'WITVEN3'}, 'price': {'N': '50'}, 'sku': {'S': 'F123'}}]
After update:  [{'quantity': {'N': '20'}, 'warehouse': {'S': 'WITROM1'}, 'price': {'N': '80'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '25'}, 'warehouse': {'S': 'WITROM2'}, 'price': {'N': '75'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '28'}, 'warehouse': {'S': 'WITROM5'}, 'price': {'N': '73'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '26'}, 'warehouse': {'S': 'WITTUR1'}, 'price': {'N': '75'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '10'}, 'warehouse': {'S': 'WITVEN1'}, 'price': {'N': '78'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '20'}, 'warehouse': {'S': 'WITVEN2'}, 'price': {'N': '78'}, 'sku': {'S': 'F123'}}, {'quantity': {'N': '50'}, 'warehouse': {'S': 'WITVEN3'}, 'price': {'N': '70'}, 'sku': {'S': 'F123'}}]

```

There are multiple approaches to perform batch updates in DynamoDB. The suitable
approach depends on factors such as ACID and/or idempotency requirements, number of items to be
updated, and familiarity with APIs.
