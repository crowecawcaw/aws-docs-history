

# Understanding the hybrid directory creation process
<a name="hybrid_directory_understanding_creation_steps"></a>

When you create a hybrid directory, Directory Service deploys two domain controllers in your VPC and joins them to your self-managed Active Directory domain. The service completes several phases to establish the connection between your self-managed AD and AWS. During this process, the directory status displays as *Creating*. The following sections describe each phase of the workflow.

## Workflow overview
<a name="hybrid_creation_workflow_overview"></a>


| Phase | Name | Summary | 
| --- | --- | --- | 
| 1 | Infrastructure provisioning | Launches EC2 domain controller instances, sets up networking, and attaches storage volumes. | 
| 2 | Pre-join connectivity assessment | Validates network connectivity, DNS resolution, and service account credentials before domain join. | 
| 3 | First domain controller join | Joins the domain as a member computer and promotes to a full domain controller, triggering AD database replication. | 
| 4 | AD site and subnet creation | Creates an AD site object and maps VPC subnets to enable correct DC Locator behavior. | 
| 5 | First domain controller configuration | Applies OU structure, delegation groups, GPOs, DNS zones, and service accounts for ongoing management. | 
| 6 | Service administrator creation | Creates an AWS-managed service administrator account used to configure the second domain controller. | 
| 7 | Second domain controller configuration | Configures a second DC for high availability, using the first DC as its DNS resolver and replication partner. | 
| 8 | Finalization | Attaches backup storage, enables health monitoring, and sets the directory status to Active. | 

## Infrastructure provisioning
<a name="hybrid_creation_infrastructure_provisioning"></a>

Directory Service begins by provisioning the infrastructure required to host your domain controllers. This phase includes the following:

DNS alias creation  
A DNS alias record is provisioned for your directory endpoint so that applications and services can locate your directory.

Domain controller instance launch  
Two Amazon EC2 instances are launched, each placed in a separate Availability Zone for high availability.

Security group configuration  
Inbound and outbound security group rules are applied to allow Active Directory traffic (such as LDAP, Kerberos, DNS, and replication) between the domain controllers and your self-managed network.

Storage volume attachment  
Persistent storage volumes are attached to both domain controller instances for the AD database (NTDS.dit) and SYSVOL.

Network interface configuration  
Each domain controller is connected to your VPC subnets so it can communicate with your self-managed domain over your established network path (VPN or ).

## Pre-join connectivity assessment
<a name="hybrid_creation_prejoin_assessment"></a>

Before joining your domain, Directory Service runs a connectivity assessment that validates the following:
+ Network connectivity to your self-managed domain controllers
+ DNS resolution of your domain name from the AWS VPC
+ Required network paths and ports between the AWS domain controllers and your self-managed environment

If the assessment fails, directory creation stops and the directory status changes to *Failed*. You can review the failure reason in the directory details to identify and correct the issue before retrying.

**Note**  
A successful connectivity assessment is required before the service proceeds with the domain join. For more information about assessments, see [Directory assessments for hybrid directories](hybrid_directory_assessment.md).

## First domain controller join
<a name="hybrid_creation_first_dc_join"></a>

The first domain controller joins your self-managed domain using the service account credentials you provided during directory creation. The join process follows this sequence:

1. The domain controller joins your Active Directory domain as a member computer.

1. The domain-joined computer is promoted to a full domain controller, which triggers Active Directory database replication from your existing self-managed domain controllers.

1. After promotion and replication complete, the first domain controller holds a full copy of your Active Directory database and can authenticate requests independently.

## AD site and subnet creation
<a name="hybrid_creation_ad_site"></a>

Directory Service creates a new Active Directory site object in your existing AD Sites and Services configuration and maps your VPC subnets to that site. This ensures that domain controller locator (DC Locator) behavior works correctly, directing authentication requests from AWS resources to the AWS-hosted domain controllers.

## First domain controller configuration
<a name="hybrid_creation_first_dc_config"></a>

After the AD site and subnets are in place, Directory Service configures the first domain controller with the management structure and policies required for ongoing operations. This includes the following:
+ Organizational unit (OU) structure for delegated administration
+ Delegation groups for role-based access
+ Group Policy Objects (GPOs) for security and configuration policies
+ DNS zones for name resolution
+ Service accounts needed for directory management

## Service administrator creation
<a name="hybrid_creation_service_admin"></a>

After the first domain controller is fully configured, Directory Service creates a service administrator account on that domain controller. This account is used internally by the service to join and configure the second domain controller without requiring further use of your service account credentials.

## Second domain controller configuration
<a name="hybrid_creation_second_dc_config"></a>

The second domain controller goes through the same configuration sequence as the first domain controller (domain join, promotion, and post-promotion configuration). However, the second domain controller differs in the following ways:

Service account  
It uses the AWS-managed service administrator account created in the previous phase to join the domain, rather than the service account credentials you provided.

Replication partner  
It points to the first domain controller as its DNS resolver and replication partner, rather than your self-managed domain controllers.

This approach reduces dependency on your self-managed network during setup and ensures the second domain controller replicates from the already-healthy first domain controller.

## Finalization
<a name="hybrid_creation_finalization"></a>

After both domain controllers are fully configured and healthy, Directory Service completes the following:

Backup storage attachment  
A backup volume is attached for automated directory snapshots.

Health monitoring activation  
Health monitoring is enabled on both domain controllers to provide ongoing availability monitoring and automatic recovery.

Directory activation  
The directory status changes from *Creating* to *Active*.

When the directory status shows *Active*, the directory is available for use with AWS applications such as WorkSpaces, Amazon RDS, and Amazon FSx for Windows File Server.

## Troubleshooting creation failures
<a name="hybrid_creation_troubleshooting"></a>

If your directory status changes to *Failed* during creation, review the status reason in the directory details. The following are common causes:

Network connectivity  
Verify that your VPN or connection allows traffic on the required Active Directory ports between your VPC subnets and self-managed domain controllers.

Service account permissions  
Confirm that the service account has the required permissions to join computers to the domain and create objects in the specified OU.

DNS resolution  
Ensure that DNS resolution of your self-managed domain name works correctly from within your VPC.

For more information, see [Hybrid directory prerequisites](create_hybrid_directory_prereqs.md).