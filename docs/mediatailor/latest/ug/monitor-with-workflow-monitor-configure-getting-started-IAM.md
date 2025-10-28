# Workflow monitor IAM policies

Workflow monitor interacts with multiple AWS services to create signal maps,
build CloudWatch and EventBridge resources, and AWS CloudFormation templates. Because workflow monitor
interacts with a wide range of services, specific AWS Identity and Access Management (IAM) policies
must be assigned for these services. The following examples indicate the
necessary IAM policies for both administrator and operator IAM
roles.

## Administrator IAM policy

The following example policy is for an administrator-level workflow monitor IAM
policy. This role allows for the creation and management of workflow monitor
resources and the supported service resources that interact with workflow monitor.

JSON

```
`{

 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:List*",
 "cloudwatch:Describe*",
 "cloudwatch:Get*",
 "cloudwatch:PutAnomalyDetector",
 "cloudwatch:PutMetricData",
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:PutCompositeAlarm",
 "cloudwatch:PutDashboard",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:DeleteAnomalyDetector",
 "cloudwatch:DeleteDashboards",
 "cloudwatch:TagResource",
 "cloudwatch:UntagResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:List*",
 "cloudformation:Describe*",
 "cloudformation:CreateStack",
 "cloudformation:UpdateStack",
 "cloudformation:DeleteStack",
 "cloudformation:TagResource",
 "cloudformation:UntagResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudfront:List*",
 "cloudfront:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeNetworkInterfaces"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:List*",
 "events:Describe*",
 "events:CreateEventBus",
 "events:PutRule",
 "events:PutTargets",
 "events:EnableRule",
 "events:DisableRule",
 "events:DeleteRule",
 "events:RemoveTargets",
 "events:TagResource",
 "events:UntagResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:Describe*",
 "logs:Get*",
 "logs:TagLogGroup",
 "logs:TagResource",
 "logs:UntagLogGroup",
 "logs:UntagResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediaconnect:List*",
 "mediaconnect:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "medialive:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediapackage:List*",
 "mediapackage:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediapackagev2:List*",
 "mediapackagev2:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediapackage-vod:List*",
 "mediapackage-vod:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediatailor:List*",
 "mediatailor:Describe*",
 "mediatailor:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "resource-groups:ListGroups",
 "resource-groups:GetGroup",
 "resource-groups:GetTags",
 "resource-groups:GetGroupQuery",
 "resource-groups:GetGroupConfiguration",
 "resource-groups:CreateGroup",
 "resource-groups:UngroupResources",
 "resource-groups:GroupResources",
 "resource-groups:DeleteGroup",
 "resource-groups:UpdateGroupQuery",
 "resource-groups:UpdateGroup",
 "resource-groups:Tag",
 "resource-groups:Untag"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:*"
 ],
 "Resource": "arn:aws:s3:::workflow-monitor-templates*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "sns:TagResource",
 "sns:UntagResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "tag:Get*",
 "tag:Describe*",
 "tag:TagResources",
 "tag:UntagResources"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Operator IAM policy

The following example policy is for an operator-level workflow monitor IAM policy.
This role allows for limited and read-only access to the workflow monitor resources
and the supported service resources that interact with workflow monitor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:List*",
 "cloudwatch:Describe*",
 "cloudwatch:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:List*",
 "cloudformation:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudfront:List*",
 "cloudfront:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeNetworkInterfaces"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:List*",
 "events:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:Describe*",
 "logs:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediaconnect:List*",
 "mediaconnect:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "medialive:List*",
 "medialive:Get*",
 "medialive:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediapackage:List*",
 "mediapackage:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediapackagev2:List*",
 "mediapackagev2:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediapackage-vod:List*",
 "mediapackage-vod:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mediatailor:List*",
 "mediatailor:Describe*",
 "mediatailor:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:Get*",
 "s3:List*"
 ],
 "Resource": "arn:aws:s3:::workflow-monitor-templates*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "tag:Get*",
 "tag:Describe*"
 ],
 "Resource": "*"
 }
 ]
}`

```
