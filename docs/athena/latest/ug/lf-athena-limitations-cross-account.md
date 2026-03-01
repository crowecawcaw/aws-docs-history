# Configure cross-account Data Catalog access

To access a data catalog in another account, you can use Athena's cross-account
AWS Glue feature or set up cross-account access in Lake Formation.

## Option A: Configure cross-account Data Catalog access in Athena

You can use Athena's cross-account AWS Glue catalog feature to register the
catalog in your account. This capability is available only in Athena engine version 2 and later
versions and is limited to same-Region use between accounts. For more
information, see [Register a Data Catalog from another account](data-sources-glue-cross-account.md "data-sources-glue-cross-account.md").

If the Data Catalog to be shared has a resource policy configured in AWS Glue, it
must be updated to allow access to the AWS Resource Access Manager and grant permissions to
Account B to use Account A's Data Catalog.

For more information, see [Configure cross-account access to AWS Glue data catalogs](security-iam-cross-account-glue-catalog-access.md "security-iam-cross-account-glue-catalog-access.md").

## Option B: Configure cross-account access in Lake Formation

AWS Lake Formation lets you use a single account to manage a central Data Catalog. You can
use this feature to implement [cross-account access](../../../lake-formation/latest/dg/access-control-cross-account.md "../../../lake-formation/latest/dg/access-control-cross-account.md") to Data Catalog metadata and underlying data. For
example, an owner account can grant another (recipient) account
`SELECT` permission on a table.

For a shared database or table to appear in the Athena Query Editor, you [create a resource
link](../../../lake-formation/latest/dg/resource-links-about.md "../../../lake-formation/latest/dg/resource-links-about.md") in Lake Formation to the shared database or table. When the recipient
account in Lake Formation queries the owner's table, [CloudTrail](../../../lake-formation/latest/dg/cross-account-logging.md "../../../lake-formation/latest/dg/cross-account-logging.md") adds
the data access event to the logs for both the recipient account and the owner
account.

For shared views, keep in mind the following points:

- Queries are run on target resource links, not on the source table or
  view, and then the output is shared to the target account.
- It is not sufficient to share only the view. All the tables that are
  involved in creating the view must be part of the cross-account
  share.
- The name of the resource link created on the shared resources must
  match the name of the resource in the owner account. If the name does
  not match, an error message like **`Failed analyzing stored view
'awsdatacatalog.`my-lf-resource-link`.`my-lf-view`':
line 3:3: Schema `schema_name` does not
exist`** occurs.

For more information about cross-account access in Lake Formation, see the following
resources in the _AWS Lake Formation Developer Guide_:

[Cross-account access](../../../lake-formation/latest/dg/access-control-cross-account.md "../../../lake-formation/latest/dg/access-control-cross-account.md")

[How resource links
work in Lake Formation](../../../lake-formation/latest/dg/resource-links-about.md "../../../lake-formation/latest/dg/resource-links-about.md")

[Cross-account
CloudTrail logging](../../../lake-formation/latest/dg/cross-account-logging.md "../../../lake-formation/latest/dg/cross-account-logging.md")
