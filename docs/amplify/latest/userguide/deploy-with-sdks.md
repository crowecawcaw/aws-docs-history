# Creating a bucket policy to deploy a static website from

S3 using the AWS SDKs

You can use the AWS SDKs to deploy a static website from Amazon S3 to Amplify Hosting.
If you deploy your website using an SDK, you must create your own bucket policy that
grants Amplify Hosting permission to retrieve the objects in your S3
bucket.

To learn more about creating bucket policies, see [Bucket
policies for Amazon S3](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") in the _Amazon Simple Storage Service User Guide_.

The following example bucket policy grants Amplify Hosting permissions to list
buckets and retrieve bucket objects for the specified AWS account, Amplify
application id, and branch.

To use this example:

- Replace `amzn-s3-demo-website-bucket/prefix` with the name of your website's bucket and prefix.
- Replace `111122223333` with your AWS account id.
- Replace `region-id` with the AWS Region that your Amplify application is located in, such as `us-east-1`.
- Replace `app_id` with you Amplify application id. This information is available in the Amplify console.
- Replace `branch_name` with your branch name.

###### Note

In your bucket policy, the `aws:SourceArn` must be a URL-encoded (percent-encoding)
branch ARN.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAmplifyToListPrefix_appid_branch_prefix_",
 "Effect": "Allow",
 "Principal": {
 "Service": "amplify.amazonaws.com"
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-website-bucket/prefix`/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`",
 "aws:SourceArn": "arn%3Aaws%3Aamplify%3A`region-id`%3A`111122223333`%3Aapps%2F`app_id`%2Fbranches%2F`branch_name`",
 "s3:prefix": ""
 }
 }
 },
 {
 "Sid": "AllowAmplifyToReadPrefix__appid_branch_prefix_",
 "Effect": "Allow",
 "Principal": {
 "Service": "amplify.amazonaws.com"
 },
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-website-bucket/prefix`/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`",
 "aws:SourceArn": "arn%3Aaws%3Aamplify%3A`region-id`%3A`111122223333`%3Aapps%2F`app_id`%2Fbranches%2F`branch_name`"
 }
 }
 },
 {
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-website-bucket`/*",
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 }
 ]
}`

```
