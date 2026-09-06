

# Migrating from CUR to Data Exports CUR 2.0
<a name="dataexports-migrate"></a>

AWS Data Exports allows you to create exports of Cost and Usage Report 2.0 (CUR 2.0). The CUR 2.0 table provides the same information as Cost and Usage Reports (CUR) along with some improvements. Data Exports enables you to create a CUR 2.0 export that is backwards compatible with the data pipelines you’ve been using to process CUR.

CUR 2.0 provides the following improvements over CUR:
+ **Consistent schema:** CUR 2.0 contains a fixed set of columns, whereas the columns included for CUR can vary monthly depending on your usage of AWS services, cost categories, and resource tags.
+ **Nested data:** CUR 2.0 reduces data sparsity by collapsing certain columns from CUR into individual columns with key-value pairs of the collapsed columns. Optionally, you can query the nested keys in Data Exports as separate columns to match the original CUR schema and data.
+ **Additional columns:** CUR 2.0 contains two additional columns: **bill\_payer\_account\_name**, **line\_item\_usage\_account\_name**, **line\_item\_iam\_principal** and **line\_item\_user\_identifier**.

The following table outlines the differences between CUR 2.0 and legacy CUR in more detail:



|  | CUR 2.0 | Legacy CUR | 
| --- | --- | --- | 
| Data schema | Fixed schema.<br />For the complete column list, see [Cost and Usage Report (CUR) 2.0](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2.html). | Dynamic schema based on AWS usage and activity.<br />For the partial column list, see [Data dictionary](https://docs.aws.amazon.com/cur/latest/userguide/data-dictionary.html). | 
| Exclusive columns | `bill_payer_account_name`<br />`line_item_usage_account_name`<br />`line_item_iam_principal`<br />`line_item_user_identifier` | None | 
| Export customization | Enables basic SQL for column selections, row filtering, and column aliasing (renaming).<br />For details about the supported SQL syntax, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-data-query.html). | Not supported. You must manually set up Athena/QuickSight to create the view you require. | 
| Nested columns with key-value pairs | `resource_tags`<br />`cost_category`<br />`product`<br />`discount` | No nested columns.<br />The four nested columns in CUR 2.0 are split into separate columns in legacy CUR (for example, `resource_tags_user_creator`). | 
| File delivery destination | S3 bucket | S3 bucket | 
| File output formats | ZIP, GZIP, Parquet | ZIP, GZIP, Parquet | 
| Integration with other AWS services | Amazon Athena, Amazon Redshift, Amazon QuickSight | Amazon Athena, Amazon Redshift, Amazon QuickSight | 
| Amazon CloudFormation support | Yes<br />For details, see [AWS Data Exports resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BCMDataExports.html) in the *AWS CloudFormation User Guide*. | Yes<br />For details, see [AWS Cost and Usage Report resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CUR.html) in the *AWS CloudFormation User Guide*. | 
| Tag and cost category data | Resource tags and Cost category names are normalized to remove special characters and spaces. In the event that there are conflicting tags or cost categories after normalization, only one value is kept. For more information, see [Column names](https://docs.aws.amazon.com/cur/latest/userguide/cur-ate-run.html#column-transformations). Tags column, which only exists in CUR 2.0, is not normalized. Select Tags column in place of Resource tags and Cost category columns since Tags contains values from Resource tags and Cost category columns.  | The behavior is different between legacy CUR Parquet and CSV file formats.<br />**Legacy CUR Parquet:** Tag and cost category names are normalized to remove special characters and spaces. In the event that there are conflicting tags or cost categories after normalization, only one value is kept. For more information, see [Column names](https://docs.aws.amazon.com/cur/latest/userguide/cur-ate-run.html#column-transformations).<br />**Legacy CUR CSV:** Tag and cost category names are not changed. | 

For more detailed information about the schema of CUR 2.0, see the [Data Exports table dictionary](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-table-dictionary.html).

You can migrate to CUR 2.0 in Data Exports in two ways:
+ [Method one: Create an export with an SQL query using the CUR schema](https://docs.aws.amazon.com/cur/latest/userguide/data-exports-migrate-one.html)
+ [Method two: Create an export of CUR 2.0 with its new schema](https://docs.aws.amazon.com/cur/latest/userguide/data-exports-migrate-two.html)