# AmazonSageMakerDomainExecution

role

The AmazonSageMakerDomainExecution role has the [AWS
policy: SageMakerStudioDomainExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md "security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md")
attached. This is an IAM role that Amazon SageMaker Unified Studio requires to call APIs
on behalf of authorized users, including those logged in to Amazon SageMaker Unified
Studio.

The default `AmazonSageMakerDomainExecution` role has the following trust
policy attached:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "datazone.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession",
 "sts:SetContext"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{{source_account_id}}"
 },
 "ForAllValues:StringLike": {
 "aws:TagKeys": "datazone*"
 }
 }
 }
 ]
}`

```
