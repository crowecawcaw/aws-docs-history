Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up permissions to

view schedule query history

To allow users to view schedule query history, edit the IAM role (that is specified
with the schedule) **Trust relationships** to add permissions.

The following is an example of a trust policy in an IAM role that allows the IAM
user `myIAMusername` to view schedule query history. Instead of
allowing an IAM user `sts:AssumeRole` permission you can choose to allow an
IAM role this permission.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "redshift.amazonaws.com",
 "redshift-serverless.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Sid": "AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/`myIAMusername`"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
