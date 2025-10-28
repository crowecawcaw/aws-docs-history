# AmazonDataZoneDomainExecutionRole

The **AmazonDataZoneDomainExecutionRole** has the AWS managed
policy **AmazonDataZoneDomainExecutionRolePolicy** attached.
Amazon DataZone creates this role for you on your behalf. For certain actions in the data
portal, Amazon DataZone assumes this role in the account in which the role is created and
checks that this role is authorized to perform the action.

The **AmazonDataZoneDomainExecutionRole** role is required in the
AWS account that hosts your Amazon DataZone domain. This role is automatically created
for you when you create your Amazon DataZone domain.

The default **AmazonDataZoneDomainExecutionRole** role has the
following trust policy.

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
 "sts:TagSession"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{{source_account_id}}"
 },
 "ForAllValues:StringLike": {
 "aws:TagKeys": [
 "datazone*"
 ]
 }
 }
 }
 ]
}`

```
