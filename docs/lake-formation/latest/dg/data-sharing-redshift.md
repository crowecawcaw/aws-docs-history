# Managing permissions for data in an Amazon Redshift datashare

With AWS Lake Formation, you can manage data securely in a datashare from Amazon Redshift. Amazon Redshift is a fully
managed, petabyte-scale data warehouse service in the AWS Cloud. Using the data sharing
capability, Amazon Redshift helps you to share data across AWS accounts. For more information about Amazon Redshift
data sharing, see [Overview of data sharing in Amazon Redshift](../../../redshift/latest/dg/data_sharing_intro.md "../../../redshift/latest/dg/data_sharing_intro.md").

In Amazon Redshift, the producer cluster administrator creates a datashare, and shares it with the data
lake administrator. For step-by-step instructions on creating a data lake administrator, see
[Create a data lake administrator](initial-lf-config.md#create-data-lake-admin "initial-lf-config.md#create-data-lake-admin").

After you (data lake administrator) accept the datashare, you must create an AWS Glue Data Catalog
database for the specific datashare. This is so that you can control access to it using Lake Formation
permissions. Lake Formation maps each datashare to a corresponding Data Catalog database. These appear as
federated databases in the Data Catalog.

A database is referred to as a _federated database_ when it points to an entity outside of the
Data Catalog. Tables and views in the Amazon Redshift datashare are listed as individual tables in the Data Catalog.
You can share the federated database with selected IAM principals and SAML users within the
same account or in another account with Lake Formation. You can also include row and column filter
expressions to restrict access to certain data. For more information, see [Data filtering and cell-level security in Lake Formation](data-filtering.md "data-filtering.md").

To provide users access to an Amazon Redshift datashare, you must do the following:

1. Update **Data Catalog settings** to enable Lake Formation permissions.
2. Accept the datashare invitation from the Amazon Redshift producer cluster administrator and register the datashare in Lake Formation.

After completing this step, you can manage the datashare within the Lake Formation Data Catalog. 3. Create a federated database and define permissions on that database. 4. Grant permissions to users on databases and tables. You can share the entire database
or a subset of tables with users in the same account or another account.
For limitations, see [Amazon Redshift data sharing limitations](notes-rs-datashare.md "notes-rs-datashare.md").

###### Topics

- [Prerequisites for setting up permissions on Amazon Redshift datashares](redshift-ds-prereqs.md "redshift-ds-prereqs.md")
- [Setting up permissions for Amazon Redshift datashares](setup-ds-perms.md "setup-ds-perms.md")
- [Querying federated databases](qerying-fed-db.md "qerying-fed-db.md")
