# Getting replication status information

Replication status can help you determine the current state of an object being replicated.
 The replication status of a source object will return either `PENDING`,
 `COMPLETED`, or `FAILED`. The replication status of a replica will
 return `REPLICA`.

You can also use replication status values when you're creating S3 Batch Replication
 jobs. For example, you can use these status values to replicate objects that have either
 never been replicated or that have failed replication. For more information about using
 these values with Batch Replication, see [Using replication status
 information with Batch Replication jobs](#replication-status-batch-replication "#replication-status-batch-replication").

###### Topics

* [Replication status overview](#replication-status-overview "#replication-status-overview")
* [Replication status if replicating to
 multiple destination buckets](#replication-status-multiple-destinations "#replication-status-multiple-destinations")
* [Replication status if
 Amazon S3 replica modification sync is enabled](#replication-status-replica-mod-syn "#replication-status-replica-mod-syn")
* [Using replication status
 information with Batch Replication jobs](#replication-status-batch-replication "#replication-status-batch-replication")
* [Finding replication status](#replication-status-usage "#replication-status-usage")

## Replication status overview


In replication, you have a source bucket on which you configure replication and one or
 more destination buckets where Amazon S3 replicates objects. When you request an object (by
 using `GetObject`) or object metadata (by using `HeadObject`) from
 these buckets, Amazon S3 returns the `x-amz-replication-status` header in the
 response: 



* When you request an object from the source bucket, Amazon S3 returns the
 `x-amz-replication-status` header if the object in your request
 is eligible for replication. 


For example, suppose that you specify the object prefix `TaxDocs`
 in your replication configuration to tell Amazon S3 to replicate only objects with
 the key name prefix `TaxDocs`. Any objects that you upload that have
 this key name prefix—for example,
 `TaxDocs/document1.pdf`—will be replicated. For object requests
 with this key name prefix, Amazon S3 returns the
 `x-amz-replication-status` header with one of the following
 values for the object's replication status: `PENDING`,
 `COMPLETED`, or `FAILED`.


###### Note

If object replication fails after you upload an object, you can't retry
 replication. You must upload the object again, or you must use
 S3 Batch Replication to replicate any failed objects. For more information
 about using Batch Replication, see [Replicating existing objects with
 Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md"). 

Objects transition to a `FAILED` state for issues such as
 missing replication role permissions, AWS Key Management Service (AWS KMS) permissions, or
 bucket permissions. For temporary failures, such as if a bucket or Region is
 unavailable, replication status doesn't transition to `FAILED`,
 but remains `PENDING`. After the resource is back online, Amazon S3
 resumes replicating those objects.
* When you request an object from a destination bucket, if the object in your
 request is a replica that Amazon S3 created, Amazon S3 returns the
 `x-amz-replication-status` header with the value
 `REPLICA`.

###### Note

Before deleting an object from a source bucket that has replication enabled, check
 the object's replication status to make sure that the object has been replicated. 

If an S3 Lifecycle configuration is enabled on the source bucket, Amazon S3 suspends
 lifecycle actions until it marks the objects' status as either
 `COMPLETED` or `FAILED`.


## Replication status if replicating to
 multiple destination buckets


When you replicate objects to multiple destination buckets, the
 `x-amz-replication-status` header acts differently. The header of the
 source object returns a value of `COMPLETED` only when replication is
 successful to all destinations. The header remains at the `PENDING` value
 until replication has completed for all destinations. If one or more destinations fail
 replication, the header returns `FAILED`.


## Replication status if
 Amazon S3 replica modification sync is enabled


When your replication rules enable Amazon S3 replica modification sync, replicas can report
 statuses other than `REPLICA`. If metadata changes are in the process of
 replicating, the `x-amz-replication-status` header returns
 `PENDING`. If replica modification sync fails to replicate metadata, the header
 returns `FAILED`. If metadata is replicated correctly, the replicas return
 the header `REPLICA`.


## Using replication status
 information with Batch Replication jobs


When creating a Batch Replication job, you can optionally specify additional filters,
 such as the object creation date and replication status, to reduce the scope of the
 job.


You can filter objects to replicate based on the
 `ObjectReplicationStatuses` value, by providing one or more of the
 following values:



* `"NONE"` – Indicates that Amazon S3 has never attempted to
 replicate the object before.
* `"FAILED"` – Indicates that Amazon S3 has attempted, but failed,
 to replicate the object before.
* `"COMPLETED"` – Indicates that Amazon S3 has successfully
 replicated the object before.
* `"REPLICA"` – Indicates that this is a replica object that
 Amazon S3 has replicated from another source.

For more information about using these replication status values with
 Batch Replication, see [Filters for a Batch Replication job](s3-batch-replication-batch.md#batch-replication-filters "s3-batch-replication-batch.md#batch-replication-filters").


## Finding replication status


To get the replication status of the objects in a bucket, you can use the Amazon S3
 Inventory tool. Amazon S3 sends a CSV file to the destination bucket that you specify in the
 inventory configuration. You can also use Amazon Athena to query the replication status in
 the inventory report. For more information about Amazon S3 Inventory, see [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md").


You can also find the object replication status by using the Amazon S3 console, the
 AWS Command Line Interface (AWS CLI), or the AWS SDK. 


In the Amazon S3 console, you can view the replication status for an object on the
 object's details page.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
 **Buckets**.
3. In the **General purpose buckets** list, choose the
 name of the replication source bucket.
4. In the **Objects** list, choose the object name. The
 object's details page appears.
5. On the **Properties** tab, scroll down to the
 **Object management overview** section. Under
 **Management configurations**, see the value under
 **Replication status**.
Use the AWS Command Line Interface (AWS CLI) `head-object` command to retrieve object
 metadata, as shown in the following example. Replace the
 ``amzn-s3-demo-source-bucket1`` with the name of your replication
 source bucket, and replace the other ``user input
 placeholders`` with your own information.


```
aws s3api head-object --bucket `amzn-s3-demo-source-bucket1` --key `object-key` --version-id `object-version-id`           
```
The command returns object metadata, including the
 `ReplicationStatus` as shown in the following example
 response.


```
{
   "AcceptRanges":"bytes",
   "ContentType":"image/jpeg",
   "LastModified":"Mon, 23 Mar 2015 21:02:29 GMT",
   "ContentLength":3191,
   "ReplicationStatus":"COMPLETED",
   "VersionId":"jfnW.HIMOfYiD_9rGbSkmroXsFj3fqZ.",
   "ETag":"\"6805f2cfc46c0f04559748bb039d69ae\"",
   "Metadata":{

   }
}
```
The following code fragments get your replication status by using the
 AWS SDK for Java and AWS SDK for .NET, respectively. 


Java

```
GetObjectMetadataRequest metadataRequest = new GetObjectMetadataRequest(bucketName, key);
ObjectMetadata metadata = s3Client.getObjectMetadata(metadataRequest);

System.out.println("Replication Status : " + metadata.getRawMetadataValue(Headers.OBJECT_REPLICATION_STATUS));
```


.NET

```
GetObjectMetadataRequest getmetadataRequest = new GetObjectMetadataRequest
    {
         BucketName = sourceBucket,
         Key        = objectKey
    };

GetObjectMetadataResponse getmetadataResponse = client.GetObjectMetadata(getmetadataRequest);
Console.WriteLine("Object replication status: {0}", getmetadataResponse.ReplicationStatus);
```
