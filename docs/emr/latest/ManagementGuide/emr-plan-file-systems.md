# Working with storage and file systems with Amazon EMR

Amazon EMR and Hadoop provide a variety of file systems that you can use when processing
cluster steps. You specify which file system to use by the prefix of the URI used to access

the data. For example, `s3://amzn-s3-demo-bucket1/path` references an Amazon S3 bucket using S3A (since EMR-7.10.0 release). The following table lists the available file systems, with
recommendations about when it's best to use each one.

Amazon EMR and Hadoop typically use two or more of the following file systems when
processing a cluster. HDFS and S3A are the two main file systems used with Amazon EMR.

###### Important

Beginning with Amazon EMR release 5.22.0, Amazon EMR uses AWS Signature Version 4 exclusively to authenticate requests to Amazon S3. Earlier Amazon EMR releases use AWS Signature Version 2 in some cases, unless the release notes indicate that Signature Version 4 is used exclusively. For more information, see [Authenticating Requests (AWS Signature Version 4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") and [Authenticating Requests (AWS Signature Version 2)](../../../AmazonS3/latest/API/auth-request-sig-v2.md "../../../AmazonS3/latest/API/auth-request-sig-v2.md") in the _Amazon Simple Storage Service Developer Guide_.

| File system                          | Prefix                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HDFS                                 | `hdfs://` (or no prefix) | HDFS is a distributed, scalable, and portable file system for Hadoop.<br>An advantage of HDFS is data awareness between the Hadoop cluster nodes<br>managing the clusters and the Hadoop cluster nodes managing the<br>individual steps. For more information, see [Hadoop<br>documentation](http://hadoop.apache.org/docs/stable "http://hadoop.apache.org/docs/stable").<br>HDFS is used by the master and core nodes. One advantage is that it's<br>fast; a disadvantage is that it's ephemeral storage which is reclaimed<br>when the cluster ends. It's best used for caching the results produced<br>by intermediate job-flow steps.                                                                                                                                                                                                                          |
| S3A                                  | `s3://, s3a://, s3n://`  | The Hadoop S3A filesystem is a open source S3 connector that enables Apache Hadoop and its ecosystem to interact directly with Amazon S3 storage. It allows<br>users to read and write data to S3 buckets using Hadoop-compatible file operations, providing a seamless integration between Hadoop applications and cloud storage.<br>NotePrior to EMR-7.10.0, Amazon EMR used EMRFS for *s3://<br>• and *s3n://<br>• scheme.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| local file system                    |                          | The local file system refers to a locally connected disk. When a<br>Hadoop cluster is created, each node is created from an EC2 instance<br>that comes with a preconfigured block of preattached disk storage called<br>an _instance store_. Data on instance store volumes<br>persists only during the life of its EC2 instance. Instance store<br>volumes are ideal for storing temporary data that is continually<br>changing, such as buffers, caches, scratch data, and other temporary<br>content. For more information, see [Amazon EC2 instance<br>storage](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md").<br>The local file system is used by HDFS, but Python also runs from the<br>local file system and you can choose to store additional application<br>files on instance store volumes. |
| (Legacy) Amazon S3 block file system | `s3bfs://`               | The Amazon S3 block file system is a legacy file storage system. We<br>strongly discourage the use of this system.<br>ImportantWe recommend that you do not use this file system because it can<br>trigger a race condition that might cause your cluster to fail.<br>However, it might be required by legacy applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Access file systems

You specify which file system to use by the prefix of the uniform resource identifier
(URI) used to access the data. The following procedures illustrate how to reference
several different types of file systems.

###### To access a local HDFS

- Specify the `hdfs:///` prefix in the URI. Amazon EMR resolves
  paths that do not specify a prefix in the URI to the local HDFS. For example,
  both of the following URIs would resolve to the same location in HDFS.

```

hdfs:///`path-to-data`

/`path-to-data`

```

###### To access a remote HDFS

- Include the IP address of the master node in the URI, as shown in the
  following examples.

```

hdfs://`master-ip-address`/`path-to-data`

`master-ip-address`/`path-to-data`

```

###### To access Amazon S3

- Use the `s3://` prefix.

```

s3://`bucket-name`/`path-to-file-in-bucket`

```

###### To access the Amazon S3 block file system

- Use only for legacy applications that require the Amazon S3 block file system. To
  access or store data with this file system, use the
  `s3bfs://` prefix in the URI.

The Amazon S3 block file system is a legacy file system that was used to support
uploads to Amazon S3 that were larger than 5 GB. With the multipart upload
functionality Amazon EMR provides through the AWS Java SDK, you can upload large files to the Amazon S3 native file system, and the Amazon S3 block file
system is deprecated. For more information about multipart upload for EMR,
see [Configure multipart upload
for Amazon S3](emr-plan-upload-s3.md#Config_Multipart "emr-plan-upload-s3.md#Config_Multipart"). For more information about S3 object-size and part-size limits, see [Amazon S3 multipart upload limits](../../../AmazonS3/latest/userguide/qfacts.md "../../../AmazonS3/latest/userguide/qfacts.md") in the **Amazon Simple Storage Service** _User Guide_.

###### Warning

Because this legacy file system can create race conditions that can
corrupt the file system, you should avoid this format and use EMRFS instead.

```

s3bfs://`bucket-name`/`path-to-file-in-bucket`

```
