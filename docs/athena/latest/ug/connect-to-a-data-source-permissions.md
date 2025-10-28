# Permissions to create and use a data source in Athena

To create and use a data source, you need the following sets of permissions.

- AmazonAthenaFullAccess that provides full access to Amazon Athena and scoped
  access to the dependencies needed to enable querying, writing results, and data
  management. For more information, see [AmazonAthenaFullAccess](../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md") in the AWS Managed Policy Reference
  Guide.
- Permissions to call the CreateDataCatalog API. These permissions are only
  needed when you create a data source that integrates with Glue connections. For
  more information on the example policy, see [Permissions required to create connector and Athena catalog](athena-catalog-access.md "athena-catalog-access.md").
- If you want to use Lake Formation fine-grain access control, in addition to the
  permissions listed above, you also need the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:RegisterResource",
 "iam:ListRoles",
 "glue:CreateCatalog",
 "glue:GetCatalogs",
 "glue:GetCatalog"
 ],
 "Resource": "*"
 }
 ]
}`

```
