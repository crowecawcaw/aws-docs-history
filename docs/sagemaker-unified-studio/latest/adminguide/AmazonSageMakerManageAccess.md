# AmazonSageMakerManageAccess-<region>-<domainId> role

AmazonSageMakerManageAccess-<region>-<domainId> role grants Amazon
SageMaker Unified Studio permissions to publish, grant access, and revoke access to
Amazon SageMaker Lakehouse, AWS Glue Data Catalog and Amazon Redshift data. It also
grants Amazon SageMaker Unified Studio access to publish and manage subscriptions on
Amazon SageMaker Catalog data and AI assets.

AmazonSageMakerManageAccess-<region>-<domainId> role has the following
Amazon DataZone managed policies attached:

- AmazonDataZoneGlueManageAccessRolePolicy
- AmazonDataZoneRedshiftManageAccessRolePolicy
- AmazonDataZoneSageMakerAccess
  The default `AmazonSageMakerManageAccess-<region>-<domainId>`
  role has the following inline policy attached:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid": "RedshiftSecretStatement",
 "Effect":"Allow",
 "Action":"secretsmanager:GetSecretValue",
 "Resource":"*",
 "Condition":{
 "StringEquals":{
 "secretsmanager:ResourceTag/AmazonDataZoneDomain":"{{domainId}}"
 }
 }
 }
 ]
}`

```

The default `AmazonSageMakerManageAccess-<region>-<domainId>`
role has the following trust policy attached:

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
 "aws:SourceAccount": "111122223333"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:datazone:us-east-1:111122223333:domain/dzd-12345"
 }
 }
 }
 ]
}`

```
