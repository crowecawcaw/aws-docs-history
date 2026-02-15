# Setup Overview

## Deployed Cluster Infrastructure

Ensure that your AWS networking requirements and Amazon EC2 instances where SAP workloads are installed, are correctly configured for SAP.

The following SAP HANA cluster specific requirements must be met:

- Two cluster nodes created in private subnets in separate Availability Zones within the same Amazon VPC and AWS Region.
- Access to the route table(s) that are associated with the chosen subnets. For more information, see [Overlay IP](sap-hana-pacemaker-rhel-concepts.md#overlay-ip-rhel "sap-hana-pacemaker-rhel-concepts.md#overlay-ip-rhel").
- Targeted Amazon EC2 instances must have connectivity to the Amazon EC2 endpoint via internet or an Amazon VPC endpoint.

## Supported Operating System

Protecting the SAP HANA Database with a pacemaker cluster requires packages from Red Hat, including cluster resource agents for SAP and AWS that are not available in standard repositories.

For deploying SAP HANA on Red Hat, either "RHEL for SAP Solutions" (BYOS) or "RHEL for SAP with High Availability and Update Services" (PAYG) are required.

## Required Access for Setup

The following access is required for setting up the cluster:

An IAM user with the following privileges:

- Modify Amazon VPC route tables
- Modify Amazon EC2 instance properties
- Create IAM policies and roles
- Create Amazon EFS file systems

Additional required access:

- Root access to the operating system of both cluster nodes
- SAP HANA administrative user access – <sid>adm
- SAP HANA SystemDB Administrative access for changing configuration and backup administration.

###### Example

These access requirements are specific to the cluster setup process and can be restricted for ongoing cluster operations and maintenance.

## Reliability Requirements Defined

The SAP Lens of the Well-Architected framework, in particular the Reliability pillar, can be used to understand the reliability requirements for your SAP workload.

The SAP HANA application is a single point of failure in a highly available SAP architecture. The impact of an outage of this component must be evaluated against factors, such as, recovery point objective (RPO), recovery time objective (RTO), cost and operation complexity. For more information, see [Reliability in SAP Lens - AWS Well-Architected Framework](../../../wellarchitected/latest/sap-lens/reliability.md "../../../wellarchitected/latest/sap-lens/reliability.md").
