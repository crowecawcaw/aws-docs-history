# Implicit Lake Formation permissions

AWS Lake Formation grants the following implicit permissions to data lake administrators, database
creators, and table creators.

**Data lake administrators**

- Have `Describe` access to all resources in the Data Catalog except for resources
  shared from another account directly to a different principal. This access cannot be
  revoked from an administrator.
- Have data location permissions everywhere in the data lake.
- Can grant or revoke access to any resources in the Data Catalog to any principal
  (including self). This access cannot be revoked from an administrator.
- Can create databases in the Data Catalog.
- Can grant the permission to create a database to another user.

###### Note

Data lake administrators can register Amazon S3 locations only if they have IAM
permissions to do so. The suggested data lake administrator policies in this guide
grant those permissions. Also, data lake administrators do not have implicit
permissions to drop databases or alter/drop tables created by others. However, they
can grant themselves permissions to do so.

For more information about data lake administrators, see [Create a data lake administrator](initial-lf-config.md#create-data-lake-admin "initial-lf-config.md#create-data-lake-admin").

**Catalog creators**

- Have all catalog permissions on catalogs that they create, have permissions
  on databases and tables that they create in the catalog, and can grant other principals in the
  same AWS account permission to create databases and tables in the catalog. A catalog creator
  who also has the `AWSLakeFormationCrossAccountManager` AWS managed
  policy can grant permissions on the catalog to other AWS accounts or
  organizations.

Data lake administrators can use the Lake Formation console or API to designate catalog
creators.

###### Note

Catalog creators do not implicitly have permissions on databases and tables that others
create in the catalog.

For more information on creating catalogs, see [Bringing your data into the AWS Glue Data Catalog](bring-your-data-overview.md "bring-your-data-overview.md").

**Database creators**

- Have all database permissions on databases that they create, have permissions
  on tables that they create in the database, and can grant other principals in the
  same AWS account permission to create tables in the database. A database creator
  who also has the `AWSLakeFormationCrossAccountManager` AWS managed
  policy can grant permissions on the database to other AWS accounts or
  organizations.

Data lake administrators can use the Lake Formation console or API to designate database
creators.

###### Note

Database creators do not implicitly have permissions on tables that others
create in the database.

For more information, see [Creating a database](creating-database.md "creating-database.md").

**Table creators**

- Have all permissions on tables that they create.
- Can grant permissions on all tables that they create to principals in the same
  AWS account.
- Can grant permissions on all tables that they create to other AWS accounts
  or organizations if they have the `AWSLakeFormationCrossAccountManager`
  AWS managed policy.
- Can view the databases that contain the tables that they create.
