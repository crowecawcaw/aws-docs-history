# Example policies to control access the Amazon EC2 API

You can use IAM policies to grant users the permissions required to work with Amazon EC2.
For step-by-step directions, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in
the _IAM User Guide_.

The following examples show policy statements that you could use to grant users permissions
to use Amazon EC2. These policies are designed for requests that are made using the AWS CLI or an
AWS SDK. In the following examples, replace each `user input placeholder`
with your own information.

###### Examples

- [Read-only access](#iam-example-read-only "#iam-example-read-only")
- [Restrict access to a specific Region](#iam-example-region "#iam-example-region")
- [Work with instances](#iam-example-instances "#iam-example-instances")
- [Launch instances (RunInstances)](#iam-example-runinstances "#iam-example-runinstances")
- [Work with Spot Instances](#iam-example-spot-instances "#iam-example-spot-instances")
- [Work with Reserved Instances](#iam-example-reservedinstances "#iam-example-reservedinstances")
- [Tag resources](#iam-example-taggingresources "#iam-example-taggingresources")
- [Work with IAM roles](#iam-example-iam-roles "#iam-example-iam-roles")
- [Work with route
  tables](#iam-example-route-tables "#iam-example-route-tables")
- [Allow a specific
  instance to view resources in other AWS services](#iam-example-source-instance "#iam-example-source-instance")
- [Work with launch
  templates](#iam-example-launch-templates "#iam-example-launch-templates")
- [Work with instance
  metadata](#iam-example-instance-metadata "#iam-example-instance-metadata")
- [Work with Amazon EBS volumes and snapshots](#iam-example-ebs "#iam-example-ebs")
  For example policies for working in the Amazon EC2 console, see [Example policies to control access to the Amazon EC2 console](iam-policies-ec2-console.md "iam-policies-ec2-console.md").

## Example: Read-only access

The following policy grants users permissions to use all Amazon EC2 API actions whose names
begin with `Describe`. The `Resource` element uses a wildcard to
indicate that users can specify all resources with these API actions. The \* wildcard is
also necessary in cases where the API action does not support resource-level
permissions. For more information about which ARNs you can use with which Amazon EC2 API
actions, see [Actions, resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md").

Users don't have permission to perform any actions on the resources (unless
another statement grants them permission to do so) because they're denied
permission to use API actions by default.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:Describe*",
 "Resource": "*"
 }
 ]
}`

```

## Example: Restrict access to a specific Region

The following policy denies users permission to use all Amazon EC2 API actions unless the
Region is Europe (Frankfurt). It uses the global condition key
`aws:RequestedRegion`, which is supported by all Amazon EC2 API actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ec2:*",
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:RequestedRegion": "eu-central-1"
 }
 }
 }
 ]
}`

```

Alternatively, you can use the condition key `ec2:Region`, which is specific to
Amazon EC2 and is supported by all Amazon EC2 API actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ec2:*",
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "ec2:Region": "eu-central-1"
 }
 }
 }
 ]
}`

```

## Work with instances

###### Examples

- [Example: Describe, launch, stop, start, and terminate
  all instances](#iam-example-instances-all "#iam-example-instances-all")
- [Example: Describe all instances, and stop, start,
  and terminate only particular instances](#iam-example-instances-specific "#iam-example-instances-specific")

### Example: Describe, launch, stop, start, and terminate

all instances

The following policy grants users permissions to use the API actions specified in the
`Action` element. The `Resource` element uses a \* wildcard
to indicate that users can specify all resources with these API actions. The \*
wildcard is also necessary in cases where the API action does not support
resource-level permissions. For more information about which ARNs you can use with
which Amazon EC2 API actions, see [Actions, resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md").

The users don't have permission to use any other API actions (unless
another statement grants them permission to do so) because users are denied
permission to use API actions by default.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeImages",
 "ec2:DescribeKeyPairs",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeAvailabilityZones",
 "ec2:RunInstances",
 "ec2:TerminateInstances",
 "ec2:StopInstances",
 "ec2:StartInstances"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Example: Describe all instances, and stop, start,

and terminate only particular instances

The following policy allows users to describe all instances, to start and
stop only instances i-1234567890abcdef0 and i-0598c7d356eba48d7,
and to terminate only instances in the `us-east-1`
Region, with the resource tag "`purpose=test`".

The first statement uses a \* wildcard for the `Resource` element to indicate
that users can specify all resources with the action; in this case, they can list
all instances. The \* wildcard is also necessary in cases where the API action does
not support resource-level permissions (in this case,
`ec2:DescribeInstances`). For more information about which ARNs you
can use with which Amazon EC2 API actions, see [Actions, resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md").

The second statement uses resource-level permissions for the
`StopInstances` and `StartInstances` actions. The
specific instances are indicated by their ARNs in the `Resource`
element.

The third statement allows users to terminate all instances in the
`us-east-1` Region that belong to the
specified AWS account, but only where the instance has the tag
`"purpose=test"`. The `Condition` element
qualifies when the policy statement is in effect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:DescribeInstances",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:StopInstances",
 "ec2:StartInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1:`111122223333`:instance/i-1234567890abcdef0",
 "arn:aws:ec2:us-east-1:`111122223333`:instance/i-0598c7d356eba48d7"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "ec2:TerminateInstances",
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:instance/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/purpose": "test"
 }
 }
 }

 ]
}`

```

## Launch instances (RunInstances)

The [RunInstances](../APIReference/API_RunInstances.md "../APIReference/API_RunInstances.md")
API action launches one or more On-Demand Instances or one or more Spot Instances. `RunInstances` requires an AMI and
creates an instance. Users can specify a key pair and security group in the request. Launching
into a VPC requires a subnet, and creates a network interface. Launching from an Amazon EBS-backed
AMI creates a volume. Therefore, the user must have permissions to use these Amazon EC2 resources.
You can create a policy statement that requires users to specify an optional parameter on
`RunInstances`, or restricts users to particular values for a parameter.

For more information about the resource-level permissions that are required to
launch an instance, see [Actions, resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md").

By default, users don't have permissions to describe, start, stop, or terminate the
resulting instances. One way to grant the users permission to manage the resulting
instances is to create a specific tag for each instance, and then create a statement
that enables them to manage instances with that tag. For more information, see [Work with instances](#iam-example-instances "#iam-example-instances").

###### Resources

- [AMIs](#iam-example-runinstances-ami "#iam-example-runinstances-ami")
- [Instance types](#iam-example-runinstances-instance-type "#iam-example-runinstances-instance-type")
- [Subnets](#iam-example-runinstances-subnet "#iam-example-runinstances-subnet")
- [EBS volumes](#iam-example-runinstances-volumes "#iam-example-runinstances-volumes")
- [Tags](#iam-example-runinstances-tags "#iam-example-runinstances-tags")
- [Tags in a launch template](#iam-example-tags-launch-template "#iam-example-tags-launch-template")
- [Elastic GPUs](#iam-example-runinstances-egpu "#iam-example-runinstances-egpu")
- [Launch templates](#iam-example-runinstances-launch-templates "#iam-example-runinstances-launch-templates")

### AMIs

The following policy allows users to launch instances using only the specified AMIs,
`ami-9e1670f7` and `ami-45cf5c3c`. The users can't
launch an instance using other AMIs (unless another statement grants the
users permission to do so).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`::image/ami-9e1670f7",
 "arn:aws:ec2:`us-east-1`::image/ami-45cf5c3c",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:key-pair/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*"
 ]
 }
 ]
}`

```

Alternatively, the following policy allows users to launch instances from all AMIs owned
by Amazon, or certain trusted and verified partners. The `Condition` element of the first statement tests
whether `ec2:Owner` is `amazon`. The users can't
launch an instance using other AMIs (unless another statement grants the
users permission to do so).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`::image/ami-*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:Owner": "amazon"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:key-pair/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*"
 ]
 }
 ]
}`

```

### Instance types

The following policy allows users to launch instances using only the
`t2.micro` or `t2.small` instance type, which you
might do to control costs. The users can't launch larger instances because
the `Condition` element of the first statement tests whether
`ec2:InstanceType` is either `t2.micro` or
`t2.small`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:InstanceType": ["t2.micro", "t2.small"]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`::image/ami-*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:key-pair/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*"
 ]
 }
 ]
}`

```

Alternatively, you can create a policy that denies users permissions to launch any
instances except `t2.micro` and `t2.small` instance
types.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*"
 ],
 "Condition": {
 "StringNotEquals": {
 "ec2:InstanceType": ["t2.micro", "t2.small"]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`::image/ami-*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:key-pair/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*"
 ]
 }
 ]
}`

```

### Subnets

The following policy allows users to launch instances using only the specified subnet,
`subnet-`12345678``. The group can't
launch instances into any another subnet (unless another statement grants the users
permission to do so).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/subnet-`12345678`",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-1`::image/ami-*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:key-pair/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*"
 ]
 }
 ]
}`

```

Alternatively, you could create a policy that denies users permissions to launch an
instance into any other subnet. The statement does this by denying permission to
create a network interface, except where subnet
`subnet-`12345678`` is specified. This
denial overrides any other policies that are created to allow launching instances
into other subnets.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*"
 ],
 "Condition": {
 "ArnNotEquals": {
 "ec2:Subnet": "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/subnet-`12345678`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`::image/ami-*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:key-pair/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*"
 ]
 }
 ]
}`

```

### EBS volumes

The following policy allows users to launch instances only if the EBS
volumes for the instance are encrypted. The user must launch an instance
from an AMI that was created with encrypted snapshots, to ensure that the
root volume is encrypted. Any additional volume that the user attaches to
the instance during launch must also be encrypted.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:*:*:volume/*"
 ],
 "Condition": {
 "Bool": {
 "ec2:Encrypted": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:*::image/ami-*",
 "arn:aws:ec2:*:*:network-interface/*",
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:key-pair/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 }
 ]
}`

```

### Tags

**Tag instances on creation**

The following policy allows users to launch instances and tag the instances during
creation. For resource-creating actions that apply tags, users must have permissions to use
the `CreateTags` action. The second statement uses the
`ec2:CreateAction` condition key to allow users to create tags only in the
context of `RunInstances`, and only for instances. Users cannot tag existing
resources, and users cannot tag volumes using the `RunInstances` request.

For more information, see [Grant permission to tag Amazon EC2 resources during creation](supported-iam-actions-tagging.md "supported-iam-actions-tagging.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:instance/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction" : "RunInstances"
 }
 }
 }
 ]
}`

```

**Tag instances and volumes on creation with specific
tags**

The following policy includes the `aws:RequestTag` condition key that requires users
to tag any instances and volumes that are created by `RunInstances` with the tags
`environment=production` and `purpose=webserver`. If users don't pass these
specific tags, or if they don't specify tags at all, the request fails.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`::image/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:key-pair/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": "production" ,
 "aws:RequestTag/purpose": "webserver"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:*/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction" : "RunInstances"
 }
 }
 }
 ]
}`

```

**Tag instances and volumes on creation with at least one specific
tag**

The following policy uses the `ForAnyValue` modifier on the
`aws:TagKeys` condition to indicate that at least one tag
must be specified in the request, and it must contain the key
`environment` or `webserver`. The tag must be
applied to both instances and volumes. Any tag values can be specified in
the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`::image/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:key-pair/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": ["environment","webserver"]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:*/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction" : "RunInstances"
 }
 }
 }
 ]
}`

```

**If instances are tagged on creation, they must be tagged with a
specific tag**

In the following policy, users do not have to specify tags in the request,
but if they do, the tag must be `purpose=test`. No other tags are
allowed. Users can apply the tags to any taggable resource in the
`RunInstances` request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:*/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/purpose": "test",
 "ec2:CreateAction" : "RunInstances"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "purpose"
 }
 }
 }
 ]
}`

```

To disallow anyone called tag on create for RunInstances

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRun",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1::image/*",
 "arn:aws:ec2:us-east-1:*:subnet/*",
 "arn:aws:ec2:us-east-1:*:network-interface/*",
 "arn:aws:ec2:us-east-1:*:security-group/*",
 "arn:aws:ec2:us-east-1:*:key-pair/*",
 "arn:aws:ec2:us-east-1:*:volume/*",
 "arn:aws:ec2:us-east-1:*:instance/*",
 "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": "ec2:CreateTags",
 "Resource": "*"
 }
 ]
}`

```

Only allow specific tags for spot-instances-request. Surprise inconsistency number 2 comes into play here. Under normal circumstances, specifying no tags will result in Unauthenticated. In the case of spot-instances-request, this policy will not be evaluated if there are no spot-instances-request tags, so a non-tag Spot on Run request will succeed.

### Tags in a launch template

In the following example, users can launch instances, but only if they use a
specific launch template (`lt-09477bcd97b0d310e`). The
`ec2:IsLaunchTemplateResource` condition key prevents users from overriding any
of the resources specified in the launch template. The second part of the statement allows
users to tag instances on creation—this part of the statement is necessary if tags
are specified for the instance in the launch template.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "ec2:LaunchTemplate": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/lt-09477bcd97b0d310e"
 },
 "Bool": {
 "ec2:IsLaunchTemplateResource": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction" : "RunInstances"
 }
 }
 }
 ]
}`

```

### Elastic GPUs

In the following policy, users can launch an instance and specify an
elastic GPU to attach to the instance. Users can launch instances in any Region, but they
can only attach an elastic GPU during a launch in the `us-east-2` Region.

The `ec2:ElasticGpuType` condition key ensures that
instances use either the `eg1.medium` or `eg1.large`
elastic GPU type.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:elastic-gpu/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:Region": "us-east-2",
 "ec2:ElasticGpuType": [
 "eg1.medium",
 "eg1.large"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:*::image/ami-*",
 "arn:aws:ec2:*:`111122223333`:network-interface/*",
 "arn:aws:ec2:*:`111122223333`:instance/*",
 "arn:aws:ec2:*:`111122223333`:subnet/*",
 "arn:aws:ec2:*:`111122223333`:volume/*",
 "arn:aws:ec2:*:`111122223333`:key-pair/*",
 "arn:aws:ec2:*:`111122223333`:security-group/*"
 ]
 }
 ]
}`

```

### Launch templates

In the following example, users can launch instances, but only if they use a
specific launch template (`lt-09477bcd97b0d310e`). Users can override any
parameters in the launch template by specifying the parameters in the
`RunInstances` action.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "ec2:LaunchTemplate": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/lt-09477bcd97b0d310e"
 }
 }
 }
 ]
}`

```

In this example, users can launch instances only if they use a launch template. The
policy uses the `ec2:IsLaunchTemplateResource` condition key to prevent users
from overriding any pre-existing ARNs in the launch template.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "ec2:LaunchTemplate": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*"
 },
 "Bool": {
 "ec2:IsLaunchTemplateResource": "true"
 }
 }
 }
 ]
}`

```

The following example policy allows user to launch instances, but only if they use
a launch template. Users cannot override the subnet and network interface parameters
in the request; these parameters can only be specified in the launch template. The
first part of the statement uses the [NotResource](../../../IAM/latest/UserGuide/reference_policies_elements_notresource.md "../../../IAM/latest/UserGuide/reference_policies_elements_notresource.md") element to allow all other resources except subnets and
network interfaces. The second part of the statement allows the subnet and network
interface resources, but only if they are sourced from the launch template.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "NotResource": ["arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*" ],
 "Condition": {
 "ArnLike": {
 "ec2:LaunchTemplate": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": ["arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*" ],
 "Condition": {
 "ArnLike": {
 "ec2:LaunchTemplate": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*"
 },
 "Bool": {
 "ec2:IsLaunchTemplateResource": "true"
 }
 }
 }
 ]
}`

```

The following example allows users to launch instances only if they use a
launch template, and only if the launch template has the tag
`Purpose=Webservers`. Users cannot override any of the launch
template parameters in the `RunInstances` action.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "NotResource": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*",
 "Condition": {
 "ArnLike": {
 "ec2:LaunchTemplate": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*"
 },
 "Bool": {
 "ec2:IsLaunchTemplateResource": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Purpose": "Webservers"
 }
 }
 }
 ]
}`

```

## Work with Spot Instances

You can use the RunInstances action to create Spot Instance requests, and tag the Spot Instance requests
on create. The resource to specify for RunInstances is
`spot-instances-request`.

The `spot-instances-request` resource is evaluated in the IAM policy as
follows:

- If you don't tag a Spot Instance request on create, Amazon EC2 does not evaluate the
  `spot-instances-request` resource in the RunInstances
  statement.
- If you tag a Spot Instance request on create, Amazon EC2 evaluates the
  `spot-instances-request` resource in the RunInstances
  statement.

Therefore, for the `spot-instances-request` resource, the following rules
apply to the IAM policy:

- If you use RunInstances to create a Spot Instance request and you don't intend to tag
  the Spot Instance request on create, you don’t need to explicitly allow the
  `spot-instances-request` resource; the call will succeed.
- If you use RunInstances to create a Spot Instance request and intend to tag the Spot Instance
  request on create, you must include the `spot-instances-request`
  resource in the RunInstances allow statement, otherwise the call will
  fail.
- If you use RunInstances to create a Spot Instance request and intend to tag the Spot Instance
  request on create, you must specify the `spot-instances-request`
  resource or `*` wildcard in the CreateTags allow statement, otherwise
  the call will fail.

You can request Spot Instances using RunInstances or RequestSpotInstances. The following
example IAM policies apply only when requesting Spot Instances using RunInstances.

**Example: Request Spot Instances using RunInstances**

The following policy allows users to request Spot Instances by using the RunInstances action.
The `spot-instances-request` resource, which is created by RunInstances,
requests Spot Instances.

###### Note

To use RunInstances to create Spot Instance requests, you can omit
`spot-instances-request` from the `Resource` list if you
do not intend to tag the Spot Instance requests on create. This is because Amazon EC2 does not
evaluate the `spot-instances-request` resource in the RunInstances
statement if the Spot Instance request is not tagged on create.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRun",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1::image/*",
 "arn:aws:ec2:us-east-1:*:subnet/*",
 "arn:aws:ec2:us-east-1:*:network-interface/*",
 "arn:aws:ec2:us-east-1:*:security-group/*",
 "arn:aws:ec2:us-east-1:*:key-pair/*",
 "arn:aws:ec2:us-east-1:*:volume/*",
 "arn:aws:ec2:us-east-1:*:instance/*",
 "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
 ]
 }
 ]
}`

```

###### Warning

**NOT SUPPORTED – Example: Deny users permission to request Spot Instances
using RunInstances**

The following policy is not supported for the `spot-instances-request`
resource.

The following policy is meant to give users the permission to launch On-Demand Instances, but deny
users the permission to request Spot Instances. The `spot-instances-request`
resource, which is created by RunInstances, is the resource that requests Spot Instances. The
second statement is meant to deny the RunInstances action for the
`spot-instances-request` resource. However, this condition is not
supported because Amazon EC2 does not evaluate the `spot-instances-request`
resource in the RunInstances statement if the Spot Instance request is not tagged on
create.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRun",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1::image/*",
 "arn:aws:ec2:us-east-1:*:subnet/*",
 "arn:aws:ec2:us-east-1:*:network-interface/*",
 "arn:aws:ec2:us-east-1:*:security-group/*",
 "arn:aws:ec2:us-east-1:*:key-pair/*",
 "arn:aws:ec2:us-east-1:*:volume/*",
 "arn:aws:ec2:us-east-1:*:instance/*"
 ]
 },
 {
 "Sid": "DenySpotInstancesRequestsNOTSUPPORTEDDONOTUSE",
 "Effect": "Deny",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
 }
 ]
}`

```

**Example: Tag Spot Instance requests on create**

The following policy allows users to tag all resources that are created during
instance launch. The first statement allows RunInstances to create the listed resources.
The `spot-instances-request` resource, which is created by RunInstances, is
the resource that requests Spot Instances. The second statement provides a `*`
wildcard to allow all resources to be tagged when they are created at instance
launch.

###### Note

If you tag a Spot Instance request on create, Amazon EC2 evaluates the
`spot-instances-request` resource in the RunInstances statement.
Therefore, you must explicitly allow the `spot-instances-request`
resource for the RunInstances action, otherwise the call will fail.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRun",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1::image/*",
 "arn:aws:ec2:us-east-1:*:subnet/*",
 "arn:aws:ec2:us-east-1:*:network-interface/*",
 "arn:aws:ec2:us-east-1:*:security-group/*",
 "arn:aws:ec2:us-east-1:*:key-pair/*",
 "arn:aws:ec2:us-east-1:*:volume/*",
 "arn:aws:ec2:us-east-1:*:instance/*",
 "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
 ]
 },
 {
 "Sid": "TagResources",
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "*"
 }
 ]
}`

```

**Example: Deny tag on create for Spot Instance requests**

The following policy denies users the permission to tag the resources that are created
during instance launch.

The first statement allows RunInstances to create the listed resources. The
`spot-instances-request` resource, which is created by RunInstances, is
the resource that requests Spot Instances. The second statement provides a `*`
wildcard to deny all resources being tagged when they are created at instance launch. If
`spot-instances-request` or any other resource is tagged on create, the
RunInstances call will fail.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRun",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1::image/*",
 "arn:aws:ec2:us-east-1:*:subnet/*",
 "arn:aws:ec2:us-east-1:*:network-interface/*",
 "arn:aws:ec2:us-east-1:*:security-group/*",
 "arn:aws:ec2:us-east-1:*:key-pair/*",
 "arn:aws:ec2:us-east-1:*:volume/*",
 "arn:aws:ec2:us-east-1:*:instance/*",
 "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
 ]
 },
 {
 "Sid": "DenyTagResources",
 "Effect": "Deny",
 "Action": "ec2:CreateTags",
 "Resource": "*"
 }
 ]
}`

```

###### Warning

**NOT SUPPORTED – Example: Allow creating a Spot Instance request
only if it is assigned a specific tag**

The following policy is not supported for the `spot-instances-request`
resource.

The following policy is meant to grant RunInstances the permission to create a Spot Instance
request only if the request is tagged with a specific tag.

The first statement allows RunInstances to create the listed resources.

The second statement is meant to grant users the permission to create a Spot Instance request
only if the request has the tag `environment=production`. If this
condition is applied to other resources created by RunInstances, specifying no tags
results in an `Unauthenticated` error. However, if no tags are specified
for the Spot Instance request, Amazon EC2 does not evaluate the
`spot-instances-request` resource in the RunInstances statement,
which results in non-tagged Spot Instance requests being created by RunInstances.

Note that specifying another tag other than `environment=production`
results in an `Unauthenticated` error, because if a user tags a Spot Instance
request, Amazon EC2 evaluates the `spot-instances-request` resource in the
RunInstances statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRun",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1::image/*",
 "arn:aws:ec2:us-east-1:*:subnet/*",
 "arn:aws:ec2:us-east-1:*:network-interface/*",
 "arn:aws:ec2:us-east-1:*:security-group/*",
 "arn:aws:ec2:us-east-1:*:key-pair/*",
 "arn:aws:ec2:us-east-1:*:volume/*",
 "arn:aws:ec2:us-east-1:*:instance/*"
 ]
 },
 {
 "Sid": "RequestSpotInstancesOnlyIfTagIsEnvironmentProductionNOTSUPPORTEDDONOTUSE",
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:us-east-1:*:spot-instances-request/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": "production"
 }
 }
 },
 {
 "Sid": "TagResources",
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "*"
 }

 ]
}`

```

**Example: Deny creating a Spot Instance request if it is assigned a
specific tag**

The following policy denies RunInstances the permission to create a Spot Instance request
if the request is tagged with `environment=production`.

The first statement allows RunInstances to create the listed resources.

The second statement denies users the permission to create a Spot Instance request if the
request has the tag `environment=production`. Specifying
`environment=production` as a tag results in an
`Unauthenticated` error. Specifying other tags or specifying no tags will
result in the creation of a Spot Instance request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRun",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1::image/*",
 "arn:aws:ec2:us-east-1:*:subnet/*",
 "arn:aws:ec2:us-east-1:*:network-interface/*",
 "arn:aws:ec2:us-east-1:*:security-group/*",
 "arn:aws:ec2:us-east-1:*:key-pair/*",
 "arn:aws:ec2:us-east-1:*:volume/*",
 "arn:aws:ec2:us-east-1:*:instance/*",
 "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
 ]
 },
 {
 "Sid": "DenySpotInstancesRequests",
 "Effect": "Deny",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:us-east-1:*:spot-instances-request/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": "production"
 }
 }
 },
 {
 "Sid": "TagResources",
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "*"
 }
 ]
}`

```

## Example: Work with Reserved Instances

The following policy gives users permission to view, modify, and purchase Reserved Instances in your
account.

It is not possible to set resource-level permissions for individual Reserved Instances. This policy
means that users have access to all the Reserved Instances in the account.

The `Resource` element uses a \* wildcard to indicate that users can specify all
resources with the action; in this case, they can list and modify all Reserved Instances in the
account. They can also purchase Reserved Instances using the account credentials. The \* wildcard is
also necessary in cases where the API action does not support resource-level
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeReservedInstances",
 "ec2:ModifyReservedInstances",
 "ec2:PurchaseReservedInstancesOffering",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeReservedInstancesOfferings"
 ],
 "Resource": "*"
 }
 ]
}`

```

To allow users to view and modify the Reserved Instances in your account, but not purchase new
Reserved Instances.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeReservedInstances",
 "ec2:ModifyReservedInstances",
 "ec2:DescribeAvailabilityZones"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: Tag resources

The following policy allows users to use the `CreateTags` action to apply tags
to an instance only if the tag contains the key`environment` and the value
`production`. No other tags are allowed and the user cannot tag any other
resource types.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": "production"
 }
 }
 }
 ]
}`

```

The following policy allows users to tag any taggable resource that already has a tag with
a key of `owner` and a value of the username. In addition, users must specify
a tag with a key of `anycompany:environment-type` and a value of either
`test` or `prod` in the request. Users can specify additional
tags in the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:*/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/anycompany:environment-type": ["test","prod"],
 "aws:ResourceTag/owner": "${aws:username}"
 }
 }
 }
 ]
}`

```

You can create an IAM policy that allows users to delete specific tags for a
resource. For example, the following policy allows users to delete tags for a
volume if the tag keys specified in the request are `environment` or
`cost-center`. Any value can be specified for the tag but the tag
key must match either of the specified keys.

###### Note

If you delete a resource, all tags associated with the resource are also deleted. Users
do not need permissions to use the `ec2:DeleteTags` action to delete a
resource that has tags; they only need permissions to perform the deleting
action.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:DeleteTags",
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "aws:TagKeys": ["environment","cost-center"]
 }
 }
 }
 ]
}`

```

This policy allows users to delete only the `environment=prod` tag on any
resource, and only if the resource is already tagged with a key of `owner`
and a value of the username. Users can't delete any other tags for a resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:*/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": "prod",
 "aws:ResourceTag/owner": "${aws:username}"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": ["environment"]
 }
 }
 }
 ]
}`

```

## Example: Work with IAM roles

The following policy allows users to attach, replace, and detach an IAM role
to instances that have the tag `department=test`. Replacing or
detaching an IAM role requires an association ID, therefore the policy also
grants users permission to use the
`ec2:DescribeIamInstanceProfileAssociations` action.

Users must have permission to use the `iam:PassRole` action in order to pass
the role to the instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AssociateIamInstanceProfile",
 "ec2:ReplaceIamInstanceProfileAssociation",
 "ec2:DisassociateIamInstanceProfile"
 ],
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:instance/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department":"test"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:DescribeIamInstanceProfileAssociations",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/DevTeam*"
 }
 ]
}`

```

The following policy allows users to attach or replace an IAM role for any
instance. Users can only attach or replace IAM roles with names that begin
with `TestRole-`. For the `iam:PassRole` action, ensure
that you specify the name of the IAM role and not the instance profile (if the
names are different). For more information, see [Instance profiles](iam-roles-for-amazon-ec2.md#ec2-instance-profile "iam-roles-for-amazon-ec2.md#ec2-instance-profile").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AssociateIamInstanceProfile",
 "ec2:ReplaceIamInstanceProfileAssociation"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:DescribeIamInstanceProfileAssociations",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/TestRole-*"
 }
 ]
}`

```

## Example: Work with route tables

The following policy allows users to add, remove, and replace routes for route
tables that are associated with VPC `vpc-ec43eb89` only. To specify a
VPC for the `ec2:Vpc` condition key, you must specify the full ARN of
the VPC.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteRoute",
 "ec2:CreateRoute",
 "ec2:ReplaceRoute"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:route-table/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:Vpc": "arn:aws:ec2:`us-east-1`:`111122223333`:vpc/vpc-ec43eb89"
 }
 }
 }
 ]
}`

```

## Example: Allow a specific instance to view

resources in other AWS services

The following is an example of a policy that you might attach to an IAM role. The
policy allows an instance to view resources in various AWS services. It uses the
`ec2:SourceInstanceARN` global condition key to specify that the instance from
which the request is made must be instance `i-093452212644b0dd6`. If the same
IAM role is associated with another instance, the other instance cannot perform any of
these actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVolumes",
 "s3:ListAllMyBuckets",
 "dynamodb:ListTables",
 "rds:DescribeDBInstances"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "ArnEquals": {
 "ec2:SourceInstanceARN": "arn:aws:ec2:`us-east-1`:`111122223333`:instance/i-093452212644b0dd6"
 }
 }
 }
 ]
}`

```

## Example: Work with launch

templates

The following policy allows users to create a launch template version and modify a
launch template, but only for a specific launch template
(`lt-`09477bcd97b0d3abc``). Users cannot work with other launch
templates.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:CreateLaunchTemplateVersion",
 "ec2:ModifyLaunchTemplate"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/lt-`09477bcd97b0d3abc`"
 }
 ]
}`

```

The following policy allows users to delete any launch template and launch
template version, provided that the launch template has the tag
`Purpose`=`Testing`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:DeleteLaunchTemplate",
 "ec2:DeleteLaunchTemplateVersions"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Purpose": "Testing"
 }
 }
 }
 ]
}`

```

## Work with instance metadata

The following policies ensure that users can only retrieve [instance metadata](ec2-instance-metadata.md "ec2-instance-metadata.md") using Instance Metadata Service Version 2
(IMDSv2). You can combine the following four policies into one policy with four
statements. When combined as one policy, you can use the policy as a service control policy
(SCP). It can work equally well as a _deny_ policy that you
apply to an existing IAM policy (taking away and limiting existing permission), or as an SCP
that is applied globally across an account, an organizational unit (OU), or an entire
organization.

###### Note

The following RunInstances metadata options policies must be used in conjunction with a
policy that gives the principal permissions to launch an instance with RunInstances. If the
principal does not also have RunInstances permissions, it will not be able to launch an
instance. For more information, see the policies in [Work with instances](#iam-example-instances "#iam-example-instances") and [Launch instances (RunInstances)](#iam-example-runinstances "#iam-example-runinstances").

###### Important

If you use Amazon EC2 Auto Scaling groups and you need to require the use of IMDSv2 on all new
instances, your Amazon EC2 Auto Scaling groups must use _launch
templates_.

When an Amazon EC2 Auto Scaling group uses a launch template, the `ec2:RunInstances` permissions
of the IAM principal are checked when a new Amazon EC2 Auto Scaling group is created. They are also checked
when an existing Amazon EC2 Auto Scaling group is updated to use a new launch template or a new version of a
launch template.

Restrictions
on the use of IMDSv1 on IAM principals for `RunInstances` are only
checked when an Amazon EC2 Auto Scaling group that is using a launch template, is created or updated. For an
Amazon EC2 Auto Scaling group that is configured to use the `Latest` or `Default` launch
template, the permissions are not checked when a new version of the launch template is
created. For permissions to be checked, you must configure the Amazon EC2 Auto Scaling group to use a _specific version_ of the launch template.

###### To enforce the use of IMDSv2 on instances launched by Amazon EC2 Auto Scaling groups, the

following additional steps are required:

1. Disable the use of launch configurations for all accounts in your organization by
   using either service control policies (SCPs) or IAM permissions boundaries for new
   principals that are created. For existing IAM principals with Amazon EC2 Auto Scaling group permissions,
   update their associated policies with this condition key. To disable the use of launch
   configurations, create or modify the relevant SCP, permissions boundary, or IAM policy
   with the `"autoscaling:LaunchConfigurationName"` condition key with the value
   specified as `null`.
2. For new launch templates, configure the instance metadata options in the launch
   template. For existing launch templates, create a new version of the launch template and
   configure the instance metadata options in the new version.
3. In the policy that gives any principal the permission to use a launch template,
   restrict association of `$latest` and `$default` by specifying
   `"autoscaling:LaunchTemplateVersionSpecified": "true"`. By restricting the
   use to a specific version of a launch template, you can ensure that new instances will
   be launched using the version in which the instance metadata options are configured. For
   more information, see [LaunchTemplateSpecification](../../../autoscaling/ec2/APIReference/API_LaunchTemplateSpecification.md "../../../autoscaling/ec2/APIReference/API_LaunchTemplateSpecification.md") in the _Amazon EC2 Auto Scaling API Reference_, specifically the `Version` parameter.
4. For an Amazon EC2 Auto Scaling group that uses a launch configuration, replace the launch configuration
   with a launch template. For more information, see [Migrate your Amazon EC2 Auto Scaling groups
   to launch templates](../../../autoscaling/ec2/userguide/migrate-to-launch-templates.md "../../../autoscaling/ec2/userguide/migrate-to-launch-templates.md") in the _Amazon EC2 Auto Scaling User Guide_.
5. For an Amazon EC2 Auto Scaling group that uses a launch template, make sure that it uses a new launch
   template with the instance metadata options configured, or uses a new version of the
   current launch template with the instance metadata options configured. For more
   information, see [update-auto-scaling-group](../../../cli/latest/reference/autoscaling/update-auto-scaling-group.md "../../../cli/latest/reference/autoscaling/update-auto-scaling-group.md").

###### Examples

- [Require the use of
  IMDSv2](#iam-example-instance-metadata-requireIMDSv2 "#iam-example-instance-metadata-requireIMDSv2")
- [Deny opt-out of
  IMDSv2](#iam-example-instance-metadata-denyoptoutIMDSv2 "#iam-example-instance-metadata-denyoptoutIMDSv2")
- [Specify maximum hop limit](#iam-example-instance-metadata-maxHopLimit "#iam-example-instance-metadata-maxHopLimit")
- [Limit who can modify the
  instance metadata options](#iam-example-instance-metadata-limit-modify-IMDS-options "#iam-example-instance-metadata-limit-modify-IMDS-options")
- [Require role
  credentials to be retrieved from IMDSv2](#iam-example-instance-metadata-require-roles-to-use-IMDSv2-credentials "#iam-example-instance-metadata-require-roles-to-use-IMDSv2-credentials")

### Require the use of

IMDSv2

The following policy specifies that you can’t call the RunInstances API unless the
instance is also opted in to require the use of IMDSv2 (indicated by
`"ec2:MetadataHttpTokens": "required"`). If you do not specify that the instance
requires IMDSv2, you get an `UnauthorizedOperation` error when you call the
RunInstances API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RequireImdsV2",
 "Effect": "Deny",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:*:*:instance/*",
 "Condition": {
 "StringNotEquals": {
 "ec2:MetadataHttpTokens": "required"
 }
 }
 }
 ]
}`

```

### Deny opt-out of

IMDSv2

The following policy specifies that you cannot call the
`ModifyInstanceMetadataOptions` API and allow the option of
IMDSv1 or IMDSv2. If you call the
`ModifyInstanceMetadataOptions` API, the `HttpTokens`
attribute must be set to `required`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "DenyIMDSv1HttpTokensModification",
 "Effect": "Deny",
 "Action": "ec2:ModifyInstanceMetadataOptions",
 "Resource": "arn:aws:ec2:*:*:instance/*",
 "Condition": {
 "StringNotEquals": {
 "ec2:Attribute/HttpTokens": "required"
 },
 "Null": {
 "ec2:Attribute/HttpTokens": false
 }
 }
 }]
}`

```

### Specify maximum hop limit

The following policy specifies that you can’t call the RunInstances API unless you also
specify a hop limit, and the hop limit can’t be more than 3. If you fail to do that, you get
an `UnauthorizedOperation` error when you call the RunInstances API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MaxImdsHopLimit",
 "Effect": "Deny",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:*:*:instance/*",
 "Condition": {
 "NumericGreaterThan": {
 "ec2:MetadataHttpPutResponseHopLimit": "3"
 }
 }
 }
 ]
}`

```

### Limit who can modify the

instance metadata options

The following policy permits only users with the role `ec2-imds-admins` to make
changes to the instance metadata options. If any principal other than the
`ec2-imds-admins` role tries to call the
ModifyInstanceMetadataOptions API, it will get an `UnauthorizedOperation`
error. This statement could be used to control the use of the
ModifyInstanceMetadataOptions API; there are currently no fine-grained access
controls (conditions) for the ModifyInstanceMetadataOptions API.

### Require role

credentials to be retrieved from IMDSv2

The following policy specifies that if this policy is applied to a role, and the role is
assumed by the EC2 service and the resulting credentials are used to sign a request, then the
request must be signed by EC2 role credentials retrieved from IMDSv2. Otherwise, all
of its API calls will get an `UnauthorizedOperation` error. This statement/policy
can be applied generally because, if the request is not signed by EC2 role credentials, it has
no effect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RequireAllEc2RolesToUseV2",
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "NumericLessThan": {
 "ec2:RoleDelivery": "2.0"
 }
 }
 }
 ]
}`

```

## Work with Amazon EBS volumes and snapshots

For example policies for working with Amazon EBS volumes and snapshots, see [Identity-based policy examples for Amazon EBS](../../../ebs/latest/userguide/security_iam_id-based-policy-examples.md "../../../ebs/latest/userguide/security_iam_id-based-policy-examples.md").
