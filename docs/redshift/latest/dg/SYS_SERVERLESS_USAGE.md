Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_SERVERLESS_USAGE

Use SYS_SERVERLESS_USAGE to view details of Amazon Redshift Serverless usage of resources. This
system view doesn't apply to provisioned Amazon Redshift clusters.

This view contains the serverless usage summary including how much compute capacity is
used to process queries and the amount of Amazon Redshift managed storage used at a 1-minute
granularity. The compute capacity is measured in Redshift processing units (RPUs) and
metered for the workloads that you run in RPU-seconds on a per-second basis. RPUs are
used to process queries on the data loaded in the data warehouse, queried from an Amazon S3
data lake, or accessed from operational databases using a federated query.
Amazon Redshift Serverless retains the information in SYS_SERVERLESS_USAGE for 7 days.

For examples on compute cost billing, see [Billing for
Amazon Redshift Serverless](../mgmt/serverless-billing.md "../mgmt/serverless-billing.md").

SYS_SERVERLESS_USAGE is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name                   | Data type        | Description                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start_time                    | timestamp        | The time when the interval began.                                                                                                                                                                                                                                                                                                                                      |
| end_time                      | timestamp        | The time when the interval completed.                                                                                                                                                                                                                                                                                                                                  |
| compute_seconds               | double precision | The accumulated compute unit (RPU) seconds<br>consumed during this time interval. This value accounts for the base<br>RPU capacity allocated for the account.                                                                                                                                                                                                          |
| compute_capacity              | double precision | The average number of compute units (Redshift<br>processing units, or RPUs) allocated during this time interval.<br>The compute_capacity value can be dynamically<br>changed.                                                                                                                                                                                          |
| data_storage                  | integer          | The average data storage space in MB used during<br>this time interval. Used data storage can change dynamically<br>as data is loaded or deleted from the<br>database.                                                                                                                                                                                                 |
| cross_region_transferred_data | integer          | The accumulated data transferred for<br>cross-Region data sharing in bytes during this time<br>interval.                                                                                                                                                                                                                                                               |
| charged_seconds               | integer          | The accumulated compute unit (RPU) seconds charged<br>during this time interval. This is computed after transactions end,<br>and hence can be 0 while a transaction runs. Use charged_seconds to<br>calculate cost for an Amazon Redshift Serverless workgroup. This value<br>accounts for the RPU capacity allocated for the Amazon Redshift Serverless<br>workgroup. |

## Usage notes

- There are situations where compute_seconds is 0 but charged_seconds is
  greater than 0, or vice versa. This is normal behavior resulting from the
  way data is recorded in the system view. For a more accurate representation
  of serverless usage details, we recommend aggregating the data.

## Example

To get the total charges for RPU hours used for a time interval by querying
charged_seconds, run the following query:

```
select trunc(start_time) "Day",
(sum(charged_seconds)/3600::double precision) * <Price for 1 RPU> as cost_incurred
from sys_serverless_usage
group by 1
order by 1
```

Note that there can be idle time during the interval. Idle time doesn't add to
RPUs consumed.
