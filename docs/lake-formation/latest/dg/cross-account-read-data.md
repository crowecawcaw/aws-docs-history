# Accessing the underlying data of a shared

table

Assume that AWS account A shares a Data Catalog table with account B—for example,
by granting `SELECT` with the grant option on the table to account B. For a
principal in account B to be able to read the shared table's underlying data, the
following conditions must be met:

- The data lake administrator in account B must accept the share. (This isn't
  necessary if accounts A and B are in the same organization or if the grant was made
  with the Lake Formation tag-based access control method.)
- The data lake administrator must re-grant to the principal the Lake Formation
  `SELECT` permission that account A granted on the shared table.
- The principal must have the following IAM permissions on the table, the database
  that contains it, and the account A Data Catalog.

###### Note

In the following IAM policy:

    + Replace `<account-id-A>` with the AWS account
     ID of account A.
    + Replace `<region>` with a valid Region.
    + Replace `<database>` with the name of the
     database in account A that contains the shared table.
    + Replace `<table>` with the name of the shared
     table.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "glue:GetDatabase",
 "glue:GetDatabases"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:table/`<database>`/`<table>`",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/`<database>`",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

###### See Also:

- [Accepting a resource share invitation from AWS RAM](accepting-ram-invite.md "accepting-ram-invite.md")
