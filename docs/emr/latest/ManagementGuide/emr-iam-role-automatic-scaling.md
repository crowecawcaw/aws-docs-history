# Service role for automatic scaling

in Amazon EMR (Auto Scaling role)

The Auto Scaling role for Amazon EMR performs a similar function as the service role,
but allows additional actions for dynamically scaling environments.

- The default role name is `EMR_AutoScaling_DefaultRole`.
- The default managed policy attached to
  `EMR_AutoScaling_DefaultRole` is
  `AmazonElasticMapReduceforAutoScalingRole`.
  The contents of version 1 of `AmazonElasticMapReduceforAutoScalingRole`
  are shown below.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "cloudwatch:DescribeAlarms",
 "elasticmapreduce:ListInstanceGroups",
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Sid": "AllowCLOUDWATCHDescribealarms"
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
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::123456789012:role/ApplicationAutoScalingEMRRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:application-autoscaling:*:123456789012:scalable-target/*"
 }
 },
 "Sid": "AllowSTSAssumerole"
 }
 ]
}`

```
