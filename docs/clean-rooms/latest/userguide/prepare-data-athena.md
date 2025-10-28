# Preparing data tables in Amazon Athena

You can query data tables that have been created as AWS Glue Data Catalog (GDC) Views in
Amazon Athena.

A GDC View is a virtual table, created from one or more underlying AWS Glue tables. It
must be created using Athena SQL in the Athena `AwsGlueCatalog` catalog.

Preparing your data tables in Amazon Athena involves the following steps:

###### Topics

- [Step 1: Complete the
  prerequisites](#prepare-data-athena-prereq "#prepare-data-athena-prereq")
- [Step 2: (Optional) Prepare your data
  for cryptographic computing](#prepare-data-athena-encrypt "#prepare-data-athena-encrypt")
- [Step 3: Next steps](#prepare-data-athena-next "#prepare-data-athena-next")

## Step 1: Complete the

prerequisites

To prepare your data tables for use with AWS Clean Rooms, you must complete the
following prerequisites:

- Your data tables are saved as one of the [supported data formats for AWS Clean Rooms](data-formats.md "data-formats.md").
- Your data tables use the [supported data types
  for AWS Clean Rooms](data-formats.md#data-types "data-formats.md#data-types").
- You have created a GDC View on your AWS Glue table using Athena SQL in the
  Athena `AwsDataCatalog` catalog.

The view will appear in:

    + The Athena console (under the `AwsDataCatalog`) as a
     View: [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home")
    + The AWS Glue console as a AWS Glue table: [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/")

For more information, see [Use Data Catalog views in Athena](../../../athena/latest/ug/views-glue.md "../../../athena/latest/ug/views-glue.md") in the
_Amazon Athena User Guide_.

###### Note

You need appropriate permissions to create Views in Athena and AWS Glue.
Also, ensure that you have access to the underlying tables referenced in
your View definition.

AWS Clean Rooms only supports the AWS Glue Catalog Type for Athena, not Lambda or
Hive Catalog Types.

- Your data tables or GDC Views are cataloged in AWS Glue and are registered
  with AWS Lake Formation.
- You have created a separate output bucket in Amazon S3 to receive the Athena
  results.
- You have set up a service role to read the data from Amazon Athena. For more
  information, see [Create a service role to read data from
  Amazon Athena](setting-up-roles.md#create-service-role-athena "setting-up-roles.md#create-service-role-athena").
  - The service role has Lake Formation Select and Describe access permissions
    on the GDC View or table.

## Step 2: (Optional) Prepare your data

for cryptographic computing

(Optional) If you're using cryptographic computing and your data table contains
sensitive information that you want to encrypt, you must encrypt the data table
using the C3R encryption client.

To prepare your data for cryptographic computing, follow the procedures in [Preparing encrypted data tables with Cryptographic Computing for Clean Rooms](prepare-encrypted-data.md "prepare-encrypted-data.md").

## Step 3: Next steps

Now that you have prepared your data tables in Amazon Athena, you are ready to:

- [Create a configured
  table](create-configured-table.md "create-configured-table.md")
- [Create an ML
  model](working-with-machine-learning-tdp.md "working-with-machine-learning-tdp.md")

The tables can be queried after:

- The collaboration creator has set up a collaboration in AWS Clean Rooms. For
  more information, see [Creating a collaboration](create-collaboration.md "create-collaboration.md").
- The collaboration creator has sent the collaboration ID to you as a
  participant in the collaboration.
