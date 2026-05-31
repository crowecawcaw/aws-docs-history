# Zero-ETL integration with Amazon OpenSearch Service

###### Topics

- [Amazon OpenSearch Service as a destination](#openSearch-0etl-destination "#openSearch-0etl-destination")
- [Limitations](#docdb-openSearch-limitations "#docdb-openSearch-limitations")

## Amazon OpenSearch Service as a destination

OpenSearch Service integration with Amazon DocumentDB enables you to stream full load and change data events to OpenSearch domains.
The ingestion infrastructure is hosted as OpenSearch ingestion pipelines and provides a high-scale, low latency mechanism to continuously stream data from Amazon DocumentDB collections.

During full load, the zero-ETL integration first extracts historical full load data to OpenSearch using an ingestion pipeline.
Once full load data is ingested, the OpenSearch ingestion pipelines will start reading data from Amazon DocumentDB change streams and eventually catch up to maintain near real time data consistency between Amazon DocumentDB and OpenSearch.
OpenSearch stores documents in indexes.
Incoming data from a Amazon DocumentDB collections can be sent to either one index or can be partitioned into different indices.
Ingestion pipelines will sync all create, update and delete events in an Amazon DocumentDB collection as corresponding create, update, and delete of OpenSearch documents to keep both data systems in sync.
Ingestion pipelines can be configured to read data from one collection and write to one index or read data from one collection and conditionally route to multiple indexes.

Ingestion pipelines can be configured to stream data from Amazon DocumentDB to Amazon OpenSearch Service using:

- Full load only
- Stream change stream events from Amazon DocumentDB without full load
- Full load followed by change streams from Amazon DocumentDB

To set up your ingestion pipeline, perform the following steps:

### Step 1: Create an Amazon OpenSearch Service domain or OpenSearch serverless collection

An Amazon OpenSearch Service collection with appropriate permissions to read data is required.
Refer to [Getting started with Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/gsg.md "../../../opensearch-service/latest/developerguide/gsg.md") or [Getting started with Amazon OpenSearch Serverless](../../../opensearch-service/latest/developerguide/serverless-getting-started.md "../../../opensearch-service/latest/developerguide/serverless-getting-started.md") in the _Amazon OpenSearch Service_ Developer Guide to create a collection.
Refer to [Amazon OpenSearch Ingestion](../../../opensearch-service/latest/developerguide/ingestion.md "../../../opensearch-service/latest/developerguide/ingestion.md") in the _Amazon OpenSearch Service_ Developer Guide to create an AIM role with the correct permissions to access write data to the collection or domain.

### Step 2: Enable change streams on the Amazon DocumentDB cluster

Ensure that change streams are enabled on the required collections in the Amazon DocumentDB cluster.
Refer to [Using change streams with Amazon DocumentDB](change_streams.md "change_streams.md") for more information.

### Step 3: Set up the pipeline role with permissions to write to the Amazon S3 bucket and destination domain or collection

After you have your Amazon DocumentDB collection created and change stream enabled, set up the pipeline role that you want to use in your pipeline configuration, and add the following permissions in the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "allowReadAndWriteToS3ForExport",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": [
 "arn:aws:s3:::my-bucket/export/*"
 ]
 }
 ]
}`

```

In order for an OpenSearch pipeline to write data to an OpenSearch domain, the domain must have a domain-level access policy that allows the **sts_role_arn** pipeline role to access it.
The following sample domain access policy allows the pipeline role named `pipeline-role`, which you created in the previous step, to write data to the domain named `ingestion-domain`:

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{your-account-id}:role/{pipeline-role}"
      },
      "Action": ["es:DescribeDomain", "es:ESHttp*"],
      "Resource": "arn:aws:es:{region}:{your-account-id}:domain/{domain-name}/*"
    }
  ]
}
```

### Step 4: Add the permissions required on the pipeline role to create X-ENI

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AttachNetworkInterface",
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DetachNetworkInterface",
 "ec2:DescribeNetworkInterfaces"
 ],
 "Resource": [
 "arn:aws:ec2:*:420497401461:network-interface/*",
 "arn:aws:ec2:*:420497401461:subnet/*",
 "arn:aws:ec2:*:420497401461:security-group/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [ "ec2:CreateTags" ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": { "aws:RequestTag/OSISManaged": "true" }
 }
 }
 ]
}`

```

### Step 5: Create the pipeline

Configure an OpenSearch ingestion pipeline specifying Amazon DocumentDB as the source.
This sample pipeline configuration assumes the use of a change stream fetching mechanism.
Refer to [Using an OpenSearch Ingestion pipeline with Amazon DocumentDB](../../../opensearch-service/latest/developerguide/configure-client-docdb.md "../../../opensearch-service/latest/developerguide/configure-client-docdb.md") in the _Amazon OpenSearch Service Developer Guide_ for more information.

## Limitations

The following limitations apply to the Amazon DocumentDB OpenSearch integration:

- Only one Amazon DocumentDB collection as the source per pipeline is supported.
- Cross-region data ingestion is not supported. Your Amazon DocumentDB cluster and OpenSearch domain must be in the same AWS region.
- Cross-account data ingestion is not supported. Your Amazon DocumentDB cluster and OpenSearch ingestion pipeline must be in the same AWS account.
- Amazon DocumentDB elastic clusters are not supported. Only Amazon DocumentDB instance-based clusters are supported.
- Ensure that the Amazon DocumentDB cluster has authentication enabled using AWS secrets. AWS secrets are the only supported authentication mechanism.
- The existing pipeline configuration can not be updated to ingest data from a different database and/or a different collection.
  To update the database and/or collection name of a pipeline, you must create a new pipeline.
