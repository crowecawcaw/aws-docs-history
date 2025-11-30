# Policy to enable Automation for your account

The following code example shows how to This permission-based policy enablesAutomation for your account

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
 "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PutRolePolicy",
 "iam:AttachRolePolicy"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
 },
 {
 "Effect": "Allow",
 "Action": "aco-automation:UpdateEnrollmentConfiguration",
 "Resource": "*"
 }
 ]
}`

```

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
