# SAP HANA Sizing

The size of the SAP HANA system required on the AWS Cloud depends on the migration scenario. As mentioned earlier, migrating SAP HANA to AWS involves two possible scenarios: rehosting or replatforming.

## Memory Requirements for Rehosting

Because rehosting implies that you are already running SAP HANA, you can determine the size of the SAP HANA system you need on the AWS Cloud from the peak memory utilization of your existing SAP HANA system. You may have oversized your on-premises SAP HANA environment (for example, to support future growth), so measuring peak memory utilization is a better approach than measuring allocated memory. When you have determined the base memory requirement, you should choose the smallest SAP-certified EC2 instance that provides more memory than your base requirement.

There are three ways to determine peak memory utilization of your existing SAP HANA system:

- SAP HANA Studio: The overview tab of the SAP HANA Studio administration view provides a memory utilization summary.
- SAP EarlyWatch alerts: This is a free, automated service from SAP that helps you monitor major administrative areas of your SAP system. See the [SAP portal](https://support.sap.com/en/offerings-programs/support-services/earlywatch-alert.html "https://support.sap.com/en/offerings-programs/support-services/earlywatch-alert.html") for details.
- SQL statements: SAP provides SQL statements that you can use to determine peak memory utilization. For details, see [SAP KBA 1999997 – FAQ: SAP HANA Memory](https://launchpad.support.sap.com/#/notes/1999997 "https://launchpad.support.sap.com/#/notes/1999997") and [SAP Note 1969700 – SQL statement collection for SAP HANA](https://service.sap.com/sap/support/notes/1969700 "https://service.sap.com/sap/support/notes/1969700").

###### Tip

We recommend determining peak memory utilization for a timeframe during which your system utilization is likely to be high (for example, during year-end processing or a major sales event).

## Memory Requirements for Replatforming

The replatforming scenario involves two possibilities:

- You are already running SAP HANA but you want to change your operating system—​for example, from Red Hat Enterprise Linux (RHEL) to SUSE Linux Enterprise Server (SLES) or the other way around—​when you migrate to the AWS Cloud, or you are migrating from an IBM POWER system to the x86 platform. In this case, you should size SAP HANA as described for the rehosting scenario.
- You are migrating from _anyDB_ to SAP HANA. There are multiple ways you can estimate your memory requirements:
  - SAP standard reports for estimation: This is the best possible approach and is based on standard sizing reports provided by SAP. For examples, see the following SAP Notes:
    - [1736976 – Sizing Report for BW on HANA](https://launchpad.support.sap.com/#/notes/1736976 "https://launchpad.support.sap.com/#/notes/1736976")
    - [1637145 – SAP BW on HANA: Sizing SAP In-Memory Database](https://launchpad.support.sap.com/#/notes/1637145 "https://launchpad.support.sap.com/#/notes/1637145")
    - [1872170 - Business Suite on HANA and S/4HANA sizing report](https://launchpad.support.sap.com/#/notes/1872170 "https://launchpad.support.sap.com/#/notes/1872170")
    - [1736976 – Sizing Report for BW on HANA](https://launchpad.support.sap.com/#/notes/1736976 "https://launchpad.support.sap.com/#/notes/1736976")

  - SQL statements: SAP provides scripts that you can run in your existing environment to get high-level SAP HANA sizing estimates. These scripts run SQL statements against your existing database to estimate SAP HANA memory requirements. For more information, see [SAP Note 1793345 - Sizing for SAP Suite on SAP HANA](https://service.sap.com/sap/support/notes/1793345 "https://service.sap.com/sap/support/notes/1793345").
  - Rule of thumb: See the PDF attached to [SAP Note 1793345 - SAP HANA Sizing for SAP Suite on SAP HANA](https://service.sap.com/sap/support/notes/1793345 "https://service.sap.com/sap/support/notes/1793345") for instructions on estimating SAP HANA memory requirements manually. Note that this will be a very rough and generic estimate.

You should also consider the following SAP notes and Knowledge Base articles for SAP HANA sizing considerations:

- [2388483 – How-To: Data Management for Technical Tables](http://service.sap.com/sap/support/notes/2388483 "http://service.sap.com/sap/support/notes/2388483")
- [1855041 – Sizing Recommendation for Master Node in BW-on-HANA](http://service.sap.com/sap/support/notes/1855041 "http://service.sap.com/sap/support/notes/1855041")
- [1702409 – HANA DB: Optimal number of scale out nodes for BW on HANA](http://service.sap.com/sap/support/notes/1702409 "http://service.sap.com/sap/support/notes/1702409")

## Instance Sizing for SAP HANA

AWS offers SAP-certified systems that are configured to meet the specific SAP HANA performance requirements. For more information, see [SAP Note 1943937 – Hardware Configuration Check Tool - Central Note](https://service.sap.com/sap/support/notes/1943937 "https://service.sap.com/sap/support/notes/1943937"), and [Amazon EC2 instances for SAP on AWS](../general/ec2-instance-types-sap.md "../general/ec2-instance-types-sap.md"). After you have determined your SAP HANA sizing, you can map your requirements to the EC2 instance family sizes. That is, you map the maximum amount of memory required for each of your SAP HANA instances to the maximum amount of memory available for your desired EC2 instance type. You should also consider appropriate storage volume types and sizes to ensure optimal performance of the SAP HANA database. For best practices and recommendations for volume types and file system layout, see the [AWS Launch Wizard for SAP](../../../launchwizard/latest/userguide/launch-wizard-sap.md "../../../launchwizard/latest/userguide/launch-wizard-sap.md").

###### Note

Only production SAP HANA systems need to run on certified configurations that meet SAP HANA key performance indicators (KPIs). SAP provides more flexibility when running SAP HANA non-production systems. For more information, see [SAP HANA TDI – FAQ](https://www.sap.com/documents/2016/05/e8705aae-717c-0010-82c7-eda71af511fa.html "https://www.sap.com/documents/2016/05/e8705aae-717c-0010-82c7-eda71af511fa.html") and [OSS Note 2271345](https://launchpad.support.sap.com/#/notes/2271345 "https://launchpad.support.sap.com/#/notes/2271345") on the SAP website.

## Network Planning and Sizing

You will need to consider network planning and sizing for the amount of data you will be transferring to AWS. Data transfer time depends on network bandwidth available to AWS and influences total downtime. Higher bandwidth helps with faster data transfer and helps reduce overall migration time. For non-production systems where downtime isn’t critical, you can use a smaller network pipe to reduce costs. Alternatively, to transfer extremely large data, you can use services like [AWS Snowball](https://aws.amazon.com/snowball/faqs/ "https://aws.amazon.com/snowball/faqs/") for a physical (non-network) transport of data to AWS. We’ll discuss AWS Snowball more extensively later in this guide.

As a guideline, you can use this formula to help estimate how long your network data transfer might take:

(Total bytes to be transferred / Transfer rate per second) = Total transfer time in seconds

For example, for a 1 TB SAP HANA appliance, the total bytes to be transferred is usually 50% of the memory, which would be 512 GB. The transfer rate per second is your network transfer rate—​if you had a 1 Gb [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/") connection to AWS, you could transfer up to 125 MB per second, and your total data transfer time would be:

512 GB / 125 MB per second = 4,096 seconds (or 1.1 hours)

After you determine the amount of data you need to transfer and how much time you have available to transfer the files, you can determine the AWS connectivity options that best fit your cost, speed, and connectivity requirements.

## SAP HANA Scale-up and Scale-out

AWS provides several types of EC2 instances for SAP HANA workloads. This gives you options for your SAP HANA scale-up and scale-out deployments. In a scale-up scenario, you utilize the compute, memory, network, and I/O capacity of a single EC2 instance. If you require more capacity, you can resize your instances to a different EC2 instance type. For example, if you’re using an R4 instance type and it becomes too small for your workload, you can change it to an R5, X1, or X1e instance type. The limitation is the maximum capacity of a single EC2 instance. In AWS, scale-up enables you to start with the smallest EC2 instance type that meets your requirements and grow as needed. If your requirements change or new requirements surface, you can easily scale up to meet the changing requirements.

In a scale-out scenario, you add capacity to your SAP HANA system by adding new EC2 instances to the SAP HANA cluster. For example, once you reach the maximum memory capacity of a single EC2 instance, you can scale out your SAP HANA cluster and add more instances. AWS has certified SAP HANA scale-out clusters that support up to 100 TiB of memory. Please note that the minimum number of recommended nodes in an SAP HANA scale-out cluster can be as low as two nodes; for more information, see [SAP Note 1702409 - HANA DB: Optimal number of scale out nodes for BW on HANA](https://launchpad.support.sap.com/#/notes/1702409 "https://launchpad.support.sap.com/#/notes/1702409"). It’s likely that your sizing estimates will reveal the need to plan for a scale-out configuration before you start your SAP HANA migration. AWS gives you the ability to easily deploy SAP HANA scale-out configurations when you use the [AWS Launch Wizard for SAP](../../../launchwizard/latest/userguide/launch-wizard-sap.md "../../../launchwizard/latest/userguide/launch-wizard-sap.md").

The following table illustrates example scale-up and scale-out sizing.

| Scenario      | Source configuration      | Target configuration      |
| ------------- | ------------------------- | ------------------------- |
| **Scale-up**  | r5.8xlarge                | r5.16xlarge               |
| **Scale-up**  | r5.16xlarge               | x2idn.16xlarge            |
| **Scale-up**  | x2idn.32xlarge            | x2iedn.32xlarge           |
| **Scale-out** | 3 nodes of x2idn.16xlarge | 4 nodes of x2idn.16xlarge |
| **Scale-out** | x2idn.32xlarge            | 3 nodes of x2idn.16xlarge |

When you finalize your SAP sizing and SAP HANA deployment models, you can plan your migration strategy.

In addition to SAP HANA sizing, you may also need to size your SAP application tier. To find the SAP Application Performance Standard (SAPS) ratings of SAP-certified EC2 instances, see [SAP Standard Application Benchmarks](https://www.sap.com/about/benchmark.html "https://www.sap.com/about/benchmark.html") and the [SAP on AWS support note](https://service.sap.com/sap/support/notes/1656099 "https://service.sap.com/sap/support/notes/1656099") on the SAP website (SAP login required).
