# Logging Amazon Keyspaces API calls with AWS CloudTrail

Amazon Keyspaces is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in Amazon Keyspaces. CloudTrail captures Data Definition Language (DDL) API calls
and Data Manipulation Language (DML) API calls for Amazon Keyspaces as events. The calls that are captured
include calls from the Amazon Keyspaces console and programmatic calls to the Amazon Keyspaces API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon Simple Storage Service
(Amazon S3) bucket, including events for Amazon Keyspaces.

If you don't configure a trail, you can still view the most recent supported events on the CloudTrail
console in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to Amazon Keyspaces, the IP address from which the request was made,
who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Configuring Amazon Keyspaces log file entries in CloudTrail](#configuring-ct-entries "#configuring-ct-entries")
- [Amazon Keyspaces Data Definition Language (DDL) information in CloudTrail](#keyspaces-in-cloudtrail-ddl "#keyspaces-in-cloudtrail-ddl")
- [Amazon Keyspaces Data Manipulation Language (DML) information in CloudTrail](#keyspaces-in-cloudtrail-dml "#keyspaces-in-cloudtrail-dml")
- [Understanding Amazon Keyspaces log file entries](#understanding-ct-entries "#understanding-ct-entries")

## Configuring Amazon Keyspaces log file entries in CloudTrail

Each Amazon Keyspaces API action logged in CloudTrail includes request parameters that are expressed in CQL
query language. For more information, see the [CQL language reference for Amazon Keyspaces (for Apache Cassandra)](cql.md "cql.md").

You can view, search, and download recent events in your
AWS account. For more information, see [Viewing events with CloudTrail event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon Keyspaces, create
a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. By
default, when you create a trail in the console, the trail applies to all AWS Regions. The
trail logs events from all Regions in the AWS partition and delivers the log files to the
Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further
analyze and act upon the event data collected in CloudTrail logs.

For more information, see the following topics in the
_AWS CloudTrail User Guide_:

- [Overview for
  creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Amazon Keyspaces Data Definition Language (DDL) information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When a DDL activity
occurs in Amazon Keyspaces, that activity is automatically recorded as a CloudTrail event along with other AWS service
events in **Event history**. The following table shows the DDL statements
that are logged for Amazon Keyspaces.

| CloudTrail `eventName` | Statement | CQL action              | AWS SDK action                                |
| ---------------------- | --------- | ----------------------- | --------------------------------------------- |
| CreateKeyspace         | DDL       | `CREATE KEYSPACE`       | `CreateKeyspace`                              |
| AlterKeyspace          | DDL       | `ALTER KEYSPACE`        | `UpdateKeyspace`                              |
| DropKeyspace           | DDL       | `DROP KEYSPACE`         | `DeleteKeyspace`                              |
| CreateTable            | DDL       | `CREATE TABLE`          | `CreateTable`                                 |
| DropTable              | DDL       | `DROP TABLE`            | `DeleteTable`                                 |
| AlterTable             | DDL       | `ALTER TABLE`           | `UpdateTable`, `TagResource`, `UntagResource` |
| CreateUdt              | DDL       | `CREATE TYPE`           | `CreateType`                                  |
| DropUdt                | DDL       | `DROP TYPE`             | `DeleteType`                                  |
| GetStream              | DDL       | no CQL action available | `GetStream`                                   |
| ListStreams            | DDL       | no CQL action available | `ListStreams`                                 |

## Amazon Keyspaces Data Manipulation Language (DML) information in CloudTrail

To enable logging of Amazon Keyspaces DML statements with CloudTrail, you have to first enable logging of
data plane API activity in CloudTrail. You can start logging Amazon Keyspaces DML events in new or existing
trails by choosing to log activity for the **data event type**
**Cassandra table** using the CloudTrail console, or by setting the
`resources.type` value to `AWS::Cassandra::Table` using the AWS CLI,
or CloudTrail API operations. For more information, see [Logging data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md").

For more information and an example that shows how to create alarms for data events, see the following
post on the AWS Database blog [Using DML auditing for Amazon Keyspaces (for Apache Cassandra)](https://aws.amazon.com/blogs/database/using-dml-auditing-for-amazon-keyspaces-for-apache-cassandra/ "https://aws.amazon.com/blogs/database/using-dml-auditing-for-amazon-keyspaces-for-apache-cassandra/").

The following table shows the data events that are logged by CloudTrail for `Cassandra table`.

| CloudTrail `eventName` | Statement | CQL action              | AWS SDK actions                                                                                            |
| ---------------------- | --------- | ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| Select                 | DML       | `SELECT`                | `GetKeyspace`, `GetTable`, `GetType`, `ListKeyspaces`, `ListTables`,<br>`ListTypes`, `ListTagsForResource` |
| Insert                 | DML       | `INSERT`                | no AWS SDK actions available                                                                               |
| Update                 | DML       | `UPDATE`                | no AWS SDK actions available                                                                               |
| Delete                 | DML       | `DELETE`                | no AWS SDK actions available                                                                               |
| `GetShardIterator`     | DML       | no CQL action available | `GetShardIterator`                                                                                         |
| `GetRecords`           | DML       | no CQL action available | `GetRecords`                                                                                               |

## Understanding Amazon Keyspaces log file entries

CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`CreateKeyspace`, `DropKeyspace`, `CreateTable`, and
`DropTable` actions:

```
`{
 "Records": [
 {
 "eventVersion": "1.05",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "AKIAIOSFODNN7EXAMPLE:alice",
 "arn": "arn:aws:sts::111122223333:assumed-role/users/alice",
 "accountId": "111122223333",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "AKIAIOSFODNN7EXAMPLE",
 "arn": "arn:aws:iam::111122223333:role/Admin",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "mfaAuthenticated": "false",
 "creationDate": "2020-01-15T18:47:56Z"
 }
 }
 },
 "eventTime": "2020-01-15T18:53:04Z",
 "eventSource": "cassandra.amazonaws.com",
 "eventName": "CreateKeyspace",
 "awsRegion": "us-east-1",
 "sourceIPAddress": "10.24.34.01",
 "userAgent": "Cassandra Client/ProtocolV4",
 "requestParameters": {
 "rawQuery": "\n\tCREATE KEYSPACE \"mykeyspace\"\n\tWITH\n\t\tREPLICATION = {'class': 'SingleRegionStrategy'}\n\t\t",
 "keyspaceName": "mykeyspace"
 },
 "responseElements": null,
 "requestID": "bfa3e75d-bf4d-4fc0-be5e-89d15850eb41",
 "eventID": "d25beae8-f611-4229-877a-921557a07bb9",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::Cassandra::Keyspace",
 "ARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/"
 }
 ],
 "eventType": "AwsApiCall",
 "apiVersion": "3.4.4",
 "recipientAccountId": "111122223333",
 "managementEvent": true,
 "eventCategory": "Management",
 "tlsDetails": {
 "tlsVersion": "TLSv1.2",
 "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
 "clientProvidedHostHeader": "cassandra.us-east-1.amazonaws.com"
 },
 {
 "eventVersion": "1.05",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "AKIAIOSFODNN7EXAMPLE:alice",
 "arn": "arn:aws:sts::111122223333:assumed-role/users/alice",
 "accountId": "111122223333",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "AKIAIOSFODNN7EXAMPLE",
 "arn": "arn:aws:iam::111122223333:role/Admin",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "mfaAuthenticated": "false",
 "creationDate": "2020-01-15T18:47:56Z"
 }
 }
 },
 "eventTime": "2020-01-15T19:28:39Z",
 "eventSource": "cassandra.amazonaws.com",
 "eventName": "DropKeyspace",
 "awsRegion": "us-east-1",
 "sourceIPAddress": "10.24.34.01",
 "userAgent": "Cassandra Client/ProtocolV4",
 "requestParameters": {
 "rawQuery": "DROP KEYSPACE \"mykeyspace\"",
 "keyspaceName": "mykeyspace"
 },
 "responseElements": null,
 "requestID": "66f3d86a-56ae-4c29-b46f-abcd489ed86b",
 "eventID": "e5aebeac-e1dd-41e3-a515-84fe6aaabd7b",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::Cassandra::Keyspace",
 "ARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/"
 }
 ],
 "eventType": "AwsApiCall",
 "apiVersion": "3.4.4",
 "recipientAccountId": "111122223333",
 "managementEvent": true,
 "eventCategory": "Management",
 "tlsDetails": {
 "tlsVersion": "TLSv1.2",
 "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
 "clientProvidedHostHeader": "cassandra.us-east-1.amazonaws.com"
 },
 {
 "eventVersion": "1.05",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "AKIAIOSFODNN7EXAMPLE:alice",
 "arn": "arn:aws:sts::111122223333:assumed-role/users/alice",
 "accountId": "111122223333",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "AKIAIOSFODNN7EXAMPLE",
 "arn": "arn:aws:iam::111122223333:role/Admin",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "mfaAuthenticated": "false",
 "creationDate": "2020-01-15T18:47:56Z"
 }
 }
 },
 "eventTime": "2020-01-15T18:55:24Z",
 "eventSource": "cassandra.amazonaws.com",
 "eventName": "CreateTable",
 "awsRegion": "us-east-1",
 "sourceIPAddress": "10.24.34.01",
 "userAgent": "Cassandra Client/ProtocolV4",
 "requestParameters": {
 "rawQuery": "\n\tCREATE TABLE \"mykeyspace\".\"mytable\"(\n\t\t\"ID\" int,\n\t\t\"username\" text,\n\t\t\"email\" text,\n\t\t\"post_type\" text,\n\t\tPRIMARY KEY((\"ID\", \"username\", \"email\")))",
 "keyspaceName": "mykeyspace",
 "tableName": "mytable"
 },
 "responseElements": null,
 "requestID": "5f845963-70ea-4988-8a7a-2e66d061aacb",
 "eventID": "fe0dbd2b-7b34-4675-a30c-740f9d8d73f9",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::Cassandra::Table",
 "ARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable"
 }
 ],
 "eventType": "AwsApiCall",
 "apiVersion": "3.4.4",
 "recipientAccountId": "111122223333",
 "managementEvent": true,
 "eventCategory": "Management",
 "tlsDetails": {
 "tlsVersion": "TLSv1.2",
 "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
 "clientProvidedHostHeader": "cassandra.us-east-1.amazonaws.com"
 },
 {
 "eventVersion": "1.05",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "AKIAIOSFODNN7EXAMPLE:alice",
 "arn": "arn:aws:sts::111122223333:assumed-role/users/alice",
 "accountId": "111122223333",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "AKIAIOSFODNN7EXAMPLE",
 "arn": "arn:aws:iam::111122223333:role/Admin",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "mfaAuthenticated": "false",
 "creationDate": "2020-01-15T18:47:56Z"
 }
 }
 },
 "eventTime": "2020-01-15T19:27:59Z",
 "eventSource": "cassandra.amazonaws.com",
 "eventName": "DropTable",
 "awsRegion": "us-east-1",
 "sourceIPAddress": "10.24.34.01",
 "userAgent": "Cassandra Client/ProtocolV4",
 "requestParameters": {
 "rawQuery": "DROP TABLE \"mykeyspace\".\"mytable\"",
 "keyspaceName": "mykeyspace",
 "tableName": "mytable"
 },
 "responseElements": null,
 "requestID": "025501b0-3582-437e-9d18-8939e9ef262f",
 "eventID": "1a5cbedc-4e38-4889-8475-3eab98de0ffd",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::Cassandra::Table",
 "ARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable"
 }
 ],
 "eventType": "AwsApiCall",
 "apiVersion": "3.4.4",
 "recipientAccountId": "111122223333",
 "managementEvent": true,
 "eventCategory": "Management",
 "tlsDetails": {
 "tlsVersion": "TLSv1.2",
 "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
 "clientProvidedHostHeader": "cassandra.us-east-1.amazonaws.com"
 }
 ]
}`
```

The following log file shows an example of a `SELECT` statement.

```
`{
 "eventVersion": "1.09",
 "userIdentity": {
 "type": "IAMUser",
 "principalId": "AKIAIOSFODNN7EXAMPLE",
 "arn": "arn:aws:iam::111122223333:user/alice",
 "accountId": "111122223333",
 "userName": "alice"
 },
 "eventTime": "2023-11-17T10:38:04Z",
 "eventSource": "cassandra.amazonaws.com",
 "eventName": "Select",
 "awsRegion": "us-east-1",
 "sourceIPAddress": "10.24.34.01",
 "userAgent": "Cassandra Client/ProtocolV4",
 "requestParameters": {
 "keyspaceName": "my_keyspace",
 "tableName": "my_table",
 "conditions": [
 "pk = **(Redacted)",
 "ck < 3**(Redacted)0",
 "region = 't**(Redacted)t'"
 ],
 "select": [
 "pk",
 "ck",
 "region"
 ],
 "allowFiltering": true
 },
 "responseElements": null,
 "requestID": "6d83bbf0-a3d0-4d49-b1d9-e31779a28628",
 "eventID": "e00552d3-34e9-4092-931a-912c4e08ba17",
 "readOnly": true,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::Cassandra::Table",
 "ARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table"
 }
 ],
 "eventType": "AwsApiCall",
 "apiVersion": "3.4.4",
 "managementEvent": false,
 "recipientAccountId": "111122223333",
 "eventCategory": "Data",
 "tlsDetails": {
 "tlsVersion": "TLSv1.3",
 "cipherSuite": "TLS_AES_128_GCM_SHA256",
 "clientProvidedHostHeader": "cassandra.us-east-1.amazonaws.com"
 }
}`
```

The following log file shows an example of an `INSERT` statement.

```
`{
 "eventVersion": "1.09",
 "userIdentity": {
 "type": "IAMUser",
 "principalId": "AKIAIOSFODNN7EXAMPLE",
 "arn": "arn:aws:iam::111122223333:user/alice",
 "accountId": "111122223333",
 "userName": "alice"
 },
 "eventTime": "2023-12-01T22:11:43Z",
 "eventSource": "cassandra.amazonaws.com",
 "eventName": "Insert",
 "awsRegion": "us-east-1",
 "sourceIPAddress": "10.24.34.01",
 "userAgent": "Cassandra Client/ProtocolV4",
 "requestParameters": {
 "keyspaceName": "my_keyspace",
 "tableName": "my_table",
 "primaryKeys": {
 "pk": "**(Redacted)",
 "ck": "1**(Redacted)8"
 },
 "columnNames": [
 "pk",
 "ck",
 "region"
 ],
 "updateParameters": {
 "TTL": "2**(Redacted)0"
 }
 }
 },
 "responseElements": null,
 "requestID": "edf8af47-2f87-4432-864d-a960ac35e471",
 "eventID": "81b56a1c-9bdd-4c92-bb8e-92776b5a3bf1",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::Cassandra::Table",
 "ARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table"
 }
 ],
 "eventType": "AwsApiCall",
 "apiVersion": "3.4.4",
 "managementEvent": false,
 "recipientAccountId": "111122223333",
 "eventCategory": "Data",
 "tlsDetails": {
 "tlsVersion": "TLSv1.3",
 "cipherSuite": "TLS_AES_128_GCM_SHA256",
 "clientProvidedHostHeader": "cassandra.us-east-1.amazonaws.com"
 }
}`
```

The following log file shows an example of an `UPDATE` statement.

```
`{
 "eventVersion": "1.09",
 "userIdentity": {
 "type": "IAMUser",
 "principalId": "AKIAIOSFODNN7EXAMPLE",
 "arn": "arn:aws:iam::111122223333:user/alice",
 "accountId": "111122223333",
 "userName": "alice"
 },
 "eventTime": "2023-12-01T22:11:43Z",
 "eventSource": "cassandra.amazonaws.com",
 "eventName": "Update",
 "awsRegion": "us-east-1",
 "sourceIPAddress": "10.24.34.01",
 "userAgent": "Cassandra Client/ProtocolV4",
 "requestParameters": {
 "keyspaceName": "my_keyspace",
 "tableName": "my_table",
 "primaryKeys": {
 "pk": "'t**(Redacted)t'",
 "ck": "'s**(Redacted)g'"
 },
 "assignmentColumnNames": [
 "nonkey"
 ],
 "conditions": [
 "nonkey < 1**(Redacted)7"
 ]
 },
 "responseElements": null,
 "requestID": "edf8af47-2f87-4432-864d-a960ac35e471",
 "eventID": "81b56a1c-9bdd-4c92-bb8e-92776b5a3bf1",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::Cassandra::Table",
 "ARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table"
 }
 ],
 "eventType": "AwsApiCall",
 "apiVersion": "3.4.4",
 "managementEvent": false,
 "recipientAccountId": "111122223333",
 "eventCategory": "Data",
 "tlsDetails": {
 "tlsVersion": "TLSv1.3",
 "cipherSuite": "TLS_AES_128_GCM_SHA256",
 "clientProvidedHostHeader": "cassandra.us-east-1.amazonaws.com"
 }
}`
```

The following log file shows an example of a `DELETE` statement.

```
`{
 "eventVersion": "1.09",
 "userIdentity": {
 "type": "IAMUser",
 "principalId": "AKIAIOSFODNN7EXAMPLE",
 "arn": "arn:aws:iam::111122223333:user/alice",
 "accountId": "111122223333",
 "userName": "alice",
 },
 "eventTime": "2023-10-23T13:59:05Z",
 "eventSource": "cassandra.amazonaws.com",
 "eventName": "Delete",
 "awsRegion": "us-east-1",
 "sourceIPAddress": "10.24.34.01",
 "userAgent": "Cassandra Client/ProtocolV4",
 "requestParameters": {
 "keyspaceName": "my_keyspace",
 "tableName": "my_table",
 "primaryKeys": {
 "pk": "**(Redacted)",
 "ck": "**(Redacted)"
 },
 "conditions": [],
 "deleteColumnNames": [
 "m",
 "s"
 ],
 "updateParameters": {}
 },
 "responseElements": null,
 "requestID": "3d45e63b-c0c8-48e2-bc64-31afc5b4f49d",
 "eventID": "499da055-c642-4762-8775-d91757f06512",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::Cassandra::Table",
 "ARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table"
 }
 ],
 "eventType": "AwsApiCall",
 "apiVersion": "3.4.4",
 "managementEvent": false,
 "recipientAccountId": "111122223333",
 "eventCategory": "Data",
 "tlsDetails": {
 "tlsVersion": "TLSv1.3",
 "cipherSuite": "TLS_AES_128_GCM_SHA256",
 "clientProvidedHostHeader": "cassandra.us-east-1.amazonaws.com"
 }
}`
```
