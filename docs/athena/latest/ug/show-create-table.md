# SHOW CREATE TABLE

Analyzes an existing table named `table_name` to generate the query that
created it.

## Synopsis

```
SHOW CREATE TABLE [db_name.]table_name
```

## Parameters

**TABLE [db\_name.]table_name**

The `db_name` parameter is optional. If omitted, the context
defaults to the current database.

###### Note

The table name is required.

## Examples

```
SHOW CREATE TABLE orderclickstoday;
```

```
SHOW CREATE TABLE `salesdata.orderclickstoday`;
```

## Troubleshooting

If you use the AWS Glue [CreateTable](../../../glue/latest/webapi/API_CreateTable.md "../../../glue/latest/webapi/API_CreateTable.md") API operation
or the AWS CloudFormation [`AWS::Glue::Table`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.md") template to create a table for use in Athena without
specifying the `TableType` property and then run a DDL query like
`SHOW CREATE TABLE` or `MSCK REPAIR TABLE`, you can
receive the error message **`FAILED: NullPointerException Name is
 null`**.

To resolve the error, specify a value for the [TableInput](../../../glue/latest/webapi/API_TableInput.md "../../../glue/latest/webapi/API_TableInput.md")
`TableType` attribute as part of the AWS Glue `CreateTable` API
call or [AWS CloudFormation template](../../../AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.md"). Possible values for `TableType` include
`EXTERNAL_TABLE` or `VIRTUAL_VIEW`.

This requirement applies only when you create a table using the AWS Glue
`CreateTable` API operation or the `AWS::Glue::Table`
template. If you create a table for Athena by using a DDL statement or an AWS Glue
crawler, the `TableType` property is defined for
you automatically.
