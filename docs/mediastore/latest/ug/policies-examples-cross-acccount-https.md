End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example container policy: Cross-account read access over HTTPS

This example policy allows access to the `GetObject` and
`DescribeObject` operations on any object (as specified by
the \* at the end of the resource path) that is owned by root user user of the specified
<other acct number>. It specifies that this access has the condition of requiring
HTTPS for the operations:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccountReadOverHttps",
 "Effect": "Allow",
 "Action": [
 "mediastore:GetObject",
 "mediastore:DescribeObject"
 ],
 "Principal": {
 "AWS": "arn:aws:iam::`333333333333`:root"
 },
 "Resource": "arn:aws:mediastore:`us-east-2`:`333333333333`:container/`<container name>`/*",
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "true"
 }
 }
 }
 ]
}`

```
