

# Automated SAP NetWeaver on AWS installation prerequisites
<a name="auto-installation-prerequisites"></a>

In addition to the prerequisites described in the [Automation prerequisites](sap-nw-automation.md#automation-prerequisites) section of this guide, verify the following prerequisites that are specific to automated SAP installation:
+ You must have an existing infrastructure deployed.

  The example described in this guide uses a SAP HANA database, an SAP Central Services (ASCS) instance, and a database instance. The * AWS for SAP* blog has a [Terraform your SAP Infrastructure on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/) example.
+ SAP media files must be available.

  You must provide the SAP installation media files, which are obtained from SAP, in an Amazon S3 bucket. For more information, see [Make SAP application software available for AWS Launch Wizard for SAP to deploy SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-software-install-details.html) in the * AWS Launch Wizard User Guide*. If you use the sample code provided in this guide, the media files are copied to local Amazon Elastic Block Store volumes.

 **SAP Notes** 

Read the following SAP Note:
+ SAP Note: [2230669 - System Provisioning Using a Parameter Input File](https://me.sap.com/notes/2230669) 

 **Additional references** 

Before you begin, you can also familiarize yourself with how SAP works on AWS by reading the following documentation:
+  [SAP on AWS Planning](https://docs.aws.amazon.com/sap/latest/general/overview-sap-planning.html) in the *General SAP Guides* 
+  [Amazon EC2 instance types for SAP on AWS](https://docs.aws.amazon.com/sap/latest/general/ec2-instance-types-sap.html) in the *General SAP Guides* 
+  [SAP NetWeaver Environment Setup for Linux on AWS](https://docs.aws.amazon.com/sap/latest/sap-netweaver/std-sap-netweaver-environment-setup.html) in the *SAP NetWeaver Guides* 