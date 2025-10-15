# Setting up live replication overview

###### Note

Objects that existed before you set up replication aren't replicated automatically. In
 other words, Amazon S3 doesn't replicate objects retroactively. To replicate objects that were
 created before your replication configuration, use S3 Batch Replication. For more
 information about configuring Batch Replication, see [Replicating existing
 objects](s3-batch-replication-batch.md "s3-batch-replication-batch.md").

To enable live replication—Same-Region Replication (SRR) or Cross-Region Replication
 (CRR)—add a replication configuration to your source bucket. This configuration tells
 Amazon S3 to replicate objects as specified. In the replication configuration, you must provide the
 following:


* **The destination buckets** – The bucket or buckets
 where you want Amazon S3 to replicate the objects.
* **The objects that you want to replicate** – You can
 replicate all objects in the source bucket or a subset of objects. You identify a subset by
 providing a [key name prefix](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#keyprefix "https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#keyprefix"), one or
 more object tags, or both in the configuration.


For example, if you configure a replication rule to replicate only objects with the key
 name prefix `Tax/`, Amazon S3 replicates objects with keys such as
 `Tax/doc1` or `Tax/doc2`. But it doesn't replicate objects with the
 key `Legal/doc3`. If you specify both a prefix and one or more tags, Amazon S3
 replicates only objects that have the specific key prefix and tags.
* **An AWS Identity and Access Management (IAM) role** – Amazon S3 assumes this
 IAM role to replicate objects on your behalf. For more information about creating this
 IAM role and managing permissions, see [Setting up permissions for live
 replication](setting-repl-config-perm-overview.md "setting-repl-config-perm-overview.md").
In addition to these minimum requirements, you can choose the following options: 


* **Replica storage class** – By default, Amazon S3 stores
 object replicas using the same storage class as the source object. You can specify a
 different storage class for the replicas.
* **Replica ownership** – Amazon S3 assumes that an object
 replica continues to be owned by the owner of the source object. So when it replicates
 objects, it also replicates the corresponding object access control list (ACL) or S3
 Object Ownership setting. If the source and destination buckets are owned by different
 AWS accounts, you can configure replication to change the owner of a replica to the
 AWS account that owns the destination bucket. For more information, see [Changing the replica owner](replication-change-owner.md "replication-change-owner.md").
You can configure replication by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), AWS SDKs, or
 the Amazon S3 REST API. For detailed walkthroughs of how to set up replication, see [Examples for configuring live replication](replication-example-walkthroughs.md "replication-example-walkthroughs.md").

 Amazon S3 provides REST API operations to support setting up replication rules. For more
 information, see the following topics in the *Amazon Simple Storage Service API Reference*:


* [PutBucketReplication](../API/API_PutBucketReplication.md "../API/API_PutBucketReplication.md")
* [GetBucketReplication](../API/API_GetBucketReplication.md "../API/API_GetBucketReplication.md")
* [DeleteBucketReplication](../API/API_DeleteBucketReplication.md "../API/API_DeleteBucketReplication.md")
###### Topics

* [Replication configuration file elements](replication-add-config.md "replication-add-config.md")
* [Setting up permissions for live
 replication](setting-repl-config-perm-overview.md "setting-repl-config-perm-overview.md")
* [Examples for configuring live replication](replication-example-walkthroughs.md "replication-example-walkthroughs.md")
