

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Offboard from AMS single-account landing zone accounts
<a name="offboarding-salz"></a>

AMS offers offboarding assistance within 30 days prior to termination of AMS.

Request offboarding assistance at least 7 days before you need it. Offboarding assistance is available in the following forms:
+ Control hand-over: AMS transfers account control back to you. Only AMS-managed infrastructure is removed; customer resources remain intact
+ Resource termination for account closure: All resources in the account are deleted—both AMS-managed and customer-created. You're expected to close the AWS account after offboarding. When submitting the offboarding request, customers can request that AMS: 
  + Delete or retain the data objects (including logs) that are stored on Amazon S3 buckets 
  + Remove or retain Amazon Simple Storage Service (Amazon S3) buckets
  + Remove or retain AWS Backup restore points
**Important**  
Any other specific requests (subject to plausibility) must be communicated to AMS before initialization of offboarding.

  **Optional Prerequisites (if required):**
**Note**  
Prior to your offboarding request, you can request AMS assistance to transfer your data in the existing format using AWS Snowball Edge or any other media that AWS interfaces with.

  In addition to data backups, AMS can provide the following customer data as part of offboarding assistance:
  + Data stored in storage services including logs
  + Customer-specific change type schemas
  + CloudFormation templates for change type schemas

The following table lists which resources are deleted or retained under each offboarding option.


| Resource / Function | Resource Termination for Account Closure | Control Hand-Over | 
| --- | --- | --- | 
| **Prerequisites: Account Contact Info** | Validate email and phone with CSDM (used for MFA reset); update Operations and Security contacts | Validate email and phone with CSDM (used for MFA reset); update Operations and Security contacts | 
| **Prerequisites: Retention Requests** | Inform CSDM of any Amazon S3 buckets or AWS Backup recovery points to retain | Confirm with CSDM if AWS CloudTrail log buckets in each region should be retained | 
| **Prerequisites: AD and Federation Planning** | Not applicable—everything is deleted | Confirm with CA/CSDM: new AD users needed? Retain MAD or join another domain? Retain AMS management hosts? Need other AD resources for new auth path? | 
| **AWS CloudFormation Stacks** | All deleted (AMS and customer) | AMS stacks (ams-\*, mc-\*) deleted; customer stacks retained | 
| **Amazon S3 Buckets** | All deleted (can request retention) | Only patching buckets deleted | 
| **IAM Roles** | All deleted | AMS roles deleted, others retained | 
| **Active Directory** | Deleted | AMS accounts removed; MAD retained with new admin credentials through Secrets Manager | 
| **Backup Vaults** | Deleted (can request retention) | Retained | 
| **Monitoring and Alerting** | SNS, CloudWatch Logs, SSM docs deleted | SNS, SSM docs removed; CloudWatch Logs retained | 
| **Networking (VPCs/Subnets)** | Deleted | Retained—handed over to you | 
| **Customer Resources (EC2, Amazon RDS, etc.)** | Deleted | No changes—you keep managing | 
| **AD Trust and Federation** | Deleted | Handed over to you | 
| **AWS CloudTrail** | Deleted | Stays enabled | 
| **Existing AMIs** | Deleted | Retained (future AMS AMIs aren't shared) | 
| **Trend Micro / EPS** | Deleted | No changes (can request uninstall) | 

If offboarding activities aren't completed upon the termination of AMS, we hand over the controls of the account(s) to enable you to complete any pending activity.

The following table lists the AMS components removed during offboarding, the impact of removal, and actions for you to take.


| Function | What was removed | Impact | Actions needed | 
| --- | --- | --- | --- | 
| Monitoring, Logging, Alerting  | AMS Monitoring removed<br />MMS (Managed Monitoring System) unsubscribed<br />Baseline CloudWatch alerts remain on existing resources<br />GuardDuty and Macie: Ownership reverts to you | AMS doesn't have access or visibility into your resources and environment. | Contingencies for removed and unsubscribed services are owned by you. | 
| Backup management | AMS Backup automation is removed although the AWS Backup service remains available for use. Backup vaults and data are retained unless deletion is requested. | AMS doesn't monitor the backup jobs or perform restoration actions during incidents. Alarms and alerts are disabled. Deletion of the IAM backup role and KMS keys render your AMS backups inoperable. | AMS Backup Plans must be reconfigured. All monitoring and remediation ownership returns to you. | 
| AMS automations for service management | AMS-curated AWS SSM automation runbooks, Amazon Simple Notification Service (SNS), and AWS Lambda functions are no longer available.  | No AMS access to your accounts. All automation disabled. | All automation including SSM, SNS, and Lambda functions need to be recreated, if required. | 
| Compliance | AMS visibility into and monitoring for all GuardDuty and AWS Config rules removed, although these rules remain on the accounts. | All monitoring, reporting, and remediation from Amazon GuardDuty and AWS Config Rules isn't managed by AMS. | Monitoring and remediation for all security and compliance tools to be assumed by you. | 
| On-instance agents | Access to Resource Scheduler, Resource Tagger or automated instance configuration to install required agents in your EC2 instances is removed. | CloudWatch and SSM Agents on instances are left in place with existing configurations; however, AMS doesn't assist with these configurations. | You manage tagging and on-instance CloudWatch and SSM agent configurations. | 
| Patch and reporting infrastructure | AMS no longer manages pre- and post- patching activities, and access and visibility to these services are removed. | AMS doesn't create a snapshot of the instance prior to patching, doesn't install and monitor the patch installation, and doesn't notify you of the outcome. Reports and "audit" S3 buckets are left in your accounts at your request. AMS doesn't generate service metric reports. | You retain the patch baselines and snapshots created in the past. Additionally, the configuration of the patch maintenance windows remains but the patches aren't installed or remediated by AMS. All reporting on infrastructure operational metrics is now your responsibility. | 
| Process management | All accounts are offboarded from the service management provided for incidents, including service requests, problem, and change, management. | All service disruption formerly remediated by AMS through incidents and service requests, and changes to the environment, as well as root cause investigations, are no longer managed by AMS. | You regain full ownership of all process management. | 