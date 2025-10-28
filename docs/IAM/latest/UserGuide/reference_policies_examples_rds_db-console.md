# Amazon RDS: Allows restoring RDS

databases, programmatically and in the console

This example shows how you might create an identity-based policy that allows restoring RDS databases. This policy defines permissions for programmatic and console access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:Describe*",
 "rds:CreateDBParameterGroup",
 "rds:CreateDBSnapshot",
 "rds:DeleteDBSnapshot",
 "rds:Describe*",
 "rds:DownloadDBLogFilePortion",
 "rds:List*",
 "rds:ModifyDBInstance",
 "rds:ModifyDBParameterGroup",
 "rds:ModifyOptionGroup",
 "rds:RebootDBInstance",
 "rds:RestoreDBInstanceFromDBSnapshot",
 "rds:RestoreDBInstanceToPointInTime"
 ],
 "Resource": "*"
 }
 ]
}`

```
