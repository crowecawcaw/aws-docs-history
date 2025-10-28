# Fine-grained access control to data

In the current release of Amazon SageMaker Unified Studio, fine-grained access control of your data is supported
so you can have granular access control over your sensitive data. You can control which
project can access specific records of data within your data assets published to the
Amazon SageMaker Unified Studio business data catalog. Amazon SageMaker Unified Studio supports row and column filters to implement
fine-grained access control.

Use **row filters** to restrict access to specific rows based
on the criteria you define. For example, if your table contains data for two regions
(America and Europe) and you want to ensure that employees in Europe can only access data
relevant to their region, you can create a row filter that includes rows where the region is
Europe (`region = 'Europe'`). This way, employees in Europe won't have access to
America’s data.

Use **column filters** to limit access to specific columns
within your data assets. For example, if your table includes sensitive information such as
Personally Identifiable Information (PII), you can create a column filter to exclude PII
columns. This ensures that subscribers can only access non-sensitive data.

To utilize fine-grained access control, you can create row and column filters for your
AWS Glue and Amazon Redshift assets in Amazon SageMaker Unified Studio. When you receive a subscription request
to access your data assets, you can approve it by applying the appropriate row and column
filters. Amazon SageMaker Unified Studio ensures that the subscriber can only access the rows and columns
permitted by the filters you applied at the time of subscription approval.

###### Topics

- [Limitations](#fine-grained-data-limitations "#fine-grained-data-limitations")
- [Create
  row filters in Amazon SageMaker Unified Studio](create-row-filter.md "create-row-filter.md")
- [Create column filters in Amazon SageMaker Unified Studio](create-column-filter.md "create-column-filter.md")
- [Delete row or column filters in Amazon SageMaker Unified Studio](delete-row-column-filter.md "delete-row-column-filter.md")
- [Edit row or column filters in Amazon SageMaker Unified Studio](edit-row-column-filter.md "edit-row-column-filter.md")
- [Grant access with filters in Amazon SageMaker Unified Studio](grant-access-with-filters.md "grant-access-with-filters.md")

## Limitations

When configuring row or column level filters for fine-grained access control,
filtering on columns whose name contains special characters impacts
which compute types can access the data.

- In cases where the column name contains special characters,
  adding an Asset Filter will automatically add double quotes “ ” around
  the column name to escape the special characters.

As a result, the asset is not accessible by data processing compute
engines such as EMR-EC2, EMR-Serverless, or Glue-ETL.
This asset is still accessible by other compute engines.

To remove this limitation, either remove the filters on the
column names containing special characters or rename the column
to remove the special characters and recreate the filter.
