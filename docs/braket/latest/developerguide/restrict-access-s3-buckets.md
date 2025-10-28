# Restrict user access to certain S3 buckets

To restrict access for certain users to specific Amazon S3 buckets, you can add a deny
policy to a specific role, user, or group.

The following example restricts permissions to retrieve and place objects into a
specific S3 bucket
(`arn:aws:s3:::amazon-braket-us-east-1-123456789012-Alice`) and also
restricts the listing of those objects.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "s3:ListBucket"
 ],
 "NotResource": [
 "arn:aws:s3:::amazon-braket-us-east-1-123456789012-Alice"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "s3:GetObject"
 ],
 "NotResource": [
 "arn:aws:s3:::amazon-braket-us-east-1-123456789012-Alice/*"
 ]
 }
 ]
}`

```

To restrict access to the bucket for a certain notebook instance, you can add the
preceding policy to the notebook execution role.
