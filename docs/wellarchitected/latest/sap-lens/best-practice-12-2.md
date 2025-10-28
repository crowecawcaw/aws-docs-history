# Best Practice 12.2 – Establish a

method for recovering configuration data

A number of different types of data, which are required to run an SAP workload, do not
reside in the SAP database. This includes operating system configuration, metadata to
recreate the required AWS resources, and data required by the SAP applications stored
within a file system. Define a process for recovering or recreating this data in the event
of data loss.

**Suggestion 12.2.1 – Define infrastructure as code approach to the
creation and change of configuration**

Manual changes made directly to individual instances can quickly lead to
inconsistencies in configuration between systems and a reliance on backups to recover
state. By using infrastructure as code, you can deploy your SAP systems and implement
changes in the same manner that you would manage application code. DevOps mechanisms, such
as a code pipeline, can provide additional control and testing to help ensure consistency
and repeatability within your landscape.

You should evaluate the following AWS services as part of your approach:

- AWS Service: [AWS Launch
  Wizard for SAP](https://aws.amazon.com/launchwizard/ "https://aws.amazon.com/launchwizard/")
- AWS Service: [EC2 Image
  Builder](https://aws.amazon.com/image-builder/ "https://aws.amazon.com/image-builder/")
- AWS Service: [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- SAP on AWS Blog: [DevOps for SAP](https://aws.amazon.com/blogs/awsforsap/category/devops/ "https://aws.amazon.com/blogs/awsforsap/category/devops/")
- AWS Documentation: [Introduction to DevOps on AWS](../../../whitepapers/latest/introduction-devops-aws/welcome.md "../../../whitepapers/latest/introduction-devops-aws/welcome.md")
- AWS Documentation: [Launch Service Catalog products created with AWS Launch Wizard](../../../launchwizard/latest/userguide/launch-wizard-sap-service-catalog.md "../../../launchwizard/latest/userguide/launch-wizard-sap-service-catalog.md")

**Suggestion 12.2.2 – Define an approach for backups of file system
contents, including the root volume**

Operating system packages and configuration, application binaries, and file system
contents are integral to running an SAP system, but are not part of the core SAP database
backup. Evaluate mechanisms to secure and restore this data, including Amazon Machine
Images (AMIs), EBS volume snapshots, and other backup options.

The frequency and alignment of AMIs, snapshots, and file system copies should be
considered, as well as the granularity for recovery and the time taken.

In certain scenarios, using infrastructure as code might reduce backup requirements
for non-business data by focusing on recreation versus restoration.

- SAP Documentation: [Required File Systems and Directories](https://help.sap.com/viewer/910828cec5d14d6685da380aec1dc4ae/CURRENT_VERSION/en-US/de6cad1446a743d3853dbcae48bddfba.html "https://help.sap.com/viewer/910828cec5d14d6685da380aec1dc4ae/CURRENT_VERSION/en-US/de6cad1446a743d3853dbcae48bddfba.html")
- AWS Documentation: [Designing a backup and recovery solution](../../../prescriptive-guidance/latest/backup-recovery/design.md "../../../prescriptive-guidance/latest/backup-recovery/design.md")

**Suggestion 12.2.3 – Document any manual settings**

Any manual activities which are not contained in the database, deployable by code, or
able to be restored using volume backups, should be recorded to ensure an SAP system can
be recreated in the worst case scenario.
