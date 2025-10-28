# Sizing

Sizing applies to three key areas - compute, network, and storage.

## Compute

AWS has certified multiple instance families with different sizes to run SAP workloads. For more details, see [Amazon EC2 Instance Types for SAP](https://aws.amazon.com/sap/instance-types/ "https://aws.amazon.com/sap/instance-types/").

To provision instances based on your requirements, you can use the [Right sizing](../../../whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md#introduction-section "../../../whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md#introduction-section") process. This process can help you optimize costs. Although it is ideal to use the right sizing approach when you move your SAP workloads to AWS Cloud, it is an [ongoing process](../../../whitepapers/latest/cost-optimization-right-sizing/right-sizing-ongoing-process.md "../../../whitepapers/latest/cost-optimization-right-sizing/right-sizing-ongoing-process.md"). We recommend you to use the latest generation of your selected instance family.

For a greenfield (new) deployment of SAP workloads, you can use the [Quick Sizer tool](https://help.sap.com/viewer/22bbe89ef68b4d0e98d05f0d56a7f6c8/2020.000/en-US/067579ee1f7f4ffba00c4abd9bc6f832.html "https://help.sap.com/viewer/22bbe89ef68b4d0e98d05f0d56a7f6c8/2020.000/en-US/067579ee1f7f4ffba00c4abd9bc6f832.html") to calculate the compute requirement in SAPS. This helps you to select the closest matching Amazon EC2 instance for a price that is most economical for you. Before completing your selection, ensure that the selected Amazon EC2 instance provides enough Amazon EBS and overall network throughput to meet your application requirements.

For migrations, you can use any of the following data sources to decide the right size of your instance:

- Source system utilization and workload patterns, such as EarlyWatch alert reports.
- Source system specification: CPU, memory, storage size + throughput + IOPS, network.
- Source system SAPS rating.

For more details, see [Compute & storage](compstore-orc-sap-nw-lx.md "compstore-orc-sap-nw-lx.md").

## Network

Network performance is often not explicitly stated as a requirement in SAP sizing. AWS enables you to check the network performance of all [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

Ensure that you have your network components setup to deploy resources related to your SAP workload. If you haven’t already setup network components like Amazon VPC, subnets, route tables etc., you can use the, [AWS Quick Start Modular and Scalable VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/") to most effectively deploy scalable Amazon VPC architecture in minutes. After setting up your Amazon VPC, you must set up Amazon EC2 instances within the Amazon VPC for your SAP workloads.

You also must set up a secured network connection between the corporate data center and the Amazon VPC along with the appropriate route table configuration, if it isn’t already configured.

## Storage

Deploying SAP workloads on AWS required a minimum storage size and layout, based on your choice of OS/DB platform. For further details, refer to the relevant SAP documentation. You need to create Amazon EBS volumes that match these requirements.

You must check that the storage required is enough to provide sufficient I/O performance. The new `gp3` volume is ideal for Oracle workloads that require smaller volume size. With `gp3`, the storage throughput and IOPS are decoupled from the size and can scale independently.

The io2 volume is well-suited for I/O-intensive database workloads that require sustained IOPS performance or more than 16,000 IOPS. The `io2 Block Express` is another provisioned IOPS SSD volume for workloads that require sub-millisecond latency, sustained IOPS performance, and more than 64,000 IOPS or 1,000 MiB/s of throughput.

For more details, see [Storage for Oracle](storeorc-orc-sap-nw-lx.md "storeorc-orc-sap-nw-lx.md").
