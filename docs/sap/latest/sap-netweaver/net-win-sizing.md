# Sizing

One of the first points to consider is whether this deployment is a completely new project (greenfield) or a migration. Sizing then applies across three key areas: compute, storage, and network.

## Compute

Understanding the compute requirement helps you select the best matching EC2 instance type from the available list of SAP-certified instances.

If this is a greenfield deployment, use the SAP Quick Sizer tool to calculate the SAP Application Performance Standard (SAPS) compute requirement and use that value to select the EC2 instance that is the closest match with the best cost. Also check that the EC2 instance you select provides sufficient EBS and overall network throughput to satisfy your application requirements.

For migrations, you can use a number of data sources to help choose the best instance size:

- Source system utilization and workload patterns (EarlyWatch alert reports, etc.)
- Source system specification: CPU, memory, storage size, throughput, IOPS, network
- Source system SAPS rating

###### Selecting EC2 Instance Type

It’s important to consider storage and network performance as well as compute, to ensure the selection of the best EC2 instance type.

After the workload is running on AWS, you can use a process called [right sizing](../../../aws-technical-content/latest/cost-optimization-right-sizing/identifying-opportunities-to-right-size.md "../../../aws-technical-content/latest/cost-optimization-right-sizing/identifying-opportunities-to-right-size.md") to refine the size that you actually need. Right sizing is best thought of as an [on-going process](../../../aws-technical-content/latest/cost-optimization-right-sizing/right-sizing-ongoing-process.md "../../../aws-technical-content/latest/cost-optimization-right-sizing/right-sizing-ongoing-process.md").

## Storage

Deploying SAP NetWeaver on Windows on AWS requires a minimum amount of storage and storage layout as per the SAP NetWeaver documentation for Windows. See the SAP documentation for further details on minimum and recommended storage sizes and storage layout. The EBS volumes should be created to match these requirements.

Verify that the amount of storage is adequate to provide sufficient I/O performance, as the performance of a General Purpose SSD (gp2) volume is related to the overall volume size. To achieve higher throughput and IOPS performance, the striping of volumes is often considered but this is usually not necessary for the NetWeaver application layer.

## Network

Network performance is often not explicitly stated as a requirement in SAP sizing, but you can check the network performance of each [EC2 instance type](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") to ensure that you are delivering the required performance.
