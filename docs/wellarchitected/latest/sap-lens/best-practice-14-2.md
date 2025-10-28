# Best Practice 14.2 – Select and

configure EBS types aligned with performance requirements

For each filesystem function and storage service, evaluate storage layout guidelines
and tuning options to ensure that IOPS and throughput performance are optimized.

**Suggestion 14.2.1 – Evaluate storage characteristics and options for
EBS volume types**

AWS has a range of volume types with unique characteristics to suit different
performance requirements of SAP workloads. Use historical data, or sizing to evaluate the
IOPS and throughput requirements. Select your volume type by considering performance,
durability, flexibility, and cost.

IOPS and throughput of the `gp3` , `io1`, and `io2`
Block Express volume types are independent of the volume size.

IOPS and throughput of the `gp2` volume type is aligned to the volume
size. Oversizing the volume may be required to ensure the required IOPS and throughput is
available.

If choosing Amazon EBS io2 Block Express, ensure that it is available for the selected
instance types.

- AWS documentation: [Amazon EBS volume types](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md")

**Suggestion 14.2.2 – Scale linearly using LVM striping
mechanisms**

When the performance requirement cannot be met by a single EBS volume, consider
striping using Logical Volume Management (LVM). For example, if a single volume has 250
MiB/s throughput capacity, having a stripe set across four volumes can deliver 1000 MiB/s
throughput.

Volumes should be of the same size and performance characteristics.

In SAP HANA benchmark testing, the best performance has been achieved using a 256 KB
stripe size for data volumes and a 64 KB stripe size for log volumes.

Be aware of instance limits for throughput, I/O, and number of attached volumes.

- AWS Documentation: [Create an LVM Logical Volume on an EBS Volume](https://aws.amazon.com/premiumsupport/knowledge-center/create-lv-on-ebs-volume/ "https://aws.amazon.com/premiumsupport/knowledge-center/create-lv-on-ebs-volume/")
- SAP Note: [2931808

* Usage of Logical Volume Manager (LVM) with SAP HANA](https://launchpad.support.sap.com/#/notes/2931808 "https://launchpad.support.sap.com/#/notes/2931808") [Requires SAP Portal
  Access]

- AWS Documentation: [Operating System and Storage Configuration - SAP HANA on AWS](../../../sap/latest/sap-hana/operating-system-and-storage-configuration.md#:~:text=Configure%20Storage%20for%20SAP%20HANA "../../../sap/latest/sap-hana/operating-system-and-storage-configuration.md#:~:text=Configure%20Storage%20for%20SAP%20HANA")

**Suggestion 14.2.3 – To ensure SAP HANA performance, follow AWS
provided storage guidelines**

AWS works with SAP to certify storage for SAP HANA workloads according to defined
performance benchmarks. The configuration provided by AWS balances performance, cost,
and durability within the framework of the SAP TDI 5 Storage KPIs. A compliant storage
layout is detailed in the documentation and used in Launch Wizard and quick start
deployments.

- AWS Documentation: [Storage Configuration for SAP HANA - SAP HANA on AWS](../../../sap/latest/sap-hana/hana-ops-storage-config.md "../../../sap/latest/sap-hana/hana-ops-storage-config.md")
  If you deviate from the AWS configuration, it is recommended that you run the SAP
  HANA Hardware and Cloud Measurement Tools.

- SAP Note: [2493172 -
  SAP HANA Hardware and Cloud Measurement Tools](https://launchpad.support.sap.com/#/notes/2493172 "https://launchpad.support.sap.com/#/notes/2493172") [Requires SAP Portal
  Access]

When deciding between general purpose and Provisioned IOPS EBS types, it should be
noted that general purpose types meet the SAP HANA Storage KPIs. An in-memory database, such
as SAP HANA, has to load data from disk to memory upon database startup. Using Provisioned
IOPS EBS types can significantly improve startup times and also speed up tasks such as
backups and restores, which are dependent on storage performance.

**Suggestion 14.2.4 – For performant local backups at a low cost, use
`st1` storage**

When SAP solutions need local storage for storing backups, consider using a
`st1` volume type for its low cost and high throughput. `st1` is
a low-cost block storage type designed for frequently accessed, throughput-intensive
workloads.

For SAP HANA, consider using AWS Backint Agent for SAP HANA to avoid the performance
and cost impact of a two-stage backup.
