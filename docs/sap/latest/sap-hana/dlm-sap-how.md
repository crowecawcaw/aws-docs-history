# How to automate the creation of EBS snapshots for SAP HANA

In a running database, to be application-consistent, EBS snapshots must be aligned with an internal database snapshot. For more information, see [Create a Data Snapshot](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/9fd1c8bb3b60455caa93b7491ae6d830.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/9fd1c8bb3b60455caa93b7491ae6d830.html") in the SAP documentation.

To create application-consistent snapshots, Amazon Data Lifecycle Manager performs the following steps with pre and post scripts:

1. In the pre script, operating system checks are performed, the I/O is paused, and the SAP HANA SQL command is run to create a consistent internal database snapshot.
2. Amazon Data Lifecycle Manager initiates EBS snapshot creation for the volumes attached to the targeted instance.
3. In the post script, the SAP HANA SQL command is run to mark the internal snapshot as either completed or failed.
   Amazon Data Lifecycle Manager also provides monitoring capabilities and manages the retention of the EBS snapshots after creation.

To automate the creation of application-consistent EBS snapshots for SAP HANA using Amazon Data Lifecycle Manager, you need the following:

- An Amazon Data Lifecycle Manager policy that is enabled for pre and post scripts for SAP HANA and that uses an AWS IAM role with the permissions required to manage application-consistent snapshots. We recommend that you also configure the policy to automatically enable the EBS snapshots for fast snapshot restore. For more information, see [Considerations](dlm-sap-considerations.md "dlm-sap-considerations.md").
- AWS Systems Manager Agent (SSM Agent) installed and running on the target instances with the SAP HANA workloads that you want to back up.
- Access to the Systems Manager document for SAP HANA, `AWSSystemsManagerSAP-CreateDLMSnapshotForSAPHANA`, which is available in all [AWS Regions where AWS Systems Manager for SAP is available](../../../general/latest/gr/ssm-sap.md "../../../general/latest/gr/ssm-sap.md").
- (Recommended) A [resource tagging](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") strategy that includes tagging your Amazon EBS volumes in a way that enables you to map them to your specific SAP HANA workloads.
  For more information about setting up your target instances, the Amazon Data Lifecycle Manager policy , and your SAP HANA environment for automated application-consistent snapshots, see [Automating application-consistent snapshots with pre and post scripts](../../../AWSEC2/latest/UserGuide/automate-app-consistent-backups.md "../../../AWSEC2/latest/UserGuide/automate-app-consistent-backups.md").
