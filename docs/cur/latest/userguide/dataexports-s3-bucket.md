

# Setting up an Amazon S3 bucket for data exports
<a name="dataexports-s3-bucket"></a>

To receive and store your data exports, you must have an Amazon S3 bucket in your AWS account or in a designated destination AWS account. When creating an export in the console, if you want the export in your own bucket, you can select an existing S3 bucket that you own, or you can create a new bucket. In either case, you need to review and confirm the application of the following default S3 bucket policy. If you want your export to be delivered to a bucket owned by another AWS account, you can specify the bucket owner and the bucket name during the Data Exports creation process. Editing the bucket policy or changing the S3 bucket owner after you’ve created an export may prevent Data Exports from delivering your exports. Storing the exports data in any S3 bucket is billed at standard Amazon S3 rates. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-quotas.html).

The following policy must be applied to every S3 bucket, whether owned by you or a different AWS account, when creating a data export:

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
      "Sid": "EnableAWSDataExportsToWriteToS3",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "bcm-data-exports.amazonaws.com"
        ]
      },
      "Action": [
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::{bucket-name}/*",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bcm-data-exports:us-east-1:{source-account-id}:export/*"
        },
        "StringEquals": {
          "aws:SourceAccount": "{source-account-id}"
          }
      }
    }
  ]
   }
```

This S3 bucket policy ensures that Data Exports can only deliver exports to the S3 bucket on behalf of the account that created the export. It also allows Data Exports to verify that the S3 bucket is still owned by the account specified during export creation.
+ To deliver exports to your S3 bucket, AWS needs write permissions for that S3 bucket. To do this, the S3 bucket policy grants the Data Exports service (`bcm-data-exports.amazonaws.com`) permission to deliver (`s3:PutObject`) reports to the S3 bucket you own (`arn:aws:s3:::<EXAMPLE-BUCKET>/*`).
+ Every time Data Exports makes the request to write to the S3 bucket, it must provide the account ID of the account that created the export. The condition keys `aws:SourceArn` and `aws:SourceAccount` enforce this.
+ This S3 bucket policy does not give AWS permissions to read or delete any objects in your S3 bucket, including the Cost and Usage Reports after they’ve been delivered.

For an Amazon S3 bucket that has access control list (ACL) enabled, Data Exports applies a `BucketOwnerFullControl` ACL to the reports when delivering them. By default, Amazon S3 objects, such as these reports, can only be read by the user or service principal who wrote them. To provide you or the S3 bucket owner with permission to read the reports, AWS needs to apply the `BucketOwnerFullControl` ACL. The ACL grants the S3 bucket owner `Permission.FullControl` for these reports. However, it’s recommended to disable ACL and use an S3 bucket policy to control access.

**Note**  
For newly-created S3 buckets, ACLs are disabled by default. For more information, see [Controlling ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html).

If you see an **Invalid bucket** error in the **Data Exports** console page, verify that the policy and S3 bucket ownership haven’t changed since report setup.