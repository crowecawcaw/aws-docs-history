# Configuring lookup table destinations for scheduled queries

Configure a lookup table as a destination to automatically refresh a lookup table
with your scheduled query results. On each scheduled execution, CloudWatch Logs populates the
specified lookup table with the query results, keeping the table current with your
latest log data. You can then reference the table with the `lookup` command
in other log queries. For more information about lookup tables, see [lookup](CWL_QuerySyntax-Lookup.md "CWL_QuerySyntax-Lookup.md").

If the lookup table doesn't exist, CloudWatch Logs creates it on the first successful
execution. Each subsequent execution is a full replacement operation—all existing
table content is replaced with the new query results.

The lookup table configuration includes the following settings:

- **Table name** – The name of the lookup
  table to create or refresh. The name can contain only alphanumeric characters
  and underscores.
- **Delivery role** – The ARN of the IAM
  role that grants CloudWatch Logs permissions to create or update the lookup table with
  query results.
- **Description** – (Optional) A description
  of the lookup table.
- **AWS KMS key** – (Optional) The ARN of the
  AWS KMS key to use to encrypt the lookup table data. If you don't specify a key,
  the data is encrypted with an AWS-owned key.
- **Tags** – (Optional) Key-value pairs to
  associate with the lookup table. Tags are applied only when the table is
  initially created.
  The destination delivery IAM role requires the following permissions, and must
  include a trust policy that allows the CloudWatch Logs service
  (`logs.amazonaws.com`) to assume the role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLookupTable",
                "logs:UpdateLookupTable",
                "logs:GetQueryResults"
            ],
            "Resource": "*"
        }
    ]
}
```

###### Note

Lookup table destination results are subject to the same lookup table quotas as
tables that you create directly, such as the maximum number of lookup tables per
account per AWS Region. If a scheduled execution fails to refresh the table, the
existing table content remains unchanged, and the failure appears in the scheduled
query execution history.
