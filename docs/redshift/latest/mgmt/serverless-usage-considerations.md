Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations when using

Amazon Redshift Serverless

For a list of AWS Regions where the Amazon Redshift Serverless is available, see the
endpoints listed for [Redshift Serverless API](../../../general/latest/gr/redshift-service.md "../../../general/latest/gr/redshift-service.md") in
the _Amazon Web Services General Reference_.

Some resources used by Amazon Redshift Serverless are subject to quotas. For more
information, see [Quotas for Amazon Redshift Serverless objects](amazon-redshift-limits.md#serverless-limits-account "amazon-redshift-limits.md#serverless-limits-account").

When you DECLARE a cursor, the result-set size specifications for
Amazon Redshift Serverless is specified in [DECLARE](../dg/declare.md "../dg/declare.md"). Amazon Redshift Serverless has a cursor maximum total result set size of 150,000 MB.

_Maintenance Window_ – Amazon Redshift Serverless offers automatic
software updates without requiring traditional maintenance windows. When a new update is available,
the system applies it within 14 days of release during idle periods. The update process typically
takes up to 15 minutes. If no 15-minute idle period occurs within 14 days, your Serverless endpoint
may experience brief unavailability. During this time, application connections to endpoints may fail.
You can monitor Redshift patch releases in the "Cluster versions for Amazon Redshift" documentation.
For information about Amazon Redshift Serverless SLAs, see [Amazon Redshift Service Level Agreement](https://aws.amazon.com/redshift/sla/ "https://aws.amazon.com/redshift/sla/").

_Track_ – When Amazon Redshift releases a new workgroup version, your
workgroup is updated automatically. You can control whether your workgroup is updated to the most
recent release or to the previous release. For information about tracks, see
[Tracks for Amazon Redshift provisioned
clusters and serverless workgroups](tracks.md "tracks.md").

_Availability Zone IDs_ – When you configure your
Amazon Redshift Serverless instance, open **Additional considerations**, and
make sure that the subnet IDs provided in **Subnet** contain at
least two of the supported Availability Zone IDs.

- For workgroups without Enhanced VPC Routing (EVR), you need two Availability Zones (AZs).
- For workgroups with EVR, you need three AZs.
  To see the subnet to
  Availability Zone ID mapping, go to the VPC console and choose
  **Subnets** to see the list of subnet IDs with their
  Availability Zone IDs. Verify that your subnet is mapped to a supported Availability
  Zone ID. To create a subnet, see [Create a subnet in
  your VPC](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet") in the _Amazon VPC User Guide_.

_Two subnets (without EVR)_ – You must have at least two subnets,
and they must span across two Availability Zones.

_Three subnets (with EVR ONLY)_ – You must have at least three subnets
when you use EVR, and they must span across three or more Availability Zones.

_Free IP address requirements_ – When using Redshift Serverless without enhanced
VPC routing (EVR) enabled, you must have at least three free IP
addresses available in each subnet. This is a requirement of the proper functioning
of the service.

When updating the RPUs for Redshift Serverless deployment, at least three free IP addresses must be available
in each subnet to accommodate the service's operational requirements.

For more information about allocating IP addresses and understanding IP addressing in Amazon VPC,
see [IP addressing for your VPCs and subnets](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in the _Amazon VPC User Guide_.

Without EVR

If you don't use enhanced VPC routing, you must
have at least three free IP addresses for each subnet,
regardless of the size of the base RPU (4 to 1024 RPUs),
or the RPU usage of your workgroup or workgroups. The need for 3 IP address is also applicable to
workgroups that have AI-driven scaling and optimization capabilities enabled.

With Enhanced VPC Routing (EVR)

If you use enhanced VPC routing with Redshift Serverless, the minimum
number of IP addresses required when creating a workgroup are as follows:

| Redshift Processing Units (RPUs) | Free IP addresses required | Minimum CIDR size |
| -------------------------------- | -------------------------- | ----------------- |
| 4                                | 9                          | /27               |
| 8                                | 9                          | /27               |
| 16                               | 13                         | /27               |
| 32                               | 13                         | /27               |
| 64                               | 21                         | /27               |
| 128                              | 37                         | /26               |
| 256                              | 69                         | /25               |
| 512                              | 133                        | /24               |
| 1024                             | 261                        | /23               |

With EVR, you also need free IP addresses when updating your workgroup to use more RPUs. The
number of free IP addresses required when updating the subnets for a workgroup are
as follows:

| Redshift Processing Units (RPUs) | Updated Redshift Processing Units (RPUs) | Free IP addresses required |
| -------------------------------- | ---------------------------------------- | -------------------------- |
| 4                                | 8                                        | 10                         |
| 8                                | 16                                       | 10                         |
| 16                               | 32                                       | 13                         |
| 32                               | 64                                       | 16                         |
| 64                               | 128                                      | 28                         |
| 128                              | 256                                      | 52                         |
| 256                              | 512                                      | 100                        |
| 512                              | 1024                                     | 197                        |

###### Note

The maximum base RPU capacity of 1024 is only available in the following
AWS Regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- Europe (Ireland)
- Europe (London)

For more information on allocating IP
addresses, see [IP
addressing](../../../vpc/latest/userguide/how-it-works.md#vpc-ip-addressing "../../../vpc/latest/userguide/how-it-works.md#vpc-ip-addressing") in the _Amazon VPC User Guide_.

_Storage space after migration_ – When migrating small
Amazon Redshift provisioned clusters to Amazon Redshift Serverless, you might see an increase in
storage-space allocation after migration. This is a result of optimized
storage-space allocation, resulting in preallocated storage space. This space is
used over a period of time as data grows in Amazon Redshift Serverless.

_Datasharing between Amazon Redshift Serverless and Amazon Redshift provisioned clusters_ – When datasharing where Amazon Redshift Serverless is the producer and a
provisioned cluster is the consumer, the provisioned cluster must have a cluster
version later than 1.0.38214. If you use a cluster version earlier than this, an
error occurs when you run a query. You can view the cluster version on the Amazon Redshift
console on the **Maintenance** tab. You can also run `SELECT
 version();`.

_Max query execution time_ – Elapsed execution time for
a query, in seconds. Execution time doesn't include time spent waiting in a queue.
If a query exceeds the set execution time, Amazon Redshift Serverless stops the query. Valid
values are 0–86,399.

_Migrating for tables with interleaved sort keys_ –
When migrating Amazon Redshift provisioned clusters to Amazon Redshift Serverless, Redshift
converts tables with interleaved sort keys and DISTSTYLE KEY to compound sort keys.
The DISTSTYLE doesn't change. For more information on distribution styles, see
[Working with data distribution styles](../dg/t_Distributing_data.md "../dg/t_Distributing_data.md") in the Amazon Redshift Developer Guide.
For more information on sort keys, see [Working with sort keys](../dg/t_Sorting_data.md "../dg/t_Sorting_data.md").

_VPC sharing_ – You can create Amazon Redshift Serverless workgroups in a
shared VPC. If you do so, we recommend that you don't delete the resource share as
it can result in the workgroup becoming unavailable.
