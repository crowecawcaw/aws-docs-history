# Step 1: Do Initial Setup

Before proceeding, you must:

1. Create an AWS account.
2. Set up root and administrative users.
3. Set up AWS IAM (Identity and Access Management) permissions. Use the policy specified
   below.
   For specific steps for all the above, see [Getting Started with IVS
   Low-Latency Streaming](../LowLatencyUserGuide/getting-started.md "../LowLatencyUserGuide/getting-started.md") in the _Amazon IVS User
   Guide_. **Important**: In "Step 3: Set Up IAM
   Permissions," use this policy for IVS Chat:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ivschat:CreateChatToken",
 "ivschat:CreateLoggingConfiguration",
 "ivschat:CreateRoom",
 "ivschat:DeleteLoggingConfiguration",
 "ivschat:DeleteMessage",
 "ivschat:DeleteRoom",
 "ivschat:DisconnectUser",
 "ivschat:GetLoggingConfiguration",
 "ivschat:GetRoom",
 "ivschat:ListLoggingConfigurations",
 "ivschat:ListRooms",
 "ivschat:ListTagsForResource",
 "ivschat:SendEvent",
 "ivschat:TagResource",
 "ivschat:UntagResource",
 "ivschat:UpdateLoggingConfiguration",
 "ivschat:UpdateRoom"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "servicequotas:ListServiceQuotas",
 "servicequotas:ListServices",
 "servicequotas:ListAWSDefaultServiceQuotas",
 "servicequotas:ListRequestedServiceQuotaChangeHistoryByQuota",
 "servicequotas:ListTagsForResource",
 "cloudwatch:GetMetricData",
 "cloudwatch:DescribeAlarms"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries",
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups",
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy",
 "iam:CreateServiceLinkedRole",
 "firehose:TagDeliveryStream"
 ],
 "Resource": "*"
 }
 ]
}`

```
