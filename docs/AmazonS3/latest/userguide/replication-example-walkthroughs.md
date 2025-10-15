# Examples for configuring live replication

The following examples provide step-by-step walkthroughs that show how to configure live
 replication for common use cases. 

###### Note

Live replication refers to Same-Region Replication (SRR) and Cross-Region Replication
 (CRR). Live replication doesn't replicate any objects that existed in the bucket before
 you set up replication. To replicate objects that existed before you set up replication,
 use on-demand replication. To sync buckets and replicate existing objects on demand, see
 [Replicating existing
 objects](s3-batch-replication-batch.md "s3-batch-replication-batch.md").

These examples demonstrate how to create a replication configuration by using the Amazon S3
 console, AWS Command Line Interface (AWS CLI), and AWS SDKs (AWS SDK for Java and AWS SDK for .NET examples are shown). 

For information about installing and configuring the AWS CLI, see the following topics in the
 *AWS Command Line Interface User Guide*:


* [Get started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html")
* [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html") – You must set up at least one profile. If
 you are exploring cross-account scenarios, set up two profiles.
For information about the AWS SDKs, see [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/") and [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/").

###### Tip

For a step-by-step tutorial that demonstrates how to use live replication to replicate data,
 see [Tutorial: Replicating data within and between AWS Regions using
 S3 Replication](https://aws.amazon.com/getting-started/hands-on/replicate-data-using-amazon-s3-replication/?ref=docs_gateway/amazons3/replication-example-walkthroughs.html "https://aws.amazon.com/getting-started/hands-on/replicate-data-using-amazon-s3-replication/?ref=docs_gateway/amazons3/replication-example-walkthroughs.html").

###### Topics

* [Configuring for buckets in
 the same account](replication-walkthrough1.md "replication-walkthrough1.md")
* [Configuring for buckets in different accounts](replication-walkthrough-2.md "replication-walkthrough-2.md")
* [Using S3 Replication Time Control](replication-time-control.md "replication-time-control.md")
* [Replicating encrypted
 objects](replication-config-for-kms-objects.md "replication-config-for-kms-objects.md")
* [Replicating metadata changes](replication-for-metadata-changes.md "replication-for-metadata-changes.md")
* [Replicating delete markers](delete-marker-replication.md "delete-marker-replication.md")
