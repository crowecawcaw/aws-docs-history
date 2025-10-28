# Create a table for an

organization wide trail using manual partitioning

To create a table for organization wide CloudTrail log files in Athena, follow the steps in
[Create a table for CloudTrail logs in Athena using
manual partitioning](create-cloudtrail-table.md "create-cloudtrail-table.md"),
but make the modifications noted in the following procedure.

###### To create an Athena table for

organization wide CloudTrail logs

1. In the `CREATE TABLE` statement, modify the `LOCATION`
   clause to include the organization ID, as in the following example:

```
LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`organization_id`/'
```

2. In the `PARTITIONED BY` clause, add an entry for the account ID as
   a string, as in the following example:

```
PARTITIONED BY (account string, region string, year string, month string, day string)
```

The following example shows the combined result:

```
...

PARTITIONED BY (account string, region string, year string, month string, day string)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS INPUTFORMAT 'com.amazon.emr.cloudtrail.CloudTrailInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`organization_id`/`Account_ID`/CloudTrail/'
```

3. In the `ALTER TABLE` statement `ADD PARTITION` clause,
   include the account ID, as in the following example:

```
ALTER TABLE table_name ADD
PARTITION (account='`111122223333`',
region='us-east-1',
year='2022',
month='08',
day='08')
```

4. In the `ALTER TABLE` statement `LOCATION` clause,
   include the organization ID, the account ID, and the partition that you want to
   add, as in the following example:

```
LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`organization_id`/`Account_ID`/CloudTrail/us-east-1/2022/08/08/'
```

The following example `ALTER TABLE` statement shows the combined
result:

```
ALTER TABLE table_name ADD
PARTITION (account='`111122223333`',
region='us-east-1',
year='2022',
month='08',
day='08')
LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`organization_id`/`111122223333`/CloudTrail/us-east-1/2022/08/08/'
```

Note that, in a large organization, using this method to manually add and maintain a
partition for each organization account ID can be cumbersome. In such a scenario,
consider using CloudTrail Lake rather than Athena. CloudTrail Lake in such a scenario offers the
following advantages:

- Automatically aggregates logs across an entire organization
- Does not require setting up or maintaining partitions or an Athena table
- Queries are run directly in the CloudTrail console
- Uses a SQL-compatible query language
  For more information, see [Working with AWS CloudTrail
  Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.
