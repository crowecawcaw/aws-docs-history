Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Behavior changes in Amazon Redshift

As Amazon Redshift continues to evolve and improve, certain changes in behavior are introduced to
enhance performance, security, and user experience. This page serves as a comprehensive resource
for you to stay informed about these critical updates, take
actions, and avoid potential disruptions to your
workloads.

## Upcoming behavior changes

The following describes upcoming behavior changes.

###### Topics

- [Scalar Python UDFs will reach end of support after June
  30, 2026](#python-udf-jun2026 "#python-udf-jun2026")
- [Amazon Redshift won’t support functions that access consumer
  information through datasharing after February 16, 2026](#datasharing-feb2026 "#datasharing-feb2026")
- [Minimum Transport Layer Security (TLS) version changes
  effective starting January 31, 2026](#tls-changes-jan2026 "#tls-changes-jan2026")
- [Amazon Redshift won’t support the creation of new scalar
  Python UDFs after October 30, 2025](#python-udf-oct2025 "#python-udf-oct2025")

### Scalar Python UDFs will reach end of support after June

30, 2026

Amazon Redshift will end support for Python UDFs after June 30, 2026. As an alternative, we
recommend that you use Lambda UDFs.

Lambda UDFs have the following advantages over Python UDFs:

- Lambda UDFs can connect to external services and APIs from within the UDF logic.
- Lambda UDFs use Lambda compute resources. Heavy compute- or memory-intensive Lambda
  UDFs don’t impact Amazon Redshift’s query performance or resource concurrency.
- Lambda UDFs support running Python code. Lambda UDFs support multiple Python
  runtimes depending on specific use cases. For more information, see [Building with
  Python](../../../lambda/latest/dg/lambda-python.md "../../../lambda/latest/dg/lambda-python.md") in the _AWS Lambda Developer Guide_.
- You can isolate custom code execution in a separate service boundary. This
  simplifies maintenance, monitoring, budgeting, and permission management.

For information on creating and using Lambda UDFs, see [Scalar Lambda UDFs](../dg/udf-creating-a-lambda-sql-udf.md "../dg/udf-creating-a-lambda-sql-udf.md") in the
_Amazon Redshift Database Developer Guide_. For information on converting existing Python UDFs to
Lambda UDFs, see the [blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

### Amazon Redshift won’t support functions that access consumer

information through datasharing after February 16, 2026

Starting February 16, 2026, Amazon Redshift will no longer support the usage of
`user_is_member_of` and related functions that access consumer user, role, or
group information through datasharing.

### Minimum Transport Layer Security (TLS) version changes

effective starting January 31, 2026

Beginning January 31, 2026, Amazon Redshift will enforce a minimum Transport Layer Security
(TLS) version of 1.2. Incoming connections that use TLS versions 1.0 or 1.1 will be
rejected. This applies to both Amazon Redshift provisioned clusters and serverless workgroups.
Amazon Redshift data warehouses not using TLS will not be affected by this change.

This update might impact you if you use TLS versions 1.0 or 1.1 to connect to Amazon Redshift.

To verify which TLS version you are currently using, you can:

For Amazon Redshift Provisioned: Check the sslversion column in the STL_CONNECTION_LOG system
table [1].

For Amazon Redshift Serverless Workgroup: Check the ssl_version column in the SYS_CONNECTION_LOG system
table [2].

To maintain uninterrupted access to your Amazon Redshift data warehouse after this change, please
follow the steps listed below:

1. Update your client to support TLS 1.2 or higher
2. Install the latest driver version with TLS 1.2+ support

We recommend using the latest version of the Amazon Redshift driver [3] if possible.

[1] [https://docs.aws.amazon.com/redshift/latest/dg/r_STL_CONNECTION_LOG.html](../dg/r_STL_CONNECTION_LOG.md "../dg/r_STL_CONNECTION_LOG.md")

[2] [https://docs.aws.amazon.com/redshift/latest/dg/SYS_CONNECTION_LOG.html](../dg/SYS_CONNECTION_LOG.md "../dg/SYS_CONNECTION_LOG.md")

[3] [https://docs.aws.amazon.com/redshift/latest/mgmt/configuring-connections.html](configuring-connections.md "configuring-connections.md")

### Amazon Redshift won’t support the creation of new scalar

Python UDFs after October 30, 2025

Amazon Redshift will no longer support the creation of new Python UDFs after October 30, 2025.
Existing Python UDFs will continue to function normally. We strongly recommend that you
migrate your existing Python UDFs to Lambda UDFs before this date.

Lambda UDFs have the following advantages over Python UDFs:

- Lambda UDFs can connect to external services and APIs from within the UDF logic.
- Lambda UDFs use Lambda compute resources. Heavy compute- or memory-intensive Lambda
  UDFs don’t impact Amazon Redshift’s query performance or resource concurrency.
- Lambda UDFs support running Python code. Lambda UDFs support multiple Python
  runtimes depending on specific use cases. For more information, see [Building with
  Python](../../../lambda/latest/dg/lambda-python.md "../../../lambda/latest/dg/lambda-python.md") in the _AWS Lambda Developer Guide_.
- You can isolate custom code execution in a separate service boundary. This
  simplifies maintenance, monitoring, budgeting, and permission management.

For information on creating and using Lambda UDFs, see [Scalar Lambda UDFs](../dg/udf-creating-a-lambda-sql-udf.md "../dg/udf-creating-a-lambda-sql-udf.md") in the
_Amazon Redshift Database Developer Guide_. For information on converting existing Python UDFs to
Lambda UDFs, see the [blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

## Recent behavior changes

###### Topics

- [Amazon Redshift uses up-to-date IANA Time Zone Database
  after Aug 26, 2025](#timezone-changes-aug2025 "#timezone-changes-aug2025")
- [Amazon Redshift Serverless RPU changes effective after August 15,
  2025](#serverless-rpu-aug2025 "#serverless-rpu-aug2025")
- [Database audit logging changes effective after
  August 10, 2025](#audit-logging-aug2025 "#audit-logging-aug2025")
- [Virtual Private Cloud Endpoint changes for serverless
  workgroups effective after June 27, 2025](#VPCE-jun2025 "#VPCE-jun2025")
- [Query monitoring changes effective after
  May 2, 2025](#query-monitoring-changes-may2025 "#query-monitoring-changes-may2025")
- [Security changes effective after January 10,
  2025](#security-changes-jan2025 "#security-changes-jan2025")

### Amazon Redshift uses up-to-date IANA Time Zone Database

after Aug 26, 2025

Beginning Aug 26, 2025, Amazon Redshift calculates time zones by adopting the latest IANA Time
Zone Database patches. This change alters how date and time conversions function for certain
time zones and time periods. This update affects explicit time zone conversions, such as
those performed with the [CONVERT_TIMEZONE](../dg/CONVERT_TIMEZONE.md "../dg/CONVERT_TIMEZONE.md") function or the
[TIMEZONE](../dg/r_TIMEZONE.md "../dg/r_TIMEZONE.md") and
[AT TIME
ZONE](../dg/r_AT_TIME_ZONE.md "../dg/r_AT_TIME_ZONE.md") commands, as well as implicit conversions that occur during type casting
operations, particularly between [TIMESTAMP](../dg/r_Datetime_types.md#r_Datetime_types-timestamp "../dg/r_Datetime_types.md#r_Datetime_types-timestamp") and [TIMESTAMPTZ](../dg/r_Datetime_types.md#r_Datetime_types-timestamptz "../dg/r_Datetime_types.md#r_Datetime_types-timestamptz") formats.

The following is a list of updates for time zone and time period combinations:

- Time zones now correctly observe daylight saving time (DST) after year 2038.
  Previously, no time zone observed DST after 2038.
- The `America/Toronto` time zone, and the time zones that link to it, have
  DST switch in 1947-1950 at 2 AM local time instead of at midnight.
- Amazon Redshift now correctly reflects local mean time (LMT) for periods before
  standardization for all time zones. This period is specific to a time zone, with most
  time zones switching to standardization before mid-19th century.
- `EET`, `CET`, `WET` and `MET` are now
  treated as normal time zones instead of abbreviations.
- The following time zone names no longer exist in Amazon Redshift:
  - `Asia/Riyadh87`
  - `Asia/Riyadh88`
  - `Asia/Riyadh89`
  - `Mideast/Riyadh87`
  - `Mideast/Riyadh88`
  - `Mideast/Riyadh89`
  - `US/Pacific-New`

For more information on the IANA Time Zone Database, see [Time Zone Database](https://www.iana.org/time-zones "https://www.iana.org/time-zones")
on the IANA Time Zone Database website.

### Amazon Redshift Serverless RPU changes effective after August 15,

2025

Beginning August 15, 2025, the AWS account quota for Amazon Redshift Serverless base Redshift
Processing Units (RPUs) is the greater of either 3,200 RPUs or 1.5 times your maximum
aggregate base RPUs from the previous six months.

### Database audit logging changes effective after

August 10, 2025

Beginning August 10, 2025, Amazon Redshift is making a change to Database Audit Logging, which
requires your action. Amazon Redshift logs information about connections and user activities in your
database to Amazon S3 buckets and CloudWatch. After August 10, 2025, Amazon Redshift will discontinue database
audit logging to your Amazon S3 buckets which have a bucket policy specifying a Redshift IAM
USER. We recommend updating your policies to use the Redshift SERVICE-PRINCIPAL instead,
within S3 bucket policies for audit logging. For information about audit logging, see [Bucket permissions for Amazon Redshift
audit logging](db-auditing.md#db-auditing-bucket-permissions "db-auditing.md#db-auditing-bucket-permissions").

To avoid any logging interruption, review and update your S3 bucket policies to grant
access to the Redshift service-principal in the associated region prior to August 10, 2025.
For information about database audit logging, see [Log files in Amazon S3](db-auditing.md#db-auditing-manage-log-files "db-auditing.md#db-auditing-manage-log-files")

For questions or concerns, contact AWS support at the following link: [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support").

### Virtual Private Cloud Endpoint changes for serverless

workgroups effective after June 27, 2025

Beginning June 27, 2025, Amazon Redshift is making a change to Virtual Private Cloud Endpoint
(VPCE) support for serverless workgroups. Prior to this date, Amazon Redshift deploys with endpoints
into a single Availability Zone (AZ) during workgroup creation, and expands VPCE support up
to three AZs over time. After this date, Amazon Redshift deploys VPCEs in up to three of the
Availability Zones specified during workgroup creation.

For more information, see [Considerations when using
Amazon Redshift Serverless](serverless-usage-considerations.md "serverless-usage-considerations.md").

For questions or concerns, contact AWS support at the following link: [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support").

###### Topics

- [Query monitoring changes effective after
  May 2, 2025](#query-monitoring-changes-may2025 "#query-monitoring-changes-may2025")
- [Security changes effective after January 10,
  2025](#security-changes-jan2025 "#security-changes-jan2025")

### Query monitoring changes effective after

May 2, 2025

Effective May 2, 2025, we will no longer offer the Query CPU time
(`max_query_cpu_time`) and Query CPU usage
(`max_query_cpu_percentage`) metrics from the **Query Limits**
tab for both existing and newly created Redshift Serverless workgroups. After this date, we will
automatically remove all query limits based on these metrics across all Redshift Serverless
workgroups.

Query limits are designed to catch runaway queries. However, Query CPU time
(`max_query_cpu_time`) and Query CPU usage
(`max_query_cpu_percentage`) can vary during the lifetime of the query, and are
thus not a consistently effective method to catch runaway queries. To catch runaway queries,
we recommend that you leverage query monitoring metrics that provide consistent and
actionable information. Some examples include:

- **Query execution time** (`max_query_execution_time`):
  To ensure queries complete within expected timeframes.
- **Return row count** (`max_scan_row_count`): To monitor
  the scale of data being processed.
- **Query queue time** (`max_query_queue_time`): To
  identify queries that spend time queueing.

For a full list of supported metrics, see [Query monitoring metrics for Amazon Redshift Serverless.](../dg/cm-c-wlm-query-monitoring-rules.md#cm-c-wlm-query-monitoring-metrics-serverless "../dg/cm-c-wlm-query-monitoring-rules.md#cm-c-wlm-query-monitoring-metrics-serverless")

### Security changes effective after January 10,

2025

Security is our top priority at Amazon Web Services (AWS). To that end, we are further
strengthening the security posture of Amazon Redshift environments by introducing enhanced security
defaults which help you adhere to best practices in data security without requiring
additional setup and reduce the risk of potential misconfiguration. To avoid any potential
disruption, review your provisioned cluster and serverless workgroup creation
configurations, scripts, and tools to make necessary changes to align with the new default
settings before the effective date.

#### Public access disabled by default

After January 10, 2025, [public
accessibility](rs-security-group-public-private.md "rs-security-group-public-private.md") will be disabled by default for all newly created provisioned
clusters, and for clusters restored from snapshots. With this release, by default,
connections to clusters will only be permitted from client applications within the same
Virtual Private Cloud (VPC). To access your data warehouse from applications in another
VPC, configure [cross-VPC](managing-cluster-cross-vpc.md "managing-cluster-cross-vpc.md") access. This
change will be reflected in the `CreateCluster` and
`RestoreFromClusterSnapshot` API operations, and corresponding SDK and AWS CLI
commands. If you create a provisioned cluster from the Amazon Redshift console, then the cluster has
public access disabled by default.

In case you still need public access, you will need to override the default and set
the `PubliclyAccessible` parameter to true when you run
`CreateCluster` or `RestoreFromClusterSnapshot` API operations.
With a publicly accessible cluster, we recommend that you must use security groups or
network access control lists (ACLs) to restrict access. For more information, see [VPC security groups](managing-vpc-security-groups.md "managing-vpc-security-groups.md")
and [Configuring security group
communication settings for an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup](rs-security-group-public-private.md "rs-security-group-public-private.md").

#### Encryption by default

After January 10, 2025, Amazon Redshift will further enhance data and cluster security by
enabling encryption as the default setting for all newly created Amazon Redshift provisioned
clusters. This does not apply to clusters restored from snapshots.

With this change, the ability to decrypt clusters will no longer be available when
using the AWS Management Console, AWS CLI, or API to create a provisioned cluster without specifying a
KMS key. The cluster will automatically be encrypted with an AWS owned key.

This update might impact you if you are creating unencrypted clusters using automated
scripts or leveraging data sharing with unencrypted clusters. To ensure a seamless
transition, update your scripts that create unencrypted clusters. Additionally, if you
regularly create new unencrypted consumer clusters and use them for data sharing, review
your configurations to ensure the producer and consumer clusters are both encrypted,
preventing disruptions to your data sharing activities. For more information, see [Amazon Redshift database encryption](working-with-db-encryption.md "working-with-db-encryption.md").

#### Enforcing SSL connections

After January 10, 2025, Amazon Redshift will enforce SSL connections by default for clients
connecting to newly created provisioned and restored clusters. This default change will
also apply to serverless workgroups.

With this change, a new default parameter group named
`default.redshift-2.0` will be introduced for all newly created or restored
clusters, with the `require_ssl` parameter set to `true` by default.
Any new clusters created without a specified parameter group will automatically utilize
the `default.redshift-2.0` parameter group. When creating a cluster through the
Amazon Redshift console, the new `default.redshift-2.0` parameter group will be
automatically selected. This change will also be reflected in the
`CreateCluster` and `RestoreFromClusterSnapshot` API operations,
and the corresponding SDK and AWS CLI commands. If you use existing or custom parameter
groups, Amazon Redshift will continue to honor the `require_ssl` value specified in your
parameter group. You continue to have the option to change the `require_ssl`
value in your custom parameter groups as needed.

For Amazon Redshift Serverless users, the default value of `require_ssl` in the
`config-parameters` will be changed to `true`. Any requests to
create new workgroups with `require_ssl` set to `false` will be
rejected. You can change the `require_ssl` value to `false` after
the workgroup is created.

For more information, see [Configuring security options for
connections](connecting-ssl-support.md "connecting-ssl-support.md").

Note that you will still have the ability to modify cluster or workgroup settings to
change the default behavior, if needed for your specific use cases.
