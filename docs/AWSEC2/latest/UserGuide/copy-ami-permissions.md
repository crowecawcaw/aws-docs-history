# Grant permissions to copy Amazon EC2 AMIs

To copy an EBS-backed or Amazon S3-backed AMI, you need the following IAM permissions:

- `ec2:CopyImage` – To copy the AMI. For EBS-backed AMIs, it
  also grants permission to copy the AMI's backing snapshots.
- `ec2:CreateTags` – To tag the target AMI. For EBS-backed
  AMIs, it also grants permission to tag the target AMI’s backing
  snapshots.
  If you're copying an instance stored-backed AMI, you need the following _additional_ IAM permissions:

- `s3:CreateBucket` – To create the S3 bucket in the target
  Region for the new AMI
- `s3:GetBucketAcl` – To read the ACL permissions for the
  source bucket
- `s3:ListAllMyBuckets` – To find an existing S3 bucket for
  AMIs in the target Region
- `s3:GetObject` – To read the objects in the source
  bucket
- `s3:PutObject` – To write the objects in the target
  bucket
- `s3:PutObjectAcl` – To write the permissions for the new
  objects in the target bucket

###### Note

Starting October 28, 2024, you can specify resource-level permissions for the
`CopyImage` action on the source AMI. Resource-level permissions for
the target AMI are available as before. For more information, see
**CopyImage** in the table under [Actions defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions") in the _Service
Authorization Reference_.

## Example IAM policy for copying

an EBS-backed AMI and tagging the target AMI and snapshots

The following example policy grants you permission to copy any EBS-backed AMI and
tag the target AMI and its backing snapshots.

###### Note

Starting October 28, 2024, you can specify snapshots in the
`Resource` element. For more information, see
**CopyImage** in the table under [Actions defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions") in the _Service
Authorization Reference_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "PermissionToCopyAllImages",
 "Effect": "Allow",
 "Action": [
 "ec2:CopyImage",
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*::image/*",
 "arn:aws:ec2:*::snapshot/*"
 ]
 }]
}`

```

## Example IAM policy for copying an EBS-backed AMI but denying tagging the new

snapshots

The `ec2:CopySnapshot` permission is automatically granted when you get the
`ec2:CopyImage` permission. Permission to tag the new backing
snapshots can be explicitly denied, overriding the `Allow` effect for the
`ec2:CreateTags` action.

The following example policy grants you permission to copy any EBS-backed AMI, but
denies you from tagging the new backing snapshots of the target AMI.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:CopyImage",
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*::image/*",
 "arn:aws:ec2:*::snapshot/*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:::snapshot/*"
 }
 ]
}`

```

## Example IAM policy for copying

an Amazon S3-backed AMI and tagging the target AMI

The following example policy grants you permission to copy any Amazon S3-backed AMI in the
specified source bucket to the specified Region, and tag the target AMI.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "PermissionToCopyAllImages",
 "Effect": "Allow",
 "Action": [
 "ec2:CopyImage",
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:*::image/*"
 },
 {
 "Effect": "Allow",
 "Action": "s3:ListAllMyBuckets",
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-source-bucket/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:GetBucketAcl",
 "s3:PutObjectAcl",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::amis-for-`111122223333`-in-`us-east-2`-`hash`"
 ]
 }
 ]
}`

```

To find the Amazon Resource Name (ARN) of the AMI source bucket, open the Amazon EC2
console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/"), in the navigation pane choose
**AMIs**, and locate the bucket name in the
**Source** column.

###### Note

The `s3:CreateBucket` permission is only needed the first time that you copy an
Amazon S3-backed AMI to an individual Region. After that, the Amazon S3 bucket that is
already created in the Region is used to store all future AMIs that you copy
to that Region.
