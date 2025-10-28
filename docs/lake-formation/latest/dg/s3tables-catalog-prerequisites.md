#

Prerequisites for integrating Amazon S3 tables catalog with the Data Catalog and Lake Formation

Following are the prerequisites to enable Amazon S3 table integration with AWS Glue Data Catalog and AWS Lake Formation.

1. The AWS analytics services integration process has been updated. If you've set up the
   integration with the preview release, you can continue to use your current integration.
   However, the updated integration process provides performance improvements. To update the
   integration:
   1. First, delete your existing S3 tables catalog in Lake Formation. To delete the
      catalog, select the `S3tablescatalog` catalog from the catalogs list, and choose
      **Delete** from **Actions**.
   2. Next, deregister the data location for the `S3tablescatalog`.
      1. On the Lake Formation console, under the **Administrations** section, choose **Data Locations**.
      2. Select a location, and from the **Actions** menu, choose
         **Remove**.
      3. When prompted for confirmation, choose **Remove**.

      For detailed instructions on deregistering a data location, see, the [Deregistering an Amazon S3 location](unregister-location.md "unregister-location.md") section. 4. Then, follow the updated integration steps in the [Enabling Amazon S3 Tables integration](enable-s3-tables-catalog-integration.md "enable-s3-tables-catalog-integration.md") secton.

2. When you enable the Amazon S3 tables integration, Lake Formation automatically registers the S3 tables'
   location. To register the table bucket location with Lake Formation, you need an IAM role/user with
   `lakeformation:RegisterResource`,
   `lakeformation:RegisterResourceWithPrivilegedAccess`, and
   `lakeformation:CreateCatalog` permissions. When a non-administrator user with
   these permissions registers a catalog location, Lake Formation automatically grants them
   the `DATA_LOCATION_ACCESS` permission for that location allowing the calling
   principal the permissions to perform all supported Lake Formation operations on the
   registered data location.
3. When you enable the S3 tables integration, you need to choose an IAM role for Lake Formation to vend credentials to allow data access.
   Create an IAM role for Lake Formation data access to your S3 table buckets. The IAM role used when registering the table bucket with Lake Formation requires the following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LakeFormationPermissionsForS3ListTableBucket",
 "Effect": "Allow",
 "Action": [
 "s3tables:ListTableBuckets"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "LakeFormationDataAccessPermissionsForS3TableBucket",
 "Effect": "Allow",
 "Action": [
 "s3tables:CreateTableBucket",
 "s3tables:GetTableBucket",
 "s3tables:CreateNamespace",
 "s3tables:GetNamespace",
 "s3tables:ListNamespaces",
 "s3tables:DeleteNamespace",
 "s3tables:DeleteTableBucket",
 "s3tables:CreateTable",
 "s3tables:DeleteTable",
 "s3tables:GetTable",
 "s3tables:ListTables",
 "s3tables:RenameTable",
 "s3tables:UpdateTableMetadataLocation",
 "s3tables:GetTableMetadataLocation",
 "s3tables:GetTableData",
 "s3tables:PutTableData"
 ],
 "Resource": [
 "arn:aws:s3tables:us-east-1:123456789012:bucket/*"
 ]
 }
 ]
}`

```

For more information, see [Requirements for roles used to register
locations](registration-role.md "registration-role.md"). 4. Add the following trust policy to the IAM role to allow the Lake Formation service to assume the role and vend temporary credentials to the integrated analytical engines.

```
{
  "Effect": "Allow",
  "Principal": {
    "Service": "lakeformation.amazonaws.com"
  },
  "Action": [
    "sts:AssumeRole",
    "sts:SetSourceIdentity",
    "sts:SetContext"  # add action to trust relationship when using IAM Identity center principals with Lake Formation
  ]
}
```
