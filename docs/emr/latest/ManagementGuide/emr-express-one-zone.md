# Upload data to Amazon S3 Express One Zone

## Overview

With Amazon EMR 6.15.0 and higher, you can use Amazon EMR with Apache Spark in
conjunction with the [Amazon S3 Express One Zone](../../../AmazonS3/latest/userguide/s3-express-one-zone.md "../../../AmazonS3/latest/userguide/s3-express-one-zone.md") storage class for improved performance on your
Spark jobs. Amazon EMR releases 7.2.0 and higher also support HBase, Flink, and Hive, so you can also
benefit from S3 Express One Zone if you use these applications. _S3 Express One Zone_ is an S3 storage class for
applications that frequently access data with hundreds of thousands of
requests per second. At the time of its release, S3 Express One Zone delivers the
lowest latency and highest performance cloud object storage in Amazon S3.

## Prerequisites

- S3 Express One Zone permissions
  – When S3 Express One Zone initially performs an action like
  `GET`, `LIST`, or `PUT` on an
  S3 object, the storage class calls `CreateSession` on
  your behalf. Your IAM policy must allow the
  `s3express:CreateSession` permission so that the
  S3A connector can invoke the
  `CreateSession` API. For an example policy with this
  permission, see [Getting started with
  Amazon S3 Express One Zone](#emr-express-one-zone-start "#emr-express-one-zone-start").
- S3A connector
  – To configure your Spark cluster to access data from an Amazon S3
  bucket that uses the S3 Express One Zone storage class, you must use the
  Apache Hadoop connector S3A. To use the connector,
  ensure all S3 URIs use the `s3a` scheme. If they don’t,
  you can change the filesystem implementation that you use for
  `s3` and `s3n` schemes.

To change the `s3` scheme, specify the following cluster
configurations:

```
[
  {
    "Classification": "core-site",
    "Properties": {
      "fs.s3.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
      "fs.AbstractFileSystem.s3.impl": "org.apache.hadoop.fs.s3a.S3A"
    }
  }
]
```

To change the `s3n` scheme, specify the following cluster
configurations:

```
[
  {
    "Classification": "core-site",
    "Properties": {
      "fs.s3n.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
      "fs.AbstractFileSystem.s3n.impl": "org.apache.hadoop.fs.s3a.S3A"
    }
  }
]
```

## Getting started with

Amazon S3 Express One Zone

###### Topics

- [Create a permission
  policy](#emr-express-one-zone-permissions "#emr-express-one-zone-permissions")
- [Create and configure your
  cluster](#emr-express-one-zone-create "#emr-express-one-zone-create")
- [Configurations
  overview](#emr-express-one-zone-configs "#emr-express-one-zone-configs")

### Create a permission

policy

Before you can create a cluster that uses Amazon S3 Express One Zone, you must
create an IAM policy to attach to the Amazon EC2 instance profile for the
cluster. The policy must have permissions to access the S3 Express One Zone
storage class. The following example policy shows how to grant the
required permission. After you create the policy, attach the policy to
the instance profile role that you use to create your EMR cluster, as
described in the [Create and configure your
cluster](#emr-express-one-zone-create "#emr-express-one-zone-create") section.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3express:*:123456789012:bucket/example-s3-bucket"
 ],
 "Action": [
 "s3express:CreateSession"
 ],
 "Sid": "AllowS3EXPRESSCreatesession"
 }
 ]
}`

```

### Create and configure your

cluster

Next, create a cluster that runs Spark, HBase, Flink, or Hive with S3 Express One Zone. The following
steps describe a high-level overview to create a cluster in the
AWS Management Console:

1. Navigate to the Amazon EMR console and select
   **Clusters** from the sidebar. Then choose
   **Create cluster**.
2. If you use Spark, select Amazon EMR release `emr-6.15.0` or higher. If you use HBase, Flink, or Hive,
   select `emr-7.2.0` or higher.
3. Select the applications that you want to
   include on your cluster, such as Spark, HBase, or Flink.
4. To enable Amazon S3 Express One Zone, enter a configuration similar to
   the following example in the **Software
   settings** section. The configurations and
   recommended values are described in the [Configurations
   overview](#emr-express-one-zone-configs "#emr-express-one-zone-configs") section that
   follows this procedure.

```
[
  {
    "Classification": "core-site",
    "Properties": {
      "fs.s3a.aws.credentials.provider": "software.amazon.awssdk.auth.credentials.InstanceProfileCredentialsProvider",
      "fs.s3a.change.detection.mode": "none",
      "fs.s3a.endpoint.region": "`aa-example-1`",
      "fs.s3a.select.enabled": "false"
    }
  },
  {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.sql.sources.fastS3PartitionDiscovery.enabled": "false"
    }
  }
]
```

5. In the **EC2 instance profile for Amazon EMR**
   section, choose to use an existing role, and use a role with the
   policy attached that you created in the [Create a permission
   policy](#emr-express-one-zone-permissions "#emr-express-one-zone-permissions") section
   above.
6. Configure the rest of your cluster settings as appropriate for
   your application, and then select **Create
   cluster**.

### Configurations

overview

The following tables describe the configurations and suggested values
that you should specify when you set up a cluster that uses S3 Express One Zone
with Amazon EMR, as described in the [Create and configure your
cluster](#emr-express-one-zone-create "#emr-express-one-zone-create") section.

**S3A
configurations**

| Parameter                                            | Default value                                                                                                                                                                                                             | Suggested value                                                              | Explanation                                                                                                                                                                                                           |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fs.s3a.aws.credentials.provider`                    | If not specified, uses `AWSCredentialProviderList` in the following order: `TemporaryAWSCredentialsProvider`, `SimpleAWSCredentialsProvider`, `EnvironmentVariableCredentialsProvider`, `IAMInstanceCredentialsProvider`. | `software.amazon.awssdk.auth.credentials.InstanceProfileCredentialsProvider` | The Amazon EMR instance profile role should have the policy that allows the S3A filesystem to call `s3express:CreateSession`. Other crendential providers also work if they have the S3 Express One Zone permissions. |
| `fs.s3a.endpoint.region`                             | null                                                                                                                                                                                                                      | The AWS Region where you created the bucket.                                 | Region resolution logic doesn't work with S3 Express One Zone storage class.                                                                                                                                          |
| `fs.s3a.select.enabled`                              | `true`                                                                                                                                                                                                                    | `false`                                                                      | Amazon S3 `select` is not supported with S3 Express One Zone storage class.                                                                                                                                           |
| `fs.s3a.change.detection.mode`                       | `server`                                                                                                                                                                                                                  | none                                                                         | Change detection by S3A works by checking MD5-based `etags`. S3 Express One Zone storage class doesn't support MD5 `checksums`.                                                                                       | **Spark configurations**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Parameter                                            | Default value                                                                                                                                                                                                             | Suggested value                                                              | Explanation                                                                                                                                                                                                           |
| ---                                                  | ---                                                                                                                                                                                                                       | ---                                                                          | ---                                                                                                                                                                                                                   |
| `spark.sql.sources.fastS3PartitionDiscovery.enabled` | `true`                                                                                                                                                                                                                    | `false`                                                                      | The internal optimization uses an S3 API parameter that the S3 Express One Zone storage class doesn't support.                                                                                                        | **Hive configurations**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Parameter                                            | Default value                                                                                                                                                                                                             | Suggested value                                                              | Explanation                                                                                                                                                                                                           |
| ---                                                  | ---                                                                                                                                                                                                                       | ---                                                                          | ---                                                                                                                                                                                                                   |
| `hive.exec.fast.s3.partition.discovery.enabled`      | `true`                                                                                                                                                                                                                    | `false`                                                                      | The internal optimization uses an S3 API parameter that the S3 Express One Zone storage class doesn't support.                                                                                                        | ## Considerations Consider the following when you integrate Apache Spark on Amazon EMR with the S3 Express One Zone storage class: <br>• The S3A connector is required to use S3 Express One Zone with Amazon EMR. Only S3A has the features and storage classes that are required to interact with S3 Express One Zone. For steps to set up the connector, see [Prerequisites](#emr-express-one-zone-prereqs "#emr-express-one-zone-prereqs"). <br>• The Amazon S3 Express One Zone storage class supports SSE-S3 and SSE-KMS encryption. For more information, see [Server-side encryption with Amazon S3](../../../AmazonS3/latest/userguide/s3-express-data-protection.md#s3-express-ecnryption "../../../AmazonS3/latest/userguide/s3-express-data-protection.md#s3-express-ecnryption"). <br>• The Amazon S3 Express One Zone storage class does not support writes with the S3A `FileOutputCommitter`. Writes with the S3A `FileOutputCommitter` on S3 Express One Zone buckets result in an error: _InvalidStorageClass: The storage class you specified is not valid_. <br>• Amazon S3 Express One Zone is supported with Amazon EMR releases 6.15.0 and higher on EMR on EC2. Additionally, it's supported on Amazon EMR releases 7.2.0 and higher on Amazon EMR on EKS and on Amazon EMR Serverless. |
