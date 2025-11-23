# Different ways to get data into Amazon EMR

Amazon EMR provides several ways to get data onto a cluster. The most common way is to
upload the data to Amazon S3 and use the built-in features of Amazon EMR to load the data onto
your cluster. You can also use the DistributedCache feature of Hadoop to
transfer files from a distributed file system to the local file system. The
implementation of Hive provided by Amazon EMR (Hive version 0.7.1.1 and later) includes
functionality that you can use to import and export data between DynamoDB and an Amazon EMR
cluster. If you have large amounts of on-premises data to process, you may find the
Direct Connect service useful.

###### Topics

- [Upload data to Amazon S3](emr-plan-upload-s3.md "emr-plan-upload-s3.md")
- [Upload data with
  AWS DataSync](emr-plan-upload-datasync.md "emr-plan-upload-datasync.md")
- [Import files with distributed
  cache with Amazon EMR](emr-plan-input-distributed-cache.md "emr-plan-input-distributed-cache.md")
- [Detecting and processing compressed files with Amazon EMR](HowtoProcessGzippedFiles.md "HowtoProcessGzippedFiles.md")
- [Import DynamoDB data into Hive with Amazon EMR](emr-plan-input-dynamodb.md "emr-plan-input-dynamodb.md")
- [Connect to data with
  AWS Direct Connect from Amazon EMR](emr-plan-input-directconnect.md "emr-plan-input-directconnect.md")
- [Upload large amounts of data for Amazon EMR with
  AWS Snowball Edge](emr-plan-input-snowball.md "emr-plan-input-snowball.md")
