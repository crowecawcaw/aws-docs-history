# Configure destination settings

This section describes the settings that you must configure for your Firehose stream based on
the destination you select.

###### Topics

- [Configure destination settings for Amazon S3](#create-destination-s3 "#create-destination-s3")
- [Configure destination settings for Apache Iceberg Tables](#create-destination-iceberg "#create-destination-iceberg")
- [Configure destination settings for
  Amazon Redshift](#create-destination-redshift "#create-destination-redshift")
- [Configure destination settings for
  OpenSearch Service](#create-destination-elasticsearch "#create-destination-elasticsearch")
- [Configure destination
  settings for OpenSearch Serverless](#create-destination-opensearch-serverless "#create-destination-opensearch-serverless")
- [Configure destination settings for HTTP
  Endpoint](#create-destination-http "#create-destination-http")
- [Configure destination settings for
  Datadog](#create-destination-datadog "#create-destination-datadog")
- [Configure destination settings for
  Honeycomb](#create-destination-honeycomb "#create-destination-honeycomb")
- [Configure destination settings for
  Coralogix](#create-destination-coralogix "#create-destination-coralogix")
- [Configure destination settings for
  Dynatrace](#create-destination-dynatrace "#create-destination-dynatrace")
- [Configure destination settings for
  LogicMonitor](#create-destination-logicmonitor "#create-destination-logicmonitor")
- [Configure destination settings for
  Logz.io](#create-destination-logz "#create-destination-logz")
- [Configure destination settings for MongoDB
  Atlas](#create-destination-mongodb "#create-destination-mongodb")
- [Configure destination settings for New
  Relic](#create-destination-new-relic "#create-destination-new-relic")
- [Configure destination settings for
  Snowflake](#create-destination-snowflake "#create-destination-snowflake")
- [Configure destination settings for
  Splunk](#create-destination-splunk "#create-destination-splunk")
- [Configure destination settings for
  Splunk Observability Cloud](#create-destination-splunk-cloud "#create-destination-splunk-cloud")
- [Configure destination settings for Sumo
  Logic](#create-destination-sumo-logic "#create-destination-sumo-logic")
- [Configure destination settings for
  Elastic](#create-destination-elastic "#create-destination-elastic")

## Configure destination settings for Amazon S3

You must specify the following settings in order to use Amazon S3 as the destination for
your Firehose stream.

######

- Enter values for the following fields.

**S3 bucket**

Choose an S3 bucket that you own where the streaming data should
be delivered. You can create a new S3 bucket or choose an existing
one.

**New line delimiter**

You can configure your Firehose stream to add a new line delimiter
between records in objects that are delivered to Amazon S3. To do so,
choose **Enabled**. To not add a new line delimiter
between records in objects that are delivered to Amazon S3, choose
**Disabled**. If you plan to use Athena to
query S3 objects with aggregated records, enable this option.

**Dynamic partitioning**

Choose **Enabled** to enable and configure
dynamic partitioning.

**Multi record deaggregation**

This is the process of parsing through the records in the
Firehose stream and separating them based either on valid JSON or on the
specified new line delimiter.

If you aggregate multiple events, logs, or records into a single
PutRecord and PutRecordBatch API call, you can still enable and
configure dynamic partitioning. With aggregated data, when you
enable dynamic partitioning, Amazon Data Firehose parses the records and looks
for multiple valid JSON objects within each API call. When the
Firehose stream is configured with Kinesis Data Stream as a source, you
can also use the built-in aggregation in the Kinesis Producer
Library (KPL). Data partition functionality is executed after data
is de-aggregated. Therefore, each record in each API call can be
delivered to different Amazon S3 prefixes. You can also leverage the
Lambda function integration to perform any other deaggregation or
any other transformation before the data partitioning
functionality.

###### Important

If your data is aggregated, dynamic partitioning can be
applied only after data deaggregation is performed. So if you
enable dynamic partitioning to your aggregated data, you must
choose **Enabled** to enable multi record
deaggregation.

Firehose stream performs the following processing steps in the
following order: KPL (protobuf) deaggregation, JSON or delimiter
deaggregation, Lambda processing, data partitioning, data format
conversion, and Amazon S3 delivery.

**Multi record deaggregation type**

If you enabled multi record deaggregation, you must specify the
method for Firehose to deaggregate your data. Use the drop-down menu to
choose either **JSON** or
**Delimited**.

**Inline parsing**

This is one of the supported mechanisms to dynamically partition
your data that is bound for Amazon S3. To use inline parsing for dynamic
partitioning of your data, you must specify data record parameters
to be used as partitioning keys and provide a value for each
specified partitioning key. Choose **Enabled** to
enable and configure inline parsing.

###### Important

If you specified an AWS Lambda function in the steps above
for transforming your source records, you can use this function
to dynamically partition your data that is bound to S3 and you
can still create your partitioning keys with inline parsing.
With dynamic partitioning, you can use either inline parsing or
your AWS Lambda function to create your partitioning keys. Or
you can use both inline parsing and your AWS Lambda function
at the same time to create your partitioning keys.

**Dynamic partitioning keys**

You can use the **Key** and
**Value** fields to specify the data record
parameters to be used as dynamic partitioning keys and jq queries to
generate dynamic partitioning key values. Firehose
supports jq 1.6 only. You can specify up to 50 dynamic partitioning
keys. You must enter valid jq expressions for your dynamic
partitioning key values in order to successfully configure dynamic
partitioning for your Firehose stream.

**S3 bucket prefix**

When you enable and configure dynamic partitioning, you must
specify the S3 bucket prefixes to which Amazon Data Firehose is to
deliver partitioned data.

In order for dynamic partitioning to be configured correctly, the
number of the S3 bucket prefixes must be identical to the number of
the specified partitioning keys.

You can partition your source data with inline parsing or with
your specified AWS Lambda function. If you specified an AWS
Lambda function to create partitioning keys for your source data,
you must manually type in the S3 bucket prefix value(s) using the
following format: "partitionKeyFromLambda:keyID". If you are using
inline parsing to specify the partitioning keys for your source
data, you can either manually type in the S3 bucket preview values
using the following format: "partitionKeyFromQuery:keyID" or you can
choose the **Apply dynamic partitioning keys**
button to use your dynamic partitioning key/value pairs to
auto-generate your S3 bucket prefixes. While partitioning your data
with either inline parsing or AWS Lambda, you can also use the
following expression forms in your S3 bucket prefix:
!{namespace:value}, where namespace can be either
partitionKeyFromQuery or partitionKeyFromLambda.

**S3 bucket and S3 error output prefix time zone**

Choose a time zone that you want to use for date and time in
[custom prefixes for Amazon S3 objects](s3-prefixes.md "s3-prefixes.md"). By default, Firehose adds a time prefix in UTC.
You can change the time zone used in S3 prefixes if you want to use different time zone.

**Buffering hints**

Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

**S3 compression**

Choose GZIP, Snappy, Zip, or Hadoop-Compatible Snappy data
compression, or no data compression. Snappy, Zip, and
Hadoop-Compatible Snappy compression is not available for
Firehose streams with Amazon Redshift as the destination.

**S3 file extension format (optional)**
Specify a file extension format for objects delivered to Amazon S3 destination bucket. If you enable this feature, specified file extension will override default file extensions appended by Data Format Conversion or S3 compression features such as .parquet or .gz. Make sure if you configured the right file extension when you use this feature with Data Format Conversion or S3 compression. File extension must start with a period (.) and can contain allowed characters: 0-9a-z!-\_.\*‘().
File extension cannot exceed 128 characters.

**S3 encryption**
Firehose supports Amazon S3 server-side encryption with AWS Key Management Service (SSE-KMS) for encrypting delivered data in Amazon S3.
You can choose to use the default encryption type specified in the destination S3 bucket or to encrypt with a key from the list of AWS KMS keys that you own.
If you encrypt the data with AWS KMS keys, you can use either the default AWS managed key (aws/s3) or a customer managed key. For more information, see [Protecting Data Using Server-Side Encryption with AWS KMS-Managed Keys
(SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").

## Configure destination settings for Apache Iceberg Tables

Firehose supports Apache Iceberg Tables as a destination in all [AWS Regions](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region") except China Regions, AWS GovCloud (US) Regions, Asia Pacific (Taipei),
Asia Pacific (Malaysia), Asia Pacific (New Zealand), and Mexico (Central).

For more information on Apache Iceberg Tables as your destination, see [Deliver data to Apache Iceberg Tables with
Amazon Data Firehose](apache-iceberg-destination.md "apache-iceberg-destination.md").

## Configure destination settings for

Amazon Redshift

This section describes settings for using Amazon Redshift as your Firehose stream
destination.

Choose either of the following procedures based on whether you have an Amazon Redshift
provisioned cluster or an Amazon Redshift Serverless workgroup.

- [Amazon Redshift Provisioned
  Cluster](#create-destination-redshift-provisioned "#create-destination-redshift-provisioned")
- [Configure destination
  settings for Amazon Redshift Serverless workgroup](#create-destination-redshift-serverless "#create-destination-redshift-serverless")

###### Note

Firehose can't write to Amazon Redshift clusters that use enhanced VPC routing.

### Amazon Redshift Provisioned

Cluster

This section describes settings for using Amazon Redshift provisioned cluster as your
Firehose stream destination.

######

- Enter values for the following fields:

**Cluster**

The Amazon Redshift cluster to which S3 bucket data is copied. Configure
the Amazon Redshift cluster to be publicly accessible and unblock Amazon Data Firehose IP
addresses. For more information, see [Grant Firehose access to an Amazon Redshift destination](controlling-access.md#using-iam-rs "controlling-access.md#using-iam-rs") .

**Authentication**

You can either choose to enter the username/password directly
or retrieve the secret from AWS Secrets Manager to access the Amazon Redshift
cluster.

    + **User name**


    Specify an Amazon Redshift user with permissions to access the
     Amazon Redshift cluster. This user must have the Amazon Redshift
     `INSERT` permission for copying data from
     the S3 bucket to the Amazon Redshift cluster.
    + **Password**



    Specify the password for the user that has permissions
     to access the cluster.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the
     credentials for the Amazon Redshift cluster. If you do not see your
     secret in the drop-down list, create one in AWS Secrets Manager
     for your Amazon Redshift credentials. For more information, see
     [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Database**

The Amazon Redshift database to where the data is copied.

**Table**

The Amazon Redshift table to where the data is copied.

**Columns**

(Optional) The specific columns of the table to which the data
is copied. Use this option if the number of columns defined in
your Amazon S3 objects is less than the number of columns within the
Amazon Redshift table.

**Intermediate S3 destination**

Firehose delivers your data to your S3 bucket first and then
issues an Amazon Redshift **COPY** command to load the data
into your Amazon Redshift cluster. Specify an S3 bucket that you own where
the streaming data should be delivered. Create a new S3 bucket,
or choose an existing bucket that you own.

Firehose doesn't delete the data from your S3 bucket after
loading it to your Amazon Redshift cluster. You can manage the data in your
S3 bucket using a lifecycle configuration. For more information,
see [Object
Lifecycle Management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the
_Amazon Simple Storage Service User Guide_.

**Intermediate S3 prefix**

(Optional) To use the default prefix for Amazon S3 objects, leave
this option blank. Firehose automatically uses a prefix in
"`YYYY/MM/dd/HH`" UTC time format for delivered
Amazon S3 objects. You can add to the start of this prefix. For more
information, see [Configure Amazon S3 object name format](s3-object-name.md "s3-object-name.md").

**COPY options**

Parameters that you can specify in the Amazon Redshift
**COPY** command. These might be required for
your configuration. For example, "`GZIP`" is required
if Amazon S3 data compression is enabled. "`REGION`" is
required if your S3 bucket isn't in the same AWS Region as
your Amazon Redshift cluster. For more information, see [COPY](../../../redshift/latest/dg/r_COPY.md "../../../redshift/latest/dg/r_COPY.md") in the
_Amazon Redshift Database Developer Guide_.

**COPY command**

The Amazon Redshift **COPY** command. For more
information, see [COPY](../../../redshift/latest/dg/r_COPY.md "../../../redshift/latest/dg/r_COPY.md") in the
_Amazon Redshift Database Developer Guide_.

**Retry duration**

Time duration (0–7200 seconds) for Firehose to retry if
data **COPY** to your Amazon Redshift cluster fails. Firehose
retries every 5 minutes until the retry duration ends. If you
set the retry duration to 0 (zero) seconds, Firehose does not retry
upon a **COPY** command failure.

**Buffering hints**

Firehose buffers incoming data before delivering it to the
specified destination. The recommended buffer size for the
destination varies from service provider to service
provider.

**S3 compression**

Choose GZIP, Snappy, Zip, or Hadoop-Compatible Snappy data
compression, or no data compression. Snappy, Zip, and
Hadoop-Compatible Snappy compression is not available for
Firehose streams with Amazon Redshift as the destination.

**S3 file extension format (optional)**
S3 file extension format (optional) – Specify a file extension format for objects
delivered to Amazon S3 destination bucket. If you enable this
feature, specified file extension will override default file
extensions appended by Data Format Conversion or S3 compression
features such as .parquet or .gz. Make sure if you configured
the right file extension when you use this feature with Data
Format Conversion or S3 compression. File extension must start
with a period (.) and can contain allowed characters:
0-9a-z!-\_.\*‘(). File extension cannot exceed 128
characters.

**S3 encryption**
Firehose supports Amazon S3 server-side encryption with AWS Key Management Service (SSE-KMS) for encrypting delivered data in Amazon S3.
You can choose to use the default encryption type specified in the destination S3 bucket or to encrypt with a key from the list of AWS KMS keys that you own.
If you encrypt the data with AWS KMS keys, you can use either the default AWS managed key (aws/s3) or a customer managed key. For more information, see [Protecting Data Using Server-Side Encryption with AWS KMS-Managed Keys
(SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").

### Configure destination

settings for Amazon Redshift Serverless workgroup

This section describes settings for using Amazon Redshift Serverless workgroup as your
Firehose stream destination.

######

- Enter values for the following fields:

**Workgroup name**

The Amazon Redshift Serverless workgroup to which S3 bucket data is copied.

Configure the Amazon Redshift Serverless workgroup to be publicly accessible and
unblock the Firehose IP addresses. For more information, see the
Connect to a publicly accessible Amazon Redshift Serverless instance section in
[Connecting to Amazon Redshift Serverless](../../../redshift/latest/mgmt/serverless-connecting.md "../../../redshift/latest/mgmt/serverless-connecting.md") and also
[Grant Firehose access to an Amazon Redshift destination](controlling-access.md#using-iam-rs "controlling-access.md#using-iam-rs") .

**Authentication**

You can either choose to enter the username/password directly
or retrieve the secret from AWS Secrets Manager to access the Amazon Redshift Serverless
workgroup.

    + **User name**


    Specify an Amazon Redshift user with permissions to access
     the Amazon Redshift Serverless workgroup. This user must have the Amazon Redshift
     `INSERT` permission for copying data from
     the S3 bucket to the Amazon Redshift Serverless workgroup.
    + **Password**



    Specify the password for the user that has permissions
     to access the Amazon Redshift Serverless workgroup.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the
     credentials for the Amazon Redshift Serverless workgroup. If you do not
     see your secret in the drop-down list, create one in
     AWS Secrets Manager for your Amazon Redshift credentials. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Database**

The Amazon Redshift database to where the data is copied.

**Table**

The Amazon Redshift table to where the data is copied.

**Columns**

(Optional) The specific columns of the table to which the data
is copied. Use this option if the number of columns defined in
your Amazon S3 objects is less than the number of columns within the
Amazon Redshift table.

**Intermediate S3 destination**

Amazon Data Firehose delivers your data to your S3 bucket first and then
issues an Amazon Redshift **COPY** command to load the data
into your Amazon Redshift Serverless workgroup. Specify an S3 bucket that you own
where the streaming data should be delivered. Create a new S3
bucket, or choose an existing bucket that you own.

Firehose doesn't delete the data from your S3 bucket after
loading it to your Amazon Redshift Serverless workgroup. You can manage the data
in your S3 bucket using a lifecycle configuration. For more
information, see [Object
Lifecycle Management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the
_Amazon Simple Storage Service User Guide_.

**Intermediate S3 prefix**

(Optional) To use the default prefix for Amazon S3 objects, leave
this option blank. Firehose automatically uses a prefix in
"`YYYY/MM/dd/HH`" UTC time format for delivered
Amazon S3 objects. You can add to the start of this prefix. For more
information, see [Configure Amazon S3 object name format](s3-object-name.md "s3-object-name.md").

**COPY options**

Parameters that you can specify in the Amazon Redshift
**COPY** command. These might be required for
your configuration. For example, "`GZIP`" is required
if Amazon S3 data compression is enabled. "`REGION`" is
required if your S3 bucket isn't in the same AWS Region as
your Amazon Redshift Serverless workgroup. For more information, see [COPY](../../../redshift/latest/dg/r_COPY.md "../../../redshift/latest/dg/r_COPY.md") in the
_Amazon Redshift Database Developer Guide_.

**COPY command**

The Amazon Redshift **COPY** command. For more
information, see [COPY](../../../redshift/latest/dg/r_COPY.md "../../../redshift/latest/dg/r_COPY.md") in the
_Amazon Redshift Database Developer Guide_.

**Retry duration**

Time duration (0–7200 seconds) for Firehose to retry if
data **COPY** to your Amazon Redshift Serverless workgroup fails.
Firehose retries every 5 minutes until the retry duration ends. If
you set the retry duration to 0 (zero) seconds, Firehose does not
retry upon a **COPY** command failure.

**Buffering hints**

Firehose buffers incoming data before delivering it to the
specified destination. The recommended buffer size for the
destination varies from service provider to service
provider.

**S3 compression**

Choose GZIP, Snappy, Zip, or Hadoop-Compatible Snappy data
compression, or no data compression. Snappy, Zip, and
Hadoop-Compatible Snappy compression is not available for
Firehose streams with Amazon Redshift as the destination.

**S3 file extension format (optional)**
S3 file extension format (optional) – Specify a file extension format for objects
delivered to Amazon S3 destination bucket. If you enable this
feature, specified file extension will override default file
extensions appended by Data Format Conversion or S3 compression
features such as .parquet or .gz. Make sure if you configured
the right file extension when you use this feature with Data
Format Conversion or S3 compression. File extension must start
with a period (.) and can contain allowed characters:
0-9a-z!-\_.\*‘(). File extension cannot exceed 128
characters.

**S3 encryption**
Firehose supports Amazon S3 server-side encryption with AWS Key Management Service (SSE-KMS) for encrypting delivered data in Amazon S3.
You can choose to use the default encryption type specified in the destination S3 bucket or to encrypt with a key from the list of AWS KMS keys that you own.
If you encrypt the data with AWS KMS keys, you can use either the default AWS managed key (aws/s3) or a customer managed key. For more information, see [Protecting Data Using Server-Side Encryption with AWS KMS-Managed Keys
(SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").

## Configure destination settings for

OpenSearch Service

Firehose supports Elasticsearch versions – 1.5, 2.3, 5.1, 5.3, 5.5, 5.6, as well
as all 6.\*, 7.\*, and 8.\* versions. Firehose supports Amazon OpenSearch Service 2.x and 3.x.

This section describes options for using OpenSearch Service for your destination.

######

- Enter values for the following fields:

\***\*OpenSearch Service domain\*\***

The OpenSearch Service domain to which your data is delivered.

\***\*Index\*\***

The OpenSearch Service index name to be used when indexing data to your OpenSearch Service
cluster.

\***\*Index rotation\*\***

Choose whether and how often the OpenSearch Service index should be rotated. If
index rotation is enabled, Amazon Data Firehose appends the corresponding
timestamp to the specified index name and rotates. For more
information, see [Configure index rotation for OpenSearch Service](es-index-rotation.md "es-index-rotation.md").

\***\*Type\*\***

The OpenSearch Service type name to be used when indexing data to your OpenSearch Service
cluster. For Elasticsearch 7.x and OpenSearch 1.x, there can be only
one type per index. If you try to specify a new type for an existing
index that already has another type, Firehose returns an error during
runtime.

For Elasticsearch 7.x, leave this field empty.

\***\*Retry duration\*\***

Time duration for Firehose to retry if an index request to
OpenSearch fails. For retry duration, you can set any value
between 0-7200 seconds. The default retry duration is 300 seconds.
Firehose will retry multiple times with exponential back off until the
retry duration expires.

After the retry duration expires, Firehose delivers the data to Dead
Letter Queue (DLQ), a configured S3 error bucket. For data delivered
to DLQ, you have to re-drive the data back from configured S3 error
bucket to OpenSearch destination.

If you want to block Firehose stream from delivering data to DLQ due to
downtime or maintenance of OpenSearch clusters, you can configure the
retry duration to a higher value in seconds. You can increase the
retry duration value above to 7200 seconds by contacting the [AWS support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

\***\*DocumentID type\*\***

Indicates the method for setting up document ID. The supported
methods are Firehose-generated document ID and OpenSearch Service-generated document
ID. Firehose-generated document ID is the default option when the
document ID value is not set. OpenSearch Service-generated document ID is the
recommended option because it supports write-heavy operations,
including log analytics and observability, consuming fewer CPU
resources at the OpenSearch Service domain and thus, resulting in improved
performance.

\***\*Destination VPC connectivity\*\***

If your OpenSearch Service domain is in a private VPC, use this section to
specify that VPC. Also specify the subnets and subgroups that you
want Amazon Data Firehose to use when it sends data to your OpenSearch Service domain. You
can use the same security groups that the OpenSearch Service domain is using. If
you specify different security groups, ensure that they allow
outbound HTTPS traffic to the OpenSearch Service domain's security
group. Also ensure that the OpenSearch Service domain's security group allows
HTTPS traffic from the security groups that you specified when you
configured your Firehose stream. If you use the same security group for
both your Firehose stream and the OpenSearch Service domain, make sure the security
group's inbound rule allows HTTPS traffic. For more information
about security group rules, see [Security group rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules") in the Amazon VPC documentation.

###### Important

When you specify subnets for delivering data to the destination in a private VPC, make sure you have enough number of free IP addresses in chosen subnets. If there is no available free IP address in a specified subnet, Firehose cannot create or add ENIs for the data delivery in the private VPC, and the delivery will be degraded or fail.

**Buffer hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

## Configure destination

settings for OpenSearch Serverless

This section describes options for using OpenSearch Serverless for your
destination.

######

- Enter values for the following fields:

\***\*OpenSearch Serverless collection\*\***

The endpoint for a group of OpenSearch Serverless indexes to which
your data is delivered.

\***\*Index\*\***

The OpenSearch Serverless index name to be used when indexing data
to your OpenSearch Serverless collection.

\***\*Destination VPC connectivity\*\***

If your OpenSearch Serverless collection is in a private VPC, use
this section to specify that VPC. Also specify the subnets and
subgroups that you want Amazon Data Firehose to use when it sends
data to your OpenSearch Serverless collection.

###### Important

When you specify subnets for delivering data to the destination in a private VPC, make sure you have enough number of free IP addresses in chosen subnets. If there is no available free IP address in a specified subnet,
Firehose cannot create or add ENIs for the data delivery in the private VPC, and the delivery will be degraded or fail.

\***\*Retry duration\*\***

Time duration for Firehose to retry if an index request to
OpenSearch Serverless fails. For retry duration, you can set any
value between 0-7200 seconds. The default retry duration is 300
seconds. Firehose will retry multiple times with exponential back off
until the retry duration expires.

After the retry duration expires, Firehose delivers the data to Dead
Letter Queue (DLQ), a configured S3 error bucket. For data delivered
to DLQ, you have to re-drive the data back from configured S3 error
bucket to OpenSearch Serverless destination.

If you want to block Firehose stream from delivering data to DLQ due to
downtime or maintenance of OpenSearch Serverless clusters, you can
configure the retry duration to a higher value in seconds. You can
increase the retry duration value above to 7200 seconds by
contacting the [AWS
support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

**Buffer hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

## Configure destination settings for HTTP

Endpoint

This section describes options for using **HTTP endpoint** for your
destination.

###### Important

If you choose an HTTP endpoint as your destination, review and follow the
instructions in [Understand HTTP endpoint delivery request and
response specifications](httpdeliveryrequestresponse.md "httpdeliveryrequestresponse.md").

######

- Provide values for the following fields:

**HTTP endpoint name - optional**

Specify a user friendly name for the HTTP endpoint. For example,
`My HTTP Endpoint Destination`.

**HTTP endpoint URL**

Specify the URL for the HTTP endpoint in the following format:
`https://xyz.httpendpoint.com`. The URL must be an
HTTPS URL.

**Authentication**

You can either choose to enter the access key directly or retrieve
the secret from AWS Secrets Manager to access the HTTP endpoint.

    + **(Optional) Access key**



    Contact the endpoint owner if you need to obtain the
     access key to enable data delivery to their endpoint from
     Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the access
     key for the HTTP endpoint. If you do not see your secret in
     the drop-down list, create one in AWS Secrets Manager for the access
     key. For more information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** or **Disabled** to
enable/disable content encoding of your request.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to the selected HTTP
endpoint.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

###### Important

For the HTTP endpoint destinations, if you are seeing 413
response codes from the destination endpoint in CloudWatch Logs,
lower the buffering hint size on your Firehose stream and try
again.

## Configure destination settings for

Datadog

This section describes options for using **Datadog** for your
destination. For more information about Datadog, see [https://docs.datadoghq.com/integrations/amazon_web_services/](https://docs.datadoghq.com/integrations/amazon_web_services/ "https://docs.datadoghq.com/integrations/amazon_web_services/").

######

- Provide values for the following fields.

**HTTP endpoint URL**

Choose where you want to send data from one of the following
options in the drop-down menu.

    + **Datadog logs - US1**
    + **Datadog logs - US3**
    + **Datadog logs - US5**
    + **Datadog logs - AP1**
    + **Datadog logs - EU**
    + **Datadog logs - GOV**
    + **Datadog metrics - US**
    + **Datadog metrics - US5**
    + **Datadog metrics - AP1**
    + **Datadog metrics - EU**
    + **Datadog configurations - US1**
    + **Datadog configurations - US3**
    + **Datadog configurations - US5**
    + **Datadog configurations - AP1**
    + **Datadog configurations - EU**
    + **Datadog configurations - US
     GOV**

**Authentication**

You can either choose to enter the API key directly or retrieve
the secret from AWS Secrets Manager to access Datadog.

    + **API key**



    Contact Datadog to obtain the API key that you need to
     enable data delivery to this endpoint from Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the API key
     for Datadog. If you do not see your secret in the drop-down
     list, create one in AWS Secrets Manager. For more information, see
     [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** or **Disabled** to
enable/disable content encoding of your request.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to the selected HTTP
endpoint.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

## Configure destination settings for

Honeycomb

This section describes options for using **Honeycomb** for your
destination. For more information about Honeycomb, see [https://docs.honeycomb.io/getting-data-in/metrics/aws-cloudwatch-metrics/](https://docs.honeycomb.io/getting-data-in/metrics/aws-cloudwatch-metrics/ "https://docs.honeycomb.io/getting-data-in/metrics/aws-cloudwatch-metrics/ ") .

######

- Provide values for the following fields:

**Honeycomb Kinesis endpoint**

Specify the URL for the HTTP endpoint in the following format:
https://api.honeycomb.io/1/kinesis\_events/{{dataset}}

**Authentication**

You can either choose to enter the API key directly or retrieve
the secret from AWS Secrets Manager to access Honeycomb.

    + **API key**



    Contact Honeycomb to obtain the API key that you need to
     enable data delivery to this endpoint from Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the API key
     for Honeycomb. If you do not see your secret in the
     drop-down list, create one in AWS Secrets Manager. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** to enable content encoding of your
request. This is the recommended option for the Honeycomb
destination.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to the selected HTTP
endpoint.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

## Configure destination settings for

Coralogix

This section describes options for using **Coralogix** for your
destination. For more information about Coralogix, see [Get Started with Coralogix](https://coralogix.com/docs/guide-first-steps-coralogix/ "https://coralogix.com/docs/guide-first-steps-coralogix/").

######

- Provide values for the following fields:

**HTTP endpoint URL**

Choose the HTTP endpoint URL from the following options in the
drop down menu:

    + **Coralogix - US**
    + **Coralogix - SINGAPORE**
    + **Coralogix - IRELAND**
    + **Coralogix - INDIA**
    + **Coralogix - STOCKHOLM**

**Authentication**

You can either choose to enter the private key directly or
retrieve the secret from AWS Secrets Manager to access Coralogix.

    + **Private key**



    Contact Coralogix to obtain the private key that you need
     to enable data delivery to this endpoint from Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the private
     key for Coralogix. If you do not see your secret in the
     drop-down list, create one in AWS Secrets Manager. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** to enable content encoding of your
request. This is the recommended option for the Coralogix
destination.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to the selected HTTP
endpoint.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

    + applicationName: the environment where you are running
     Data Firehose
    + subsystemName: the name of the Data Firehose
     integration
    + computerName: the name of the Firehose stream in
     use

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it to the
specified destination. The recommended buffer size for the
destination varies based on the service provider.

## Configure destination settings for

Dynatrace

This section describes options for using **Dynatrace** for your
destination. For more information, see [https://www.dynatrace.com/support/help/technology-support/cloud-platforms/amazon-web-services/integrations/cloudwatch-metric-streams/](https://www.dynatrace.com/support/help/technology-support/cloud-platforms/amazon-web-services/integrations/cloudwatch-metric-streams/ "https://www.dynatrace.com/support/help/technology-support/cloud-platforms/amazon-web-services/integrations/cloudwatch-metric-streams/").

######

- Choose options to use Dynatrace as the destination for your Firehose stream.

**Ingestion type**

Choose whether you want to deliver **Metrics** or
**Logs** (default) in Dynatrace for further
analysis and processing.

**HTTP endpoint URL**

Choose the HTTP endpoint URL (**Dynatrace US**,
**Dynatrace EU**, or **Dynatrace
Global**) from the drop-down menu.

**Authentication**

You can either choose to enter the API token directly or retrieve
the secret from AWS Secrets Manager to access Dynatrace.

    + **API token**



    Generate the Dynatrace API token that you need to enable
     data delivery to this endpoint from Firehose. For more
     information, see [Dynatrace API - Tokens and
     authentication](https://docs.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication "https://docs.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication").
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the API token
     for Dynatrace. If you do not see your secret in the
     drop-down list, create one in AWS Secrets Manager. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**API URL**

Provide the API URL of your Dynatrace environment.

**Content encoding**

Choose whether you want to enable content encoding to compress
body of the request. Amazon Data Firehose uses content encoding to compress the
body of a request before sending it to the destination. When
enabled, the content it compressed in the **GZIP**
format.

**Retry duration**

Specify how long Firehose retries sending data to the selected HTTP
endpoint.

After sending data, Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Firehose sends data to the HTTP endpoint, either
during the initial attempt or after retrying, it restarts the
acknowledgement timeout counter and waits for an acknowledgement
from the HTTP endpoint.

Even if the retry duration expires, Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it to the
specified destination. The buffer hints include the buffer size and
interval for your streams. The recommended buffer size for the
destination varies according to the service provider.

## Configure destination settings for

LogicMonitor

This section describes options for using **LogicMonitor** for your
destination. For more information, see [https://www.logicmonitor.com](https://www.logicmonitor.com "https://www.logicmonitor.com").

######

- Provide values for the following fields:

**HTTP endpoint URL**

Specify the URL for the HTTP endpoint in the following
format.

```
https://ACCOUNT.logicmonitor.com
```

**Authentication**

You can either choose to enter the API key directly or retrieve
the secret from AWS Secrets Manager to access LogicMonitor.

    + **API key**



    Contact LogicMonitor to obtain the API key that you need
     to enable data delivery to this endpoint from Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the API key
     for LogicMonitor. If you do not see your secret in the
     drop-down list, create one in AWS Secrets Manager. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** or **Disabled** to
enable/disable content encoding of your request.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to the selected HTTP
endpoint.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

## Configure destination settings for

Logz.io

This section describes options for using **Logz.io** for your
destination. For more information, see [https://logz.io/](https://logz.io/ "https://logz.io/").

###### Note

In the Europe (Milan) region, Logz.io is not supported as an Amazon Data Firehose destination.

######

- Provide values for the following fields:

**HTTP endpoint URL**

Specify the URL for the HTTP endpoint in the following format. The
URL must be an `HTTPS` URL.

```
https://listener-aws-metrics-stream-<region>.logz.io/
```

For example

```
https://listener-aws-metrics-stream-us.logz.io/
```

**Authentication**

You can either choose to enter the shipping token directly or
retrieve the secret from AWS Secrets Manager to access Logz.io.

    + **Shipping token**



    Contact Logz.io to obtain the shipping token that you need
     to enable data delivery to this endpoint from Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the shipping
     token for Logz.io. If you do not see your secret in the
     drop-down list, create one in AWS Secrets Manager. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to Logz.io.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

## Configure destination settings for MongoDB

Atlas

This section describes options for using **MongoDB Atlas** for your
destination. For more information, see [MongoDB Atlas on Amazon Web Services](https://www.mongodb.com/products/platform/atlas-cloud-providers/aws "https://www.mongodb.com/products/platform/atlas-cloud-providers/aws").

######

- Provide values for the following fields:

**API Gateway URL**

Specify the URL for the HTTP endpoint in the following
format.

```
 `https://xxxxx.execute-api.region.amazonaws.com/stage`
```

The URL must be an `HTTPS` URL.

**Authentication**

You can either choose to enter the API key directly or retrieve
the secret from AWS Secrets Manager to access MongoDB Atlas.

    + **API key**



    Follow instructions in [MongoDB Atlas on Amazon Web Services](https://www.mongodb.com/products/platform/atlas-cloud-providers/aws "https://www.mongodb.com/products/platform/atlas-cloud-providers/aws") to obtain the `APIKeyValue` that you need to enable data delivery to this endpoint from Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the API Key for API Gateway that is backed by Lambda interacting with MongoDB Atlas. If you do not see your secret in the
     drop-down list, create one in AWS Secrets Manager. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** or **Disabled** to
enable/disable content encoding of your request.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to the selected
third-party provider.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

## Configure destination settings for New

Relic

This section describes options for using **New Relic** for your
destination. For more information, see [https://newrelic.com](https://newrelic.com "https://newrelic.com").

######

- Provide values for the following fields:

**HTTP endpoint URL**

Choose the HTTP endpoint URL from the following options in the
drop-down list.

    + **New Relic logs - US**
    + **New Relic metrics - US**
    + **New Relic metrics - EU**

**Authentication**

You can either choose to enter the API key directly or retrieve
the secret from AWS Secrets Manager to access New Relic.

    + **API key**



    Enter your License Key, which is a 40-characters
     hexadecimal string, from your New Relic One Account
     settings. You need this API key to enable data delivery to
     this endpoint from Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the API key
     for New Relic. If you do not see your secret in the
     drop-down list, create one in AWS Secrets Manager. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** or **Disabled** to
enable/disable content encoding of your request.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to the New Relic HTTP
endpoint.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

## Configure destination settings for

Snowflake

This section describes options for using Snowflake for your destination.

###### Note

Firehose integration with Snowflake is available in the US East (N. Virginia), US
West (Oregon), Europe (Ireland), US East (Ohio), Asia Pacific (Tokyo), Europe
(Frankfurt), Asia Pacific (Singapore), Asia Pacific (Seoul), and Asia Pacific
(Sydney), Asia Pacific (Mumbai), Europe (London), South America (Sao Paulo), Canada
(Central), Europe (Paris), Asia Pacific (Osaka), Europe (Stockholm), Asia Pacific
(Jakarta) AWS Regions.

###### Connection settings

######

- Provide values for the following fields:

**Snowflake account URL**

Specify a Snowflake account URL. For example:
`xy12345.us-east-1.aws.snowflakecomputing.com`. Refer
to [Snowflake documentation](https://docs.snowflake.com/en/user-guide/admin-account-identifier#format-2-legacy-account-locator-in-a-region "https://docs.snowflake.com/en/user-guide/admin-account-identifier#format-2-legacy-account-locator-in-a-region") on how to determine your
account URL. Note that you mustn't specify the port number, whereas
protocol (https://) is optional.

**Authentication**

You can either choose to enter the userlogin, private key, and
passphrase manually or retrieve the secret from AWS Secrets Manager to access
Snowflake.

    + **User login**


    Specify the Snowflake user to be used for loading data.
     Make sure the user has access to insert data into the
     Snowflake table.
    + **Private key**


    Specify the private key for authentication with Snowflake
     in `PKCS8` format. Additionally, do not include
     PEM header and footer as part of the private key. If the key
     is split across multiple lines, remove the line breaks.
     Following is an example of what your private key must look
     like.



    ```
    -----BEGIN PRIVATE KEY-----
    KEY_CONTENT
    -----END PRIVATE KEY-----
    ```

    Remove the space in `KEY_CONTENT` and provide
     that to Firehose. No header/footer or newline characters are
     required.
    + **Passphrase**



    Specify the passphrase to decrypt the encrypted private
     key. You can leave this field empty if the private key is
     not encrypted. For information, see [Using Key Pair Authentication & Key
     Rotation](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation "https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation").
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the
     credentials for Snowflake. If you do not see your secret in
     the drop-down list, create one in AWS Secrets Manager. For more
     information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Role configuration**

Use default Snowflake role – If this option is selected, Firehose will not pass any role to Snowflake. Default role is assumed to load data. Please make sure the default role has permission to insert data in to Snowflake table.

Use custom Snowflake role – Enter a non-default Snowflake role to be assumed by Firehose when loading data into Snowflake table.

**Snowflake connectivity**

Options are **Private** or **Public**.

**Private VPCE ID (optional)**

The VPCE ID for Firehose to privately connect with Snowflake. The ID
format is
com.amazonaws.vpce.[region].vpce-svc-`[id]`.
For more information, see [AWS PrivateLink & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink "https://docs.snowflake.com/en/user-guide/admin-security-privatelink").

###### Note

If your Snowflake cluster is private link enabled, use
`AwsVpceIds`-based network policy to allow
Amazon Data Firehose data. Firehose doesn't require you to configure an IP-based
network policy in your Snowflake account. Having an IP-based
network policy enabled could interfere with Firehose connectivity.
If you have an edge case that requires IP-based policy, contact
the Firehose team by submitting a [support ticket](https://support.console.aws.amazon.com/support/home?region=us-east-1#/case/create "https://support.console.aws.amazon.com/support/home?region=us-east-1#/case/create"). For a list of the VPCE IDs that you
can use, refer to the [Accessing Snowflake in VPC](controlling-access.md#using-iam-snowflake-vpc "controlling-access.md#using-iam-snowflake-vpc").

###### Database configuration

- You must specify the following settings in order to use Snowflake as the destination for your
  Firehose stream.
  - Snowflake database – All data in Snowflake is maintained in databases.
  - Snowflake schema – Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views
  - Snowflake table – All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.

**Data loading options for your Snowflake table**

- Use JSON keys as column names
- Use VARIANT columns
  - Content column name – Specify a column name in the table, where the raw data has to be loaded.
  - Metadata column name (optional) – Specify a column name in the table, where the
    metadata information has to be loaded. When you enable this field, you
    will see the following column in the Snowflake table based on the source
    type.

  **For Direct PUT as source**

  ```
  {
  "firehoseDeliveryStreamName" : "`streamname`",
  "IngestionTime" : "`timestamp`"
  }
  ```

  **For Kinesis Data Stream as
  source**

  ```
  {
  "kinesisStreamName" : "`streamname`",
  "kinesisShardId" : "`Id`",
  "kinesisPartitionKey" : "`key`",
  "kinesisSequenceNumber" : "`1234`",
  "subsequenceNumber" : "`2334`",
  "IngestionTime" : "`timestamp`"
  }
  ```

**Retry duration**

Time duration (0–7200 seconds) for Firehose to retry if either opening channel or
delivery to Snowflake fails due to Snowflake service issues. Firehose retries with
exponential backoff until the retry duration ends. If you set the retry duration to 0
(zero) seconds, Firehose does not retry upon Snowflake failures and routes data to Amazon S3
error bucket.

**Buffer hints**

Amazon Data Firehose buffers incoming data before delivering it to the specified destination. The
recommended buffer size for the destination varies from service provider to service
provider. For more information, see [Configure buffering hints](create-configure-backup.md#buffering-hints "create-configure-backup.md#buffering-hints").

## Configure destination settings for

Splunk

This section describes options for using Splunk for your destination.

###### Note

Firehose delivers data to Splunk clusters configured with Classic Load Balancer or an Application Load Balancer.

######

- Provide values for the following fields:

**Splunk cluster endpoint**

To determine the endpoint, see [Configure Amazon Data Firehose to Send Data to the Splunk
Platform](http://docs.splunk.com/Documentation/AddOns/latest/Firehose/ConfigureFirehose "http://docs.splunk.com/Documentation/AddOns/latest/Firehose/ConfigureFirehose") in the Splunk documentation.

**Splunk endpoint type**

Choose `Raw endpoint` in most cases. Choose `Event
 endpoint` if you preprocessed your data using AWS Lambda to
send data to different indexes by event type. For information about
what endpoint to use, see [Configure Amazon Data Firehose to send data to the Splunk
platform](http://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureFirehose "http://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureFirehose") in the Splunk documentation.

**Authentication**

You can either choose to enter the authentication token directly
or retrieve the secret from AWS Secrets Manager to access Splunk.

    + **Authentication token**



    To set up a Splunk endpoint that can receive data from
     Amazon Data Firehose, see [Installation and configuration overview for the Splunk
     Add-on for Amazon Data Firehose](http://docs.splunk.com/Documentation/AddOns/released/Firehose/Installationoverview "http://docs.splunk.com/Documentation/AddOns/released/Firehose/Installationoverview") in the Splunk
     documentation. Save the token that you get from Splunk when
     you set up the endpoint for this Firehose stream and add it
     here.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the
     authentication token for Splunk. If you do not see your
     secret in the drop-down list, create one in AWS Secrets Manager. For
     more information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**HEC acknowledgement timeout**

Specify how long Amazon Data Firehose waits for the index acknowledgement from
Splunk. If Splunk doesn’t send the acknowledgment before the timeout
is reached, Amazon Data Firehose considers it a data delivery failure. Amazon Data Firehose then
either retries or backs up the data to your Amazon S3 bucket, depending
on the retry duration value that you set.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to Splunk.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
Splunk. If an error occurs or the acknowledgment doesn’t arrive
within the acknowledgment timeout period, Amazon Data Firehose starts the retry
duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to Splunk (either the initial
attempt or a retry), it restarts the acknowledgement timeout counter
and waits for an acknowledgement from Splunk.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it to the
specified destination. The recommended buffer size for the
destination varies based on the service provider.

## Configure destination settings for

Splunk Observability Cloud

This section describes options for using **Splunk Observability Cloud** for your
destination. For more information, see [https://docs.splunk.com/observability/en/gdi/get-data-in/connect/aws/aws-apiconfig.html#connect-to-aws-using-the-splunk-observability-cloud-api](https://docs.splunk.com/Observability/gdi/get-data-in/connect/aws/aws-apiconfig.html#connect-to-aws-using-the-splunk-observability-cloud-api "https://docs.splunk.com/Observability/gdi/get-data-in/connect/aws/aws-apiconfig.html#connect-to-aws-using-the-splunk-observability-cloud-api").

######

- Provide values for the following fields:

**Cloud Ingest Endpoint URL**

You can find your Splunk Observability Cloud’s Real-time Data Ingest URL in Profile > Organizations > Real-time Data Ingest Endpoint in Splunk Observability console.

**Authentication**

You can either choose to enter the access token directly or
retrieve the secret from AWS Secrets Manager to access Splunk Observability
Cloud.

    + **Access Token**



    Copy your Splunk Observability access token with INGEST
     authorization scope from **Access Tokens**
     under **Settings** in Splunk Observability
     console.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the access
     token for Splunk Observability Cloud. If you do not see your
     secret in the drop-down list, create one in AWS Secrets Manager. For
     more information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content Encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** or **Disabled** to
enable/disable content encoding of your request.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to the selected HTTP
endpoint.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
destination varies from service provider to service provider.

## Configure destination settings for Sumo

Logic

This section describes options for using **Sumo Logic** for your
destination. For more information, see [https://www.sumologic.com](https://www.sumologic.com "https://www.sumologic.com").

######

- Provide values for the following fields:

**HTTP endpoint URL**

Specify the URL for the HTTP endpoint in the following format:
`https://deployment
 name.sumologic.net/receiver/v1/kinesis/dataType/access
 token`. The URL must be an HTTPS URL.

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** or **Disabled** to
enable/disable content encoding of your request.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to Sumo Logic.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
Elastic destination varies from service provider to service
provider.

## Configure destination settings for

Elastic

This section describes options for using **Elastic** for your
destination.

######

- Provide values for the following fields:

**Elastic endpoint URL**

Specify the URL for the HTTP endpoint in the following format:
`https://<cluster-id>.es.<region>.aws.elastic-cloud.com`.
The URL must be an HTTPS URL.

**Authentication**

You can either choose to enter the API key directly or retrieve
the secret from AWS Secrets Manager to access Elastic.

    + **API key**



    Contact Elastic to obtain the API key that you require to
     enable data delivery to their service from Firehose.
    + **Secret**


    Select a secret from AWS Secrets Manager that contains the API key
     for Elastic. If you do not see your secret in the drop-down
     list, create one in AWS Secrets Manager. For more information, see
     [Authenticate with AWS Secrets Manager in Amazon Data Firehose](using-secrets-manager.md "using-secrets-manager.md").

**Content encoding**

Amazon Data Firehose uses content encoding to compress the body
of a request before sending it to the destination. Choose
**GZIP** (which is what selected by default) or
**Disabled** to enable/disable content encoding
of your request.

**Retry duration**

Specify how long Amazon Data Firehose retries sending data to Elastic.

After sending data, Amazon Data Firehose first waits for an acknowledgment from
the HTTP endpoint. If an error occurs or the acknowledgment doesn’t
arrive within the acknowledgment timeout period, Amazon Data Firehose starts the
retry duration counter. It keeps retrying until the retry duration
expires. After that, Amazon Data Firehose considers it a data delivery failure and
backs up the data to your Amazon S3 bucket.

Every time that Amazon Data Firehose sends data to the HTTP endpoint (either the
initial attempt or a retry), it restarts the acknowledgement timeout
counter and waits for an acknowledgement from the HTTP endpoint.

Even if the retry duration expires, Amazon Data Firehose still waits for the
acknowledgment until it receives it or the acknowledgement timeout
period is reached. If the acknowledgment times out, Amazon Data Firehose determines
whether there's time left in the retry counter. If there is time
left, it retries again and repeats the logic until it receives an
acknowledgment or determines that the retry time has expired.

If you don't want Amazon Data Firehose to retry sending data, set this value to 0.

**Parameters - optional**

Amazon Data Firehose includes these key-value pairs in each HTTP
call. These parameters can help you identify and organize your
destinations.

**Buffering hints**

Amazon Data Firehose buffers incoming data before delivering it
to the specified destination. The recommended buffer size for the
Elastic destination is 1 MiB.
