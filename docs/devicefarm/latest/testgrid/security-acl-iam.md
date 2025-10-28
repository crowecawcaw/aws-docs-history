# Access control and IAM

Be aware of the following when you use the desktop browser testing feature:

- Your AWS access and secret keys are used for all actions with the SDK and CLI.
- URLs generated with the `CreateTestGridUrl` API call can be used to create sessions on your
  behalf until the URL expires.
- Artifact URLs can be viewed by anyone with the limited lifetime URL.
  The desktop browser testing feature is integrated with AWS Identity and Access Management (IAM), which you can use to:

- Create users and groups in your AWS account.
- Easily share your AWS resources between the users in your AWS account.
- Assign unique security credentials to each user.
- Control each user's access to services and resources.
- Get a single bill for all users in your AWS account.
  IAM is used to restrict access to operations and resources. The following example IAM policy grants the
  user access only to Device Farm resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "devicefarm:*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following IAM Policy allows access to Device Farm resources as well as the
required permissions for VPC connection configuration:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "devicefarm:*",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/testgrid.devicefarm.amazonaws.com/AWSServiceRoleForDeviceFarmTestGrid",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "testgrid.devicefarm.amazonaws.com"
 }
 }
 }
 ]
}`

```

The following IAM policy allows the user to create URLs with the `CreateTestGridUrl` API
call:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "devicefarm:CreateTestGridUrl"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

For more information about IAM, see the following:

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Getting started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md")
- [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")
