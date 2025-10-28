# Automated SAP NetWeaver on AWS installation prerequisites

In addition to the prerequisites described in the [Automation prerequisites](sap-nw-automation.md#automation-prerequisites "sap-nw-automation.md#automation-prerequisites") section of this guide, verify the following prerequisites that are specific to automated SAP installation:

- You must have an existing infrastructure deployed.

The example described in this guide uses a SAP HANA database, an SAP Central Services (ASCS) instance, and a database instance. The _AWS for SAP_ blog has a [Terraform your SAP Infrastructure on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/ "https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/") example.

- SAP media files must be available.

You must provide the SAP installation media files, which are obtained from SAP, in an Amazon S3 bucket. For more information, see [Make SAP application software available for AWS Launch Wizard for SAP to deploy SAP](../../../launchwizard/latest/userguide/launch-wizard-sap-software-install-details.md "../../../launchwizard/latest/userguide/launch-wizard-sap-software-install-details.md") in the _AWS Launch Wizard User Guide_. If you use the sample code provided in this guide, the media files are copied to local Amazon Elastic Block Store volumes.

**SAP Notes**

Read the following SAP Note:

- SAP Note: [2230669 - System Provisioning Using a Parameter Input File](https://launchpad.support.sap.com/#/notes/2230669 "https://launchpad.support.sap.com/#/notes/2230669")

**Additional references**

Before you begin, you can also familiarize yourself with how SAP works on AWS by reading the following documentation:

- [SAP on AWS Planning](../general/overview-sap-planning.md "../general/overview-sap-planning.md") in the _General SAP Guides_
- [Amazon EC2 instance types for SAP on AWS](../general/ec2-instance-types-sap.md "../general/ec2-instance-types-sap.md") in the _General SAP Guides_
- [SAP NetWeaver Environment Setup for Linux on AWS](std-sap-netweaver-environment-setup.md "std-sap-netweaver-environment-setup.md") in the _SAP NetWeaver Guides_
