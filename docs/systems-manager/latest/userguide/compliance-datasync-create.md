AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Creating a resource data sync for

Compliance

You can use the resource data sync feature in AWS Systems Manager to send compliance data from
all of your managed nodes to a target Amazon Simple Storage Service (Amazon S3) bucket. When you create the sync,
you can specify managed nodes from multiple AWS accounts, AWS Regions, and your
[hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. Resource data sync then automatically updates the centralized
data when new compliance data is collected. With all compliance data stored in a target
S3 bucket, you can use services like Amazon Athena and Amazon Quick Suite to query and analyze the
aggregated data. Configuring resource data sync for Compliance is a one-time
operation.

Use the following procedure to create a resource data sync for Compliance by using the
AWS Management Console.

###### To create and configure an S3 bucket for resource data sync (console)

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Create a bucket to store your aggregated compliance data. For more
   information, see [Create a
   Bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the _Amazon Simple Storage Service User Guide_. Make a note of
   the bucket name and the AWS Region where you created it.
3. Open the bucket, choose the **Permissions** tab, and then
   choose **Bucket Policy**.
4. Copy and paste the following bucket policy into the policy editor. Replace
   amzn-s3-demo-bucket and `Account-ID` with the name of
   the S3 bucket you created and a valid AWS account ID. Optionally, replace
   `Bucket-Prefix` with the name of an Amazon S3 prefix
   (subdirectory). If you didn't create a prefix, remove
   `Bucket-Prefix`/ from the ARN in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SSMBucketPermissionsCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
 },
 {
 "Sid": " SSMBucketDelivery",
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket/`Bucket-Prefix`/*/accountid=`111122223333`/*"],
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control"
 }
 }
 }
 ]
}`

```

###### To create a resource data sync

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose **Account management**, **Resource Data
   Syncs**, and then choose **Create resource data
   sync**.
4. In the **Sync name** field, enter a name for the sync
   configuration.
5. In the **Bucket name** field, enter the name of the Amazon S3
   bucket you created at the start of this procedure.
6. (Optional) In the **Bucket prefix** field, enter the name of
   an S3 bucket prefix (subdirectory).
7. In the **Bucket region** field, choose **This
   region** if the S3 bucket you created is located in the current
   AWS Region. If the bucket is located in a different AWS Region, choose
   **Another region**, and enter the name of the
   Region.

###### Note

If the sync and the target S3 bucket are located in different Regions, you
might be subject to data transfer pricing. For more information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). 8. Choose **Create**.
