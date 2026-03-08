# lookup

Use `lookup` to enrich your query results with reference data
from a lookup table. A lookup table contains CSV data that you upload to
Amazon CloudWatch Logs. When a query runs, the `lookup` command matches a
field in your log events against a field in the lookup table and appends the
specified output fields to the results.

Use lookup tables for data enrichment scenarios such as mapping user IDs
to user details, product codes to product information, or error codes to
error descriptions.

## Creating and managing lookup tables

Before you can use the `lookup` command in a query, you
must create a lookup table. You can create and manage lookup tables
from the CloudWatch console or by using the Amazon CloudWatch Logs API.

###### To create a lookup table (console)

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**,
   and then choose the **Logs** tab.
3. Scroll to **Lookup tables** and choose
   **Manage**.
4. Choose **Create lookup table**.
5. Enter a name for the lookup table. The name can contain only
   alphanumeric characters, hyphens, and underscores.
6. (Optional) Enter a description.
7. Upload a CSV file. The file must include a header row with
   column names, use UTF-8 encoding, and not exceed 10 MB.
8. (Optional) Specify a AWS KMS key to encrypt the table
   data.
9. Choose **Create**.

After you create a lookup table, you can view it in the CloudWatch Logs Insights
query editor. Choose the **Lookup tables** tab to
browse available tables and their fields.

To update a lookup table, select the table and choose
**Actions**, **Update**. Upload a
new CSV file to replace all existing content. To delete a lookup table,
choose **Actions**,
**Delete**.

###### Note

You can create up to 100 lookup tables per account per
AWS Region. CSV files can be up to 10 MB. You can also manage
lookup tables by using the Amazon CloudWatch Logs API. For more information, see
[CreateLookupTable](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLookupTable.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLookupTable.md") in the _Amazon CloudWatch Logs API
Reference_.

## Query syntax for lookup

###### Command structure

The following shows the format of this command.

```
lookup `table` `lookup-field` as `log-field` [,...] `output-mode` `output-field`[,...]
```

The command uses the following arguments:

- `table` – The
  name of the lookup table to use.
- `lookup-field` –
  The field in the lookup table to match against.
- `log-field` – The
  field in your log events to match. The match is exact and
  case-sensitive.
- `output-mode` –
  Specify `OUTPUT` to add the output fields
  to the results. If a field with the same name already exists
  in the log event, it is overwritten.
- `output-field` –
  One or more fields from the lookup table to add to the
  results.

###### Example: Enrich log events with user details

Suppose you have a log group with events that contain an
`id` field, and a lookup table named
`user_data` with columns `id`,
`name`, `email`, and
`department`. The following query enriches each log
event with the user's name, email, and department from the lookup
table.

```
fields action, status, name, email, department
| lookup user_data id OUTPUT name, email, department
```

###### Example: Use lookup with aggregation

You can use lookup output fields with aggregation functions. The
following query enriches log events with user details and then
counts events grouped by email address.

```
fields user_id, action, username, email, department
| lookup user_data user_id OUTPUT username, email, department
| stats count(*) by email
```

###### Example: Use lookup with filter

You can filter results based on fields returned by the lookup.
The following query enriches log events and then filters to show
only events from a specific department.

```
fields user_id, action
| lookup user_data user_id OUTPUT username, email, department
| filter department = "Engineering"
```
