# Using access points in IAM policies

You can use an IAM policy to enforce that a specific NFS client, identified by its IAM
role, can only access a specific access point. To do this, you use the
`elasticfilesystem:AccessPointArn` IAM condition key. The
`AccessPointArn` is the Amazon Resource Name (ARN) of the access point
that the file system is mounted with.

Following is an example of a file system policy that allows the IAM role
`app1` to access the file system using access point
`fsap-01234567`. The policy also allows `app2` to use the file
system using access point `fsap-89abcdef`.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "MyFileSystemPolicy",
 "Statement": [
 {
 "Sid": "App1Access",
 "Effect": "Allow",
 "Principal": { "AWS": "arn:aws:iam::111122223333:role/app1" },
 "Action": [
 "elasticfilesystem:ClientMount",
 "elasticfilesystem:ClientWrite"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`111122223333`:file-system/*",
 "Condition": {
 "StringEquals": {
 "elasticfilesystem:AccessPointArn" : "arn:aws:elasticfilesystem:us-east-1:222233334444:access-point/fsap-01234567"
 }
 }
 },
 {
 "Sid": "App2Access",
 "Effect": "Allow",
 "Principal": { "AWS": "arn:aws:iam::111122223333:role/app2" },
 "Action": [
 "elasticfilesystem:ClientMount",
 "elasticfilesystem:ClientWrite"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`111122223333`:file-system/*",
 "Condition": {
 "StringEquals": {
 "elasticfilesystem:AccessPointArn" : "arn:aws:elasticfilesystem:us-east-1:222233334444:access-point/fsap-89abcdef"
 }
 }
 }
 ]
}`

```
