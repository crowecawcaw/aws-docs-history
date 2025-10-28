# Route incoming records to a single

Iceberg table

If you want Firehose to insert data to a single Iceberg table, simply configure a single
database and table in your stream configuration as shown in the following example JSON.
For a single table, you do not require JQ expression and Lambda function for providing
the routing information to Firehose. If you provide these fields along with JQ or Lambda,
then Firehose will take input from JQ or Lambda.

```
[
  {
    "DestinationDatabaseName": "UserEvents",
    "DestinationTableName": "customer_id",
    "UniqueKeys": [
      "COLUMN_PLACEHOLDER"
    ],
    "S3ErrorOutputPrefix": "OPTIONAL_PREFIX_PLACEHOLDER"
  }
]
```

In this example, Firehose routes all input records to `customer_id` table in
`UserEvents` database. If you want to perform update or delete operations
on a single table, then you must provide the operation for each incoming record to
Firehose using either the [JSONQuery
method](apache-iceberg-format-input-record-different.md#apache-iceberg-route-jq "apache-iceberg-format-input-record-different.md#apache-iceberg-route-jq") or [Lambda
method](apache-iceberg-format-input-record-different.md#apache-iceberg-route-lambda "apache-iceberg-format-input-record-different.md#apache-iceberg-route-lambda").
