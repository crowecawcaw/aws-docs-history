Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Redshift Spectrum and AWS Lake Formation

This topic describes how to use Redshift Spectrum with Lake Formation. Lake Formation is a service for sharing analytics data.

You can use AWS Lake Formation to centrally define and enforce database, table, and column-level
access policies to data stored in Amazon S3. After your data is registered with an AWS Glue Data Catalog
enabled with Lake Formation, you can query it by using several services, including Redshift Spectrum.

Lake Formation provides the security and governance of the Data Catalog. Within Lake Formation, you can grant and
revoke permissions to the Data Catalog objects, such as databases, tables, columns, and
underlying Amazon S3 storage.

###### Important

You can only use Redshift Spectrum with a Lake Formation enabled Data Catalog in AWS Regions where Lake Formation is available.
For a list of available Regions, see
[AWS Lake Formation endpoints and quotas](../../../general/latest/gr/lake-formation.md "../../../general/latest/gr/lake-formation.md") in the _AWS General Reference_.

By using Redshift Spectrum with Lake Formation, you can do the following:

- Use Lake Formation as a centralized place where you grant and revoke permissions and access control policies on all of your data in the data lake.
  Lake Formation provides a hierarchy of permissions to control access to databases and tables in a Data Catalog.
  For more information, see
  [Overview of Lake Formation permissions](../../../lake-formation/latest/dg/lake-formation-permissions.md "../../../lake-formation/latest/dg/lake-formation-permissions.md") in the _AWS Lake Formation Developer Guide_.
- Create external tables and run queries on data in the data lake. Before users in your account
  can run queries, a data lake account administrator registers your existing Amazon S3 paths
  containing source data with Lake Formation. The administrator also creates tables and grants
  permissions to your users. Access can be granted on databases, tables, or columns.

The administrator can use data filters in Lake Formation to grant granular access control over your sensitive data stored
in Amazon S3. For more information, see
[Using data filters for row-level and cell-level security](#spectrum-lake-formation-data-filters "#spectrum-lake-formation-data-filters").

After the data is registered in the Data Catalog, each time users try to run queries,
Lake Formation verifies access to the table for that specific principal. Lake Formation vends temporary
credentials to Redshift Spectrum, and the query runs.

- Run Redshift Spectrum queries against an automounted AWS Glue Data Catalog using IAM credentials obtained with `GetCredentials` or `GetClusterCredentials`,
  and manage Lake Formation permissions by database user (IAMR:username or IAM:username).
  When you use Redshift Spectrum with a Data Catalog enabled for Lake Formation, one of the following must be in place:

- An IAM role associated with the
  cluster that has permission to the Data Catalog.
- A federated IAM identity configured to manage access to external resources. For
  more information,
  see [Using a federated identity to manage Amazon Redshift access to local resources and Amazon Redshift external tables](../mgmt/authorization-fas-spectrum.md "../mgmt/authorization-fas-spectrum.md").

###### Important

You can't chain IAM roles when using Redshift Spectrum with a Data Catalog enabled for Lake Formation.

To learn more about the steps required to set up AWS Lake Formation to use with Redshift Spectrum, see
[Tutorial: Creating a data lake from a JDBC source in Lake Formation](../../../lake-formation/latest/dg/getting-started-tutorial-jdbc.md "../../../lake-formation/latest/dg/getting-started-tutorial-jdbc.md") in the _AWS Lake Formation Developer Guide_.
Specifically, see
[Query the data in the data lake using Amazon Redshift Spectrum](../../../lake-formation/latest/dg/tut-query-redshift.md "../../../lake-formation/latest/dg/tut-query-redshift.md")
for details about integration with Redshift Spectrum.
The data and AWS resources used in this topic depend on previous steps in the tutorial.

## Using data filters for row-level and cell-level security

You can define data filters in AWS Lake Formation to control your Redshift Spectrum queries' row-level and cell-level access to data defined in your Data Catalog.
To set this up, you perform the following tasks:

- Create a data filter in Lake Formation with the following information:

      + A column specification with a list of columns to include or exclude from query results.
      + A row filter expression that specifies the rows to include in the query results.

  For more information about how to create a data filter, see
  [Data filters in Lake Formation](../../../lake-formation/latest/dg/data-filters-about.md "../../../lake-formation/latest/dg/data-filters-about.md") in the _AWS Lake Formation Developer Guide_.

- Create an external table in Amazon Redshift that references a table in your Lake Formation enabled Data Catalog.
  For details on how to query a Lake Formation table using Redshift Spectrum, see
  [Query the data in the data lake using Amazon Redshift Spectrum](../../../lake-formation/latest/dg/tut-query-redshift.md "../../../lake-formation/latest/dg/tut-query-redshift.md") in the _AWS Lake Formation Developer Guide_.

After the table is defined in Amazon Redshift, you can query the Lake Formation table and access only the rows and columns that are allowed by the data filter.

For a detailed guide on how to set up row-level and cell-level security in Lake Formation, and then query using Redshift Spectrum, see
[Use Amazon Redshift Spectrum with row-level and cell-level security policies defined in AWS Lake Formation](https://aws.amazon.com/blogs/big-data/use-amazon-redshift-spectrum-with-row-level-and-cell-level-security-policies-defined-in-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/use-amazon-redshift-spectrum-with-row-level-and-cell-level-security-policies-defined-in-aws-lake-formation/").
