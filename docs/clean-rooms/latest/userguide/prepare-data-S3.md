# Preparing data tables in Amazon S3

You can analyze data tables that have been cataloged in AWS Glue and stored in Amazon S3. If
your data tables are already cataloged in AWS Glue, skip to [Creating a configured table in
AWS Clean Rooms](create-configured-table.md "create-configured-table.md").

###### Important

When preparing your data in Amazon S3 for use with AWS Clean Rooms, you must ensure that your
AWS Glue table location exactly matches the directory path where your data files are
stored.

For example: If your data is stored in
`s3://mybucket/folder/subfolder/data.parquet`, your AWS Glue table
location must point to ``s3://mybucket/folder/subfolder/`. Setting the
 table location to a parent directory (``s3://mybucket/folder/``) will
result in the table appearing empty when queried.

Preparing your data tables in Amazon S3 involves the following steps:

###### Topics

- [Step 1: Complete the prerequisites](#prep-data-tables-prereq "#prep-data-tables-prereq")
- [Step 2: (Optional) Prepare your data for
  cryptographic computing](#optional-encrypt "#optional-encrypt")
- [Step 3: Upload your data table to Amazon S3](#upload-to-s3 "#upload-to-s3")
- [Step 4: Create an AWS Glue table](#create-glue-crawler "#create-glue-crawler")
- [Step 5: Next steps](#prepare-data-S3-next "#prepare-data-S3-next")

## Step 1: Complete the prerequisites

To prepare your data tables for use with AWS Clean Rooms, you must complete the
following prerequisites:

- Your data tables are saved as one of the [supported data formats for AWS Clean Rooms](data-formats.md "data-formats.md").
- Your data tables are cataloged in AWS Glue and use the [supported data types for AWS Clean Rooms](data-formats.md#data-types "data-formats.md#data-types").
- All of your data tables are stored in Amazon Simple Storage Service (Amazon S3) in the same
  AWS Region in which the collaboration was created.
- The AWS Glue Data Catalog must be in the same Region as the collaboration.
- The AWS Glue Data Catalog is in the same AWS account as the membership.
- The Amazon S3 bucket isn't registered with AWS Lake Formation.

## Step 2: (Optional) Prepare your data for

cryptographic computing

(Optional) If you're using cryptographic computing and your data table contains
sensitive information that you want to encrypt, you must encrypt the data table
using the C3R encryption client.

To prepare your data for cryptographic computing, follow the procedures in [Preparing encrypted data tables with Cryptographic Computing for Clean Rooms](prepare-encrypted-data.md "prepare-encrypted-data.md").

## Step 3: Upload your data table to Amazon S3

###### Note

If you intend to use encrypted data tables in the collaboration, you must
first encrypt the data for cryptographic computing before you upload your data
table to Amazon S3. For more information, see [Preparing encrypted data tables with Cryptographic Computing for Clean Rooms](prepare-encrypted-data.md "prepare-encrypted-data.md").

###### To upload your data table to Amazon S3

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Buckets**, and then choose a bucket where you
   want to store your data table.
3. Choose **Upload**, and then follow the prompts.
4. Choose the **Objects** tab to view the prefix where your
   data is stored. Make a note of the name of the folder.

You can select the folder to view the data.

## Step 4: Create an AWS Glue table

If you already have an AWS Glue data table, you can skip this step.

In this step, you set up a crawler in AWS Glue that crawls all the files in your S3
bucket and creates an AWS Glue table. For more information, see [Defining crawlers in
AWS Glue](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") in the _AWS Glue User Guide_.

For more information about supported AWS Glue Data Catalog data types, see [Supported data types](data-formats.md#data-types "data-formats.md#data-types").

###### Note

AWS Clean Rooms doesn't currently support S3 buckets registered with
AWS Lake Formation.

The following procedure describes how to create an AWS Glue table. If you want to use
an encrypted AWS Glue Data Catalog object with an AWS Key Management Service (AWS KMS) key, you need to configure
the KMS key permissions policy to allow access to that encrypted table. For more
information, see [Setting
up encryption in AWS Glue](../../../glue/latest/dg/set-up-encryption.md "../../../glue/latest/dg/set-up-encryption.md") in the _AWS Glue Developer
Guide_.

###### To create an AWS Glue table

1. Follow the [Working with crawlers on the AWS Glue console](../../../glue/latest/dg/console-crawlers.md "../../../glue/latest/dg/console-crawlers.md")
   procedure in the _AWS Glue User Guide_.
2. Make a note of the AWS Glue database name and AWS Glue table name.

## Step 5: Next steps

Now that you have prepared your data tables in Amazon S3, you are ready to:

- [Create a configured
  table](create-configured-table.md "create-configured-table.md")
- [Create an ML
  model](working-with-machine-learning-tdp.md "working-with-machine-learning-tdp.md")

The tables can be queried after:

- The collaboration creator has set up a collaboration in AWS Clean Rooms. For
  more information, see [Creating a collaboration](create-collaboration.md "create-collaboration.md").
- The collaboration creator has sent the collaboration ID to you as a
  participant in the collaboration.
