# Grant IAM permissions for

EC2 Instance Connect

To connect to an instance using EC2 Instance Connect, you must create an IAM policy that
grants your users permissions for the following actions and condition:

- `ec2-instance-connect:SendSSHPublicKey` action – Grants
  permission to push the public key to an instance.
- `ec2:osuser` condition – Specifies the name of the OS user
  that can push the public key to an instance. Use the default username for the
  AMI that you used to launch the instance. The default username for AL2023 and
  Amazon Linux 2 is `ec2-user`, and for Ubuntu it's `ubuntu`.
- `ec2:DescribeInstances` action – Required when using the EC2
  console because the wrapper calls this action. Users might already have
  permission to call this action from another policy.
- `ec2:DescribeVpcs` action – Required when connecting to an
  IPv6 address.
  Consider restricting access to specific EC2 instances. Otherwise, all IAM principals
  with permission for the `ec2-instance-connect:SendSSHPublicKey` action can
  connect to all EC2 instances. You can restrict access by specifying resource ARNs or by
  using resource tags as [condition keys](../../../service-authorization/latest/reference/list_amazonec2instanceconnect.md#amazonec2instanceconnect-policy-keys "../../../service-authorization/latest/reference/list_amazonec2instanceconnect.md#amazonec2instanceconnect-policy-keys").

For more information, see [Actions, resources, and condition keys for Amazon EC2 Instance Connect](../../../service-authorization/latest/reference/list_amazonec2instanceconnect.md "../../../service-authorization/latest/reference/list_amazonec2instanceconnect.md").

For information about creating IAM policies, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md")
in the _IAM User Guide_.

## Allow

users to connect to specific instances

The following IAM policy grants permission to connect to specific instances,
identified by their resource ARNs.

In the following example IAM policy, the following actions and condition are
specified:

- The `ec2-instance-connect:SendSSHPublicKey` action grants users
  permission to connect to two instances, specified by the resource ARNs. To
  grant users permission to connect to _all_
  EC2 instances, replace the resource ARNs with the `*`
  wildcard.
- The `ec2:osuser` condition grants permission to connect to the
  instances only if the `ami-username` is specified
  when connecting.
- The `ec2:DescribeInstances` action is specified to grant
  permission to users who will use the console to connect to your instances.
  If your users will only use an SSH client to connect to your instances, you
  can omit `ec2:DescribeInstances`. Note that the
  `ec2:Describe*` API actions do not support resource-level
  permissions. Therefore, the `*` wildcard is necessary in the
  `Resource` element.
- The `ec2:DescribeVpcs` action is specified to grant permission
  to users who will use the console to connect to your instances using an IPv6
  address. If your users will only use a public IPv4 address, you can omit
  `ec2:DescribeVpcs`. Note that the `ec2:Describe*`
  API actions do not support resource-level permissions. Therefore, the
  `*` wildcard is necessary in the `Resource`
  element.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "ec2-instance-connect:SendSSHPublicKey",
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`i-1234567890abcdef0`",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`i-0598c7d356eba48d7`"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:osuser": "`ami-username`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to connect to instances with specific tags

Attribute-based access control (ABAC) is an authorization strategy that defines
permissions based on tags that can be attached to users and AWS resources. You can
use resource tags to control access to an instance. For more information about using
tags to control access to your AWS resources, see [Controlling access to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources") in the _IAM User Guide_.

In the following example IAM policy, the
`ec2-instance-connect:SendSSHPublicKey` action grants users
permission to connect to any instance (indicated by the `*` wildcard in
the resource ARN) on condition that the instance has a resource tag with
key=`tag-key` and value=`tag-value`.

The `ec2:DescribeInstances` action is specified to grant permission to
users who will use the console to connect to your instances. If your users will use
only an SSH client to connect to your instances, you can omit
`ec2:DescribeInstances`. Note that the `ec2:Describe*` API
actions do not support resource-level permissions. Therefore, the `*`
wildcard is necessary in the `Resource` element.

The `ec2:DescribeVpcs` action is specified to grant permission to users
who will use the console to connect to your instances using an IPv6 address. If your
users will only use a public IPv4 address, you can omit
`ec2:DescribeVpcs`. Note that the `ec2:Describe*` API
actions do not support resource-level permissions. Therefore, the `*`
wildcard is necessary in the `Resource` element.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "ec2-instance-connect:SendSSHPublicKey",
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/`tag-key`": "`tag-value`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*"
 }
 ]
}`

```
