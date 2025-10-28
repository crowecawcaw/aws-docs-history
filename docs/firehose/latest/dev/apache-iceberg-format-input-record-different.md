# Route incoming records to

different Iceberg tables

Amazon Data Firehose can route incoming records in a stream to different Iceberg tables based on
the content of the record. Records are not kept in order when delivered from Amazon Data Firehose.
Consider the following sample input record.

```
{
  "deviceId": "Device1234",
  "timestamp": "2024-11-28T11:30:00Z",
  "data": {
    "temperature": 21.5,
    "location": {
      "latitude": 37.3324,
      "longitude": -122.0311
    }
  },
  "powerlevel": 84,
  "status": "online"
}
```

```
{
  "deviceId": "Device4567",
  "timestamp": "2023-11-28T10:40:00Z",
  "data": {
    "pressure": 1012.4,
    "location": {
      "zipcode": 24567
    }
  },
  "powerlevel": 82,
  "status": "online"
}
```

In this example, the `**deviceId**` field has
two possible values – `Device1234` and `Device4567`. When
an incoming record has `**deviceId**` field as
`Device1234`, we want to write the record to an Iceberg table named
`Device1234`, and when an incoming record has `**deviceId**` field as `Device4567`, we want to write
the record to a table named `Device4567`.

Note that the records with `Device1234` and `Device4567` might
have a different set of fields that map to different columns in the corresponding
Iceberg table. The incoming records might have a nested JSON structure where the
**`deviceId`** can be nested within the JSON
record. In the upcoming sections, we discuss how you can route records to different
tables by providing the appropriate routing information to Firehose in such scenarios.

## Provide routing information to Firehose with

JSONQuery expression

The simplest and most cost effective way to provide record routing information to
Firehose is by providing a JSONQuery expression. With this approach, you provide
JSONQuery expressions for three parameters – `Database Name`,
`Table Name`, and (optionally) `Operation`. Firehose uses the
expression that you provide to extract information from your incoming stream records
to route the records.

The `Database Name` parameter specifies the name of the destination
database. The `Table Name` parameter specifies the name of the
destination table. `Operation` is an optional parameter that indicates
whether to insert the incoming stream record as a new record into the destination
table, or to modify or delete an existing record in the destination table. The
Operation field must have one of the following values – `insert`,
`update`, or `delete`.

For each of these three parameters, you can either provide a static value or a
dynamic expression where the value is retrieved from the incoming record. For
example, if you want to deliver all incoming stream records to a single database
named `IoTevents`, the Database Name would have a static value of
`“IoTevents”`. If the destination table name must be obtained from a
field in the incoming record, the Table Name is a dynamic expression that specifies
the field in the incoming record from which the destination table name needs to be
retrieved.

In the following example, we use a static value for Database Name, a dynamic value
for Table Name, and a static value for operation. Note that specifying the Operation
is optional. If no operation is specified, Firehose inserts the incoming records into
the destination table as new records by default.

```
Database Name : "IoTevents"
Table Name : .deviceId
Operation : "insert"
```

If the `deviceId` field is nested within the JSON record, we specify
Table Name with the nested field information as `.event.deviceId`.

###### Note

- When you specify the operation as `update` or
  `delete`, you must either specify unique keys for the
  destination table when you set up your Firehose stream, or set [identifier-field-ids](https://iceberg.apache.org/spec/#identifier-field-ids "https://iceberg.apache.org/spec/#identifier-field-ids") in Iceberg when you run [create table](https://iceberg.apache.org/docs/1.5.1/spark-ddl/#create-table "https://iceberg.apache.org/docs/1.5.1/spark-ddl/#create-table") or [alter table](https://iceberg.apache.org/docs/1.5.1/spark-ddl/#alter-table-set-identifier-fields "https://iceberg.apache.org/docs/1.5.1/spark-ddl/#alter-table-set-identifier-fields") operations in Iceberg. If you fail to specify
  this, then Firehose throws an error and delivers data to an S3 error
  bucket.
- The `Database Name` and `Table Name` values must
  exactly match with your destination database and table names. If they do
  not match, then Firehose throws an error and delivers data to an S3 error
  bucket.

## Provide routing information using an

AWS Lambda function

There might be scenarios where you have complex rules that determine how to route
incoming records to a destination table. For example, you might have a rule that
defined if a field contains the value A, B, or F, that should be routed to a
destination table named `TableX` or you might want to augment the
incoming stream record by adding additional attributes. For example, if a record
contains a field `device_id` as 1, you might want to add another field
that `device_type` as “modem“, and write the additional field to the
destination table column. In such cases, you can transform the source stream by
using an AWS Lambda function in Firehose and provide routing information as part of the
output of the Lambda transformation function. To understand how you can transform the
source stream by using an AWS Lambda function in Firehose, see [Transform source data in Amazon Data
Firehose](data-transformation.md "data-transformation.md").

When you use Lambda for transformation of a source stream in Firehose, the output must
contain `recordId`, `result`, and `data` or
`KafkaRecordValue` parameters. The parameter `recordId`
contains the input stream record, `result` indicates whether the
transformation was successful, and `data` contains the Base64-encoded
transformed output of your Lambda function. For more information, see [Required parameters for data
transformation](data-transformation-status-model.md "data-transformation-status-model.md").

```
{
  "recordId": "49655962066601463032522589543535113056108699331451682818000000",
  "result": "Ok",
  "data": "1IiwiI6ICJmYWxsIiwgImdgU21IiwiI6ICJmYWxsIiwg==tcHV0ZXIgU2NpZW5jZSIsICJzZW1"
}
```

To specify routing information to Firehose on how to route the stream record to a
destination table as part of your Lambda function, the output of your Lambda function
must contain an additional section for `metadata`. The following example
shows how the metadata section is added to the Lambda output for a Firehose stream that
uses Kinesis Data Streams as a data source to instruct Firehose that it must insert the record as a new
record into table named `Device1234` of the database
`IoTevents`.

```
 {
"recordId": "49655962066601463032522589543535113056108699331451682818000000",
    "result": "Ok",
    "data": "1IiwiI6ICJmYWxsIiwgImdgU21IiwiI6ICJmYWxsIiwg==tcHV0ZXIgU2NpZW5jZSIsICJzZW1",

    "metadata":{
"otfMetadata":{
            "destinationTableName":"Device1234",
            "destinationDatabaseName":"IoTevents",
            "operation":"insert"
        }
    }
  }
```

Similarly, the following example shows how you can add the metadata section to the
Lambda output for a Firehose that uses Amazon Managed Streaming for Apache Kafka as a data source to instruct Firehose that
it must insert the record as a new record into a table named `Device1234`
in the database `IoTevents`.

```
{
"recordId": "49655962066601463032522589543535113056108699331451682818000000",
    "result": "Ok",
    "kafkaRecordValue": "1IiwiI6ICJmYWxsIiwgImdgU21IiwiI6ICJmYWxsIiwg==tcHV0ZXIgU2NpZW5jZSIsICJzZW1",

    "metadata":{
"otfMetadata":{
            "destinationTableName":"Device1234",
            "destinationDatabaseName":"IoTevents",
            "operation":"insert"
        }
    }
  }
```

For this example,

- `destinationDatabaseName` refers to the name of the target
  database and is a required field.
- `destinationTableName` refers to the name of the target table
  and is a required field.
- `operation` is an optional field with possible values as
  `insert`, `update`, and `delete`. If
  you do not specify any values, the default operation is
  `insert`.

###### Note

- When you specify the operation as `update` or
  `delete`, you must either specify unique keys for the
  destination table when you set up your Firehose stream, or set [identifier-field-ids](https://iceberg.apache.org/spec/#identifier-field-ids "https://iceberg.apache.org/spec/#identifier-field-ids") in Iceberg when you run [create table](https://iceberg.apache.org/docs/1.5.1/spark-ddl/#create-table "https://iceberg.apache.org/docs/1.5.1/spark-ddl/#create-table") or [alter table](https://iceberg.apache.org/docs/1.5.1/spark-ddl/#alter-table-set-identifier-fields "https://iceberg.apache.org/docs/1.5.1/spark-ddl/#alter-table-set-identifier-fields") operations in Iceberg. If you fail to specify
  this, then Firehose throws an error and delivers data to an S3 error
  bucket.
- The `Database Name` and `Table Name` values must
  exactly match with your destination database and table names. If they do
  not match, then Firehose throws an error and delivers data to an S3 error
  bucket.
- When your Firehose stream has both a Lambda transformation function and a
  JSONQuery expression, Firehose first checks for the metadata field in Lambda
  output to determine how to route the record to the appropriate
  destination table, and then look at the output of your JSONQuery
  expression for missing fields.

If the Lambda or JSONQuery expression don't provide the required
routing information, then Firehose assumes this as a single table scenario
and looks for single table information in the unique keys configuration.

For more information, see the [Route incoming records
to a single Iceberg table](apache-iceberg-format-input-record.md "apache-iceberg-format-input-record.md"). If Firehose fails to determine routing
information and match the record to a specified destination table, it
delivers the data to your specified S3 error bucket.

### Sample Lambda function

This Lambda function is a sample Python code that parses the incoming stream
records and adds required fields to specify how the data should be written to
specific tables. You can use this sample code to add the metadata section for
routing information.

```
import json
import base64


def lambda_handler(firehose_records_input, context):
    print("Received records for processing from DeliveryStream: " + firehose_records_input['deliveryStreamArn'])

    firehose_records_output = {}
    firehose_records_output['records'] = []


    for firehose_record_input in firehose_records_input['records']:

        # Get payload from Lambda input, it could be different with different sources
        if 'kafkaRecordValue' in firehose_record_input:
            payload_bytes = base64.b64decode(firehose_record_input['kafkaRecordValue']).decode('utf-8')
        else
            payload_bytes = base64.b64decode(firehose_record_input['data']).decode('utf-8')

        # perform data processing on customer payload bytes here

        # Create output with proper record ID, output data (may be different with different sources), result, and metadata
        firehose_record_output = {}

        if 'kafkaRecordValue' in firehose_record_input:
            firehose_record_output['kafkaRecordValue'] = base64.b64encode(payload_bytes.encode('utf-8'))
        else
            firehose_record_output['data'] = base64.b64encode(payload_bytes.encode('utf-8'))

        firehose_record_output['recordId'] = firehose_record_input['recordId']
        firehose_record_output['result'] =  'Ok'
        firehose_record_output['metadata'] = {
            'otfMetadata': {
                'destinationDatabaseName': 'your_destination_database',
                'destinationTableName': 'your_destination_table',
                'operation': 'insert'
                }
            }
        firehose_records_output['records'].append(firehose_record_output)
    return firehose_records_output
```
