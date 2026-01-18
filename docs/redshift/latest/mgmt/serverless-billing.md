Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Billing for Amazon Redshift Serverless

## Billing for compute capacity

You can purchase capacity for Amazon Redshift Serverless in two ways:

- **You can purchase on-demand capacity** – When you choose on-demand compute
  capacity, you pay for resources as you go. This is the best choice if you're just
  beginning to use Amazon Redshift Serverless or if you don't have a good sense yet of your steady usage patterns.
  On-demand offers the most flexibility.
  For more information, see [Billing for on-demand compute capacity](serverless-billing-on-demand.md "serverless-billing-on-demand.md").
- **You can purchase reservations** – A reservation provides a discount
  when you buy a preset amount of
  compute resources for a specific amount of time, for example for a year. It's a good idea when you know you're going to
  use an amount of capacity steadily. It's helpful for saving money when
  you can forecast some of your capacity needs.
  For more information, see [Billing for serverless reservations](serverless-billing-reserved.md "serverless-billing-reserved.md").

You can use reservations and on-demand resources together. It isn't required that you use one or the other.

For detailed pricing information, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

## Billing for storage

Primary storage capacity is billed as Redshift Managed Storage (RMS). Storage is
billed by GB / month. Storage billing is separate from billing for compute capacity.
Storage used for user snapshots is billed at the standard backup billing rates,
depending on your usage tier.

Data transfer costs and machine learning (ML) costs apply separately, the same as
provisioned clusters. Snapshot replication and data sharing across AWS Regions are
billed at the transfer rates outlined on the pricing page. For more information, see
[Amazon Redshift pricing](https://aws.amazon.com//redshift/pricing/ "https://aws.amazon.com//redshift/pricing/").

### Visualizing billing usage with

CloudWatch

The metric `SnapshotStorage`, which tracks snapshot storage usage, is
generated and sent to CloudWatch. For more information about CloudWatch, see [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")

## Using the Amazon Redshift Serverless free

trial

Amazon Redshift Serverless offers a free trial. If you participate in the free trial, you can
view the free trial credit balance in the Redshift console, and check free trial usage
in the [SYS_SERVERLESS_USAGE](../dg/SYS_SERVERLESS_USAGE.md "../dg/SYS_SERVERLESS_USAGE.md")
system view. Note that billing details for free trial usage does not appear in the
billing console. You can only view usage in the billing console after the free trial
ends. For more information about the Amazon Redshift Serverless free trial, see [Amazon Redshift Serverless free trial](https://aws.amazon.com//redshift/free-trial/ "https://aws.amazon.com//redshift/free-trial/").

## Billing usage notes

- **Recording usage** - A query or transaction is
  only metered and recorded after the transaction completes, is rolled back, or
  stopped. For instance, if a transaction runs for two days, RPU usage is recorded
  after it completes. You can monitor ongoing use in real time by querying
  `sys_serverless_usage`. Transaction recording may reflect as RPU
  usage variation and effect costs for specific hours and for daily use.
- **Writing explicit transactions** - It's
  important as a best practice to end transactions. If you don't end or roll back
  an open transaction, Amazon Redshift Serverless continues to use RPUs. For example, if
  you write an explicit `BEGIN TRAN`, it's important to have
  corresponding `COMMIT` and `ROLLBACK` statements.
- **Cancelled queries** - If you run a query and
  cancel it before it finishes, you are still billed for the time the query ran.
- **Scaling** - The Amazon Redshift Serverless instance may
  initiate scaling for handling periods of higher load, in order to maintain
  consistent performance. Your Amazon Redshift Serverless billing includes both base
  compute and scaled capacity at the same RPU rate.
- **Scaling down** - Amazon Redshift Serverless scales up
  from its base RPU capacity to handle periods of higher load. In some cases, RPU
  capacity can remain at a higher setting for a period after query load falls. We
  recommend that you set maximum RPU hours in the console to guard against
  unexpected cost.
- **System tables** - When you query a system
  table, the query time is billed.
- **Redshift Spectrum** - When you have Amazon Redshift Serverless, and
  you run queries, there isn't a separate charge for data-lake queries. For
  queries on data stored in Amazon S3, the charge is the same, by transaction time, as
  queries on local data.
- **Federated queries** - Federated queries are
  charged in terms of RPUs used over a specific time interval, in the same manner
  as queries on the data warehouse or data lake.
- **Storage** - Storage is billed separately, by GB
  / month.
- **Minimum charge** - The minimum charge is for 60
  seconds of resource usage, metered on a per-second basis.
- **Snapshot billing** - Snapshot billing doesn't
  change. It's charged according to storage, billed at a rate of GB / month. You
  can restore your data warehouse to specific points in the last 24 hours at a 30
  minute granularity, free of charge. For more information, see [Amazon Redshift pricing](https://aws.amazon.com//redshift/pricing/ "https://aws.amazon.com//redshift/pricing/").
- **Automatic optimizations run using extra compute resources** ‐
  Amazon Redshift Serverless usually runs automatic optimization operations alongside
  user queries. These operations are known as autonomics,
  and you aren’t charged for them.

If you enable allocating extra compute resources, Amazon Redshift will run
autonomics when necessary even in periods of high user activity.
In such cases, you can be billed for the time spent running
autonomics. For more information, see [Allocating extra compute resources for automatic database optimization](../dg/t_extra-compute-autonomics.md "../dg/t_extra-compute-autonomics.md") in the _Amazon Redshift Database Developer Guide_.

### Amazon Redshift Serverless best

practices for keeping billing predictable

The following are best practices and built-in settings that help keep your billing
consistent.

- Make sure to end each transaction. When you use `BEGIN` to
  start a transaction, it's important to `END` it as well.
- Use best-practice error handling to respond gracefully to errors and end
  each transaction. Minimizing open transactions helps to avoid unnecessary
  RPU use.
- Use `SESSION TIMEOUT` to help end open transactions and idle
  sessions. It causes any session kept idle or inactive for more than 3600
  seconds (1 hour) to time out. It causes any transaction kept open and
  inactive for more than 21600 seconds (6 hours) to time out. This timeout
  setting can be changed explicitly for a specific user, such as when you want
  to keep a session open for a long-running query. The topic [CREATE USER](../dg/r_CREATE_USER.md "../dg/r_CREATE_USER.md") shows how to
  adjust `SESSION TIMEOUT` for a user.
  - In most cases, we recommend that you don't extend the
    `SESSION TIMEOUT` value, unless you have a use case
    that requires it specifically. If the session remains idle, with an
    open transaction, it can result in a case where RPUs are used until
    the session is closed. This will result in unnecessary cost.
  - Amazon Redshift Serverless has a maximum time of 86,399 seconds (24 hours)
    for a running query. The maximum period of inactivity for an open
    transaction is six hours before Amazon Redshift Serverless ends the session
    associated with the transaction. For more information, see [Quotas for Amazon Redshift Serverless objects](amazon-redshift-limits.md#serverless-limits-account "amazon-redshift-limits.md#serverless-limits-account").

## Amazon Redshift Serverless billing with

connection pooling

Amazon Redshift Serverless treats all incoming queries as billable user activity, including lightweight
health-check queries sent by connection pools. This behavior applies regardless of
whether the query originates from an application, a JDBC/ODBC driver, or a connection
pooling framework. Each health-check query triggers compute usage, and charges are
incurred regardless of query purpose or origin. As a result, maintaining open connection
pools can generate costs even when no actual user workloads are running.

Connection pooling maintains a pool of persistent connections between applications and
the Amazon Redshift Serverless endpoint. To ensure these connections remain healthy and available,
pooling mechanisms often send lightweight or empty queries (for example, `SELECT
 1`) at regular intervals. These automated queries verify connection
status.

When you use connection pooling, consider these best practices to minimize unintended
charges:

- Adjust health check frequency by reviewing and optimizing the frequency of
  health check or keep-alive queries in your connection pooling
  configuration.
- Optimize idle system settings by configuring connection pooling to minimize
  unnecessary connection churn or background query activity during system idle
  times.
- Implement application-level pooling or improved connection lifecycle
  management if it can reduce overhead.
- Disable heartbeat or validation queries if your connection pooling
  configuration allows it. Check your specific connection string parameters or
  configuration files to adjust these settings.
- Fine-tune TCP keepalive settings: If you can't disable the driver's internal
  heartbeat mechanisms, adjust Transmission Control Protocol (TCP) keepalive
  settings at the operating system or application level to address connection
  timeout issues. Refer to your operating system, JDBC/ODBC driver, or connection
  pool documentation for details.
- Optimize database connection pooling: Configure your connection pool
  (HikariCP, Apache Database Connection Pool) to manage connections and minimize
  connection overhead. Focus on parameters such as maximum connections, idle
  timeout, and validation queries (if necessary). This optimization helps align
  Amazon Redshift Serverless compute usage with actual workload demand, potentially reducing
  costs.

## Cost optimization for Amazon Redshift Serverless with zero-ETL

To optimize costs while running zero-ETL integrations on Amazon Redshift Serverless, you can right-size
your environments and adjust your refresh settings based on workload needs. Consider
making the following adjustments:

- Use the lower base RPU capacity of 8 RPU where available for workloads.
- Configure the REFRESH_INTERVAL of your target Redshift instance to balance
  freshness with cost. Shorter intervals ensure near real-time updates but drive
  up compute costs. Longer intervals (5 minutes or longer) reduce charges for
  workloads where immediate freshness is not critical, such as reporting or
  historical analysis. To edit your Redshift target REFRESH_INTERVAL, see the
  refresh interval clause in the [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") description.
- Maximize utilization of your Amazon Redshift Serverless environment by concurrently running
  analytics workloads while zero-ETL data is being ingested. This ensures that
  compute capacity is actively serving multiple business purposes.
