

# Understanding audit records

Aurora DSQL delivers each audit record as a JSON object that contains details about a statement that ran. The following sections describe where to find audit records and the fields that each record contains.

## How records are delivered to your chosen Amazon S3 bucket
<a name="audit-logging-s3-objects"></a>

Audit records are delivered to your bucket as gzip-compressed files. Each line of a file is one audit record in JSON format. By default, object keys look like the following example:

```text
AWSLogs/111122223333/dsql/us-east-1/2026/11/04/18/111122223333_dsql_audit_logs_us-east-1_20261104T18Z_{{unique-id}}.log.gz
```

The date and hour in the key come from the `event_timestamp` field of the records, in Coordinated Universal Time (UTC). An hour can have more than one file.

To change the object path, see [Setting up audit log delivery](audit-logging-setup.md#audit-logging-set-up-delivery).

To view the audit records in your bucket, use the Amazon S3 console or the AWS CLI.

------
#### [ Console ]

**To view audit records (console)**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3).

1. In the navigation pane, choose **General purpose buckets**, and then choose the name of your bucket.

1. Choose the folders of the object key to find a file. By default, choose **AWSLogs**, your AWS account ID, **dsql**, the Region of your cluster, and then the date and hour of the records.

1. Select the check box next to a file, and then choose **Download**.

1. Decompress the downloaded file. Each line of the file is one audit record in JSON format.

------
#### [ CLI ]

The following AWS CLI commands list the audit log files in a bucket, and then print the records of one of the files. Replace {{amzn-s3-demo-destination-bucket}} with the name of your bucket, {{111122223333}} with your AWS account ID, and {{object-key}} with the key of a file:

```bash
aws s3 ls s3://{{amzn-s3-demo-destination-bucket}}/AWSLogs/{{111122223333}}/dsql/ --recursive
aws s3 cp s3://{{amzn-s3-demo-destination-bucket}}/{{object-key}} - | gunzip
```

------

You can also use the AWS SDKs or the Amazon S3 API. For more information, see [Downloading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the *Amazon S3 User Guide*.

## Record payload
<a name="audit-logging-record-payload"></a>

**Example – UPDATE statement**  
The following example shows the audit record of an `UPDATE` statement with two bound parameters. The cluster audited the statement with `dsql_audit.log_parameter` and `dsql_audit.log_rows` turned on:

```json
{
  "resource_arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abcdefghijklmnopqrstuvwxyz",
  "event_timestamp": 1793817600123,
  "schema_version": "1.0",
  "aws_region": "us-east-1",
  "cluster_id": "abcdefghijklmnopqrstuvwxyz",
  "type": "SESSION",
  "database": "postgres",
  "session_id": "c5hq2mgy4bwgdk3tsx7qnrmb4e",
  "iam_principal": "AROA123456789EXAMPLE",
  "iam_arn": "arn:aws:iam::111122223333:role/OrdersService",
  "session_user": "app_user",
  "user_id": "26384",
  "client_application": "orders-service",
  "transaction_id": "a3kq7zr2mfxv4c6tybw5hnde4q",
  "statement_id": 4,
  "substatement_id": 1,
  "class": "WRITE",
  "command": "UPDATE",
  "statement_text": "UPDATE orders SET status = $1 WHERE order_id = $2",
  "parameters": "shipped,1001",
  "rows_affected": 1
}
```

**Example – CREATE TABLE statement**  
The following example shows the two audit records of a `CREATE TABLE` statement that defines a primary key. The first record is for the table, and the second record is for the index of the primary key. The cluster audited the statement with `dsql_audit.log_parameter` and `dsql_audit.log_rows` turned on:

```json
{
  "resource_arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abcdefghijklmnopqrstuvwxyz",
  "event_timestamp": 1793817000456,
  "schema_version": "1.0",
  "aws_region": "us-east-1",
  "cluster_id": "abcdefghijklmnopqrstuvwxyz",
  "type": "SESSION",
  "database": "postgres",
  "session_id": "k2fq6nhv3cwdmb7xsr4tyl5gpa",
  "iam_principal": "AROA123456789EXAMPLE",
  "iam_arn": "arn:aws:iam::111122223333:role/OrdersService",
  "session_user": "admin",
  "user_id": "15579",
  "client_application": "psql",
  "transaction_id": "m7tq4xw2bhkf5zdcvn3ryg6sla",
  "statement_id": 1,
  "substatement_id": 1,
  "class": "DDL",
  "command": "CREATE TABLE",
  "object_type": "TABLE",
  "object_name": "public.orders",
  "statement_text": "CREATE TABLE orders (order_id int PRIMARY KEY, status text);",
  "parameters": "<none>",
  "rows_affected": 0
}
{
  "resource_arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abcdefghijklmnopqrstuvwxyz",
  "event_timestamp": 1793817000456,
  "schema_version": "1.0",
  "aws_region": "us-east-1",
  "cluster_id": "abcdefghijklmnopqrstuvwxyz",
  "type": "SESSION",
  "database": "postgres",
  "session_id": "k2fq6nhv3cwdmb7xsr4tyl5gpa",
  "iam_principal": "AROA123456789EXAMPLE",
  "iam_arn": "arn:aws:iam::111122223333:role/OrdersService",
  "session_user": "admin",
  "user_id": "15579",
  "client_application": "psql",
  "transaction_id": "m7tq4xw2bhkf5zdcvn3ryg6sla",
  "statement_id": 1,
  "substatement_id": 1,
  "class": "DDL",
  "command": "CREATE INDEX",
  "object_type": "INDEX",
  "object_name": "public.orders_pkey",
  "statement_text": "CREATE TABLE orders (order_id int PRIMARY KEY, status text);",
  "parameters": "<none>",
  "rows_affected": 0
}
```

## Record fields
<a name="audit-logging-record-format"></a>

Each audit record contains the following fields.


| Field | Description | 
| --- |--- |
| resource\_arn | The ARN of the cluster. | 
| event\_timestamp | The start time of the statement, in milliseconds since the Unix epoch, in UTC. | 
| schema\_version | The version of the audit record format, such as 1.0. | 
| aws\_region | The AWS Region of the cluster. | 
| cluster\_id | The ID of the cluster. | 
| type | The type of audit record. The value is SESSION. | 
| database | The name of the database, such as postgres. | 
| session\_id | The ID of the connection. Use it to find the other records of the same connection. | 
| iam\_principal | The unique ID of the IAM role or user that authenticated the connection. | 
| iam\_arn | The ARN of the IAM role or user that authenticated the connection. | 
| session\_user | The database role that the connection uses. | 
| user\_id | The object identifier (OID) of the database role that ran the statement. This role can differ from session\_user, for example after SET LOCAL ROLE or in the body of a SECURITY DEFINER function. | 
| client\_application | The application\_name that the client set for the connection. | 
| transaction\_id | The ID of the transaction. Use it to find the other records of the same transaction. | 
| statement\_id | A number that identifies the statement. Records that have the same transaction\_id and statement\_id come from the same statement. | 
| substatement\_id | A number that identifies a substatement within the statement. | 
| class | The class of the statement: READ, WRITE, FUNCTION, ROLE, DDL, or MISC. | 
| command | The command, such as SELECT, INSERT, or CREATE TABLE. | 
| object\_type | The type of the object, such as TABLE, INDEX, or FUNCTION. Included in DDL and FUNCTION records when the statement acts on an object, and in ROLE records for GRANT and REVOKE statements on an object. | 
| object\_name | The fully qualified name of the object, such as public.orders. Included only in DDL and FUNCTION records, and only when the statement acts on an object. | 
| statement\_text | The text of the statement as the client sent it, including any literal values. Contains <not logged> when dsql\_audit.log\_statement is off. | 
| parameters | The values of the statement's bound parameters, as one comma-separated string. Contains <not logged> when dsql\_audit.log\_parameter or dsql\_audit.log\_statement is off, and <none> when the statement has no bound parameters. | 
| rows\_affected | The number of rows that the statement read or changed. Included only when dsql\_audit.log\_rows is on. | 

## Format details
<a name="audit-logging-format-details"></a>

The following details describe how Aurora DSQL formats audit records.
+ **Record order.** Records can arrive out of order. To order records, sort them by `event_timestamp`, `session_id`, `transaction_id`, `statement_id`, and then `substatement_id`.
+ **Omitted fields.** Records omit fields that don't apply. For example, a record includes `rows_affected` only when `dsql_audit.log_rows` is `on`.
+ **Several records for one statement.** A statement can produce more than one record. For example, a `CREATE TABLE` statement that defines a primary key produces one record for the table and one for its index. These records have the same `transaction_id`, `statement_id`, and `substatement_id`, and differ in `command`, `object_type`, and `object_name`.
+ **Literal values in statement text.** The `statement_text` field contains the statement as the client sent it, including any literal values. To keep sensitive values out of audit records, pass them as bound parameters and keep `dsql_audit.log_parameter` turned off. To protect these fields with a customer managed key, see [Data protection](audit-logging-iam.md#audit-logging-data-protection).
+ **Tables in statement text.** `READ` and `WRITE` records don't include `object_type` and `object_name`. To find the tables that a statement accessed, use `statement_text`.
+ **Placeholder values.** Some fields contain a placeholder instead of a value:
  + `<not logged>` – In `statement_text` when `dsql_audit.log_statement` is `off`. In `parameters` when `dsql_audit.log_parameter` or `dsql_audit.log_statement` is `off`. To record these values, turn on the setting.
  + `<none>` – In `parameters` when the statement has no bound parameters.
  + `<long param suppressed>` – In `parameters`, in place of a variable-length value that's longer than `dsql_audit.log_parameter_max_size`.