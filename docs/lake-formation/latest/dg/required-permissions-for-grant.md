# IAM permissions required to grant or

revoke Lake Formation permissions

All principals, including the data lake administrator, need the following AWS Identity and Access Management
(IAM) permissions to grant or revoke AWS Lake Formation Data Catalog permissions or data location
permissions with the Lake Formation API or the AWS CLI:

- `lakeformation:GrantPermissions`
- `lakeformation:BatchGrantPermissions`
- `lakeformation:RevokePermissions`
- `lakeformation:BatchRevokePermissions`
- `glue:GetTable`, `glue:GetDatabase`, or
  `glue:GetCatalog` for a table, database, or catalog that you're
  granting permissions using the named resource method.

###### Note

Data lake administrators have implicit Lake Formation permissions to grant and revoke Lake Formation
permissions. But they still need the IAM permissions on the Lake Formation grant and revoke API
operations.

IAM roles with `AWSLakeFormationDataAdmin` AWS managed policy cannot add new data lake administrators because this policy contains
an explicit deny for the Lake Formation API operation, `PutDataLakeSetting`.

The following IAM policy is recommended for principals who are not data lake
administrators and who want to grant or revoke permissions using the Lake Formation console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:ListPermissions",
 "lakeformation:GrantPermissions",
 "lakeformation:BatchGrantPermissions",
 "lakeformation:RevokePermissions",
 "lakeformation:BatchRevokePermissions",
 "glue:GetCatalogs",
 "glue:GetDatabases",
 "glue:SearchTables",
 "glue:GetTables",
 "glue:GetCatalog",
 "glue:GetDatabase",
 "glue:GetTable",
 "iam:ListUsers",
 "iam:ListRoles",
 "sso-directory:DescribeUser",
 "sso-directory:DescribeGroup",
 "sso:DescribeInstance"
 ],
 "Resource": "*"
 }
 ]
}`

```

All of the `glue:` and `iam:` permissions in this policy are
available in the AWS managed policy `AWSGlueConsoleFullAccess`.

To grant permissions by using Lake Formation tag-based access control (LF-TBAC), principals need
additional IAM permissions. For more information, see [Lake Formation tag-based access control best
practices and considerations](lf-tag-considerations.md "lf-tag-considerations.md") and [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md").

###### Cross-account permissions

Users who want to grant cross-account Lake Formation permissions by using the named resource
method must also have the permissions in the
`AWSLakeFormationCrossAccountManager` AWS managed policy.

Data lake administrators need those same permissions for granting cross-account
permissions, plus the AWS Resource Access Manager (AWS RAM) permission to enable granting permissions to
organizations. For more information, see [Data lake administrator permissions](permissions-reference.md#persona-dl-admin "permissions-reference.md#persona-dl-admin").

###### The administrative user

A principal with administrative permissions—for example, with the
`AdministratorAccess` AWS managed policy—has permissions to grant
Lake Formation permissions and create data lake administrators. To deny a user or role access to
Lake Formation administrator operations, attach or add into its policy a `Deny` statement
for administrator API operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "lakeformation:GetDataLakeSettings",
 "lakeformation:PutDataLakeSettings"
 ],
 "Effect": "Deny",
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

###### Important

To prevent users from adding themselves as an administrator with an extract,
transform, and load (ETL) script, make sure that all non-administrator users and roles are
denied access to these API operations. The `AWSLakeFormationDataAdmin` AWS
managed policy contains an explict deny for the Lake Formation API operation,
`PutDataLakeSetting` that prevents users from adding new data lake
administrators.
