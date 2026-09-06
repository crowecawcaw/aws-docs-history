

# Setup Overview
<a name="sap-nw-pacemaker-rhel-setup-overview"></a>

You must meet the following prerequisites before commencing setup.

**Topics**
+ [Deployed Cluster Infrastructure](#cluster-nw-rhel)
+ [Supported Operating System](#supported-os-nw-rhel)
+ [SAP and Red Hat references](#references-nw-rhel)
+ [Required Access for Setup](#access-nw-rhel)
+ [Reliability Requirements Defined](#reliability-nw-rhel)

## Deployed Cluster Infrastructure
<a name="cluster-nw-rhel"></a>

Ensure that your AWS networking requirements and Amazon EC2 instances where SAP workloads are installed, are correctly configured for SAP. For more information, see [SAP NetWeaver Environment Setup for Linux on AWS](https://docs.aws.amazon.com/sap/latest/sap-netweaver/std-sap-netweaver-environment-setup.html).

See the following ASCS cluster specific requirements.
+ Two cluster nodes created in private subnets in separate Availability Zones within the same Amazon VPC and AWS Region
+ Access to the route table(s) that are associated with the chosen subnets

  For more information, see [AWS – Overlay IP](sap-nw-pacemaker-rhel-concepts.md#overlay-ip-nw-rhel).
+ Amazon EC2 instances must have connectivity to the Amazon EC2 endpoint via either internet or an Amazon VPC endpoint.

## Supported Operating System
<a name="supported-os-nw-rhel"></a>

Protecting the ABAP SAP Central Services (ASCS) with a pacemaker cluster requires packages from Red Hat, including targeted cluster resource agents for SAP and AWS that may not be available in standard repositories.

For deploying SAP applications on Red Hat, SAP and Red Hat recommend using Red Hat Enterprise Linux for SAP Solutions (RHEL for SAP). RHEL for SAP provides additional benefits, including Extended Update Support (EUS), configuration and tuning packages for SAP applications, and High Availability Add-On. For more details, see Red Hat website at [Red Hat Enterprise Linux for SAP Solutions](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux/sap).

RHEL for SAP is available at [AWS Marketplace](https://aws.amazon.com/marketplace) with an hourly or annual subscription. You can also use the bring your own subscription (BYOS) model.

## SAP and Red Hat references
<a name="references-nw-rhel"></a>

In addition to this guide, see the following references for more details.

 **RHEL 9 Documentation (Recommended):** 
+  [Red Hat documentation – Deploying SAP NetWeaver or S/4HANA Application Server High Availability with Simple Mount (RHEL 9)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/deploying_sap_netweaver_or_s4hana_application_server_high_availability_with_simple_mount/index) 
+  [Red Hat documentation – Configuring HA clusters to manage SAP NetWeaver or SAP S/4HANA Application server instances using the RHEL HA Add-On (RHEL 9)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/configuring_ha_clusters_to_manage_sap_netweaver_or_sap_s4hana_application_server_instances_using_the_rhel_ha_add-on) 
+  [SAP Note: 3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316) 

 **RHEL 8 Documentation:** 
+  [Red Hat documentation – Configuring HA clusters to manage SAP NetWeaver or SAP S/4HANA Application server instances using the RHEL HA Add-On (RHEL 8)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/8/html/configuring_ha_clusters_to_manage_sap_netweaver_or_sap_s4hana_application_server_instances_using_the_rhel_ha_add-on) 
+  [SAP Note: 2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999) 
+  [SAP Note: 2777782 - SAP HANA DB: Recommended OS settings for RHEL 8](https://me.sap.com/notes/2777782) 

 **RHEL 7 Documentation (Extended Life Phase - Not recommended for new installations):** 
+  [Red Hat documentation – RHEL Guidelines for Configuring SAP S/4HANA ASCS/ERS with Standalone Enqueue Server 2 (ENSA2) in Pacemaker (RHEL 7)](https://access.redhat.com/articles/3974941) 
+  [SAP Note: 2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://me.sap.com/notes/2002167) 

 **General SAP Notes:** 
+  [SAP Note: 1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://me.sap.com/notes/1656099) 

You must have SAP portal access for reading all SAP Notes.

## Required Access for Setup
<a name="access-nw-rhel"></a>

The following access is required for setting up the cluster.
+ An IAM user with the following privileges.
  + modify Amazon VPC route tables
  + modify Amazon EC2 instance properties
  + create IAM policies and roles
  + create Amazon EFS file systems
+ Root access to the operating system of both cluster nodes
+ SAP administrative user access – `<sid>adm` 

  In case of a new install, this user is created by the install process.

## Reliability Requirements Defined
<a name="reliability-nw-rhel"></a>

The SAP Lens of the Well-Architected framework, in particular the Reliability pillar, can be used to understand the reliability requirements for your SAP workload.

The ASCS is a single point of failure in a highly available SAP architecture. The impact of an outage of this component must be evaluated against factors, such as, recovery point objective (RPO), recovery time objective (RTO), cost and operation complexity. For more information, see [Reliability](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/reliability.html) in SAP Lens - AWS Well-Architected Framework.