# Operating System

You can deploy your SAP workload on SUSE Linux Enterprise Server (SLES) for SAP, Red Hat Enterprise Linux for SAP with High Availability and Update Services (RHEL for SAP with HA and US), or RHEL for SAP Solutions.

SLES for SAP and RHEL for SAP with HA and US are available in the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace") under an hourly or an annual subscription model.

## SLES

SLES for SAP provides additional benefits, including Extended Service Pack Overlap Support (ESPOS), configuration and tuning packages for SAP applications, and High Availability Extensions (HAE). See the [SUSE SLES for SAP product page](https://www.suse.com/products/sles-for-sap/ "https://www.suse.com/products/sles-for-sap/"). We strongly recommend using SLES for SAP instead of SLES for all your SAP workloads.

If you plan to use Bring Your Own Subscription (BYOS) images provided by SUSE, ensure that you have the registration code required to register your instance with SUSE to access repositories for software updates.

## RHEL

RHEL for SAP with HA and US provides access to Red Hat Pacemaker cluster software for High Availability, extended update support, and the libraries that are required to configure pacemaker HA. For details, see the [RHEL for SAP Offerings on AWS FAQ](https://access.redhat.com/articles/3671571 "https://access.redhat.com/articles/3671571")in the _Red Hat knowledgebase_.

If you plan to use the BYOS model with RHEL, either through the [Red Hat Cloud Access program](https://access.redhat.com/articles/3490141 "https://access.redhat.com/articles/3490141") or another means, ensure that you have access to a RHEL for SAP Solutions subscription. For details, see [Overview of the Red Hat Enterprise Linux for SAP Solutions subscription](https://access.redhat.com/solutions/3082481 "https://access.redhat.com/solutions/3082481") in the _Red Hat knowledgebase_.

The correct subscription is required to download the required packages for configuring the Pacemaker cluster.

## Compute

AWS provides a wide array of SAP supported Amazon EC2 instances for your SAP workloads. See [SAP Note 1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") for details. Based on the results of your sizing exercise, you can deploy your IBM Db2 on any of the SAP supported Amazon EC2 instances that meets your requirement.

## Storage

[Amazon EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") volumes are designed to be highly available and durable. EBS volume data is replicated across multiple servers in an AZ to prevent the loss of data from the failure of any single component. Due to this built in protection, you don’t have to configure RAID 1 for volumes containing database transaction log files and Db2 binaries.

We don’t recommend RAID 5 for container files for data, index, or temporary tablespaces on AWS for the following reasons:

- As mentioned previously, volumes are replicated within AZ by default.
- Parity write operations of RAID 5 consume some of the Input/Output Operations Per Second (IOPS) available to your volume and will reduce the overall Input/Output (IO) available for database operations by about 20-30% over RAID 0 configuration.
