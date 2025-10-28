# Setting up an Amazon S3 bucket for data

exports

You must have an Amazon S3 bucket in your AWS account to receive and store your data
exports. When creating an export in the console, you can select an existing S3 bucket that you
own, or you can create a new bucket. In either case, you need to review and confirm the
application of the following default S3 bucket policy. Editing this policy in the Amazon S3
console or changing the S3 bucket owner after you’ve created an export prevents Data Exports from
delivering your exports. Storing the exports data in your S3 bucket is billed at standard
Amazon S3 rates. For more information, see [Quotas and
restrictions](dataexports-quotas.md "dataexports-quotas.md").

###### Note

The account that creates the export must also own the S3 bucket that AWS sends the
exports to. You cannot configure an export to deliver to an S3 bucket owned by another
account.

The following policy is applied to every S3 bucket when creating a data export:

This S3 bucket policy ensures that Data Exports can only deliver exports to the S3 bucket on
behalf of the account that created the export. It also allows Data Exports to verify that the S3
bucket is still owned by the account that created the export.

- To deliver exports to your S3 bucket, AWS needs write permissions for that S3
  bucket. To do this, the S3 bucket policy grants the Data Exports service
  (`bcm-data-exports.amazonaws.com`) permission to deliver
  (`s3:PutObject`) reports to the S3 bucket you own
  (`arn:aws:s3:::<EXAMPLE-BUCKET>/*`).
- Every time Data Exports makes the request to write to the S3 bucket, it must provide the
  account ID of the account that created the export. The condition keys
  `aws:SourceArn` and `aws:SourceAccount` enforce this.
- This S3 bucket policy does not give AWS permissions to read or delete any objects in
  your S3 bucket, including the Cost and Usage Reports after they’ve been delivered.
  For an Amazon S3 bucket that has access control list (ACL) enabled, Data Exports applies a
  `BucketOwnerFullControl` ACL to the reports when delivering them. By default,
  Amazon S3 objects, such as these reports, can only be read by the user or service principal
  who wrote them. To provide you or the S3 bucket owner with permission to read the reports,
  AWS needs to apply the `BucketOwnerFullControl` ACL. The ACL grants the S3 bucket
  owner `Permission.FullControl` for these reports. However, it’s recommended to
  disable ACL and use an S3 bucket policy to control access.

###### Note

For newly-created S3 buckets, ACLs are disabled by default. For more information, see
[Controlling ownership of objects and disabling ACLs for your bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md").

If you see an **Invalid bucket** error in the **Data Exports**
console page, verify that the policy and S3 bucket ownership haven’t changed since report
setup.
