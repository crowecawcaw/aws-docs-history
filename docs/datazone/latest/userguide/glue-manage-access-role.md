# AmazonDataZoneGlueAccess-<region>-<domainId>

The `AmazonDataZoneGlueAccess-<region>-<domainId>` role has
the `AmazonDataZoneGlueManageAccessRolePolicy` attached. This role grants
Amazon DataZone permissions to publish AWS Glue data to the catalog. It also gives
Amazon DataZone permissions to grant access or revoke access to AWS Glue published
assets in the catalog.

The default `AmazonDataZoneGlueAccess-<region>-<domainId>`
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
