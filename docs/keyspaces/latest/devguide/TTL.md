# Expire data with Time to Live (TTL) for Amazon Keyspaces (for Apache Cassandra)

Amazon Keyspaces (for Apache Cassandra) Time to Live (TTL) helps you simplify your application logic and optimize the price of
storage by expiring data from tables automatically. Data that you no longer need is
automatically deleted from your table based on the Time to Live value that you set.

This makes it
easier to comply with data retention policies based on business, industry, or regulatory
requirements that define how long data needs to be retained or specify when data must be
deleted.

For example, you can use TTL in an AdTech application to schedule when data for specific
ads expires and is no longer visible to clients. You can also use TTL to retire older data
automatically and save on your storage costs.

You can set a default TTL value for the entire
table, and overwrite that value for individual rows and columns. TTL operations don't impact
your application's performance. Also, the number of rows and columns marked to expire with
TTL doesn't affect your table's availability.

Amazon Keyspaces automatically filters out expired data so that expired data isn't returned in query
results or available for use in data manipulation language (DML) statements. Amazon Keyspaces typically deletes
expired data from storage within 10 days of the expiration date.

In rare cases, Amazon Keyspaces may not be able
to delete data within 10 days if there is sustained activity on the underlying storage partition
to protect availability. In these cases, Amazon Keyspaces continues to attempt to delete the expired data
once traffic on the partition decreases.

After the data is
permanently deleted from storage, you stop incurring storage fees.

You can set, modify, or disable default TTL settings for new and existing tables by using
the console, Cassandra Query Language (CQL), or the AWS CLI.

On tables with default TTL configured, you
can use CQL statements to override the default TTL settings of the table and apply custom
TTL values to rows and columns. For more information, see [Use the INSERT statement to set custom Time to Live (TTL) values for new rows](TTL-how-to-insert-cql.md "TTL-how-to-insert-cql.md") and [Use the UPDATE statement to edit custom Time to Live (TTL)
settings for rows and columns](TTL-how-to-update-cql.md "TTL-how-to-update-cql.md").

TTL pricing is based on the size of the rows being deleted or updated by using Time to Live. TTL
operations are metered in units of `TTL deletes`. One TTL delete is consumed per
KB of data per row that is deleted or updated.

For example, to update a row that stores 2.5
KB of data and to delete one or more columns within the row at the same time requires three
TTL deletes. Or, to delete an entire row that contains 3.5 KB of data requires four TTL
deletes.

One TTL delete is consumed per KB of deleted data per row. For more information
about pricing, see [Amazon Keyspaces (for Apache Cassandra)
pricing](https://aws.amazon.com/keyspaces/pricing "https://aws.amazon.com/keyspaces/pricing").

###### Topics

- [Amazon Keyspaces Time to Live and integration with AWS
  services](#ttl-howitworks_integration "#ttl-howitworks_integration")
- [Create a new table with default Time to Live (TTL) settings](TTL-how-to-create-table.md "TTL-how-to-create-table.md")
- [Update the default Time to Live (TTL) value of a table](TTL-how-to-update-default.md "TTL-how-to-update-default.md")
- [Create table with custom Time to Live (TTL) settings enabled](TTL-how-to-enable-custom-new.md "TTL-how-to-enable-custom-new.md")
- [Update table with custom Time to Live (TTL)](TTL-how-to-enable-custom-alter.md "TTL-how-to-enable-custom-alter.md")
- [Use the INSERT statement to set custom Time to Live (TTL) values for new rows](TTL-how-to-insert-cql.md "TTL-how-to-insert-cql.md")
- [Use the UPDATE statement to edit custom Time to Live (TTL)
  settings for rows and columns](TTL-how-to-update-cql.md "TTL-how-to-update-cql.md")

## Amazon Keyspaces Time to Live and integration with AWS

services

The following TTL metric is available in Amazon CloudWatch to enable continuous
monitoring.

- `TTLDeletes` – The units consumed to delete or update data
  in a row by using Time to Live (TTL).

For more information about how to monitor CloudWatch metrics, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

When you use CloudFormation, you can turn on TTL when creating an Amazon Keyspaces table. For more information,
see the [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.md").
