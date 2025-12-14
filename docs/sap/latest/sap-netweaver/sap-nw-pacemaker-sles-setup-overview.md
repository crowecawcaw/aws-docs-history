# Setup Overview

You must meet the following prerequisites before commencing setup.

###### Topics

- [Deployed Cluster Infrastructure](#cluster-nw-sles "#cluster-nw-sles")
- [Supported Operating System](#supported-os-nw-sles "#supported-os-nw-sles")
- [SAP and SUSE references](#references-nw-sles "#references-nw-sles")
- [Required Access for Setup](#access-nw-sles "#access-nw-sles")
- [Reliability Requirements Defined](#reliability-nw-sles "#reliability-nw-sles")

## Deployed Cluster Infrastructure

Ensure that your AWS networking requirements and Amazon EC2 instances where SAP workloads are installed, are correctly configured for SAP. For more information, see [SAP NetWeaver Environment Setup for Linux on AWS](std-sap-netweaver-environment-setup.md "std-sap-netweaver-environment-setup.md").

See the following ASCS cluster specific requirements.

- Two cluster nodes created in private subnets in separate Availability Zones within the same Amazon VPC and AWS Region
- Access to the route table(s) that are associated with the chosen subnets

For more information, see [AWS – Overlay IP](sap-nw-pacemaker-sles-concepts.md#overlay-ip-sles "sap-nw-pacemaker-sles-concepts.md#overlay-ip-sles").

- Amazon EC2 instances must have connectivity to the Amazon EC2 endpoint via either internet or an Amazon VPC endpoint.

## Supported Operating System

Protecting the ABAP SAP Central Services (ASCS) with a pacemaker cluster requires packages from SUSE, including targeted cluster resource agents for SAP and AWS that may not be available in standard repositories.

For deploying SAP applications on SUSE, SAP and SUSE recommend using SUSE Linux Enterprise Server for SAP applications (SLES for SAP). SLES for SAP provides additional benefits, including Extended Service Pack Overlap Support (ESPOS), configuration and tuning packages for SAP applications, and High Availability Extensions (HAE). For more details, see SUSE website at [SUSE Linux Enterprise Server for SAP Applications](https://www.suse.com/products/sles-for-sap/ "https://www.suse.com/products/sles-for-sap/").

SLES for SAP is available at [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace") with an hourly or annual subscription. You can also use the bring your own subscription (BYOS) model.

## SAP and SUSE references

In addition to this guide, see the following references for more details.

- [SUSE documentation – SAP S/4 HANA - Enqueue Replication 2 High Availability Cluster With Simple Mount](https://documentation.suse.com/sbp/sap-15/html/SAP-S4HA10-setupguide-simplemount-sle15/index.html "https://documentation.suse.com/sbp/sap-15/html/SAP-S4HA10-setupguide-simplemount-sle15/index.html")
- [SUSE documentation – SAP S/4 HANA - Enqueue Replication 2 High Availability Cluster](https://documentation.suse.com/sbp/all/single-html/SAP-S4HA10-setupguide-sle15/#id-1 "https://documentation.suse.com/sbp/all/single-html/SAP-S4HA10-setupguide-sle15/#id-1")
- [SAP Note: 1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://me.sap.com/notes/1656099 "https://me.sap.com/notes/1656099")
- [SAP Note: 1984787 - SUSE Linux Enterprise Server 12: Installation Notes](https://me.sap.com/notes/1984787 "https://me.sap.com/notes/1984787")
- [SAP Note: 2578899 - SUSE Linux Enterprise Server 15: Installation Notes](https://me.sap.com/notes/2578899 "https://me.sap.com/notes/2578899")
- [SAP Note: 1275776 - Linux: Preparing SLES for SAP environments](https://me.sap.com/notes/1275776 "https://me.sap.com/notes/1275776")

You must have SAP portal access for reading all SAP Notes.

## Required Access for Setup

The following access is required for setting up the cluster.

- An IAM user with the following privileges.
  - modify Amazon VPC route tables
  - modify Amazon EC2 instance properties
  - create IAM policies and roles
  - create Amazon EFS file systems

- Root access to the operating system of both cluster nodes
- SAP administrative user access – `<sid>adm`

In case of a new install, this user is created by the install process.

## Reliability Requirements Defined

The SAP Lens of the Well-Architected framework, in particular the Reliability pillar, can be used to understand the reliability requirements for your SAP workload.

The ASCS is a single point of failure in a highly available SAP architecture. The impact of an outage of this component must be evaluated against factors, such as, recovery point objective (RPO), recovery time objective (RTO), cost and operation complexity. For more information, see [Reliability](../../../wellarchitected/latest/sap-lens/reliability.md "../../../wellarchitected/latest/sap-lens/reliability.md") in SAP Lens - AWS Well-Architected Framework.
