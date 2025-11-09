# Deleting the Amazon S3 Bucket for Home Folders and Application Settings Persistence

WorkSpaces Applications adds an Amazon S3 bucket policy to the buckets that it creates to prevent them from
being accidentally deleted. To delete an S3 bucket, you must first delete the S3
bucket policy. Following are the bucket policies that you must delete for home folders and application settings persistence.

**Home folders policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PreventAccidentalDeletionOfBucket",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:DeleteBucket",
 "Resource": "arn:aws:s3:::appstream2-36fb080bb8-`region-code`-`account-id-without-hyphens`"
 }
 ]
}`

```

**Application settings persistence policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PreventAccidentalDeletionOfBucket",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:DeleteBucket",
 "Resource": "arn:aws:s3:::appstream-app-settings-`region-code`-`account-id-without-hyphens`-`unique-identifier`"
 }
 ]
}`

```

For more information, see [Deleting or Emptying a Bucket](../../../AmazonS3/latest/userguide/delete-or-empty-bucket.md "../../../AmazonS3/latest/userguide/delete-or-empty-bucket.md") in the
_Amazon Simple Storage Service User Guide_.
