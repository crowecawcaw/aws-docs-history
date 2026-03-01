# Maintenance for table buckets

Amazon S3 offers maintenance operations to enhance the management and performance of your
table buckets. The following option is enabled by default for all table buckets. You can edit or
disable this option by specifying a maintenance configuration file for your table bucket.

Editing this configuration requires the
`s3tables:PutTableBucketMaintenanceConfiguration` permission.

###### Topics

- [Unreferenced file removal](#s3-table-bucket-maintenance-unreferenced "#s3-table-bucket-maintenance-unreferenced")
- [Consideration and limitations](#s3-tables-buckets-considerations-see-more "#s3-tables-buckets-considerations-see-more")

## Unreferenced file removal

Unreferenced file removal identifies and deletes all objects that are not referenced by any
table snapshots. As part of your unreferenced file removal policy, you can configure two properties:
`unreferencedDays` (3 days by default) and `nonCurrentDays` (10 days by
default).

For any object not referenced by your table and older than the `unreferencedDays`
property, S3 marks the object as noncurrent. S3 deletes noncurrent objects after the
number of days specified by the `nonCurrentDays` property.

###### Note

Deletes of noncurrent objects are permanent with no way to recover these objects.

To view or recover objects that have been marked as noncurrent, you must contact
AWS Support. For information about contacting AWS Support, see [Contact AWS](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") or the [AWS Support
Documentation](https://aws.amazon.com/documentation/aws-support/ "https://aws.amazon.com/documentation/aws-support/").

Unreferenced file removal determines the objects to delete from your table with
reference only to that table. Any reference made to these objects outside of the table
will not prevent unreferenced file removal from deleting an object.

If you disable unreferenced file removal, any in-progress jobs will not be affected.
The new configuration will take effect for the next job after the configuration change.
For more information, see the pricing information in the [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

You can only configure unreferenced file removal at the table bucket level. This
configuration will apply to every table in your bucket.

**To configure unreferenced file removal by using the AWS CLI**

The following example will set the `unreferencedDays` to 4 days and
the `nonCurrentDays` to 10 days using the
`PutTableBucketMaintenanceConfiguration` API.

```
aws s3tables put-table-bucket-maintenance-configuration \
   --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket \
   --type icebergUnreferencedFileRemoval \
   --value '{"status":"enabled","settings":{"icebergUnreferencedFileRemoval":{"unreferencedDays":4,"nonCurrentDays":10}}}'
```

For more information, see [put-table-bucket-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-bucket-maintenance-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-bucket-maintenance-configuration.html") in the
_AWS CLI Command Reference_.

## Consideration and limitations

To learn more about additional consideration and limits for unreferenced file removal,
see [Considerations and limitations for maintenance jobs](s3-tables-considerations.md "s3-tables-considerations.md").
