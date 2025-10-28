# AmazonDataZoneRedshiftAccess-<region>-<domainId>

The `AmazonDataZoneRedshiftAccess-<region>-<domainId>` role
has the `AmazonDataZoneRedshiftManageAccessRolePolicy` attached. This
role grants Amazon DataZone permissions to publish Amazon Redshift data to the catalog.
It also gives Amazon DataZone permissions to grant access or revoke access to Amazon
Redshift or Amazon Redshift Serverless published assets in the catalog.

The default
`AmazonDataZoneRedshiftAccess-<region>-<domainId>` role
has the following inline permissions policy attached:

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

The default `AmazonDataZoneRedshiftManageAccessRole<timestamp>`
has the following trust policy attached:

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
