# Granting permissions on a data location shared with your

account

After a Data Catalog resource is shared with your AWS account, as a data lake
administrator, you can grant permissions on the resource to other principals in your
account. If the `ALTER` permission is granted on a shared table, and the table
points to a registered Amazon S3 location, you must also grant data location permissions on the
location. Likewise, if the `CREATE_TABLE` or `ALTER` permission is
granted on a shared database and the database has a location property that points to a
registered location, you must also grant data location permissions on the location.

To grant data location permissions on a shared location to a principal in your
account, your account must have been granted the `DATA_LOCATION_ACCESS`
permission on the location with the grant option. When you then grant
`DATA_LOCATION_ACCESS` to another principal in your account, you must include
the Data Catalog ID (AWS account ID) of the owner account. The owner account is the account
that registered the location.

You can use the AWS Lake Formation console, the API, or the AWS Command Line Interface (AWS CLI to grant data
location permissions.

###### To grant permissions on a data location shared with your account (console)

- Follow the steps in [Granting data location permissions (same
  account)](granting-location-permissions-local.md "granting-location-permissions-local.md").

For **Storage locations**, you must type the locations. For
**Registered account location**, enter the AWS account ID of the
owner account.

###### To grant permissions on a data location shared with your account (AWS CLI)

- Enter one of the following commands to grant permissions to either a user or a
  role.

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=arn:aws:iam::`<account-id>`:user/`<user-name>` --permissions "DATA_LOCATION_ACCESS" --resource '{ "DataLocation": {"CatalogId":"`<owner-account-ID>`","ResourceArn":"arn:aws:s3:::`<s3-location>`"}}'
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=arn:aws:iam::`<account-id>`:role/`<role-name>` --permissions "DATA_LOCATION_ACCESS" --resource '{ "DataLocation": {"CatalogId":"`<owner-account-ID>`","ResourceArn":"arn:aws:s3:::`<s3-location>`"}}'
```
