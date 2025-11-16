# Upload data to Amazon S3

For information on how to upload objects to Amazon S3, see [Add an object to your
bucket](../../../AmazonS3/latest/userguide/PuttingAnObjectInABucket.md "../../../AmazonS3/latest/userguide/PuttingAnObjectInABucket.md") in the _Amazon Simple Storage Service User Guide_. For more information
about using Amazon S3 with Hadoop, see [http://wiki.apache.org/hadoop/AmazonS3](http://wiki.apache.org/hadoop2/AmazonS3 "http://wiki.apache.org/hadoop2/AmazonS3").

###### Topics

- [Create and configure an Amazon S3
  bucket](#create-s3-bucket-input "#create-s3-bucket-input")
- [Configure multipart upload for Amazon S3](#Config_Multipart "#Config_Multipart")
- [Best practices](#emr-bucket-bestpractices "#emr-bucket-bestpractices")
- [Upload data to Amazon S3 Express One Zone](emr-express-one-zone.md "emr-express-one-zone.md")

## Create and configure an Amazon S3

bucket

Amazon EMR uses the AWS SDK for Java with Amazon S3 to store input data, log files, and output
data. Amazon S3 refers to these storage locations as _buckets_.
Buckets have certain restrictions and limitations to conform with Amazon S3 and DNS
requirements. For more information, see [Bucket restrictions and
limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the _Amazon Simple Storage Service User Guide_.

This section shows you how to use the Amazon S3 AWS Management Console to create and then set
permissions for an Amazon S3 bucket. You can also create and set permissions for an
Amazon S3 bucket using the Amazon S3 API or AWS CLI. You can also use curl along with a
modification to pass the appropriate authentication parameters for Amazon S3.

See the following resources:

- To create a bucket using the console, see [Create a bucket](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md") in the
  _Amazon S3 User Guide_.
- To create and work with buckets using the AWS CLI, see [Using high-level S3 commands with the AWS Command Line Interface](../../../AmazonS3/latest/userguide/using-s3-commands.md "../../../AmazonS3/latest/userguide/using-s3-commands.md") in the
  _Amazon S3 User Guide_.
- To create a bucket using an SDK, see [Examples
  of creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-get-location-example.md "../../../AmazonS3/latest/userguide/create-bucket-get-location-example.md") in the
  _Amazon Simple Storage Service User Guide_.
- To work with buckets using curl, see [Amazon S3 authentication tool for curl](https://aws.amazon.com/code/amazon-s3-authentication-tool-for-curl/ "https://aws.amazon.com/code/amazon-s3-authentication-tool-for-curl/").
- For more information on specifying Region-specific buckets, see [Accessing a
  bucket](../../../AmazonS3/latest/userguide/UsingBucket.md#access-bucket-intro "../../../AmazonS3/latest/userguide/UsingBucket.md#access-bucket-intro") in the _Amazon Simple Storage Service User Guide_.
- To work with buckets using Amazon S3 Access Points, see [Using a bucket-style alias for your access point](../../../AmazonS3/latest/userguide/access-points-alias.md "../../../AmazonS3/latest/userguide/access-points-alias.md") in the
  _Amazon S3 User Guide_. You can easily use Amazon S3 Access
  Points with the Amazon S3 Access Point Alias instead of the Amazon S3 bucket name.
  You can use the Amazon S3 Access Point Alias for both existing and new
  applications, including Spark, Hive, Presto and others.

###### Note

If you enable logging for a bucket, it enables only bucket access logs,
not Amazon EMR cluster logs.

During bucket creation or after, you can set the appropriate permissions to
access the bucket depending on your application. Typically, you give yourself
(the owner) read and write access and give authenticated users read
access.

Required Amazon S3 buckets must exist before you can create a cluster. You must
upload any required scripts or data referenced in the cluster to Amazon S3.

## Configure multipart upload for Amazon S3

Amazon EMR supports Amazon S3 multipart upload through the AWS SDK for Java. Multipart
upload lets you upload a single object as a set of parts. You can upload these
object parts independently and in any order. If transmission of any part fails,
you can retransmit that part without affecting other parts. After all parts of
your object are uploaded, Amazon S3 assembles the parts and creates the
object.

For more information, see [Multipart
upload overview](../../../AmazonS3/latest/userguide/mpuoverview.md "../../../AmazonS3/latest/userguide/mpuoverview.md") in the _Amazon Simple Storage Service User Guide_.

In addition, Amazon EMR offers properties that allow you to more precisely control
the clean-up of failed multipart upload parts.

The following table describes the Amazon EMR configuration properties for multipart
upload. You can configure these using the `core-site` configuration
classification. For more information, see [Configure applications](../ReleaseGuide/configure-apps.md "../ReleaseGuide/configure-apps.md") in the
_Amazon EMR Release Guide_.

| Configuration parameter name          | Default value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fs.s3n.multipart.uploads.enabled`    | `true`        | A Boolean type that indicates whether to enable multipart<br>uploads. When EMRFS consistent view is enabled, multipart<br>uploads are enabled by default and setting this value to<br>`false` is ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `fs.s3n.multipart.uploads.split.size` | `134217728`   | Specifies the maximum size of a part, in bytes, before<br>EMRFS starts a new part upload when multipart uploads is<br>enabled. The minimum value is `5242880` (5 MB).<br>If a lesser value is specified, `5242880` is<br>used. The maximum is `5368709120` (5 GB). If a<br>greater value is specified, `5368709120` is<br>used.<br>If EMRFS client-side encryption is disabled and the Amazon S3<br>Optimized Committer is also disabled, this value also<br>controls the maximum size that a data file can grow until<br>EMRFS uses multipart uploads rather than a<br>`PutObject` request to upload the file. For<br>more information, see |
| `fs.s3n.ssl.enabled`                  | `true`        | A Boolean type that indicates whether to use http or https.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `fs.s3.buckets.create.enabled`        | `false`       | A Boolean type that indicates whether a bucket should be<br>created if it does not exist. Setting to `false`<br>causes an exception on `CreateBucket`<br>operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `fs.s3.multipart.clean.enabled`       | `false`       | A Boolean type that indicates whether to enable background<br>periodic clean-up of incomplete multipart uploads.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `fs.s3.multipart.clean.age.threshold` | `604800`      | A long type that specifies the minimum age of a multipart<br>upload, in seconds, before it is considered for cleanup. The<br>default is one week.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `fs.s3.multipart.clean.jitter.max`    | `10000`       | An integer type that specifies the maximum amount of random<br>jitter delay in seconds added to the 15-minute fixed delay<br>before scheduling next round of clean-up.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Disable multipart uploads

Console

###### To disable multipart uploads with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console
   at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left
   navigation pane, choose **Clusters**,
   and then choose **Create
   cluster**.
3. Under **Software settings**, enter
   the following configuration:
   `classification=core-site,properties=[fs.s3n.multipart.uploads.enabled=false]`.
4. Choose any other options that apply to your cluster.
5. To launch your cluster, choose **Create
   cluster**.

CLI

###### To disable multipart upload using the AWS CLI

This procedure explains how to disable multipart upload
using the AWS CLI. To disable multipart upload, type the
`create-cluster` command with the
`--bootstrap-actions` parameter.

1. Create a file, `myConfig.json`,
   with the following contents and save it in the same
   directory where you run the command:

```
[
  {
    "Classification": "core-site",
    "Properties": {
      "fs.s3n.multipart.uploads.enabled": "false"
    }
  }
]
```

2. Type the following command and replace
   `myKey` with the name of
   your EC2 key pair.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name "`Test cluster`" \
--release-label `emr-7.11.0` --applications Name=`Hive` Name=`Pig` \
--use-default-roles --ec2-attributes KeyName=`myKey` --instance-type `m5.xlarge` \
--instance-count `3` --configurations file://myConfig.json
```

API

###### To disable multipart upload using the API

- For information on using Amazon S3 multipart uploads
  programmatically, see [Using the
  AWS SDK for Java for multipart upload](../../../AmazonS3/latest/userguide/UsingMPDotJavaAPI.md "../../../AmazonS3/latest/userguide/UsingMPDotJavaAPI.md") in
  the _Amazon Simple Storage Service User Guide_.

For more information about the AWS SDK for Java, see
[AWS SDK
for Java](https://aws.amazon.com/sdkforjava/ "https://aws.amazon.com/sdkforjava/").

## Best practices

The following are recommendations for using Amazon S3 buckets with EMR
clusters.

### Enable versioning

Versioning is a recommended configuration for your Amazon S3 bucket. By
enabling versioning, you ensure that even if data is unintentionally deleted
or overwritten it can be recovered. For more information, see [Using versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md") in the
Amazon Simple Storage Service User Guide.

### Clean up failed multipart uploads

EMR cluster components use multipart uploads via the AWS SDK for Java
with Amazon S3 APIs to write log files and output data to Amazon S3 by default. For
information about changing properties related to this configuration using
Amazon EMR, see [Configure multipart upload for Amazon S3](#Config_Multipart "#Config_Multipart"). Sometimes the upload of a large file can result in an incomplete Amazon S3
multipart upload. When a multipart upload is unable to complete
successfully, the in-progress multipart upload continues to occupy your
bucket and incurs storage charges. We recommend the following options to
avoid excessive file storage:

- For buckets that you use with Amazon EMR, use a lifecycle configuration
  rule in Amazon S3 to remove incomplete multipart uploads three days after
  the upload initiation date. Lifecycle configuration rules allow you
  to control the storage class and lifetime of objects. For more
  information, see [Object lifecycle management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md"), and [Aborting incomplete multipart uploads using a bucket lifecycle
  policy](../../../AmazonS3/latest/userguide/mpuoverview.md#mpu-abort-incomplete-mpu-lifecycle-config "../../../AmazonS3/latest/userguide/mpuoverview.md#mpu-abort-incomplete-mpu-lifecycle-config").
- Enable Amazon EMR's multipart cleanup feature by setting
  `fs.s3.multipart.clean.enabled` to `true`
  and tuning other cleanup parameters. This feature is useful at high
  volume, large scale, and with clusters that have limited uptime. In
  this case, the `DaysAfterIntitiation` parameter of a
  lifecycle configuration rule may be too long, even if set to its
  minimum, causing spikes in Amazon S3 storage. Amazon EMR's multipart cleanup
  allows more precise control. For more information, see [Configure multipart upload for Amazon S3](#Config_Multipart "#Config_Multipart").

### Manage version markers

We recommend that you enable a lifecycle configuration rule in Amazon S3 to
remove expired object delete markers for versioned buckets that you use with
Amazon EMR. When deleting an object in a versioned bucket, a delete marker is
created. If all previous versions of the object subsequently expire, an
expired object delete marker is left in the bucket. While you are not
charged for delete markers, removing expired markers can improve the
performance of LIST requests. For more information, see [Lifecycle configuration for a bucket with versioning](../../../AmazonS3/latest/userguide/lifecycle-configuration-bucket-with-versioning.md "../../../AmazonS3/latest/userguide/lifecycle-configuration-bucket-with-versioning.md") in the
Amazon Simple Storage Service User Guide.

### Performance best practices

Depending on your workloads, specific types of usage of EMR clusters and
applications on those clusters can result in a high number of requests
against a bucket. For more information, see [Request rate and
performance considerations](../../../AmazonS3/latest/userguide/request-rate-perf-considerations.md "../../../AmazonS3/latest/userguide/request-rate-perf-considerations.md") in the
_Amazon Simple Storage Service User Guide_.
