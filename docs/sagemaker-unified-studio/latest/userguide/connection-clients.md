# Retrieving AWS client with

SDK for Python (Boto3)

You can retrieve an SDK for Python (Boto3) AWS client initialized with the connection's
credentials.

###### Example

The following example shows how to create a Redshift client using
create_client() from Redshift connection.

```
`redshift_connection: Connection = proj.connection("`project.redshift`")
redshift_client = redshift_connection.create_client()`
```

Some connections are directly associated with an AWS service, and will
default to using that AWS service's client if no service name is specified.
Those connections are listed in the following table.

| Connection Type | AWS Service Name |
| --------------- | ---------------- |
| ATHENA          | athena           |
| DYNAMODB        | dynamodb         |
| REDSHIFT        | redshift         |
| S3              | s3               |
| S3_FOLDER       | s3               |

For other connection types, you must specify an AWS service name.

###### Example

See the following example for details.

```
`iam_connection: Connection = proj.connection("project.iam")
glue_client = iam_connection.create_client("glue")`
```
