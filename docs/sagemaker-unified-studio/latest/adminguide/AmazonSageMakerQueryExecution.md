# AmazonSageMakerQueryExecution

This role is used while running a query execution. AWS LakeFormation assumes this
role to vend credentials needed by Amazon Athena during query execution.

The AmazonSageMakerQueryExecution role has the [AWS
policy: SageMakerStudioQueryExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioQueryExecutionRolePolicy.md "security-iam-awsmanpol-SageMakerStudioQueryExecutionRolePolicy.md")
attached.

The default `AmazonSageMakerQueryExecution` role has the following trust
policy attached:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "lakeformation.amazonaws.com",
 "glue.amazonaws.com"
 ]
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{{source_account}}"
 }
 }
 }
 ]
}`

```

###### Important

If you are using your own query execution role (instead of this default
AmazonSageMakerQueryExecution role), then you must modify the permissions of your
provisioning role (whether you're using this default [AmazonSageMakerProvisioning-<domainAccountId> role](AmazonSageMakerProvisioning.md "AmazonSageMakerProvisioning.md") role
or your own custom provisioning role) to include `iam:PassRole` and
`iam:GetRole` permissions. These permissions enable your provisioning
role to pass the query execution role to AWS LakeFormation during creation of federated
connections. You can include these permissions by attaching the following inline policy to your
provisioning role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IamRolePermissionsForQueryExecution",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole",
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/{your-role}"
 }
 ]
}`

```
