# Amazon S3 on Outposts with local Amazon EMR on Outposts

Amazon EMR is a managed cluster platform that simplifies running big data frameworks, such
as Apache Hadoop and Apache Spark, on AWS to process and
analyze vast amounts of data. By using these frameworks and related open-source projects,
you can process data for analytics purposes and business intelligence workloads. Amazon EMR
also helps you transform and move large amounts of data into and out of other AWS data
stores and databases, and supports Amazon S3 on Outposts. For more information about Amazon EMR, see
[Amazon EMR on Outposts](../../../emr/latest/ManagementGuide/emr-plan-outposts.md "../../../emr/latest/ManagementGuide/emr-plan-outposts.md") in the _Amazon EMR Management Guide_.

For Amazon S3 on Outposts, Amazon EMR started to support the Apache Hadoop S3A
connector in version 7.0.0. Earlier versions of Amazon EMR don't support local S3 on Outposts,
and the EMR File System (EMRFS) is not supported.

###### Supported applications

Amazon EMR with Amazon S3 on Outposts supports the following applications:

- Hadoop
- Spark
- Hue
- Hive
- Sqoop
- Pig
- Hudi
- Flink
  For more information, see the [Amazon EMR Release
  Guide](../../../emr/latest/ReleaseGuide/emr-release-components.md "../../../emr/latest/ReleaseGuide/emr-release-components.md").

## Create and configure an Amazon S3 on Outposts

bucket

Amazon EMR uses the AWS SDK for Java with Amazon S3 on Outposts to store input data and output
data. Your Amazon EMR log files are stored in a Regional Amazon S3 location that you select and
aren't stored locally on the Outpost. For more information, see [Amazon EMR
logs](../../../emr/latest/ManagementGuide/emr-manage-view-web-log-files.md "../../../emr/latest/ManagementGuide/emr-manage-view-web-log-files.md") in the _Amazon EMR Management Guide_.

To conform with Amazon S3 and DNS requirements, S3 on Outposts buckets have naming
restrictions and limitations. For more information, see [Creating an S3 on Outposts bucket](S3OutpostsCreateBucket.md "S3OutpostsCreateBucket.md").

With Amazon EMR version 7.0.0 and later, you can use Amazon EMR with S3 on Outposts and the S3A
file system.

###### Prerequisites

S3 on Outposts permissions – When you create your
Amazon EMR instance profile, your role must contain the AWS Identity and Access Management (IAM) namespace for
S3 on Outposts. S3 on Outposts has its own namespace, `s3-outposts*`. For an
example policy that uses this namespace, see [Setting up IAM with S3 on Outposts](S3OutpostsIAM.md "S3OutpostsIAM.md").

S3A connector – To configure your EMR cluster to
access data from an Amazon S3 on Outposts bucket, you must use the Apache Hadoop
S3A connector. To use the connector, ensure that all of your S3 URIs use the
`s3a` scheme. If they don't, you can configure the file system implementation
that you use for your EMR cluster so that your S3 URIs work with the S3A connector.

To configure the file system implementation to work with the S3A connector, you use the
`fs.`file_scheme`.impl` and
`fs.AbstractFileSystem.`file_scheme`.impl`
configuration properties for your EMR cluster, where
`file_scheme` corresponds to the type of S3
URIs that you have. To use the following example, replace the `user input
 placeholders` with your own information. For example, to change
the file system implementation for S3 URIs that use the `s3` scheme, specify the
following cluster configuration properties:

```
[
  {
"Classification": "core-site",
    "Properties": {
    "fs.`s3`.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
    "fs.AbstractFileSystem.`s3`.impl": "org.apache.hadoop.fs.s3a.S3A"
    }
  }
]

```

To use S3A, set the `fs.`file_scheme`.impl`
configuration property to `org.apache.hadoop.fs.s3a.S3AFileSystem`, and set the
`fs.AbstractFileSystem.`file_scheme`.impl`
property to `org.apache.hadoop.fs.s3a.S3A`.

For example, if you are accessing the path
`s3a://`bucket`/...`, set the
`fs.s3a.impl` property to
`org.apache.hadoop.fs.s3a.S3AFileSystem`, and set the
`fs.AbstractFileSystem.s3a.impl` property to
`org.apache.hadoop.fs.s3a.S3A`.

## Getting started using Amazon EMR with

Amazon S3 on Outposts

The following topics explain how to get started using Amazon EMR with
Amazon S3 on Outposts.

###### Topics

- [Create a permissions policy](#create-permission-policy "#create-permission-policy")
- [Create and configure your cluster](#configure-cluster "#configure-cluster")
- [Configurations overview](#configurations-overview "#configurations-overview")
- [Considerations](#considerations "#considerations")

### Create a permissions policy

Before you can create an EMR cluster that uses Amazon S3 on Outposts, you must create
an IAM policy to attach to the Amazon EC2 instance profile for the cluster. The policy
must have permissions to access the S3 on Outposts access point Amazon Resource Name
(ARN). For more information about creating IAM policies for S3 on Outposts, see
[Setting up IAM with S3 on Outposts](S3OutpostsIAM.md "S3OutpostsIAM.md").

The following example policy shows how to grant the required permissions. After
you create the policy, attach the policy to the instance profile role that you use
to create your EMR cluster, as described in the [Create and configure your cluster](#configure-cluster "#configure-cluster")
section. To use this example, replace the `user input
 placeholders` with your own information.

```
{
"Version":"2012-10-17",
  "Statement": [
        {
  "Effect": "Allow",
            "Resource": "arn:aws:s3-outposts:`us-west-2`:`111122223333`:outpost/`op-01ac5d28a6a232904`/accesspoint/`access-point-name`,
            "Action": [
                "s3-outposts:*"
            ]
        }
    ]

 }
```

### Create and configure your cluster

To create a cluster that runs Spark with S3 on Outposts, complete the following
steps in the console.

###### To create a cluster that runs Spark with

S3 on Outposts

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/elasticmapreduce/](https://console.aws.amazon.com/elasticmapreduce/ "https://console.aws.amazon.com/elasticmapreduce/").
2. In the left navigation pane, choose **Clusters**.
3. Choose **Create cluster**.
4. For **Amazon EMR release**, choose
   **emr-7.0.0** or later.
5. For Application bundle, choose **Spark interactive**.
   Then select any other supported applications that you want to be included in
   your cluster.
6. To enable Amazon S3 on Outposts, enter your configuration settings.

###### Sample configuration settings

To use the following sample configuration settings, replace the
`user input placeholders`
with your own information.

```
[
 {
   "Classification": "core-site",
   "Properties": {
     "fs.s3a.bucket.`DOC-EXAMPLE-BUCKET`.accesspoint.arn": "arn:aws:s3-outposts:`us-west-2`:`111122223333`:outpost/`op-01ac5d28a6a232904`/accesspoint/`access-point-name`"
     "fs.s3a.committer.name": "magic",
     "fs.s3a.select.enabled": "false"
    }
  },
  {
    "Classification": "hadoop-env",
    "Configurations": [
      {
        "Classification": "export",
        "Properties": {
          "JAVA_HOME": "/usr/lib/jvm/java-11-amazon-corretto.x86_64"
          }
       }
     ],
     "Properties": {}
   },
   {
     "Classification": "spark-env",
     "Configurations": [
       {
         "Classification": "export",
         "Properties": {
           "JAVA_HOME": "/usr/lib/jvm/java-11-amazon-corretto.x86_64"
         }
       }
      ],
      "Properties": {}
     },
     {
      "Classification": "spark-defaults",
      "Properties": {
        "spark.executorEnv.JAVA_HOME": "/usr/lib/jvm/java-11-amazon-corretto.x86_64",
        "spark.sql.sources.fastS3PartitionDiscovery.enabled": "false"
      }
     }
  ]

```

7. In the **Networking** section, choose a virtual private
   cloud (VPC) and subnet that are on your AWS Outposts rack. For more information
   about Amazon EMR on Outposts, see [EMR clusters on
   AWS Outposts](../../../emr/latest/ManagementGuide/emr-plan-outposts.md "../../../emr/latest/ManagementGuide/emr-plan-outposts.md") in the _Amazon EMR Management
   Guide_.
8. In the **EC2 instance profile for Amazon EMR** section, choose
   the IAM role that has the [permissions policy that you created earlier](#create-permission-policy "#create-permission-policy") attached.
9. Configure your remaining cluster settings, and then choose
   **Create cluster**.

### Configurations overview

The following table describes S3A configurations and
the values to specify for their parameters when you set up a cluster that uses
S3 on Outposts with Amazon EMR.

| Parameter                                            | Default value                                                                          | Required value for S3 on Outposts                 | Explanation                                                                                                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fs.s3a.aws.credentials.provider`                    | If not specified, S3A will look for S3 in Region bucket with the Outposts bucket name. | The access point ARN of the S3 on Outposts bucket | Amazon S3 on Outposts supports virtual private cloud (VPC)-only access points as the only means to access your Outposts buckets. |
| `fs.s3a.committer.name`                              | `file`                                                                                 | `magic`                                           | Magic committer is the only supported committer for S3 on Outposts.                                                              |
| `fs.s3a.select.enabled`                              | `TRUE`                                                                                 | `FALSE`                                           | S3 Select is not supported on Outposts.                                                                                          |
| `JAVA_HOME`                                          | `/usr/lib/jvm/java-8`                                                                  | `/usr/lib/jvm/java-11-amazon-corretto.x86_64`     | S3 on Outposts on S3A requires Java version 11.                                                                                  | The following table describes Spark configurations and the values to specify for their parameters when you set up a cluster that uses S3 on Outposts with Amazon EMR.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Parameter                                            | Default value                                                                          | Required value for S3 on Outposts                 | Explanation                                                                                                                      |
| ---                                                  | ---                                                                                    | ---                                               | ---                                                                                                                              |
| `spark.sql.sources.fastS3PartitionDiscovery.enabled` | `TRUE`                                                                                 | `FALSE`                                           | S3 on Outposts doesn't support fast partition.                                                                                   |
| `spark.executorEnv.JAVA_HOME`                        | `/usr/lib/jvm/java-8`                                                                  | `/usr/lib/jvm/java-11-amazon-corretto.x86_64`     | S3 on Outposts on S3A requires Java version 11.                                                                                  | ### Considerations Consider the following when you integrate Amazon EMR with S3 on Outposts buckets: <br>• Amazon S3 on Outposts is supported with Amazon EMR version 7.0.0 and later. <br>• The S3A connector is required to use S3 on Outposts with Amazon EMR. Only S3A has the features required to interact with S3 on Outposts buckets. For S3A connector setup information, see [Prerequisites](#s3a-outposts-prerequisites "#s3a-outposts-prerequisites"). <br>• Amazon S3 on Outposts supports only server-side encryption with Amazon S3 managed keys (SSE-S3) with Amazon EMR. For more information, see [Data encryption in S3 on Outposts](s3-outposts-data-encryption.md "s3-outposts-data-encryption.md"). <br>• Amazon S3 on Outposts doesn't support writes with the S3A FileOutputCommitter. Writes with the S3A FileOutputCommitter on S3 on Outposts buckets result in the following error: **`InvalidStorageClass: The storage class you specified is not valid`**. <br>• Amazon S3 on Outposts isn't supported with Amazon EMR Serverless or Amazon EMR on EKS. <br>• Amazon EMR logs are stored in a Regional Amazon S3 location that you select, and are not stored locally in the S3 on Outposts bucket. |
