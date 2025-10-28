# Managing CloudTrail Lake federation resources with AWS Lake Formation

When you federate an event data store, CloudTrail registers the federation role ARN
and event data store in AWS Lake Formation, the service responsible for allowing
fine-grained access control of the federated resources in the AWS Glue Data
Catalog. This section describes how you can use Lake Formation to manage the CloudTrail Lake
federation resources.

When you enable federation, CloudTrail creates the following resources in the AWS Glue Data Catalog.

- **Managed database** – CloudTrail creates 1 database with the name `aws:cloudtrail` per account. CloudTrail manages the database. You
  can't delete or modify the database in AWS Glue.
- **Managed federated table** – CloudTrail creates 1 table for each federated event data store and uses the event data store ID for the table name.
  CloudTrail manages the tables. You can't delete or modify the tables in AWS Glue. To delete a table, you must [disable federation](query-disable-federation.md "query-disable-federation.md") on the event data store.

## Controlling access to federated resources

You can use one of two permissions methods to control access to the
managed database and tables.

- **IAM only access control** – With IAM only access control, all
  users in the account with the required IAM permissions are given access to all Data Catalog resources.
  For information about how AWS Glue works with IAM, see [How AWS Glue works with IAM](../../../glue/latest/dg/security_iam_service-with-iam.md "../../../glue/latest/dg/security_iam_service-with-iam.md").

On the Lake Formation console, this method appears as **Use only IAM access control**.

###### Note

If you want to create data filters and use other Lake Formation
features, you must use Lake Formation access control.

- **Lake Formation access control** – This methods provides the following advantages.
  - You can implement column-level, row-level, and cell-level security by creating [data filters](../../../lake-formation/latest/dg/data-filters-about.md "../../../lake-formation/latest/dg/data-filters-about.md"). For more information, see
    [Securing data lakes with row-level access control](../../../lake-formation/latest/dg/cbac-tutorial.md "../../../lake-formation/latest/dg/cbac-tutorial.md") in the _AWS Lake Formation Developer Guide_.
  - Database and tables are only visible to Lake Formation administrators and creators of the database and resources.
    If another user needs access to these resources, you must explicitly [grant access by using Lake Formation permissions](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md").

For more information about access control, see [Methods for fine-grained access control](../../../lake-formation/latest/dg/access-control-fine-grained.md "../../../lake-formation/latest/dg/access-control-fine-grained.md").

## Determining

the permissions method for a federated resource

When you enable federation for the first time, CloudTrail creates a managed
database and managed federated table using your Lake Formation data lake settings.

After CloudTrail enables federation, you can verify which permissions method you
are using for the managed database and managed federated table by checking
the permissions for those resources. If the `ALL`
(_Super_) to `IAM_ALLOWED_PRINCIPALS`
setting is present for the resource, the resource is managed exclusively by
IAM permissions. If the setting is missing, the resource is managed by
Lake Formation permissions. For more information about Lake Formation permissions, see [Lake Formation
permissions reference](../../../lake-formation/latest/dg/lf-permissions-reference.md "../../../lake-formation/latest/dg/lf-permissions-reference.md").

The permissions method for the managed database and managed federated
table can differ. For example, if you check the values for the database and
table, you could see the following:

- For the database, the value that assigns `ALL` (_Super_) to
  `IAM_ALLOWED_PRINCIPALS` is present in the
  permissions indicating that the you're using IAM only access
  control for the database.
- For the table, the value that assigns `ALL` (_Super_) to
  `IAM_ALLOWED_PRINCIPALS` not present, which indicates access control by Lake Formation permissions.

You can switch between access methods at any time by adding or removing
`ALL` (_Super_) to `IAM_ALLOWED_PRINCIPALS` permission on
any federated resource in Lake Formation.

## Cross-account sharing using Lake Formation

This section describes how to share a managed database and managed
federated table across accounts by using Lake Formation.

You can share a managed database across accounts by taking these steps:

1. Update the [cross-account data sharing version](../../../lake-formation/latest/dg/optimize-ram.md "../../../lake-formation/latest/dg/optimize-ram.md") to version 4.
2. Remove `Super` to `IAM_ALLOWED_PRINCIPALS` permissions from the database if present to switch to Lake Formation access control.
3. Grant `Describe` permissions to the external account on the database.
4. If a Data Catalog resource is shared with your AWS account and your account is not in the same AWS organization as the sharing account,
   accept the resource share invitation from AWS Resource Access Manager (AWS RAM). For more information, see [Accepting a resource share invitation from AWS RAM](../../../lake-formation/latest/dg/accepting-ram-invite.md "../../../lake-formation/latest/dg/accepting-ram-invite.md").

After completing these steps, the database should be visible to the external account. By default, sharing the database does not give access to any tables in the database.

You can share all or individual managed federated tables with an external account by taking these steps:

1. Update the [cross-account data sharing version](../../../lake-formation/latest/dg/optimize-ram.md "../../../lake-formation/latest/dg/optimize-ram.md") to version 4.
2. Remove `Super` to `IAM_ALLOWED_PRINCIPALS` permissions from the table if present to switch to Lake Formation access control.
3. (Optional) Specify any [data filters](../../../lake-formation/latest/dg/data-filters-about.md "../../../lake-formation/latest/dg/data-filters-about.md") to restrict columns or rows.
4. Grant `Select` permissions to the external account on the table.
5. If a Data Catalog resource is shared with your AWS account and your account is not in the same AWS organization as the sharing account,
   accept the resource share invitation from AWS Resource Access Manager (AWS RAM). For an organization, you can auto accept using RAM settings. For more information, see [Accepting a resource share invitation from AWS RAM](../../../lake-formation/latest/dg/accepting-ram-invite.md "../../../lake-formation/latest/dg/accepting-ram-invite.md").
6. The table should now be visible. To enable Amazon Athena queries on this table,
   create a [resource link in this account](../../../lake-formation/latest/dg/create-resource-link-table.md "../../../lake-formation/latest/dg/create-resource-link-table.md") with the shared table.

The owning account can revoke sharing at any point by removing permissions for the external account from Lake Formation,
or by [disabling federation](query-disable-federation.md "query-disable-federation.md") in CloudTrail.
