# Read, Write and Upload data into Amazon S3 Express One Zone with Amazon EMR on EKS

With Amazon EMR releases 7.2.0 and higher, you can use Amazon EMR on EKS with the [Amazon S3 Express One Zone](../../../AmazonS3/latest/userguide/s3-express-one-zone.md "../../../AmazonS3/latest/userguide/s3-express-one-zone.md")
storage class for improved performance when you run jobs and workloads. S3 Express One Zone is a a high-performance, single-zone Amazon S3 storage class that delivers consistent,
single-digit millisecond data access for most latency-sensitive applications. At the time of its release,
S3 Express One Zone delivers the lowest latency and highest performance cloud object storage in Amazon S3.

## Prerequisites

Before you can use S3 Express One Zone with Amazon EMR on EKS, you must have the following prerequisites:

- [Completed setting up Amazon EMR on EKS](setting-up.md "setting-up.md").
- After you set up Amazon EMR on EKS, [create a virtual cluster](virtual-cluster.md#create-virtul-cluster "virtual-cluster.md#create-virtul-cluster").

## Getting started with S3 Express One Zone

Follow these steps to get started with S3 Express One Zone

1. Add the `CreateSession` permission to your job execution role.
   When S3 Express One Zone initially performs an action like `GET`, `LIST`, or `PUT` on an S3 object,
   the storage class calls `CreateSession` on your behalf. The following is an example of how to grant the `CreateSession` permission.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3express:*:*:bucket/`DOC-EXAMPLE-BUCKET`"
 ],
 "Action": [
 "s3express:CreateSession"
 ],
 "Sid": "AllowS3EXPRESSCreatesession"
 }
 ]
}`

```

2. You must use the Apache Hadoop connector S3A to access the S3 Express buckets, so change your Amazon S3 URIs to use the `s3a` scheme to use the connector.
   If they don’t use the scheme, you can change the filesystem implementation that you use for `s3` and `s3n` schemes.

To change the `s3` scheme, specify the following cluster configurations:

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

To change the s3n scheme, specify the following cluster configurations:

```
[
  {
    "Classification": "core-site",
    "Properties": {
      "fs.s3n.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
      "fs.AbstractFileSystem.s3n.impl": "org.apache.hadoop.fs.s3a.S3A",
      "fs.s3a.endpoint.region": "`us-west-2`",
      "fs.s3a.change.detection.mode": "none",
      "fs.s3a.select.enabled": "false"
    }
  },
   {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.hadoop.fs.s3a.aws.credentials.provider": "software.amazon.awssdk.auth.credentials.WebIdentityTokenFileCredentialsProvider",
      "spark.sql.sources.fastS3PartitionDiscovery.enabled": "false"
    }
  }
]
```

3. In your spark-submit configuration, use the web identity credential provider.

```
"spark.hadoop.fs.s3a.aws.credentials.provider=com.amazonaws.auth.WebIdentityTokenCredentialsProvider"
```
