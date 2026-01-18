# Calling the Amazon RDS Data API from a Python application

You can call the Amazon RDS Data API (Data API) from a Python application.

The following examples use the AWS SDK for Python (Boto). For more information about Boto, see the
[AWS SDK for Python (Boto 3) documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html").

In each example, replace the DB cluster's Amazon Resource Name (ARN) with
the ARN for your Aurora DB cluster. Also, replace the secret ARN with
the ARN of the secret in Secrets Manager that allows access to the DB cluster.

###### Topics

- [Running a SQL query](#data-api.calling.python.run-query "#data-api.calling.python.run-query")
- [Running a DML SQL statement](#data-api.calling.python.run-inert "#data-api.calling.python.run-inert")
- [Running a SQL transaction](#data-api.calling.python.run-transaction "#data-api.calling.python.run-transaction")

## Running a SQL query

You can run a `SELECT` statement and fetch the results with a Python application.

The following example runs a SQL query.

```
import boto3

rdsData = boto3.client('rds-data')

cluster_arn = '`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`'
secret_arn = '`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`'

response1 = rdsData.execute_statement(
            resourceArn = cluster_arn,
            secretArn = secret_arn,
            database = '`mydb`',
            sql = '`select * from employees limit 3`')

print (response1['records'])
[
    [
        {
            'longValue': 1
        },
        {
            'stringValue': 'ROSALEZ'
        },
        {
            'stringValue': 'ALEJANDRO'
        },
        {
            'stringValue': '2016-02-15 04:34:33.0'
        }
    ],
    [
        {
            'longValue': 1
        },
        {
            'stringValue': 'DOE'
        },
        {
            'stringValue': 'JANE'
        },
        {
            'stringValue': '2014-05-09 04:34:33.0'
        }
    ],
    [
        {
            'longValue': 1
        },
        {
            'stringValue': 'STILES'
        },
        {
            'stringValue': 'JOHN'
        },
        {
            'stringValue': '2017-09-20 04:34:33.0'
        }
    ]
]
```

## Running a DML SQL statement

You can run a data manipulation language (DML) statement to insert, update, or delete data in your database.
You can also use parameters in DML statements.

###### Important

If a call isn't part of a transaction because it doesn't include
the `transactionID` parameter, changes that result from the
call are committed automatically.

The following example runs an insert SQL statement and uses
parameters.

```
import boto3

cluster_arn = '`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`'
secret_arn = '`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`'

rdsData = boto3.client('rds-data')


param1 = {'name':'firstname', 'value':{'stringValue': '`JACKSON`'}}
param2 = {'name':'lastname', 'value':{'stringValue': '`MATEO`'}}
paramSet = [param1, param2]

response2 = rdsData.execute_statement(resourceArn=cluster_arn,
                                      secretArn=secret_arn,
                                      database='`mydb`',
                                      sql='`insert into employees(first_name, last_name) VALUES(:firstname, :lastname)`',
                                      parameters = paramSet)

print (response2["numberOfRecordsUpdated"])
```

## Running a SQL transaction

You can start a SQL transaction, run one or more SQL statements, and then
commit the changes with a Python application.

###### Important

A transaction times out if there are no calls that use its transaction ID
in three minutes. If a transaction times out before it's
committed, it's rolled back automatically.

If you don't specify a transaction ID, changes that result from
the call are committed automatically.

The following example runs a SQL transaction that inserts a row in a
table.

```
import boto3

rdsData = boto3.client('rds-data')

cluster_arn = '`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`'
secret_arn = '`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`'

tr = rdsData.begin_transaction(
     resourceArn = cluster_arn,
     secretArn = secret_arn,
     database = '`mydb`')

response3 = rdsData.execute_statement(
     resourceArn = cluster_arn,
     secretArn = secret_arn,
     database = '`mydb`',
     sql = '`insert into employees(first_name, last_name) values('XIULAN', 'WANG')`',
     transactionId = tr['transactionId'])

cr = rdsData.commit_transaction(
     resourceArn = cluster_arn,
     secretArn = secret_arn,
     transactionId = tr['transactionId'])

cr['transactionStatus']
'Transaction Committed'

response3['numberOfRecordsUpdated']
1
```

###### Note

If you run a data definition language (DDL) statement, we recommend continuing to run the statement after
the call times out. When a DDL statement terminates before it is finished
running, it can result in errors and possibly corrupted data structures. To
continue running a statement after a call exceeds the RDS Data API timeout interval of 45 seconds, set the `continueAfterTimeout`
parameter to `true`.
