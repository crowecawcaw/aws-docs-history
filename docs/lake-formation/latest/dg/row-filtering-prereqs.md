# Permissions required for querying tables with

cell-level filtering

The following AWS Identity and Access Management (IAM) permissions are required to run queries against tables
with cell-level filtering.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:StartQueryPlanning",
 "lakeformation:GetQueryState",
 "lakeformation:GetWorkUnits",
 "lakeformation:GetWorkUnitResults"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about Lake Formation permissions, see [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md").
