# Generating estimates for Windows Servers and SQL Servers on

EC2 Dedicated Hosts

You can use the workload calculator in AWS Pricing Calculator as a guide to the AWS tenancy
qualifications for Microsoft Windows Server and SQL Server on Amazon Elastic Compute Cloud (Amazon EC2). You can use
the workload calculator to estimate AWS cost using minimal information or generate a rough
estimate.

For options for using Microsoft software licenses on the AWS Cloud, see [Microsoft Licensing on
AWS](https://aws.amazon.com/windows/resources/licensing/ "https://aws.amazon.com/windows/resources/licensing/").

###### Topics

- [Procedure](#windows-sql-ec2-estimate "#windows-sql-ec2-estimate")
- [Licensing and tenancy
  recommendations](#estimate-workload-tenancy-ec2 "#estimate-workload-tenancy-ec2")
- [Machine specifications](#estimate-workload-configure-ec2 "#estimate-workload-configure-ec2")
- [Review dedicated hosts](#estimate-dedicatedhost-ec2 "#estimate-dedicatedhost-ec2")
- [Pricing strategy](#estimate-workload-pricing-ec2 "#estimate-workload-pricing-ec2")
- [Cost details](#estimate-workload-cost-ec2 "#estimate-workload-cost-ec2")
- [Bulk upload instructions for Dedicated Hosts](estimate-bulk-upload-ec2.md "estimate-bulk-upload-ec2.md")

## Procedure

###### To generate an estimate for Windows Server and SQL Server on Amazon EC2 Dedicated Hosts

1. Open AWS Pricing Calculator at [https://calculator.aws/#/](https://calculator.aws/#/ "https://calculator.aws/#/").
2. Choose **Create estimate**.
3. Do one of the following:
   - Under **Windows Server and SQL Server on Amazon EC2**, choose
     **Configure**.
   - From the **Find service** search bar, search for **Windows Server and SQL Server on Amazon EC2**. Then, choose **Configure**.

4. On the **Configure Windows Server and SQL Server on Amazon EC2**
   page, choose your customized settings.
   - For more information about license and tenancy options, see [Licensing and tenancy
     recommendations](#estimate-workload-tenancy-ec2 "#estimate-workload-tenancy-ec2").
   - For more information about machine specifications, see [Machine specifications](#estimate-workload-configure-ec2 "#estimate-workload-configure-ec2").
   - For more information about pricing strategy options, see [Pricing strategy](#estimate-workload-pricing-ec2 "#estimate-workload-pricing-ec2").
   - For more information about reviewing dedicated hosts, see [Review dedicated hosts](#estimate-dedicatedhost-ec2 "#estimate-dedicatedhost-ec2").
   - For more instructions about cost details, see [Cost details](#estimate-workload-cost-ec2 "#estimate-workload-cost-ec2").
   - For instructions on how to bulk upload your machine specifications for Dedicated Hosts, see [Bulk upload instructions for Dedicated Hosts](estimate-bulk-upload-ec2.md "estimate-bulk-upload-ec2.md").

5. Choose **Save and add service** or **Save and view summary**.

## Licensing and tenancy

recommendations

You can determine your AWS licensing and tenancy options for your workload through
your choices for Windows Server and SQL Server licensing inputs. The licensing options
include AWS provided licenses with License Included (LI) offerings. They also include
your existing licenses with Bring Your Own License (BYOL) offerings for optimal cost
savings. You can identify which is the most suitable cloud tenancy.

The following table shows the AWS licensing and tenancy scenarios supported by AWS Pricing Calculator.

| Windows Server | SQL Server | AWS tenancy                       |
| -------------- | ---------- | --------------------------------- |
| LI             | LI         | Shared tenancy                    |
| LI             | BYOL       | Shared tenancy or Dedicated Hosts |
| BYOL           | BYOL       | Dedicated Hosts                   |
| BYOL           | LI         | Not supported                     |

## Machine specifications

Based on your choice of machine specification, we recommend that you select the Amazon EC2
instance that AWS Pricing Calculator uses to generate an estimate for your cost. You can also select
another instance or instances of your choosing or add multiple machine specifications
for a workload.

This section defines the terms that are mentioned in the **Configure machine
specifications** section.

\***\*Machine description\*\***

A description for the machine. This is generally a hostname identifier. If
you don't know the hostname identifier, specify unique software components
that run on this machine—for example, `WebApp DB1` or
`Webserver 1`.

\***\*Operating system\*\***

Depending on your tenancy qualification, you can choose an operating
system with a licensing option. The default value is
`Windows`.

\***\*SQL Server edition\*\***

Depending on your tenancy qualification, you can choose a SQL Server with
licensing option. The default value is `SQL Standard`.

\***\*vCPU, Memory\*\***

Enter the number of vCPUs and memory inputs for your machine
configuration. For example, 4vCPU and 8GB of memory.

\***\*Quantity\*\***

The default value is 1. This is the minimum number that's required.

## Review dedicated hosts

The **Review dedicated hosts** table shows your recommended
dedicated hosts instance family based on your inputs. You can see details such as host
family and description, instances, license count, and used capacity (virtual cores).
List count shows the license needed for a specific dedicated host.

Choose the instances to see the machines that are optimally packed within a single
dedicated host.

By choosing **Download CSV**, you can download the dedicated host, instance, and license information.

## Pricing strategy

Your choices in the **pricing strategy** section determine the
pricing strategy that AWS Pricing Calculator uses to generate your estimate.

**Pricing model**

The pricing model determines whether you're searching for a pay-as-you-use
instance or an instance that you can reserve in advance. For Reserved
Instance (RI) payment options, see **payment
options**.

The default value is `Standard Reserved Instances`. This is
because it's the most common Amazon EC2 purchase, and it offers the flexibility
with highest discount for most use cases.

**Reservation term**

When you reserve an RI, you purchase a reservation for the period of your
contract. For your contract term, choose 1 year or 3 years. By default, a
term is 1 year. This is to save costs.

**Payment options**

Payment options determine when you pay for your RI reservation.

**Full upfront** - You pay for the entire reservation
upfront, resulting in a single payment but no monthly, recurring payments.
This option provides the best discount.

**Partial upfront** - You pay for a smaller, partial
upfront fee along with monthly payments.

**No upfront** - You only pay on a monthly basis.

The default value is **No upfront**. It gives you the
least costly start-up price.

## Cost details

The cost details section provides details for your workload.

**EC2 Instance costs**

A summary of the itemized breakdown for an EC2 instance. Pause on each row
to show additional information, such as instance type, operating system, SQL
version, vCPU, memory, quantity, optimize CPU, and SQL passive node.

**Amazon EBS costs**

The itemized cost breakdown for Amazon EBS.

**SQL bring your own license summary**

A summary to clarify the number of cores for your BYOL SQL Server
licenses.
