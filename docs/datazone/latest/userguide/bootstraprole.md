# AmazonDataZoneProvisioningRole-<domainAccountId>

The `AmazonDataZoneProvisioningRole-<domainAccountId>` has the
`AmazonDataZoneRedshiftGlueProvisioningPolicy` attached. This role
grants Amazon DataZone the permissions required to interoperate with AWS Glue and
Amazon Redshift.

The default `AmazonDataZoneProvisioningRole-<domainAccountId>`
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
 "aws:SourceAccount": "{{domain_account}}"
 }
 }
 }
 ]
}`

```
