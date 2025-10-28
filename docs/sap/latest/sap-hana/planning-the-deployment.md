# Plan the deployment

Consider the following when planning your SAP HANA deployment.

###### Topics

- [Compute](#compute "#compute")
- [Operating System](#operating-system "#operating-system")
- [Amazon Machine Image (AMI)](#amazon-machine-image-ami "#amazon-machine-image-ami")
- [Storage](#storage "#storage")
- [Network](#network "#network")

## Compute

AWS provides multiple instance families with different sizes to run SAP HANA workloads. See the SAP [Certified and Supported SAP HANA Hardware Directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=v:deCertified;ve:23 "https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=v:deCertified;ve:23") and the [Amazon EC2 Instance Types for SAP](https://aws.amazon.com/sap/instance-types/ "https://aws.amazon.com/sap/instance-types/") page to find the list of certified Amazon EC2 instances. For your production workloads, ensure that you choose an instance type that has been certified by SAP. You can run your non-production workloads on any size of a particular certified instance family to save costs.

## Operating System

You can deploy your SAP HANA workload on SLES, SLES for SAP, RHEL for SAP with high availability and Update Services or RHEL for SAP Solutions.

SLES for SAP and RHEL for SAP with high availability and US products are available in AWS Marketplace under an hourly or an annual subscription model.

###### SLES for SAP

SLES for SAP provides additional benefits, including Extended Service Pack Overlap Support (ESPOS), configuration and tuning packages for SAP applications, and High Availability Extensions (HAE). For details, see the SUSE [SLES for SAP product page](https://www.suse.com/products/sles-for-sap/ "https://www.suse.com/products/sles-for-sap/") to learn more about the benefits of using SLES for SAP. We strongly recommend using SLES for SAP instead of SLES for all your SAP workloads.

If you plan to use Bring Your Own Subscription (BYOS) images provided by SUSE, ensure that you have the registration code required to register your instance with SUSE to access repositories for software updates.

###### RHEL for SAP

RHEL for SAP with high availability and Update services provides access to Red Hat Pacemaker cluster software for High Availability, extended update support, and the libraries that are required to run SAP HANA. For details, see the [RHEL for SAP Offerings on AWS FAQ](https://access.redhat.com/articles/3671571 "https://access.redhat.com/articles/3671571") in the Red Hat Knowledgebase.

If you plan to use the BYOS model with RHEL, either through the [Red Hat Cloud Access](https://access.redhat.com/articles/3490141 "https://access.redhat.com/articles/3490141") program or another means, ensure that you have access to a RHEL for SAP Solutions subscription. For details, see [Overview of Red Hat Enterprise Linux for SAP Solutions subscription](https://access.redhat.com/solutions/3082481 "https://access.redhat.com/solutions/3082481") in the Red Hat Knowledgebase.

## Amazon Machine Image (AMI)

A base AMI is required to launch an Amazon EC2 instance. Depending on your choice of operating system, ensure that you have access to the appropriate AMI in your target region for the deployment.

If you plan to use the SLES for SAP or RHEL for SAP Amazon Machine Images (AMIs) offered in AWS Marketplace, ensure that you have completed the subscription process. You can search for _SLES for SAP_ or _RHEL for SAP_ in the AWS Marketplace, and follow the instructions to complete your subscription.

If you are using AWS CLI, you will need to provide the AMI ID when you launch the instance.

## Storage

Deploying SAP HANA on AWS requires specific storage size and performance to ensure that SAP HANA data and log volumes both meet the SAP KPIs and sizing recommendations. Refer the [SAP HANA on AWS Operations Guide](hana-ops-storage-config.md "hana-ops-storage-config.md") to understand the storage configuration details for different instance types. You need to configure your storage based on these recommendations during instance launch. If you plan to use FSx for ONTAP storage, see [SAP HANA on AWS with FSx for ONTAP](sap-hana-amazon-fsx.md "sap-hana-amazon-fsx.md") for more details.

## Network

Ensure that your network constructs are set up to deploy resources related to SAP HANA. If you haven’t already set up network components such as Amazon VPC, subnets, route table, etc., you can use the AWS Modular and Scalable VPC reference deployment to easily deploy a scalable VPC architecture in minutes. For details, see the [reference deployment guide](../../../quickstart/latest/vpc/welcome.md "../../../quickstart/latest/vpc/welcome.md").
