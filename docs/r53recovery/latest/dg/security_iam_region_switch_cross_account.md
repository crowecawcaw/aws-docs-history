# Cross-account resource permissions

If resources are in different accounts, you'll need a cross-account role. The following is a sample trust policy for a cross-account role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:role/RegionSwitchExecutionRole"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "sts:ExternalId": "UniqueExternalId123"
 }
 }
 }
 ]
}`

```

And the following is the permission for the plan execution role to assume this cross-account role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::987654321098:role/RegionSwitchCrossAccountRole",
 "Condition": {
 "StringEquals": {
 "sts:ExternalId": "UniqueExternalId123"
 }
 }
 }
 ]
}`

```
