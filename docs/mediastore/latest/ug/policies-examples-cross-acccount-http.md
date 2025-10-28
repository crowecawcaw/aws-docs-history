End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example container policy: Cross-account read access—HTTP enabled

This example policy allows users to retrieve an object through an HTTP request. It
allows this access to authenticated users with cross-account access. The object is
not required to be hosted on a server with an SSL/TLS certificate:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccountReadOverHttpOrHttps",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`333333333333`:root"
 },
 "Action": [
 "mediastore:GetObject",
 "mediastore:DescribeObject"
 ],
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
