Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing access to data sharing API operations with IAM

policies

To control the access to the data sharing API operations, use IAM action-based
policies. For information about how to manage IAM policies, see [Managing
IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the _IAM User Guide_.

For information on the permissions required to use the data sharing API operations, see
[Permissions
required to use the data sharing API operations](../mgmt/redshift-iam-access-control-identity-based.md "../mgmt/redshift-iam-access-control-identity-based.md") in the
_Amazon Redshift Management Guide_.

To make cross-account data sharing more secure, you can use a conditional key
`ConsumerIdentifier` for the `AuthorizeDataShare` and
`DeauthorizeDataShare` API operations. By doing this, you can explicitly
control which AWS accounts can make calls to the two API operations.

You can deny authorizing or deauthorizing data sharing for any consumer that isn't
your own account. To do so, specify the AWS account number in the IAM policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Deny",
 "Action": [
 "redshift:AuthorizeDataShare",
 "redshift:DeauthorizeDataShare"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "redshift:ConsumerIdentifier": "555555555555"
 }
 }
 }
 ]
}`

```

You can allow a producer with a DataShareArn `testshare2` to
explicitly share with a consumer with an AWS account of 111122223333 in the
IAM policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "redshift:AuthorizeDataShare",
 "redshift:DeauthorizeDataShare"
 ],
 "Resource": "arn:aws:redshift:us-east-1:666666666666:datashare:af06285e-8a45-4ee9-b598-648c218c8ff1/testshare2",
 "Condition": {
 "StringEquals": {
 "redshift:ConsumerIdentifier": "111122223333"
 }
 }
 }
 ]
}`

```
