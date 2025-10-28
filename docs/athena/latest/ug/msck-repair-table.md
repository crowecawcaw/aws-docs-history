# MSCK REPAIR TABLE

Use the `MSCK REPAIR TABLE` command to update the metadata in the catalog after
you add Hive compatible partitions.

The `MSCK REPAIR TABLE` command scans a file system such as Amazon S3 for Hive
compatible partitions that were added to the file system after the table was created.
`MSCK REPAIR TABLE` compares the partitions in the table metadata and the
partitions in S3. If new partitions are present in the S3 location that you specified when
you created the table, it adds those partitions to the metadata and to the Athena
table.

When you add physical partitions, the metadata in the catalog becomes inconsistent with
the layout of the data in the file system, and information about the new partitions needs to
be added to the catalog. To update the metadata, run `MSCK REPAIR TABLE` so that
you can query the data in the new partitions from Athena.

###### Note

`MSCK REPAIR TABLE` only adds partitions to metadata; it does not remove
them. To remove partitions from metadata after the partitions have been manually deleted
in Amazon S3, run the command `ALTER TABLE `table-name` DROP
 PARTITION`. For more information see [ALTER TABLE DROP
PARTITION](alter-table-drop-partition.md "alter-table-drop-partition.md").

## Considerations and

limitations

When using `MSCK REPAIR TABLE`, keep in mind the following points:

- It is possible it will take some time to add all partitions. If this operation
  times out, it will be in an incomplete state where only a few partitions are
  added to the catalog. You should run `MSCK REPAIR TABLE` on the same
  table until all partitions are added. For more information, see [Partition your data](partitions.md "partitions.md").
- For partitions that are not compatible with Hive, use [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md") to load the partitions so that
  you can query their data.
- Partition locations to be used with Athena must use the `s3`
  protocol (for example,
  `s3://amzn-s3-demo-bucket/`folder`/`).
  In Athena, locations that use other protocols (for example,
  `s3a://`bucket`/`folder`/`)
  will result in query failures when `MSCK REPAIR TABLE` queries are
  run on the containing tables.
- Because `MSCK REPAIR TABLE` scans both a folder and its subfolders
  to find a matching partition scheme, be sure to keep data for separate tables in
  separate folder hierarchies. For example, suppose you have data for table 1 in
  `s3://amzn-s3-demo-bucket1` and data for table 2 in
  `s3://amzn-s3-demo-bucket1/table-2-data`. If both tables
  are partitioned by string, `MSCK REPAIR TABLE` will add the
  partitions for table 2 to table 1. To avoid this, use separate folder structures
  like `s3://amzn-s3-demo-bucket1` and
  `s3://amzn-s3-demo-bucket2` instead. Note that this
  behavior is consistent with Amazon EMR and Apache Hive.
- Due to a known issue, `MSCK REPAIR TABLE` fails silently when
  partition values contain a colon (`:`) character (for example, when
  the partition value is a timestamp). As a workaround, use [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md").
- `MSCK REPAIR TABLE` does not add partition column names that begin
  with an underscore (\_). To work around this limitation, use [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md").

## Synopsis

```
MSCK REPAIR TABLE table_name
```

## Examples

```
MSCK REPAIR TABLE orders;
```

## Troubleshooting

After you run `MSCK REPAIR TABLE`, if Athena does not add the partitions to
the table in the AWS Glue Data Catalog, check the following:

- AWS Glue access – Make sure that the
  AWS Identity and Access Management (IAM) role has a policy that allows the
  `glue:BatchCreatePartition` action. For more information, see
  [Allow glue:BatchCreatePartition in the IAM policy](#msck-repair-table-troubleshooting-allow-gluebatchcreatepartition-in-the-policy "#msck-repair-table-troubleshooting-allow-gluebatchcreatepartition-in-the-policy") later in this document.
- Amazon S3 access – Make sure that the role
  has a policy with sufficient permissions to access Amazon S3, including the [`s3:DescribeJob`](../../../AmazonS3/latest/API/API_control_DescribeJob.md "../../../AmazonS3/latest/API/API_control_DescribeJob.md") action. For an example of which
  Amazon S3 actions to allow, see the example bucket policy in [Configure cross-account access in Athena to Amazon S3
  buckets](cross-account-permissions.md "cross-account-permissions.md").
- Amazon S3 object key casing – Make sure that
  the Amazon S3 path is in lower case instead of camel case (for example,
  `userid` instead of `userId`), or use `ALTER
TABLE ADD PARTITION` to specify the object key names. For more
  information, see [Change or redefine the Amazon S3 path](#msck-repair-table-troubleshooting-change-or-redefine-the-amazon-s3-path "#msck-repair-table-troubleshooting-change-or-redefine-the-amazon-s3-path") later in this document.
- Query timeouts – `MSCK REPAIR
TABLE` is best used when creating a table for the first time or when
  there is uncertainty about parity between data and partition metadata. If you
  use `MSCK REPAIR TABLE` to add new partitions frequently (for
  example, on a daily basis) and are experiencing query timeouts, consider using
  [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md").
- Partitions missing from file system – If
  you delete a partition manually in Amazon S3 and then run `MSCK REPAIR
TABLE`, you may receive the error message **`Partitions
missing from filesystem`**. This occurs because `MSCK REPAIR
TABLE` doesn't remove stale partitions from table metadata. To remove
  the deleted partitions from table metadata, run [ALTER TABLE DROP
  PARTITION](alter-table-drop-partition.md "alter-table-drop-partition.md") instead. Note that [SHOW
  PARTITIONS](show-partitions.md "show-partitions.md") similarly lists only the partitions in metadata, not the
  partitions in the file system.
- "NullPointerException name is null"
  error

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

The following sections provide some additional detail.

### Allow glue:BatchCreatePartition in the IAM policy

Review the IAM policies attached to the role that you're using to run `MSCK
 REPAIR TABLE`. When you [use the AWS Glue Data Catalog with Athena](data-sources-glue.md "data-sources-glue.md"), the IAM
policy must allow the `glue:BatchCreatePartition` action. For an example
of an IAM policy that allows the `glue:BatchCreatePartition` action,
see [AWS managed policy:
AmazonAthenaFullAccess](managed-policies.md#amazonathenafullaccess-managed-policy "managed-policies.md#amazonathenafullaccess-managed-policy").

### Change or redefine the Amazon S3 path

If one or more object keys in the Amazon S3 path are in camel case instead of lower
case, `MSCK REPAIR TABLE` might not add the partitions to the
AWS Glue Data Catalog. For example, if your Amazon S3 path includes the object key name
`userId`, the following partitions might not be added to the
AWS Glue Data Catalog:

```
s3://amzn-s3-demo-bucket/path/userId=1/

s3://amzn-s3-demo-bucket/path/userId=2/

s3://amzn-s3-demo-bucket/path/userId=3/
```

To resolve this issue, do one of the following:

- Use lower case instead of camel case when you create your Amazon S3 object
  keys:

```
s3://amzn-s3-demo-bucket/path/userid=1/

s3://amzn-s3-demo-bucket/path/userid=2/

s3://amzn-s3-demo-bucket/path/userid=3/
```

- Use [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md") to redefine the location, as
  in the following example:

```
ALTER TABLE table_name ADD [IF NOT EXISTS]
PARTITION (userId=1)
LOCATION 's3://amzn-s3-demo-bucket/path/userId=1/'
PARTITION (userId=2)
LOCATION 's3://amzn-s3-demo-bucket/path/userId=2/'
PARTITION (userId=3)
LOCATION 's3://amzn-s3-demo-bucket/path/userId=3/'
```

Note that although Amazon S3 object key names can use upper case, Amazon S3 bucket names
themselves must always be in lower case. For more information, see [Object
key naming guidelines](../../../AmazonS3/latest/userguide/object-keys.md#object-key-guidelines "../../../AmazonS3/latest/userguide/object-keys.md#object-key-guidelines") and [Bucket naming
rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md "../../../AmazonS3/latest/userguide/bucketnamingrules.md") in the _Amazon S3 User Guide_.
