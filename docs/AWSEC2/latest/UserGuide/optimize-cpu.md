# Optimize CPUs for License-Included instances

Workloads such as Microsoft SQL Server often require high levels of memory and IOPS but a low vCPU count.
AWS provides a broad set of instance types that can cover most of your infrastructure needs. However,
to reduce vCPU-based licensing costs for Windows and Microsoft SQL Server, you can customize the number
of vCPUs running on your EC2 instance while maintaining the same memory and IOPS. To configure CPU options
on your instance and save on vCPU-based licensing costs for both license-included and
Bring-Your-Own-License (BYOL) workloads, use the Optimize CPUs feature.

For more information, see this [blog post](https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpus-best-practices-for-sql-server-workloads-continued/ "https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpus-best-practices-for-sql-server-workloads-continued/")
about best practices to optimize CPUs for SQL Server workloads.

## Supported license types

Optimize CPUs supports billing based on the number of active CPUs for the following
types of license configurations for instances launched from a license-included AMI. For
more information about license types, see [AMI billing information fields](billing-info-fields.md "billing-info-fields.md").

**License-included AMI instance billing**

| Licenses included                         | Usage operation   | Price per vCPU hour |
| ----------------------------------------- | ----------------- | ------------------- |
| Windows Server                            | RunInstances:0002 | $0.046              |
| Windows Server with SQL Server Enterprise | RunInstances:0102 | $0.421              |
| Windows Server with SQL Server Standard   | RunInstances:0006 | $0.166              |
| Windows Server with SQL Server Web        | RunInstances:0202 | $0.063              |

## Supported purchasing options

Optimize CPUs supports the following purchasing options for license included instances:

- On-Demand
- Savings Plans

###### Warning

If you use Reserved Instances, discounts may not be applied when you configure Optimize CPUs
for license included instances in the same payer account. We recommend that you use Savings Plans
to reduce vCPU-based licensing costs and provide comparable savings on your compute costs.

Accounts that used both Optimize CPUs and Reserved Instances for Windows and SQL Server on the same instance
type before October 15, 2025, were added to an opt-out list to maintain their current billing experience.
To take advantage of Optimize CPU license savings, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to be removed
from the opt-out list.

## How Optimize CPUs works to save on licensing fees

The following examples help to illustrate the cost savings that are possible
when you configure your CPU usage.

**Example 1: Default billing** This example shows an r7i.8xlarge instance launched
from a license-included Windows and SQL Server Enterprise AMI that ran for 100 hours with the default
CPU configuration of 32 vCPUs for the instance type (3200 vCPU hours).

The bill shows one line item with a combined rate that includes both usage and licensing fees.

![Sample bill with default billing for license-included Windows and SQL Server Enterprise instance.](images/optimize-cpus-sample-bill-default.png)

**Example 2: Optimize CPUs billing** This example shows an r7i.8xlarge
instance launched from a license-included Windows and SQL Server Enterprise AMI. To save on license fees,
the number of CPUs that are active was reduced to 16 vCPUs. Then the instance ran for 100 hours
with the new configuration.

The bill shows the following two line items.

Billing description: **Elastic Compute Cloud**

The first line item shows the baseline cost of the Windows and SQL Server instance that ran for 100 hours
($211.68).

Billing description: **Amazon EC2 Optimize CPU License Included Third Party Fees**

The second line item covers licensing fees based on the number of vCPUs that were active
for the billing period ($673.60).

![Sample bill with Optimize CPUs billing for a license-included Windows and SQL Server Enterprise instance.](images/optimize-cpus-sample-bill-optimized.png)

**Example 3: Optimize CPUs billing with Savings Plans** This example shows an
r7i.8xlarge instance launched from a license-included Windows and SQL Server Enterprise AMI. To save on
license fees, the number of CPUs that are active was reduced to 16 vCPUs. Then the instance ran for 100 hours
with the new configuration.

A one year _No Upfront Compute Savings Plan_ with a $1.60/hour (rounded) commitment provides
further cost savings that reduce the baseline cost of the Windows and SQL Server instance. The Savings Plan commitment
covers the full 100 hour usage of the r7i.8xlarge instance for a Savings Plans rate of $1.53362/hour.

The bill shows the following line items.

Billing description: **Savings Plans for Compute usage**

The first line item shows the Savings Plan commitment for the full 100 hour usage ($160.00).

Billing description: **Elastic Compute Cloud**

The second line item contains two entries. The first entry shows what the baseline cost of the
Windows and SQL Server instance that ran for 100 hours would have been without the Savings Plan ($211.68).
The second entry shows that the full baseline cost was covered by the Compute Savings Plan (-$211.68),
which yields a net cost of zero for this line item.

Billing description: **Amazon EC2 Optimize CPU License Included Third Party Fees**

The third line item covers licensing fees based on the number of vCPUs that were active
for the billing period ($673.60).

![Sample bill with a Savings Plan and Optimize CPUs billing for a license-included Windows and SQL Server Enterprise instance.](images/optimize-cpus-sample-bill-savings-plan.png)
