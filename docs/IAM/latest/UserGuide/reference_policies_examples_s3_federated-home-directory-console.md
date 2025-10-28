# Amazon S3:

Allows federated users access to their Amazon S3 home directory, programmatically and in the
console

This example shows how you might create an identity-based policy that allows federated principals to access their own home directory bucket
object in S3. The home directory is a bucket that includes a `home` folder and
folders for individual federated
principals. This policy defines permissions for programmatic and console access. To use this policy, replace the `italicized placeholder text` in the example policy with your own information.
Then, follow the directions in [create a policy](access_policies_create.md "access_policies_create.md") or [edit a policy](access_policies_manage-edit.md "access_policies_manage-edit.md").

The `${aws:userid}` variable in this policy resolves to
`role-id:specified-name`. The `role-id` part of the federated principal
ID is a unique identifier assigned to the federated principal's role during creation. For more
information, see [Unique identifiers](reference_identifiers.md#identifiers-unique-ids "reference_identifiers.md#identifiers-unique-ids"). The `specified-name` is the [RoleSessionName parameter](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md#API_AssumeRoleWithWebIdentity_RequestParameters "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md#API_AssumeRoleWithWebIdentity_RequestParameters") passed to the `AssumeRoleWithWebIdentity`
request when the federated principal assumed their role.

You can view the role ID using the AWS CLI command `aws iam get-role --role-name
 `specified-name``. For example, imagine that you
 specify the friendly name `John`and the CLI returns the role ID
`AROAXXT2NJT7D3SIQN7Z6`. In this case, the federated principal's user ID is
 `AROAXXT2NJT7D3SIQN7Z6:John`. This policy then allows the federated principal John
 to access the Amazon S3 bucket with prefix `AROAXXT2NJT7D3SIQN7Z6:John`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3ConsoleAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetAccountPublicAccessBlock",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation",
 "s3:GetBucketPolicyStatus",
 "s3:GetBucketPublicAccessBlock",
 "s3:ListAccessPoints",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ListObjectsInBucket",
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringLike": {
 "s3:prefix": [
 "",
 "home/",
 "home/${aws:userid}/*"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/home/${aws:userid}",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/home/${aws:userid}/*"
 ]
 }
 ]
}`

```
