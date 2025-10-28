# Example bucket

policies for directory buckets

This section provides example directory bucket policies. To use these policies, replace
the `user input placeholders` with your own
information.

The following example bucket policy allows AWS account ID
`111122223333` to use the
`CreateSession` API operation with the default `ReadWrite` session
for the specified directory bucket. This policy grants access to the Zonal endpoint (object
level) API operations.

###### Example – Bucket policy to allow `CreateSession` calls with the default

`ReadWrite` session

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadWriteAccess",
 "Effect": "Allow",
 "Resource": "arn:aws:s3express:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-bucket--usw2-az1--x-s3`",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root"
 ]
 },
 "Action": [
 "s3express:CreateSession"
 ]
 }
 ]
}`

```

###### Example – Bucket policy to allow `CreateSession` calls with a

`ReadOnly` session

The following example bucket policy allows AWS account ID
`111122223333` to use the
`CreateSession` API operation. This policy uses the
`s3express:SessionMode` condition key with the `ReadOnly`
value to set a read-only session.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadOnlyAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`111122223333`"
 },
 "Action": "s3express:CreateSession",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "s3express:SessionMode": "ReadOnly"
 }
 }
 }
 ]
}`

```

###### Example – Bucket policy to allow cross-account access for `CreateSession`

calls

The following example bucket policy allows AWS account ID
`111122223333` to use the
`CreateSession` API operation for the specified directory bucket that's
owned by AWS account ID
`444455556666`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccount",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "s3express:CreateSession"
 ],
 "Resource": "arn:aws:s3express:`us-west-2`:`444455556666`:bucket/`amzn-s3-demo-bucket--usw2-az1--x-s3`"
 }
 ]
}`

```
