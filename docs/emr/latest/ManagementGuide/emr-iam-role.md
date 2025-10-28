# Service role for Amazon EMR (EMR role)

The Amazon EMR role defines the allowable actions for Amazon EMR when it provisions
resources and performs service-level tasks that aren't performed in the context of
an Amazon EC2 instance running within a cluster. For example, the service role is used to
provision EC2 instances when a cluster launches.

- The default role name is `EMR_DefaultRole_V2`.
- The Amazon EMR scoped default managed policy attached to
  `EMR_DefaultRole_V2` is
  `AmazonEMRServicePolicy_v2`. This v2 policy replaces the
  deprecated default managed policy,
  `AmazonElasticMapReduceRole`.
  `AmazonEMRServicePolicy_v2` depends on scoped down access to resources
  that Amazon EMR provisions or uses. When you use this policy, you need to pass the user
  tag `for-use-with-amazon-emr-managed-policies = true` when provisioning
  the cluster. Amazon EMR will automatically propagate those tags. Additionally, you may
  need to manually add a user tag to specific types of resources, such as EC2 security
  groups that were not created by Amazon EMR. See [Tagging resources to use managed
  policies](emr-managed-iam-policies.md#manually-tagged-resources "emr-managed-iam-policies.md#manually-tagged-resources").

###### Important

Amazon EMR uses this Amazon EMR service role and the `AWSServiceRoleForEMRCleanup` role to clean up cluster
resources in your account that you no longer use, such as Amazon EC2 instances. You
must include actions for the role policies to delete or terminate the resources.
Otherwise, Amazon EMR can’t perform these cleanup actions, and you might incur costs
for unused resources that remain on the cluster.

The following shows the contents of the current
`AmazonEMRServicePolicy_v2` policy. You can also see the current
content of the [`AmazonEMRServicePolicy_v2`](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRServicePolicy_v2 "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRServicePolicy_v2") managed policy on the IAM
console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateInTaggedNetwork",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:RunInstances",
 "ec2:CreateFleet",
 "ec2:CreateLaunchTemplate",
 "ec2:CreateLaunchTemplateVersion"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "CreateWithEMRTaggedLaunchTemplate",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateFleet",
 "ec2:RunInstances",
 "ec2:CreateLaunchTemplateVersion"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:launch-template/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "CreateEMRTaggedLaunchTemplate",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateLaunchTemplate"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:launch-template/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "CreateEMRTaggedInstancesAndVolumes",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances",
 "ec2:CreateFleet"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ec2:*:*:volume/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "ResourcesToLaunchEC2",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances",
 "ec2:CreateFleet",
 "ec2:CreateLaunchTemplate",
 "ec2:CreateLaunchTemplateVersion"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*",
 "arn:aws:ec2:*::image/ami-*",
 "arn:aws:ec2:*:*:key-pair/*",
 "arn:aws:ec2:*:*:capacity-reservation/*",
 "arn:aws:ec2:*:*:placement-group/pg-*",
 "arn:aws:ec2:*:*:fleet/*",
 "arn:aws:ec2:*:*:dedicated-host/*",
 "arn:aws:resource-groups:*:*:group/*"
 ]
 },
 {
 "Sid": "ManageEMRTaggedResources",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateLaunchTemplateVersion",
 "ec2:DeleteLaunchTemplate",
 "ec2:DeleteNetworkInterface",
 "ec2:ModifyInstanceAttribute",
 "ec2:TerminateInstances"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "ManageTagsOnEMRTaggedResources",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags",
 "ec2:DeleteTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ec2:*:*:volume/*",
 "arn:aws:ec2:*:*:network-interface/*",
 "arn:aws:ec2:*:*:launch-template/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "CreateNetworkInterfaceNeededForPrivateSubnet",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "TagOnCreateTaggedEMRResources",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*",
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ec2:*:*:volume/*",
 "arn:aws:ec2:*:*:launch-template/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": [
 "RunInstances",
 "CreateFleet",
 "CreateLaunchTemplate",
 "CreateNetworkInterface"
 ]
 }
 }
 },
 {
 "Sid": "TagPlacementGroups",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags",
 "ec2:DeleteTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:placement-group/pg-*"
 ]
 },
 {
 "Sid": "ListActionsForEC2Resources",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeCapacityReservations",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeImages",
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceTypeOfferings",
 "ec2:DescribeLaunchTemplates",
 "ec2:DescribeNetworkAcls",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribePlacementGroups",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVolumes",
 "ec2:DescribeVolumeStatus",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcs"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "CreateDefaultSecurityGroupWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSecurityGroup"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "CreateDefaultSecurityGroupInVPCWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSecurityGroup"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:vpc/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "TagOnCreateDefaultSecurityGroupWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true",
 "ec2:CreateAction": "CreateSecurityGroup"
 }
 }
 },
 {
 "Sid": "ManageSecurityGroups",
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "CreateEMRPlacementGroups",
 "Effect": "Allow",
 "Action": [
 "ec2:CreatePlacementGroup"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:placement-group/pg-*"
 ]
 },
 {
 "Sid": "DeletePlacementGroups",
 "Effect": "Allow",
 "Action": [
 "ec2:DeletePlacementGroup"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AutoScaling",
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:DeleteScalingPolicy",
 "application-autoscaling:DeregisterScalableTarget",
 "application-autoscaling:DescribeScalableTargets",
 "application-autoscaling:DescribeScalingPolicies",
 "application-autoscaling:PutScalingPolicy",
 "application-autoscaling:RegisterScalableTarget"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ResourceGroupsForCapacityReservations",
 "Effect": "Allow",
 "Action": [
 "resource-groups:ListGroupResources"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AutoScalingCloudWatch",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:DescribeAlarms"
 ],
 "Resource": [
 "arn:aws:cloudwatch:*:*:alarm:*_EMR_Auto_Scaling"
 ]
 },
 {
 "Sid": "PassRoleForAutoScaling",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/EMR_AutoScaling_DefaultRole"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "application-autoscaling.amazonaws.com*"
 }
 }
 },
 {
 "Sid": "PassRoleForEC2",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/EMR_EC2_DefaultRole"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "ec2.amazonaws.com*"
 }
 }
 },
 {
 "Sid": "CreateAndModifyEmrServiceVPCEndpoint",
 "Effect": "Allow",
 "Action": [
 "ec2:ModifyVpcEndpoint",
 "ec2:CreateVpcEndpoint"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:vpc-endpoint/*",
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*",
 "arn:aws:ec2:*:*:vpc/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "CreateEmrServiceVPCEndpoint",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateVpcEndpoint"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:vpc-endpoint/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true",
 "aws:RequestTag/Name": "emr-service-vpce"
 }
 }
 },
 {
 "Sid": "TagEmrServiceVPCEndpoint",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:vpc-endpoint/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateVpcEndpoint",
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true",
 "aws:RequestTag/Name": "emr-service-vpce"
 }
 }
 }
 ]
}`

```

Your service role should use the following trust policy.

###### Important

The following trust policy includes the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition keys, which
limit the permissions that you give Amazon EMR to particular resources in your
account. Using them can protect you against [the confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSTSAssumerole",
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::123456789012:role/EMRServiceRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:elasticmapreduce:*:123456789012:*"
 }
 }
 }
 ]
}`

```
