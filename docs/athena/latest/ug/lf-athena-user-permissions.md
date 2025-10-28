# Manage Lake Formation and Athena user

permissions

Lake Formation vends credentials to query Amazon S3 data stores or federated catalogs that are
registered with Lake Formation. If you previously used IAM policies to allow or deny permissions
to read catalogs or data locations in Amazon S3, you can use Lake Formation permissions instead.
However, other IAM permissions are still required.

Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The following sections summarize the permissions required to use Athena to query data
registered in Lake Formation. For more information, see [Security in AWS Lake Formation](../../../lake-formation/latest/dg/security.md "../../../lake-formation/latest/dg/security.md") in the
_AWS Lake Formation Developer Guide_.

###### Permissions Summary

- [Identity-based
  permissions for Lake Formation and Athena](#lf-athena-user-permissions-identity-based "#lf-athena-user-permissions-identity-based")
- [Amazon S3
  permissions for Athena query results locations](#lf-athena-user-permissions-query-results-locations "#lf-athena-user-permissions-query-results-locations")
- [Athena workgroup memberships to query history](#lf-athena-user-permissions-workgroup-memberships-query-history "#lf-athena-user-permissions-workgroup-memberships-query-history")
- [Lake Formation permissions to data](#lf-athena-user-permissions-data "#lf-athena-user-permissions-data")
- [IAM permissions to write to
  Amazon S3 locations](#lf-athena-user-permissions-s3-write "#lf-athena-user-permissions-s3-write")
- [Permissions to encrypted
  data, metadata, and Athena query results](#lf-athena-user-permissions-encrypted "#lf-athena-user-permissions-encrypted")
- [Resource-based
  permissions for Amazon S3 buckets in external accounts (optional)](#lf-athena-user-permissions-s3-cross-account "#lf-athena-user-permissions-s3-cross-account")

## Identity-based

permissions for Lake Formation and Athena

Anyone using Athena to query data registered with Lake Formation must have an IAM
permissions policy that allows the `lakeformation:GetDataAccess` action.
The [AWS managed policy:
AmazonAthenaFullAccess](managed-policies.md#amazonathenafullaccess-managed-policy "managed-policies.md#amazonathenafullaccess-managed-policy") allows this action. If
you use inline policies, be sure to update permissions policies to allow this
action.

In Lake Formation, a _data lake administrator_ has permissions to create
metadata objects such as databases and tables, grant Lake Formation permissions to other
users, and register new Amazon S3 locations or data catalogs. To register new locations,
permissions to the service-linked role for Lake Formation are required. For more information,
see [Create
a data lake administrator](../../../lake-formation/latest/dg/getting-started-setup.md#create-data-lake-admin "../../../lake-formation/latest/dg/getting-started-setup.md#create-data-lake-admin") and [Service-linked role permissions for Lake Formation](../../../lake-formation/latest/dg/service-linked-roles.md#service-linked-role-permissions "../../../lake-formation/latest/dg/service-linked-roles.md#service-linked-role-permissions") in the _AWS Lake Formation
Developer Guide_.

A Lake Formation user can use Athena to query databases, tables, table columns, and
underlying Amazon S3 data stores or catalogs based on Lake Formation permissions granted to them by
data lake administrators. Users cannot create databases or tables, or register new
Amazon S3 locations with Lake Formation. For more information, see [Create a data lake
user](../../../lake-formation/latest/dg/cloudtrail-tut-create-lf-user.md "../../../lake-formation/latest/dg/cloudtrail-tut-create-lf-user.md") in the _AWS Lake Formation Developer Guide_.

In Athena, identity-based permissions policies, including those for Athena
workgroups, still control access to Athena actions for Amazon Web Services account users. In
addition, federated access might be provided through the SAML-based authentication
available with Athena drivers. For more information, see [Use workgroups to control query
access and costs](workgroups-manage-queries-control-costs.md "workgroups-manage-queries-control-costs.md"), [Use IAM policies to control workgroup
access](workgroups-iam-policy.md "workgroups-iam-policy.md"), and
[Enable federated access to the Athena API](access-federation-saml.md "access-federation-saml.md").

For more information, see [Granting Lake Formation
permissions](../../../lake-formation/latest/dg/lake-formation-permissions.md "../../../lake-formation/latest/dg/lake-formation-permissions.md") in the _AWS Lake Formation Developer Guide_.

## Amazon S3

permissions for Athena query results locations

The query results locations in Amazon S3 for Athena cannot be registered with Lake Formation. Lake Formation permissions don't limit access to these locations. Unless you limit access, Athena users can access query result files and metadata when they don't have Lake Formation permissions for the data. To avoid this, we recommend that you use workgroups to specify the location for query results and align workgroup membership with Lake Formation permissions. You can then use IAM permissions policies to limit access to query results locations. For more information about query results, see [Work with query results and recent queries](querying.md "querying.md").

## Athena workgroup memberships to query history

Athena query history exposes a list of saved queries and complete query strings. Unless you use workgroups to separate access to query histories, Athena users who are not authorized to query data in Lake Formation are able to view query strings run on that data, including column names, selection criteria, and so on. We recommend that you use workgroups to separate query histories, and align Athena workgroup membership with Lake Formation permissions to limit access. For more information, see [Use workgroups to control query
access and costs](workgroups-manage-queries-control-costs.md "workgroups-manage-queries-control-costs.md").

## Lake Formation permissions to data

In addition to the baseline permission to use Lake Formation, Athena users must have Lake Formation
permissions to access resources that they query. These permissions are granted and
managed by a Lake Formation administrator. For more information, see [Security and access control to metadata and data](../../../lake-formation/latest/dg/security-data-access.md#security-data-access-permissions "../../../lake-formation/latest/dg/security-data-access.md#security-data-access-permissions") in the
_AWS Lake Formation Developer Guide_.

## IAM permissions to write to

Amazon S3 locations

Lake Formation permissions to Amazon S3 do not include the ability to write to Amazon S3.
Create Table As Statements (CTAS) require write access to the Amazon S3 location of tables. To run CTAS queries on data registered with Lake Formation, Athena users must have IAM permissions to write to the table Amazon S3 locations in addition to the appropriate Lake Formation permissions to read the data locations. For more information, see [Create a table from query results (CTAS)](ctas.md "ctas.md").

## Permissions to encrypted

data, metadata, and Athena query results

Underlying source data in Amazon S3 and metadata in the catalog that is registered with
Lake Formation can be encrypted. There is no change to the way that Athena handles encryption
of query results when using Athena to query data registered with Lake Formation. For more
information, see [Encrypt Athena query results
stored in Amazon S3](encrypting-query-results-stored-in-s3.md "encrypting-query-results-stored-in-s3.md").

- Encrypting source data – Encryption
  of Amazon S3 data locations source data is supported. Athena users who query
  encrypted Amazon S3 locations that are registered with Lake Formation need permissions to
  encrypt and decrypt data. For more information about requirements, see [Supported Amazon S3 encryption
  options](encryption.md#encryption-options-S3-and-Athena "encryption.md#encryption-options-S3-and-Athena") and [Permissions to
  encrypted data in Amazon S3](encryption.md#permissions-for-encrypting-and-decrypting-data "encryption.md#permissions-for-encrypting-and-decrypting-data").
- Encrypting metadata – Encrypting
  metadata in the AWS Glue Data Catalog is supported. For principals using Athena,
  identity-based policies must allow the `"kms:GenerateDataKey"`,
  `"kms:Decrypt"`, and `"kms:Encrypt"` actions for
  the key used to encrypt metadata. For more information, see [Encrypting your
  Data Catalog](../../../glue/latest/dg/encrypt-glue-data-catalog.md "../../../glue/latest/dg/encrypt-glue-data-catalog.md") in the _AWS Glue Developer Guide_ and [Configure access from Athena to
  encrypted metadata in the AWS Glue Data Catalog](access-encrypted-data-glue-data-catalog.md "access-encrypted-data-glue-data-catalog.md").

## Resource-based

permissions for Amazon S3 buckets in external accounts (optional)

To query an Amazon S3 data location in a different account, a resource-based IAM
policy (bucket policy) must allow access to the location. For more information, see
[Configure cross-account access in Athena to Amazon S3
buckets](cross-account-permissions.md "cross-account-permissions.md").

For information about accessing catalogs in another account, see [Option A: Configure
cross-account Data Catalog access in Athena](lf-athena-limitations-cross-account.md#lf-athena-limitations-cross-account-glue "lf-athena-limitations-cross-account.md#lf-athena-limitations-cross-account-glue").
