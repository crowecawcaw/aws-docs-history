# AmazonDataZoneSageMakerProvisioningRolePolicyRole-<domainAccountId>

The `AmazonDataZoneSageMakerProvisioningRolePolicyRole` role has the
`AmazonDataZoneSageMakerProvisioningRolePolicy` and the
`AmazonDataZoneRedshiftGlueProvisioningPolicy` attached. This role
grants Amazon DataZone permissions required to interoperate with AWS Glue, Amazon
Redshift, and Amazon Sagemaker.

The `AmazonDataZoneSageMakerProvisioningRolePolicyRole` role has the
following inline policy attached:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SageMakerStudioTagOnCreate",
 "Effect": "Allow",
 "Action": [
 "sagemaker:AddTags"
 ],
 "Resource": "arn:aws:sagemaker:*:111122223333:*/*",
 "Condition": {
 "Null": {
 "sagemaker:TaggingAction": "false"
 }
 }
 }
 ]
}`

```

The `AmazonDataZoneSageMakerProvisioningRolePolicyRole` role has the
following trust policy attached:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DataZoneTrustPolicyStatement",
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
