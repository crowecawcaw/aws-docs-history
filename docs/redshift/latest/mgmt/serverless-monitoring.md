Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Monitoring queries and workloads with

Amazon Redshift Serverless

You can monitor your Amazon Redshift Serverless queries and workload with the provided system
views.

_Monitoring views_ are system views in
Amazon Redshift Serverless that are used to monitor query and workload usage. These views are
located in the `pg_catalog` schema. The system views available have been
designed to give you the information needed to monitor Amazon Redshift Serverless, which is much
simpler than that needed for provisioned clusters. The SYS system views have been
designed to work with Amazon Redshift Serverless. To display the information provided by these
views, run SQL SELECT statements.

System views are defined to support the following monitoring objectives.

**Workload monitoring**

You can monitor your query activities over time to:

- Understand workload patterns, so you know what is normal
  (baseline) and what is within business service level agreements
  (SLAs).
- Rapidly identify deviation from normal, which might be a transient
  issue or something that warrants further action.

**Data load and unload monitoring**

Data movement in and out of Amazon Redshift Serverless is a critical function. You
use COPY and UNLOAD to load or unload data, and you must monitor progress
closely in terms of bytes/rows transferred and files completed to track
adherence to business SLAs. This is normally done by running system table
queries frequently (that is, every minute) to track progress and raise
alerts for investigation/corrective action if significant deviations are
detected.

**Failure and problem diagnostics**

There are cases where you must take action for query or runtime failures.
Developers rely on system tables to self-diagnose issues and determine
correct remedies.

**Performance tuning**

You might need to tune queries that are not meeting SLA requirements
either from the start, or have degraded over time. To tune, you must have
runtime details including run plan, statistics, duration, and resource
consumption. You need baseline data for offending queries to determine the
cause for deviation and to guide you how to improve performance.

**User objects event monitoring**

You need to monitor actions and activities on user objects, such as
refreshing materialized views, vacuum, and analyze. This includes
system-managed events like auto-refresh for materialized views. You want to
monitor when an event ends if it is user initiated, or the last successful
run if system initiated.

**Usage tracking for billing**

You can monitor your usage trends over time to:

- Inform budget planning and business expansion estimates.
- Identify potential cost-saving opportunities like removing cold
  data.

Use the SYS system views to monitor Amazon Redshift Serverless;. For more information about the
SYS monitoring views, go to [SYS monitoring
views](../dg/serverless_views-monitoring.md "../dg/serverless_views-monitoring.md") in the Amazon Redshift Database Developer Guide.
