

# Examples for configuring live replication
<a name="replication-example-walkthroughs"></a>

The following examples provide step-by-step walkthroughs that show how to configure live replication for common use cases. 

**Note**  
Live replication refers to Same-Region Replication (SRR) and Cross-Region Replication (CRR). Live replication doesn't replicate any objects that existed in the bucket before you set up replication. To replicate objects that existed before you set up replication, use on-demand replication. To sync buckets and replicate existing objects on demand, see [Replicating existing objects](s3-batch-replication-batch.md).

These examples demonstrate how to create a replication configuration by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and AWS SDKs (AWS SDK for Java and AWS SDK for .NET examples are shown). 

For information about installing and configuring the AWS CLI, see the following topics in the *AWS Command Line Interface User Guide*:
+  [Get started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) 
+  [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) – You must set up at least one profile. If you are exploring cross-account scenarios, set up two profiles.

For information about the AWS SDKs, see [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/) and [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/).

**Tip**  
For a step-by-step tutorial that demonstrates how to use live replication to replicate data, see [Tutorial: Replicating data within and between AWS Regions using S3 Replication](https://aws.amazon.com/getting-started/hands-on/replicate-data-using-amazon-s3-replication/?ref=docs_gateway/amazons3/replication-example-walkthroughs.html).

**Topics**
+ [Configuring for buckets in the same account](replication-walkthrough1.md)
+ [Configuring for buckets in different accounts](replication-walkthrough-2.md)
+ [Using S3 Replication Time Control](replication-time-control.md)
+ [Replicating encrypted objects](replication-config-for-kms-objects.md)
+ [Replicating metadata changes](replication-for-metadata-changes.md)
+ [Replicating delete markers](delete-marker-replication.md)
+ [Replicating annotations](#replication-annotations)

## Replicating annotations
<a name="replication-annotations"></a>

When you configure replication on a bucket, Amazon S3 replicates annotations automatically as part of live replication. Each annotation replicates independently as changes occur. To replicate annotations, the replication IAM role must include the `s3:GetObjectVersionAnnotationForReplication` permission on the source bucket.

The following example shows the source bucket statement in the IAM role permissions policy with the annotation replication permission included:

```
{
   "Effect": "Allow",
   "Action": [
      "s3:GetObjectVersionForReplication",
      "s3:GetObjectVersionAcl",
      "s3:GetObjectVersionTagging",
      "s3:GetObjectVersionAnnotationForReplication"
   ],
   "Resource": [
      "arn:aws:s3:::{{amzn-s3-demo-source-bucket}}/*"
   ]
}
```

No additional destination bucket permissions are required for annotation replication. The `s3:ReplicateObject` permission on the destination bucket covers annotation replication.

Note the following behaviors for annotation replication:
+ Annotation additions and updates on the source are replicated to the destination. Each annotation replicates independently as changes occur.
+ Annotation deletions on the source are not replicated to the destination. If you delete an annotation on the source, the annotation persists on the destination.
+ If you repeatedly delete and recreate annotations on the source with different names, annotations accumulate on the destination over time because deletions are not replicated.

If you don't want annotations to replicate to a destination bucket, the destination bucket owner can add a Deny statement for the `s3:ReplicateObjectAnnotation` action to the destination bucket policy. Object replication continues to succeed; only annotation replication is blocked. The following example shows the Deny statement:

```
...
   "Statement":[
      {
         "Effect":"Deny",
         "Principal":{
            "AWS":"arn:aws:iam::{{source-bucket-account-id}}:{{role/service-role/source-account-IAM-role}}"
         },
         "Action":"s3:ReplicateObjectAnnotation",
         "Resource":"arn:aws:s3:::{{amzn-s3-demo-destination-bucket}}/*"
      }
   ]
...
```

For more information about annotation replication behavior, see [What does Amazon S3 replicate?](replication-what-is-isnot-replicated.md). For permission setup instructions, see [Setting up permissions for live replication](setting-repl-config-perm-overview.md).