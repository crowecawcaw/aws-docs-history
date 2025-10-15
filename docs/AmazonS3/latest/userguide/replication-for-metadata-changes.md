# Replicating metadata changes with
 replica modification sync

Amazon S3 replica modification sync can help you keep object metadata such as tags, access control
 lists (ACLs), and Object Lock settings replicated between replicas and source objects. By
 default, Amazon S3 replicates metadata from the source objects to the replicas only. When
 replica modification sync is enabled, Amazon S3 replicates metadata changes made to the replica copies
 back to the source object, making the replication bidirectional (two-way
 replication).


## Enabling
 replica modification sync


You can use Amazon S3 replica modification sync with new or existing replication rules. You can
 apply it to an entire bucket or to objects that have a specific prefix.


To enable replica modification sync by using the Amazon S3 console, see [Examples for configuring live replication](replication-example-walkthroughs.md "replication-example-walkthroughs.md"). This topic provides instructions
 for enabling replica modification sync in your replication configuration when the source and
 destination buckets are owned by the same or different AWS accounts.


To enable replica modification sync by using the AWS Command Line Interface (AWS CLI), you must add a replication
 configuration to the bucket containing the replicas with
 `ReplicaModifications` enabled. To set up two-way replication, create a
 replication rule from the source bucket (``amzn-s3-demo-source-bucket``) to the
 bucket containing the replicas (``amzn-s3-demo-destination-bucket``). Then,
 create a second replication rule from the bucket containing the replicas
 (``amzn-s3-demo-destination-bucket``) to the source bucket
 (``amzn-s3-demo-source-bucket``). The source and destination buckets can be
 in the same or different AWS Regions.


###### Note

You must enable replica modification sync on both the source and destination buckets to replicate
 replica metadata changes like object access control lists (ACLs), object tags, or
 Object Lock settings on the replicated objects. Like all replication rules, you can
 apply these rules to the entire bucket or to a subset of objects filtered by prefix
 or object tags.


In the following example configuration, Amazon S3 replicates metadata changes under the
 prefix ``Tax`` to the bucket
 ``amzn-s3-demo-source-bucket``, which contains the source objects.



```
{
    "Rules": [
        {
            "Status": "Enabled",
            "Filter": {
                "Prefix": "`Tax`"
            },
            "SourceSelectionCriteria": {
                "ReplicaModifications":{
                    "Status": "Enabled"
                }
            },
            "Destination": {
                "Bucket": "arn:aws:s3:::`amzn-s3-demo-source-bucket`"
            },
            "Priority": 1
        }
    ],
    "Role": "IAM-Role-ARN"
}
```

For full instructions on creating replication rules by using the AWS CLI, see [Configuring replication for buckets in the same
 account](replication-walkthrough1.md "replication-walkthrough1.md").
