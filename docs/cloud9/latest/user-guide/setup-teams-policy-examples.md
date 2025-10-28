AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Customer managed policy examples for teams using

AWS Cloud9

The following are some examples of policies that you can use to restrict the environments
that users in a group can create in an AWS account.

- [Prevent users in a group
  from creating environments](#setup-teams-policy-examples-prevent-environments "#setup-teams-policy-examples-prevent-environments")
- [Prevent users in a
  group from creating EC2 environments](#setup-teams-policy-examples-prevent-ec2-environments "#setup-teams-policy-examples-prevent-ec2-environments")
- [Allow users in a group
  to create EC2 environments only with specific Amazon EC2 instance types](#setup-teams-policy-examples-specific-instance-types "#setup-teams-policy-examples-specific-instance-types")
- [Allow users in a group
  to create only a single EC2 environment per AWS Region](#setup-teams-policy-examples-single-ec2-environment "#setup-teams-policy-examples-single-ec2-environment")

## Prevent users in a group

from creating environments

The following customer managed policy, when attached to an AWS Cloud9 users group, prevents
those users from creating environments in an AWS account. This is useful if you want an
administrator user in your AWS account to manage creating environments. Otherwise, users in
an AWS Cloud9 users group do this.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "cloud9:CreateEnvironmentEC2",
 "cloud9:CreateEnvironmentSSH"
 ],
 "Resource": "*"
 }
 ]
}`

```

The preceding customer managed policy explicitly overrides `"Effect":
 "Allow"` for `"Action": "cloud9:CreateEnvironmentEC2"` and
`"cloud9:CreateEnvironmentSSH"` on `"Resource": "*"` in the
`AWSCloud9User` managed policy that's already attached to the AWS Cloud9 users
group.

## Prevent users in a

group from creating EC2 environments

The following customer managed policy, when attached to an AWS Cloud9 users group, prevents
those users from creating EC2 environments in an AWS account. This is useful if you want an
administrator user in your AWS account to manage creating EC2 environments. Otherwise, users
in an AWS Cloud9 users group do this. This assumes you didn't also attach a policy that prevents
users in that group from creating SSH environments. Otherwise, those users can't create
environments.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "cloud9:CreateEnvironmentEC2",
 "Resource": "*"
 }
 ]
}`

```

The preceding customer managed policy explicitly overrides `"Effect":
 "Allow"` for `"Action": "cloud9:CreateEnvironmentEC2"` on
`"Resource": "*"` in the `AWSCloud9User` managed policy that's
already attached to the AWS Cloud9 users group.

## Allow users in a group

to create EC2 environments only with specific Amazon EC2 instance types

The following customer managed policy, when attached to an AWS Cloud9 users group, allows
users in the user group to create EC2 environments that only use instance types starting with
`t2` in an AWS account. This policy assumes you didn't also attach a policy
that prevents users in that group from creating EC2 environments. Otherwise, those users can't
create EC2 environments.

You can replace `"t2.*"` in the following policy with a different instance
class (for example, `"m4.*"`). Or, you can restrict it to multiple instance
classes or instance types (for example, `[ "t2.*", "m4.*" ]` or `[
 "t2.micro", "m4.large" ]`).

For an AWS Cloud9 users group, detach the `AWSCloud9User` managed policy from the
group. Then, add the following customer managed policy in its place. If you don't detach the
`AWSCloud9User` managed policy, the following customer managed policy will have
no effect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloud9:CreateEnvironmentSSH",
 "cloud9:GetUserPublicKey",
 "cloud9:UpdateUserSettings",
 "cloud9:GetUserSettings",
 "iam:GetUser",
 "iam:ListUsers",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "cloud9:CreateEnvironmentEC2",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "cloud9:InstanceType": "t2.*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloud9:DescribeEnvironmentMemberships"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "Null": {
 "cloud9:UserArn": "true",
 "cloud9:EnvironmentId": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "cloud9.amazonaws.com"
 }
 }
 }
 ]
}`

```

The preceding customer managed policy also allows those users to create SSH environments.
To prevent those users from creating SSH environments altogether, remove
`"cloud9:CreateEnvironmentSSH",` from the preceding customer managed
policy.

## Allow users in a group

to create only a single EC2 environment in each AWS Region

The following customer managed policy, when attached to an AWS Cloud9 users group, allows
each of those users to create a maximum of one EC2 environment in each AWS Region that AWS Cloud9 is
available in. This is done by restricting the name of the environment to one specific name in that
AWS Region. In this example, the environment is restricted to
`my-demo-environment`.

###### Note

AWS Cloud9 doesn't enable restricting environments to specific AWS Regions from being
created. AWS Cloud9 also doesn't enable restricting the overall number of environments that can
be created. The only exception is published [service
limits](limits.md "limits.md").

For an AWS Cloud9 users group, detach the `AWSCloud9User` managed policy from the
group, and then add the following customer managed policy in its place. If you don't detach
the `AWSCloud9User` managed policy, the following customer managed policy has no
effect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloud9:CreateEnvironmentSSH",
 "cloud9:GetUserPublicKey",
 "cloud9:UpdateUserSettings",
 "cloud9:GetUserSettings",
 "iam:GetUser",
 "iam:ListUsers",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloud9:CreateEnvironmentEC2"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloud9:EnvironmentName": "my-demo-environment"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloud9:DescribeEnvironmentMemberships"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "Null": {
 "cloud9:UserArn": "true",
 "cloud9:EnvironmentId": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "cloud9.amazonaws.com"
 }
 }
 }
 ]
}`

```

The preceding customer managed policy allows those users to create SSH environments. To
prevent those users from creating SSH environments altogether, remove
`"cloud9:CreateEnvironmentSSH",` from the preceding customer managed
policy.

For more examples, see [Customer managed
policy examples](security-iam.md#auth-and-access-control-customer-policies-examples "security-iam.md#auth-and-access-control-customer-policies-examples").
