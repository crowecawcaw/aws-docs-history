# Prerequisites for creating views

- To create views in Data Catalog, you must register the underlying Amazon S3 data
  locations of the reference tables with Lake Formation. For details on registering data
  with Lake Formation, see [Adding an Amazon S3 location to your data lake](register-data-lake.md "register-data-lake.md").
- Only IAM roles can create Data Catalog views. Other IAM identities can't create
  Data Catalog views.
- The IAM role that defines the view must have the following
  permissions:
  - Lake Formation `SELECT` permission with the `Grantable`
    option on all reference tables, all columns included.
  - Lake Formation `CREATE_TABLE` permission on the target database where
    views are being created.
  - A trust policy for the Lake Formation and AWS Glue services to assume the role.

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Sid": "DataCatalogViewDefinerAssumeRole1",
   "Effect": "Allow",
   "Principal": {
   "Service": [
   "glue.amazonaws.com",
   "lakeformation.amazonaws.com"
   ]
   },
   "Action": "sts:AssumeRole"
   }
   ]
  }`

  ```

  - The iam:PassRole permission for AWS Glue and Lake Formation.

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Sid": "DataCatalogViewDefinerPassRole1",
   "Action": [
   "iam:PassRole"
   ],
   "Effect": "Allow",
   "Resource": "*",
   "Condition": {
   "StringEquals": {
   "iam:PassedToService": [
   "glue.amazonaws.com",
   "lakeformation.amazonaws.com"
   ]
   }
   }
   }
   ]
  }`

  ```

  - AWS Glue and Lake Formation permissions.

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Allow",
   "Action": [
   "Glue:GetDatabase",
   "Glue:GetDatabases",
   "Glue:CreateTable",
   "Glue:GetTable",
   "Glue:GetTables",
   "Glue:BatchGetPartition",
   "Glue:GetPartitions",
   "Glue:GetPartition",
   "Glue:GetTableVersion",
   "Glue:GetTableVersions",
   "Glue:PassConnection",
   "lakeFormation:GetDataAccess"
   ],
   "Resource": "*"
   }
   ]
  }`

  ```

- You can't create views in a database that has `Super` or
  `ALL` permission granted to the `IAMAllowedPrincipals`
  group. You can either revoke the `Super` permission for the
  `IAMAllowedPrincipals` group on a database, see [Step 4: Switch your data stores to the
  Lake Formation permissions model](upgrade-glue-lake-formation.md#upgrade-glue-lake-formation-step4 "upgrade-glue-lake-formation.md#upgrade-glue-lake-formation-step4"), or create a new
  database with the **Use only IAM access control for new tables in this
  database** box unchecked under **Default permissions for
  newly created tables**.
