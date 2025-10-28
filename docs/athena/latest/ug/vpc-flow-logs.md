# Query Amazon VPC flow logs

Amazon Virtual Private Cloud flow logs capture information about the IP traffic going to and from network
interfaces in a VPC. Use the logs to investigate network traffic patterns and identify
threats and risks across your VPC network.

To query your Amazon VPC flow logs, you have two options:

######

- Amazon VPC Console – Use the Athena integration
  feature in the Amazon VPC Console to generate an AWS CloudFormation template that creates an Athena
  database, workgroup, and flow logs table with partitioning for you. The template
  also creates a set of [predefined
  flow log queries](../../../vpc/latest/userguide/flow-logs-athena.md#predefined-queries "../../../vpc/latest/userguide/flow-logs-athena.md#predefined-queries") that you can use to obtain insights about the traffic
  flowing through your VPC.

For information about this approach, see [Query flow logs using
Amazon Athena](../../../vpc/latest/userguide/flow-logs-athena.md "../../../vpc/latest/userguide/flow-logs-athena.md") in the _Amazon VPC User Guide_.

- Amazon Athena console – Create your tables and
  queries directly in the Athena console. For more information, continue reading this
  page.
  Before you begin querying the logs in Athena, [enable VPC flow
  logs](../../../AmazonVPC/latest/UserGuide/flow-logs.md "../../../AmazonVPC/latest/UserGuide/flow-logs.md"), and configure them to be saved to your Amazon S3 bucket. After you create the
  logs, let them run for a few minutes to collect some data. The logs are created in a GZIP
  compression format that Athena lets you query directly.

When you create a VPC flow log, you can use a custom format when you want to specify the
fields to return in the flow log and the order in which the fields appear. For more
information about flow log records, see [Flow log records](../../../vpc/latest/userguide/flow-logs.md#flow-log-records "../../../vpc/latest/userguide/flow-logs.md#flow-log-records") in the
_Amazon VPC User Guide_.

## Considerations and

limitations

When you create tables in Athena for Amazon VPC flow logs, remember the following
points:

- By default, in Athena, Parquet will access columns by name. For more
  information, see [Handle schema updates](handling-schema-updates-chapter.md "handling-schema-updates-chapter.md").
- Use the names in the flow log records for the column names in Athena. The names
  of the columns in the Athena schema should exactly match the field names in the
  Amazon VPC flow logs, with the following differences:
  - Replace the hyphens in the Amazon VPC log field names with underscores in
    the Athena column names. For information about acceptable characters for
    database names, table names, and column names in Athena, see [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md").
  - Escape the flow log record names that are [reserved
    keywords](reserved-words.md "reserved-words.md") in Athena by enclosing them with backticks.

- VPC flow logs are AWS account specific. When you publish your log files to
  Amazon S3, the path that Amazon VPC creates in Amazon S3 includes the ID of the AWS account
  that was used to create the flow log. For more information, see [Publish
  flow logs to Amazon S3](../../../vpc/latest/userguide/flow-logs-s3.md "../../../vpc/latest/userguide/flow-logs-s3.md") in the _Amazon VPC User Guide_.

###### Topics

- [Create a table for Amazon VPC flow
  logs and query it](vpc-flow-logs-create-table-statement.md "vpc-flow-logs-create-table-statement.md")
- [Create tables for flow logs in Apache Parquet
  format](vpc-flow-logs-parquet.md "vpc-flow-logs-parquet.md")
- [Create and query a table for Amazon VPC
  flow logs using partition projection](vpc-flow-logs-partition-projection.md "vpc-flow-logs-partition-projection.md")
- [Create tables for
  flow logs in Apache Parquet format using partition projection](vpc-flow-logs-partition-projection-parquet-example.md "vpc-flow-logs-partition-projection-parquet-example.md")
- [Additional
  resources](query-examples-vpc-logs-additional-resources.md "query-examples-vpc-logs-additional-resources.md")
