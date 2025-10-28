# Replicating delete markers between

buckets

By default, when S3 Replication is enabled and an object is deleted in the source
bucket, Amazon S3 adds a delete marker in the source bucket only. This action helps protect data
in the destination buckets from accidental or malicious deletions. If you have _delete marker replication_ enabled, these markers are copied to the destination
buckets, and Amazon S3 behaves as if the object was deleted in both the source and destination
buckets. For more information about how delete markers work, see [Working with delete markers](DeleteMarker.md "DeleteMarker.md").

###### Note

- Delete marker replication isn't supported for tag-based replication rules.
  Delete marker replication also doesn't adhere to the 15-minute service-level
  agreement (SLA) that's granted when you're using S3 Replication Time Control (S3 RTC).
- If you're not using the latest replication configuration XML version, delete
  operations affect replication differently. For more information, see [How delete operations affect replication](replication-what-is-isnot-replicated.md#replication-delete-op "replication-what-is-isnot-replicated.md#replication-delete-op").
- If you enable delete marker replication and your source bucket has an S3 Lifecycle expiration rule,
  the delete markers added by the S3 Lifecycle expiration rule won't be replicated
  to the destination bucket.

## Enabling delete marker replication

You can start using delete marker replication with a new or existing replication rule. You can apply delete marker replication
to an entire bucket or to objects that have a specific prefix.

To enable delete marker replication by using the Amazon S3 console, see [Using the S3 console](replication-walkthrough1.md#enable-replication "replication-walkthrough1.md#enable-replication"). This topic provides instructions for enabling
delete marker replication in your replication configuration when the source and destination buckets are
owned by the same or different AWS accounts.

To enable delete marker replication by using the AWS Command Line Interface (AWS CLI), you must add a replication
configuration to the source bucket with `DeleteMarkerReplication` enabled, as
shown in the following example configuration.

In the following example replication configuration, delete markers are replicated to
the destination bucket `amzn-s3-demo-destination-bucket` for objects under
the prefix `Tax`.

```
{
    "Rules": [
        {
            "Status": "Enabled",
            "Filter": {
                "Prefix": "`Tax`"
            },
            "DeleteMarkerReplication": {
                "Status": "Enabled"
            },
            "Destination": {
                "Bucket": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
            },
            "Priority": 1
        }
    ],
    "Role": "`IAM-Role-ARN`"
}
```

For full instructions on creating replication rules through the AWS CLI, see [Configuring replication for buckets in the same
account](replication-walkthrough1.md "replication-walkthrough1.md").
