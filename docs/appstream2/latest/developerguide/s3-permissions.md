# Amazon S3 Bucket Permissions

The Amazon S3 bucket that you choose must have a bucket policy that
provides sufficient access to the AppStream 2.0 service principal to access and download
objects from the Amazon S3 bucket. You will need to modify the following
bucket policy, then apply it to the Amazon S3 bucket you intend to use for
application icons, setup scripts, and VHDs. For more information about how to apply
a policy to an Amazon S3 bucket, see [Adding a bucket policy
using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md").

Make sure that the access control lists (ACLs) for your Amazon S3 buckets
are disabled. For more information, see [Disabling ACLs for all new buckets and enforcing Object Ownership](../../../AmazonS3/latest/userguide/ensure-object-ownership.md "../../../AmazonS3/latest/userguide/ensure-object-ownership.md").

This section presents examples of typical use cases for bucket policies. These
sample policies use `bucket` as the resource value. To test
these policies, replace the `user input placeholders` with
your own information (such as your bucket name).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAppStream2.0ToRetrieveObjects",
 "Effect": "Allow",
 "Principal": {
 "Service": ["appstream.amazonaws.com"]
 },
 "Action": ["s3:GetObject"],
 "Resource": [
 "arn:aws:s3:::`bucket`/`VHD object`",
 "arn:aws:s3:::`bucket`/`Setup script object`",
 "arn:aws:s3:::`bucket`/`Application icon object`",
 "arn:aws:s3:::`bucket`/`Session scripts zip file object`"
 ]
 }
 ]
}`

```

###### Note

The bucket policy example defines specific objects in the S3 bucket that
AppStream 2.0 can access. You can also use prefixes and wildcards to simplify policy
management as you increase your app blocks. For more information about bucket
policies, see [Using bucket
policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md"). For more information about common bucket examples, see
[Bucket policy
examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md").

If you are using an AppStream 2.0 app block, then AppStream 2.0 requires additional permissions
to upload the application package to your appropriate Amazon S3 bucket. For
more information about AppStream 2.0 app blocks, see [AppStream 2.0 App Blocks](appstream-app-blocks.md "appstream-app-blocks.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAppStream2.0ToPutAndRetrieveObjects",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "appstream.amazonaws.com"
 ]
 },
 "Action": [
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject",
 "s3:GetBucketOwnershipControls"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket`",
 "arn:aws:s3:::`bucket`/`AppStream2`/*",
 "arn:aws:s3:::`bucket`/`Setup script object`",
 "arn:aws:s3:::`bucket`/`Application icon object`",
 "arn:aws:s3:::`bucket`/`Session scripts zip file object`"
 ]
 }
 ]
}`

```
