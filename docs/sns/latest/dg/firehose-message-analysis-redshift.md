# Analyzing Amazon SNS messages stored in Amazon Redshift

destinations

This topic describes how to analyze Amazon SNS messages that are sent through delivery
streams to Amazon Redshift destinations.

###### To analyze SNS messages sent through Firehose delivery streams to Amazon Redshift destinations

1. Configure your Amazon Redshift resources. For instructions, see [Getting started with Amazon Redshift](../../../redshift/latest/gsg/getting-started.md "../../../redshift/latest/gsg/getting-started.md") in the
   _Amazon Redshift Getting Started Guide_.
2. Configure your delivery stream. For instructions, see [Choose Amazon Redshift for
   Your Destination](../../../firehose/latest/dev/create-destination.md#create-destination-redshift "../../../firehose/latest/dev/create-destination.md#create-destination-redshift") in the _Amazon Data Firehose Developer Guide_.
3. Run a query. For more information, see [Querying a database using the query editor](../../../redshift/latest/mgmt/query-editor.md "../../../redshift/latest/mgmt/query-editor.md") in the
   _Amazon Redshift Management Guide_.

## Example query

For this example query, assume the following:

- Messages are stored in the `notifications` table in the default
  `public` schema.
- The `Timestamp` property from the SNS message is stored in the table's
  `timestamp` column with a column data type of
  `timestamptz`.

###### Note

To transform the JSON metadata for the Amazon Redshift endpoint, you can use the SQL
`COPY` command. For more information, see [Copy from JSON examples](../../../redshift/latest/dg/r_COPY_command_examples.md#r_COPY_command_examples-copy-from-json "../../../redshift/latest/dg/r_COPY_command_examples.md#r_COPY_command_examples-copy-from-json") and [Load from JSON data using the 'auto ignorecase' option](../../../redshift/latest/dg/r_COPY_command_examples.md#copy-from-json-examples-using-auto-ignorecase "../../../redshift/latest/dg/r_COPY_command_examples.md#copy-from-json-examples-using-auto-ignorecase") in the
_Amazon Redshift Database Developer Guide_.

The following query returns all SNS messages received in the specified date range:

```
SELECT *
FROM public.notifications
WHERE timestamp > '2020-12-01T09:00:00.000Z' AND timestamp < '2020-12-02T09:00:00.000Z';
```
