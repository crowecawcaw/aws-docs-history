Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with streaming ingestion

from Apache Kafka sources

This topic describes how to consume streaming data from Amazon MSK, Apache Kafka or Confluent Cloud
using a materialized view.

The purpose of Amazon Redshift streaming ingestion is to simplify the process for
directly ingesting stream data from a streaming service into Amazon Redshift or
Amazon Redshift Serverless. This works with Amazon MSK Provisioned and Amazon MSK Serverless, with open-source Apache Kafka, and with
Confluent Cloud. Amazon Redshift
streaming ingestion removes the need to stage an Apache Kafka topic in
Amazon S3 before ingesting the stream data into Redshift.

On a technical level, streaming ingestion provides
low-latency, high-speed ingestion of
stream or topic data into an Amazon Redshift materialized view. Following setup, using materialized
view refresh, you can take in large data volumes.

You must have an Apache Kafka source available before configuring Amazon Redshift streaming
ingestion. If you do not have a source, create one using the following instructions:

- **Amazon MSK** — [Getting Started Using
  Amazon MSK](../../../msk/latest/developerguide/getting-started.md "../../../msk/latest/developerguide/getting-started.md")
- **Apache Kafka** —
  [Apache Kafka Quickstart](https://kafka.apache.org/quickstart "https://kafka.apache.org/quickstart")
- **Confluent Cloud** —
  [Quick Start for Confluent Cloud](https://docs.confluent.io/cloud/current/get-started/index.html "https://docs.confluent.io/cloud/current/get-started/index.html")

## Setting up streaming ingestion from Kafka

Use the following procedures to set up streaming ingestion to Amazon Redshift from Amazon MSK, or Apache Kafka sources
that are not AWS-managed (Apache Kafka and Confluent Cloud).

###### Topics

- [Set
  up authentication](#materialized-view-streaming-ingestion-getting-started-MSK-setup-auth "#materialized-view-streaming-ingestion-getting-started-MSK-setup-auth")
- [Setting up your VPC](#materialized-view-streaming-ingestion-getting-started-MSK-Setup-VPC "#materialized-view-streaming-ingestion-getting-started-MSK-Setup-VPC")
- [Create a Materialized View](#materialized-view-streaming-ingestion-getting-started-MSK-setup-materialized-view "#materialized-view-streaming-ingestion-getting-started-MSK-setup-materialized-view")

### Set

up authentication

This section describes setting up authentication to allow your Amazon Redshift application to access
an Amazon MSK source.

After you create your application's role, attach one of the following policies to allow access to
your Amazon MSK, Apache Kafka, or Confluent Cloud cluster. For mTLS authentication, you can store the certificates that Amazon Redshift uses in ACM or Secrets Manager,
so you must choose the policy that matches where the certificate is stored.

Note that self-signed certificates are not supported for authentication or data in
transit when you use direct streaming ingestion into Amazon Redshift with any of the supported
Apache Kafka streaming sources. These include Amazon MSK, Apache Kafka, and Confluent
Cloud. Consider using certificates generated with AWS Certificate Manager or any other publicly
trusted certificate authority.

Amazon Redshift IAM authentication with MSK is only supported on Kafka version 2.7.1 or
above.

**AUTHENTICATION IAM (Amazon MSK only):**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MSKIAMpolicy",
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:ReadData",
 "kafka-cluster:DescribeTopic",
 "kafka-cluster:Connect"
 ],
 "Resource": [
 "arn:aws:kafka:*:`111122223333`:cluster/MyTestCluster/*",
 "arn:aws:kafka:*:`111122223333`:topic/MyTestCluster/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:AlterGroup",
 "kafka-cluster:DescribeGroup"
 ],
 "Resource": [
 "arn:aws:kafka:*:`111122223333`:group/MyTestCluster/*"
 ]
 }
 ]
}`

```

**AUTHENTICATION MTLS: using a certificate stored in AWS Certificate Manager**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MSKmTLSACMpolicy",
 "Effect": "Allow",
 "Action": [
 "acm:ExportCertificate"
 ],
 "Resource": [
 "arn:aws:acm:us-east-1:444455556666:certificate/certificate_ID"
 ]
 }
 ]
}`

```

**AUTHENTICATION MTLS: using a certificate stored in AWS Secrets Manager**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MSKmTLSSecretsManagerpolicy",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:444455556666:secret:secret_ID"
 ]
 }
 ]
}`

```

Amazon MSK
If you use AUTHENTICATION NONE to connect to a Amazon MSK source, no IAM role is required.
However, if you use AUTHENTICATION IAM
or MTLS to authenticate with your Amazon MSK cluster, your Amazon Redshift cluster or Amazon Redshift Serverless namespace
must have an attached
IAM role with
appropriate permissions. Create an IAM role with a trust policy that allows your Amazon Redshift cluster
or Amazon Redshift Serverless namespace to assume
the role.
After you create the role, add one of the following permissions to support IAM or MTLS.
For mTLS authentication, the certificates that Amazon Redshift uses can be stored in AWS Certificate Manager
or AWS Secrets Manager, so you must choose the policy that matches where the certificate is stored.
Attach the role to your Amazon Redshift provisioned cluster or Redshift Serverless namespace. For information about how to configure the trust policy for the IAM role, see [Authorizing Amazon Redshift to access other AWS services on your behalf](../mgmt/authorizing-redshift-service.md "../mgmt/authorizing-redshift-service.md").

The following table shows complimentary configuration options to set for streaming ingestion from Amazon MSK:

| Amazon Redshift configuration | Amazon MSK configuration | Port to open between Redshift and Amazon MSK |
| ----------------------------- | ------------------------ | -------------------------------------------- |
| AUTHENTICATION NONE           | TLS transport disabled   | 9092                                         |
| AUTHENTICATION NONE           | TLS transport enabled    | 9094                                         |
| AUTHENTICATION IAM            | IAM                      | 9098/9198                                    |
| AUTHENTICATION MTLS           | TLS transport enabled    | 9094                                         |

Amazon Redshift authentication is set in the CREATE EXTERNAL SCHEMA statement.

###### Note

In a case where the Amazon MSK cluster has Mutual Transport Layer Security (mTLS) authentication enabled, configuring Amazon Redshift to use AUTHENTICATION NONE
directs it to use port 9094 for unauthenticated access. However, this will fail because the port is being used by mTLS authentication. Because of this, we
recommend that you switch to AUTHENTICATION mtls when you use mTLS.

Apache Kafka or Confluent Cloud
For Apache Kafka and Confluent Cloud, Amazon Redshift supports the following connection protocols:

- You can use mTLS or plaintext with TLS transport
  for authentication when connecting to Apache Kafka.
- You can only use mTLS
  for authentication when connecting to Confluent Cloud.

Amazon Redshift supports the following encryption protocols for connecting to Apache Kafka or Confluent Cloud:

**Supported
authentication methods for Apache Kafka and Confluent Cloud**

| Amazon Redshift     | Kafka Security Protocol | Apache Kafka support   | Confluent Cloud support |
| ------------------- | ----------------------- | ---------------------- | ----------------------- |
| AUTHENTICATION NONE | PLAINTEXT               | No                     | No                      |
| AUTHENTICATION NONE | SSL                     | Yes                    | No                      |
| AUTHENTICATION IAM  | SASL_SSL                | No                     | No                      |
| AUTHENTICATION MTLS | SSL                     | Yes (with certificate) | Yes (with certificate)  |

Note that Amazon Redshift does not support SASL/SCRAM or SASL/PLAINTEXT.

### Setting up your VPC

After you create your authentication resources, check your VPC and verify that your Amazon Redshift
cluster or Amazon Redshift Serverless workgroup has a route to get to
your Apache Kafka source.

###### Note

For Amazon MSK, the inbound security group rules for your Amazon MSK cluster
should allow your Amazon Redshift cluster's or your Redshift Serverless workgroup's security group.
The ports you specify depend on the authentication methods configured
on your Amazon MSK cluster. For
more information, see [Port
information](../../../msk/latest/developerguide/port-info.md "../../../msk/latest/developerguide/port-info.md") and [Access from within AWS but outside the VPC](../../../msk/latest/developerguide/aws-access.md "../../../msk/latest/developerguide/aws-access.md").

Next, enable enhanced VPC routing on your Amazon Redshift cluster or Amazon Redshift Serverless workgroup. For more information,
see [Enabling enhanced VPC routing](../mgmt/enhanced-vpc-enabling-cluster.md "../mgmt/enhanced-vpc-enabling-cluster.md").

### Create a Materialized View

In this section, you set up the materialized view that Amazon Redshift uses to access your Apache Kafka streaming data.

Assuming you have an Apache Kafka cluster available, the first step is to define a schema in Redshift
with `CREATE EXTERNAL SCHEMA` and to reference the cluster as the data source. Following that, to
access data in the topic, define the `STREAM` in a materialized view. You can store records from your
topic using the default Amazon Redshift VARBYTE datatype, or define a schema that converts the data to
the semi-structured `SUPER` format. When
you query the materialized view, the returned records are a point-in-time view of the topic.

1. In Amazon Redshift, create an external schema to map to the Apacke Kafka cluster. The syntax is the following:

```
CREATE EXTERNAL SCHEMA MySchema
FROM KAFKA
[ IAM_ROLE [ default | 'iam-role-arn' ] ]
AUTHENTICATION [ none | iam | mtls ]
{AUTHENTICATION_ARN 'acm-certificate-arn' |  SECRET_ARN 'asm-secret-arn'};
```

In the `FROM` clause, `KAFKA` denotes that
the schema maps data from an Apache Kafka source.

`AUTHENTICATION` denotes the authentication type for streaming ingestion. There
are three types available:

    * **none** – Specifies that there is no authentication
     required. This corresponds to Unauthenticated access on MSK. This corresponds to SSL authentication in Apache Kafka.
     This authentication method is not supported for Confluent Cloud.
    * **iam** – Specifies IAM authentication.
     You can only use IAM authentication with Amazon MSK. When you choose this, make sure
     that the IAM role has permissions for IAM authentication.
     For more information about setting up the required IAM policies, see
     [Setting up streaming ingestion from Kafka](#materialized-view-streaming-ingestion-getting-started-MSK-setup "#materialized-view-streaming-ingestion-getting-started-MSK-setup").
    * **mtls** – Specifies that mutual transport layer security provides
     secure communication by
     facilitating authentication between a client and server. In this case, the client is Redshift and the server is Apache Kafka.
     For more
     information about configuring streaming ingestion with mTLS, see [Authentication with mTLS for Redshift
     streaming ingestion from Apache Kafka sources](materialized-view-streaming-ingestion-mtls.md "materialized-view-streaming-ingestion-mtls.md").

Note that Amazon MSK authentication with a username and password isn't supported for streaming ingestion.

The `AUTHENTICATION_ARN` parameter specifies the ARN of the ACM mutual transport
layer security (mTLS) certificate you use to establish an encrypted connection.

The `SECRET_ARN` parameter specifies the arn of the AWS Secrets Manager secret containing
the certificate to be used by Amazon Redshift for mTLS.

The following examples show how to set the broker URI for the Amazon MSK cluster when you create the external
schema:

**Using IAM authentication:**

```
CREATE EXTERNAL SCHEMA my_schema
FROM KAFKA
IAM_ROLE 'arn:aws:iam::012345678901:role/my_role'
AUTHENTICATION IAM
URI 'b-1.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9098,b-2.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9098'
```

**Using no authentication:**

```
CREATE EXTERNAL SCHEMA my_schema
FROM KAFKA
AUTHENTICATION none
URI 'b-1.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9092,b-2.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9092'
```

**Using mTLS:**

```
CREATE EXTERNAL SCHEMA my_schema
FROM KAFKA
IAM_ROLE 'arn:aws:iam::012345678901:role/my_role'
AUTHENTICATION MTLS
URI 'b-1.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9094,b- 2.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9094'
{AUTHENTICATION_ARN 'acm-certificate-arn' |  SECRET_ARN 'asm-secret-arn'}
```

For more information on creating an external schema, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md"). 2. Create a materialized view to consume the data from the topic. Use a SQL command such as the following sample.

```
CREATE MATERIALIZED VIEW MyView AUTO REFRESH YES AS
SELECT *
FROM MySchema."mytopic";
```

Kafka topic names are case sensitive and can contain both
uppercase and lowercase letters. To ingest from topics with uppercase
names, you can set the configuration
`enable_case_sensitive_identifier` to `true`
at the session or database level. For more information, see [Names and identifiers](r_names.md "r_names.md") and
[enable_case_sensitive_identifier](r_enable_case_sensitive_identifier.md "r_enable_case_sensitive_identifier.md").

To turn on auto refresh, use `AUTO REFRESH YES`. The default behavior is manual refresh. 3. Metadata columns include the following:

| Metadata column      | Data type                   | Description                                                                                                                                                                                                                                                |
| -------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kafka_partition      | bigint                      | Partition id of the record from the Kafka<br>topic                                                                                                                                                                                                         |
| kafka_offset         | bigint                      | Offset of the record in the Kafka topic for<br>a given partition                                                                                                                                                                                           |
| kafka_timestamp_type | char(1)                     | Type of timestamp used in the Kafka record:<br>• _C_ – Record creation time (CREATE_TIME) on the client side<br>• _L_ – Record append time (LOG_APPEND_TIME) on the Kafka server side<br>• _U_ – Record creation time is not available (NO_TIMESTAMP_TYPE) |
| kafka_timestamp      | timestamp without time zone | The timestamp value for the record                                                                                                                                                                                                                         |
| kafka_key            | varbyte                     | The key of the Kafka record                                                                                                                                                                                                                                |
| kafka_value          | varbyte                     | The record received from Kafka                                                                                                                                                                                                                             |
| kafka_headers        | super                       | The header of the record received from Kafka                                                                                                                                                                                                               |
| refresh_time         | timestamp without time zone | The time the refresh started                                                                                                                                                                                                                               |

It's important to note if you have business logic in your materialized view definition that
results in business logic errors, this can result in ingestion failures in streaming
ingestion in some cases. This might lead to you having to drop and re-create the materialized view. To avoid this, we
recommend that you keep your business logic simple and run additional logic on the data after you ingest it. 4. Refresh the view, which invokes Amazon Redshift to read from the topic and load data
into the materialized view.

```
REFRESH MATERIALIZED VIEW MyView;
```

5. Query data in the materialized view.

```
select * from MyView;
```

The materialized view is updated directly from the topic when
`REFRESH` is run. You create a materialized view that
maps to the Kafka topic data source. You can perform filtering and
aggregations on the data as part of the materialized view definition.
Your streaming ingestion materialized view (base materialized view) can
reference only one Kafka topic, but you can create additional
materialized views that join with the base materialized view and with
other materialized views or tables.

For more information about limitations for streaming ingestion, see [Streaming ingestion behavior and data types](materialized-view-streaming-ingestion.md#materialized-view-streaming-ingestion-limitations "materialized-view-streaming-ingestion.md#materialized-view-streaming-ingestion-limitations").
