# AmazonSageMakerProvisioning-<domainAccountId> role

AmazonSageMakerProvisioning-<domainAccountId> role is used by Amazon SageMaker
Unified Studio to provision and manage resources defined in the selected blueprints in
your account.

AmazonSageMakerProvisioning-<domainAccountId> role has the [AWS policy: SageMakerStudioProjectProvisioningRolePolicy](security-iam-awsmanpol-SageMakerStudioProjectProvisioningRolePolicy.md "security-iam-awsmanpol-SageMakerStudioProjectProvisioningRolePolicy.md") attached.

The default `AmazonSageMakerProvisioning-<domainAccountId>` role has
the following trust policy attached:

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

###### Important

If you are using your own query execution role (instead of the default
[AmazonSageMakerQueryExecution](AmazonSageMakerQueryExecution.md "AmazonSageMakerQueryExecution.md") role), then you must modify the permissions of your
provisioning role (whether you're using this default AmazonSageMakerProvisioning role
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
