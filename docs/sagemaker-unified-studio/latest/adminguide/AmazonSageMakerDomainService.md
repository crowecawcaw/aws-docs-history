# AmazonSageMakerDomainService role

The AmazonSageMakerDomainService role has the [AWS
policy: SageMakerStudioDomainServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioDomainServiceRolePolicy.md")
attached. This is a service role for domain level actions performed by Amazon SageMaker
Unified Studio.

The default `AmazonSageMakerDomainService` role has the following trust
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
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{{domain_account}}"
 }
 }
 }
 ]
}`

```
