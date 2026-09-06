

# Setup Overview
<a name="sap-hana-pacemaker-sles-setup-overview"></a>

## Deployed Cluster Infrastructure
<a name="_deployed_cluster_infrastructure"></a>

Ensure that your AWS networking requirements and Amazon EC2 instances where SAP workloads are installed, are correctly configured for SAP.

The following SAP HANA cluster specific requirements must be met:
+ Two cluster nodes created in private subnets in separate Availability Zones within the same Amazon VPC and AWS Region.
+ Access to the route table(s) that are associated with the chosen subnets. For more information, see [Overlay IP](sap-hana-pacemaker-sles-concepts.md#overlay-ip-sles).
+ Targeted Amazon EC2 instances must have connectivity to the Amazon EC2 endpoint via internet or an Amazon VPC endpoint.

## Supported Operating System
<a name="_supported_operating_system"></a>

Protecting the SAP HANA Database with a pacemaker cluster requires packages from SUSE, including cluster resource agents for SAP and AWS that are not available in standard repositories.

For deploying SAP HANA on SUSE, SAP and SUSE recommend using SUSE Linux Enterprise Server for SAP applications (SLES for SAP). SLES for SAP provides additional benefits, including:
+ Extended Service Pack Overlap Support (ESPOS)
+ Configuration and tuning packages for SAP applications
+ High Availability Extensions (HAE)

To learn more, see [SUSE Linux Enterprise Server for SAP Applications](https://www.suse.com/products/sles-for-sap/).

SLES for SAP is available at AWS Marketplace with:
+ Hourly subscription
+ Annual subscription
+ Bring Your Own Subscription (BYOS) mode

## Required Access for Setup
<a name="_required_access_for_setup"></a>

The following access is required for setting up the cluster:

An IAM user with the following privileges:
+ Modify Amazon VPC route tables
+ Modify Amazon EC2 instance properties
+ Create IAM policies and roles
+ Create Amazon EFS file systems

Additional required access:
+ Root access to the operating system of both cluster nodes
+ SAP HANA administrative user access – <sid>adm
+ SAP HANA SystemDB Administrative access for changing configuration and backup administration.

**Example**  
These access requirements are specific to the cluster setup process and can be restricted for ongoing cluster operations and maintenance.

## Reliability Requirements Defined
<a name="_reliability_requirements_defined"></a>

The SAP Lens of the Well-Architected framework, in particular the Reliability pillar, can be used to understand the reliability requirements for your SAP workload.

The SAP HANA application is a single point of failure in a highly available SAP architecture. The impact of an outage of this component must be evaluated against factors, such as, recovery point objective (RPO), recovery time objective (RTO), cost and operation complexity. For more information, see [Reliability in SAP Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/reliability.html).