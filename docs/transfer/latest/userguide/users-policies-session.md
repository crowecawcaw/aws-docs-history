# Creating a session policy for an Amazon S3

bucket

A _session policy_ is an AWS Identity and Access Management (IAM) policy that restricts
users to certain portions of an Amazon S3 bucket. It does so by evaluating access in real
time.

###### Note

Session policies are only used with Amazon S3. For Amazon EFS, you use POSIX file
permissions to limit access.

You can use a session policy when you need to give the same access to a group of users
to a particular portion of your Amazon S3 bucket. For example, a group of users might need
access to only the `home` directory. That group of users share the same IAM
role.

###### Note

The maximum length of a session policy is 2048 characters. For more details, see
the [Policy request parameter](../APIReference/API_CreateUser.md#API_CreateUser_RequestSyntax "../APIReference/API_CreateUser.md#API_CreateUser_RequestSyntax") for the `CreateUser` action in the
_API reference_.

To create a session policy, use the following policy variables in your IAM
policy:

- `${transfer:HomeBucket}`
- `${transfer:HomeDirectory}`
- `${transfer:HomeFolder}`
- `${transfer:UserName}`

###### Important

You can't use the preceding variables in Managed Policies. Nor can you use
them as policy variables in an IAM role definition. You create these variables in
an IAM policy and supply them directly when setting up your user. Also, you
can't use the `${aws:Username}` variable in this session policy.
This variable refers to an IAM user name and not the username required by
AWS Transfer Family.

## Example session policy

The following code shows an example session policy.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowListingOfUserFolder",
 "Action": [
 "s3:ListBucket"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3:::${transfer:HomeBucket}"
 ],
 "Condition": {
 "StringLike": {
 "s3:prefix": [
 "${transfer:HomeFolder}/*",
 "${transfer:HomeFolder}"
 ]
 }
 }
 },
 {
 "Sid": "HomeDirObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObjectVersion",
 "s3:DeleteObject",
 "s3:GetObjectVersion",
 "s3:GetObjectACL",
 "s3:PutObjectACL"
 ],
 "Resource": "arn:aws:s3:::${transfer:HomeDirectory}/*"
 }
 ]
}`

```

###### Note

The preceding policy example assumes that users have their home directories set to include a trailing slash, to signify that it is a directory.
If, on the other hand, you set a user's `HomeDirectory` without the trailing slash, then you should include it as part of your policy.

In the previous example policy, note the use of the
`transfer:HomeFolder`, `transfer:HomeBucket`, and
`transfer:HomeDirectory` policy parameters. These parameters are set
for the `HomeDirectory` that is configured for the user, as described in
[HomeDirectory](../APIReference/API_CreateUser.md#TransferFamily-CreateUser-request-HomeDirectory "../APIReference/API_CreateUser.md#TransferFamily-CreateUser-request-HomeDirectory") and
[Implementing your API Gateway method](authentication-api-gateway.md#authentication-api-method "authentication-api-gateway.md#authentication-api-method").
These parameters have the following definitions:

- The `transfer:HomeBucket` parameter is replaced with the first component of
  `HomeDirectory`.
- The `transfer:HomeFolder` parameter is replaced with the remaining portions of the
  `HomeDirectory` parameter.
- The `transfer:HomeDirectory` parameter has the leading forward slash
  (`/`) removed so that it can be used as part of an S3 Amazon
  Resource Name (ARN) in a `Resource` statement.

###### Note

If you are using logical directories—that is, the user's `homeDirectoryType` is `LOGICAL`—these policy parameters (`HomeBucket`,
`HomeDirectory`, and `HomeFolder`) are not supported.

For example, assume that the `HomeDirectory` parameter that is
configured for the Transfer Family user is `/home/bob/amazon/stuff/`.

- `transfer:HomeBucket` is set to `/home`.
- `transfer:HomeFolder` is set to `/bob/amazon/stuff/`.
- `transfer:HomeDirectory` becomes `home/bob/amazon/stuff/`.

The first `"Sid"` allows the user to list all directories starting from
`/home/bob/amazon/stuff/`.

The second `"Sid"` limits the user'`put` and
`get` access to that same path,
`/home/bob/amazon/stuff/`.

With the preceding policy in place, when a user logs in, they can access only
objects in their home directory. At connection time, AWS Transfer Family replaces these
variables with the appropriate values for the user. Doing this makes it easier to
apply the same policy documents to multiple users. This approach reduces the
overhead of IAM role and policy management for managing your users' access to
your Amazon S3 bucket.

You can also use a session policy to customize access for each of your users based
on your business requirements. For more information, see [Permissions for AssumeRole, AssumeRoleWithSAML, and
AssumeRoleWithWebIdentity](../../../IAM/latest/UserGuide/id_credentials_temp_control-access_assumerole.md "../../../IAM/latest/UserGuide/id_credentials_temp_control-access_assumerole.md") in the
_IAM User Guide_.

###### Note

AWS Transfer Family stores the policy JSON, instead of the Amazon Resource Name (ARN) of
the policy. So, when you change the policy in the IAM console, you need to
return to AWS Transfer Family console and update your users with the latest policy
contents. You can update the user on the **Policy Info** tab in
the **User configuration** section.

If you are using the AWS CLI, you can use the following command to update the
policy.

```
aws transfer update-user --server-id `server` --user-name `user` --policy \
   "$(aws iam get-policy-version --policy-arn `policy` --version-id `version` --output json)"
```

## Nested substitutions for session

policies

Nested substitutions are not performed in Transfer Family session policies. Session policies
can use nested variables, such as `${transfer:HomeDirectory}`. When the
policy is processed, the outer variable (e.g.,
`${transfer:HomeDirectory}`) might get replaced with a value that
contains another variable (e.g.,
{`amzn-s3-demo-bucket:/$(transfer:UserName}`). However, the nested
variable is not further substituted with the actual username (e.g.,
**johndoe**).

This means that when creating session policies for Transfer Family, you need to account for
this behavior and ensure that the policy structure and variable usage are designed
accordingly. The nested variables may not be resolved as expected, and the policy
might not grant the intended permissions. It's important to thoroughly test and
validate the session policies to ensure they work as expected. This behavior is a
key consideration when implementing access control and permissions for your Transfer Family
environment.

One solution to this issue is to use the actual Amazon S3 bucket name in your session
policy. So, for example, rather than specifying
`${transfer:HomeDirectory}` in your session policy, use the
following, where amzn-s3-demo-bucket is your actual bucket:
`${amzn-s3-demo-bucket/transfer:UserName}`.
