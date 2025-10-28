# Prepare input data tables

In AWS Entity Resolution, each of your _input data tables_ contain
source records. These records contain consumer identifiers such as first name, last name, email
address, or phone number. These source records can be matched with other source records that you
provide within the same or other input data tables. Each record must have a unique Record ID
([Unique ID](glossary.md#unique-id-defn "glossary.md#unique-id-defn")) and you must define it as a
primary key while creating a schema mapping within AWS Entity Resolution.

Every input data table is available as an AWS Glue table backed by Amazon S3. You can use your
first-party data already within Amazon S3, or import data tables from other third-party SaaS providers
into Amazon S3. After you upload the data to Amazon S3, you can use an AWS Glue crawler to create a data table
in the AWS Glue Data Catalog. You can then use the data table as an input to AWS Entity Resolution.

The following sections describe how to prepare first-party data and third-party data.

###### Topics

- [Preparing first-party input data](prepare-input-data.md "prepare-input-data.md")
- [Preparing third-party input data](prepare-third-party-input-data.md "prepare-third-party-input-data.md")
