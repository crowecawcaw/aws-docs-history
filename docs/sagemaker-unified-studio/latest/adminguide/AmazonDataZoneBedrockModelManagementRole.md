# AmazonDataZoneBedrockModelManagementRole

Amazon SageMaker Unified Studio uses this role to create an inference profile for an Amazon Bedrock model in
a project. The inference profile is required for the project to interact with the model.
You can either let Amazon SageMaker Unified Studio automatically create a unique provisioning role, or you can
provide a custom provisioning role.

The AmazonDataZoneBedrockModelManagementRole has the [AWS policy: AmazonDataZoneBedrockModelManagementPolicy](security-iam-awsmanpol-AmazonDataZoneBedrockModelManagementPolicy.md "security-iam-awsmanpol-AmazonDataZoneBedrockModelManagementPolicy.md")
attached.

The default `AmazonDataZoneBedrockModelManagementRole` has the following
trust policy attached:

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
 "sts:SetContext"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{{accountId}}"
 }
 }
 }
 ]
}`

```
