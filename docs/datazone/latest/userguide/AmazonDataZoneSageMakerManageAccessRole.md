# AmazonDataZoneSageMakerManageAccessRole-<region>-<domainId>

The `AmazonDataZoneSageMakerManageAccessRole` role has the
`AmazonDataZoneSageMakerAccess`, the
`AmazonDataZoneRedshiftManageAccessRolePolicy`, and the
`AmazonDataZoneGlueManageAccessRolePolicy` attached. This role grants
Amazon DataZone permissions to publish and manage subscriptions for data lake, data
warehouse, and Amazon Sagemaker assets.

The `AmazonDataZoneSageMakerManageAccessRole` role has the following
inline policy attached:

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

The `AmazonDataZoneSageMakerManageAccessRole` role has the following
trust policy attached:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DatazoneTrustPolicyStatement",
 "Effect": "Allow",
 "Principal": {
 "Service": ["datazone.amazonaws.com",
 "sagemaker.amazonaws.com"]
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
