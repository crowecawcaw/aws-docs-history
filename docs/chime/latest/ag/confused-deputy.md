**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Cross-service confused deputy prevention

The confused deputy problem is an information security issue that occurs when an entity without permission to perform an action calls a more-privileged entity to perform the action. This can allow malicious actors to run
commands or modify resources they otherwise would not have permission to run or access. For more information, see
[The confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the _AWS Identity and Access Management User Guide_.

In AWS, cross-service impersonation can lead to a confused deputy scenario. Cross-service impersonation happens when one service (the _calling service_) calls another service (the _called service_).
A malicious actor can use the calling service to alter resources in another service by using permissions that they normally would not have.

AWS provides service principals with managed access to resources on your account to help you protect your resources' security. We recommend using the `aws:SourceAccount` global condition context key in your resource
policies. These keys limit the permissions that Amazon Chime gives another service to that resource.

The following example shows an S3 bucket policy that uses the `aws:SourceAccount` global condition context key in the configured `CallDetailRecords` S3 bucket to help prevent the confused
deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`AmazonChimeAclCheck668426`",
 "Effect": "Allow",
 "Principal": {
 "Service": "chime.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`your-cdr-bucket`"
 },
 {
 "Sid": "`AmazonChimeWrite668426`",
 "Effect": "Allow",
 "Principal": {
 "Service": "chime.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`your-cdr-bucket`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "`bucket-owner-full-control`",
 "aws:SourceAccount": "`112233446677`"
 }
 }
 }
 ]
}`

```
