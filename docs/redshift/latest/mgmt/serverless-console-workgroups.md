Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing properties for a

workgroup

In Amazon Redshift Serverless, a workgroup is a collection of compute resources available for
use. When you choose Amazon Redshift Serverless, in the AWS console, you can choose
**Workgroup configuration** from the navigation menu to
view a list. You can use the **Search** box to find workgroups
that meet your search criteria. Each workgroup entry has a few properties
displayed:

- **Workgroup** - The name of the workgroup. You can
  select it to view and edit the workgroup's properties.
- **Status** - Shows whether the workgroup is
  available.
- **Namespace** - The namespace associated with the
  workgroup. Each workgroup is associated with one namespace.
- **Creation date** - The date (UTC) that the workgroup was
  created.
- **Tags** - Tags associated with the workgroup.
  Additionally, **Workgroup configuration** has another list for managed workgroups,
  which are Amazon Redshift Serverless workgroups managed by AWS Glue. For more information on managed workgroups, see
  [Managed workgroups](../dg/iceberg-integration-managed-workgroups.md "../dg/iceberg-integration-managed-workgroups.md")
  in the Amazon Redshift Database Developer Guide.

## Workgroup properties

You can list workgroups by choosing **Workgroup
configuration** in the left menu. Then you can choose a
workgroup from the list. Several panels show properties for the workgroup.
You can also perform actions. **General information**
displays the following:

- **Workgroup** - The name of the workgroup.
- **Namespace** - The namespace associated with the
  workgroup. You can choose it to view its properties. A workgroup is
  associated with a single namespace.
- **Date created** - When the workgroup was
  created.
- **Status** - Indicates if the workgroup resources
  are available. If it's available, you can connect with a client to
  the Amazon Redshift Serverless instance, in order to query data or create
  database resources, or you can connect with query editor v2.
- **Endpoint** - The URL.
- **JDBC URL** - The URL to establish JDBC client
  connections. You can use this URL to connect with a JDBC driver for
  Amazon Redshift. For more information, see [Configuring a connection
  for JDBC driver version 2.x for Amazon Redshift](jdbc20-install.md "jdbc20-install.md").
- **ODBC URL** - The URL to establish ODBC client
  connections. It contains properties, like the database and user ID,
  and their values.
- **Workgroup version and Patch version** -
  Amazon Redshift Serverless regularly releases new versions and patches. You
  can use the workgroup version and Patch version numbers to track
  software updates to your Amazon Redshift Serverless workgroup. For more
  information about changes and features in specific patches, see
  [Cluster versions
  for Amazon Redshift](cluster-versions.md "cluster-versions.md").

The **Data access** tab contains several panels:

- **Network and security** - You can see network
  properties, such as the **Virtual private cloud
  (VPC)** identifier, **VPC security
  group** list, **Enhanced VPC
  routing**,
  **IP address type**, and the **Publicly
  accessible** setting. If you choose
  **Edit**, you can change these settings.
  Additionally, you can select **Turn on enhanced VPC
  routing**, which routes network traffic between your
  serverless database and data repositories through a VPC, for
  enhanced privacy and security. You can also select **Turn on
  Public Accessible**, which makes the database publicly
  accessible from outside the VPC, allowing instances and devices to
  connect.

The **IP address type** can be set to dual-stack
mode to support access to workgroups on both IPv4 an IPv6 at the
same time. For more information about network layer communications
Internet Protocols (IP), see [Internet
Protocol](https://en.wikipedia.org/wiki/Internet_Protocol "https://en.wikipedia.org/wiki/Internet_Protocol") in _Wikipedia_.

- **Redshift managed VPC endpoints** - You can
  create managed VPC endpoints to access Amazon Redshift Serverless from
  another VPC.

The **Limits** tab has settings for controlling capacity
and use limits for Amazon Redshift Serverless. It contains the following
panels:

- **Base capacity in Redshift processing units
  (RPUs)** - You can set the base capacity of the compute
  resources used to process your workload. For more information, see
  [Compute capacity for Amazon Redshift Serverless](serverless-capacity.md "serverless-capacity.md").
- **Usage limits** - You can set up to four limits
  for the maximum compute resources that your Amazon Redshift Serverless instance can
  use in a time period, and select actions for Amazon Redshift Serverless to perform
  when reaching those limits. For example, you can set your workgroup
  to have two limits, one of 500 RPU hours and one of 900 RPU hours.
  You can have Amazon Redshift Serverless send you an alert when it reaches the first
  limit of 500 RPU hours, then turn off user queries when it reaches
  the second limit of 900 hours. These limits help control your costs
  and make them more predictable.
- **Query limits** - You can set limits on queries,
  like the timeout setting. These limits help you optimize cost and
  performance.

The **Tabs** tab has the **Tags** panel,
which shows any tags that you created for your workgroup. For more
information about tagging resources, see [Tagging resources in
Amazon Redshift Serverless](serverless-tagging-resources.md "serverless-tagging-resources.md").

## Managed workgroup properties

You can also choose workgroups managed by the AWS Glue Data Catalog under the
**Managed workgroups** list.

Managed workgroups have different
properties from regular workgroups. For more information on managed workgroups, see
[Managed workgroups](../dg/iceberg-integration-managed-workgroups.md "../dg/iceberg-integration-managed-workgroups.md")
in the Amazon Redshift Database Developer Guide.

**General information** displays the following:

- **Workgroup** - The name of the managed workgroup.
- **Date created** - The date (UTC) that the managed workgroup was
  created.
- **Catalog ARN** - The Amazon Resource Name (ARN) for the
  managed workgroup in the AWS Glue Data Catalog.
- **Status** - Indicates if the managed workgroup's compute resources are available.
  If the resources are available, you can connect to the catalog that uses the managed workgroup
  with an Apache Iceberg-compatible SQL client in order
  to query data or create database resources. You can also connect to the catalog using the Amazon Redshift query editor v2.

**Query and database monitoring** contains the
**Managed workgroup performance** graph, showing
the average elapsed time of all queries from the workgroup over time.

The **Query history** tab is a list of all queries
from the managed workgroup. Its details include information such as the user
who ran the query, the client engine from which the query originated, and the
query’s ID and status. The Users tab is a list of all the users in the workgroup.
The **Performance metrics** tab shows various metrics such as
average query time, number of completed queries, and percentage of
storage capacity used.
