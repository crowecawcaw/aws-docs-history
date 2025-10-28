# Best Practice 14.3 - Evaluate Amazon

EFS and Amazon FSx performance suitability for your SAP use case

Amazon EFS (Linux) and Amazon FSx (Windows) provide highly durable and available file
systems that can span multiple Availability Zones. Both solutions are designed to deliver
high performance, however, when choosing to use network file systems consider the access
patterns. For example, many small files, highly parallel writes or high write/read ratios
might not be suitable. For SAP workloads, this might apply to SAP HANA XSA, Java
executables, or large numbers of job and spool logs.

Amazon FSx for NetApp ONTAP is also a SAP-certified storage type for workloads including S/4HANA,
Business Suite on HANA, BW/4HANA, Business Warehouse on HANA, and Data Mart Solutions on
HANA. FSx for ONTAP allows you to easily create application-consistent snapshots,
space-efficient database clones in seconds and automatic replication of your database across
AWS Regions.

**Suggestion 14.3.1 – Evaluate scale and performance
options**

Amazon EFS has two modes for performance (general purpose and max I/O) and two
different performance modes (bursting mode and provisioned). For SAP applications, general
purpose performance mode usually provides sufficient I/O. There may be scenarios in which
provisioned throughput should be considered, such as when the amount of data in your file
system is low relative to throughput demands.

- AWS Documentation: [Amazon Elastic File
  System (EFS) | FAQs - Scale and Performance](https://aws.amazon.com/efs/faq/#Scale_and_performance "https://aws.amazon.com/efs/faq/#Scale_and_performance")
- AWS Documentation: [Amazon FSx
  for Windows File Server Features | Scale and Performance](https://aws.amazon.com/fsx/windows/features/#Performance_and_scale "https://aws.amazon.com/fsx/windows/features/#Performance_and_scale")
- AWS Documentation: [SAP HANA on AWS with Amazon FSx for NetApp ONTAP](../../../sap/latest/sap-hana/sap-hana-amazon-fsx.md "../../../sap/latest/sap-hana/sap-hana-amazon-fsx.md")

**Suggestion 14.3.2 - Consider temporary provisioning for short-term
requirements**

Use cases related to migrations or one-off activities might benefit from a temporary
file system where performance characteristics can be adjusted for the duration of the
event.
