# Offboard from AMS single-account landing zone accounts

AMS offers off-boarding assistance within 30 days prior to termination of AMS.

You must request off-boarding assistance at least 7 days before such assistance can be provided.
Off-boarding assistance can be offered in two forms:

- Control hand-over: AMS transfers account control back to you along with access credentials for all AMS-managed applications, or
- Resource termination for account closure: AMS deletes all of the data in your AMS-managed
  environment and de-provisions any active resources in the account. When
  submitting the offboarding request, customers can request that AMS:
  - Delete or retain the data objects (including logs) that are stored on Amazon S3 buckets
  - Remove or retain Amazon S3 buckets
  - Remove or retain AWS Backup restore points

###### Important

Any other specific requests (subject to plausibility) must be communicated
to AMS before initialization of offboarding.

**Optional Prerequisites (if required):**

###### Note

Prior to the offboarding request, customers can request AMS assistance
to transfer your data in the existing format using AWS Snowball Edge or any other
media that AWS interfaces with.

In addition to data backups, the following customer data can be provided as
part of off-boarding assistance:

    + Data stored in storage services including logs
    + Customer-specific change type schemas
    + CloudFormation templates for change type schemas

If off-boarding activities are not completed upon the termination of AMS, we hand over the controls of the account(s) to enable you to complete any pending activity.

| Function                               | What was removed                                                                                                                                                                                                    | Impact                                                                                                                                                                                                                                                                                           | Actions needed                                                                                                                                                                                                                                                                            |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monitoring, Logging, Alerting          | AMS Monitoring removed MMS (Managed Monitoring System) unsubscribed Resource Tagger and Alarm Manager removed Baseline CloudWatch alerts remain on existing resources GuardDuty and Macie: Ownership reverts to you | AMS no longer has access or visibility into your resources and environment.                                                                                                                                                                                                                      | Contingencies for removed and unsubscribed services are owned by you.                                                                                                                                                                                                                     |
| Backup management                      | AMS Backup automation is removed although the AWS Backup service remains available for use. Backup vaults and data are retained unless deletion is requested.                                                       | AMS no longer monitors the backup jobs or performs restoration actions during incidents. Alarms and alerts are disabled. Deletion of the IAM backup role and KMS keys render your AMS backups inoperable.                                                                                        | AMS Backup Plans must be reconfigured. All monitoring and remediation ownership returns to you.                                                                                                                                                                                           |
| AMS automations for service management | AMS-curated AWS SSM automation runbooks, Amazon Simple Notification Service (SNS), and AWS Lambda functions are no longer available.                                                                                | No AMS access to your accounts. All automation disabled.                                                                                                                                                                                                                                         | All automation including SSM, SNS, and Lambda functions need to be recreated, if required.                                                                                                                                                                                                |
| Compliance                             | AMS visibility into and monitoring for all GuardDuty and AWS Config rules removed, although these rules remain on the accounts.                                                                                     | All monitoring, reporting, and remediation from Amazon GuardDuty and AWS Config Rules is no longer managed by AMS.                                                                                                                                                                               | Monitoring and remediation for all security and compliance tools to be assumed by you.                                                                                                                                                                                                    |
| On-instance agents                     | Access to Resource Scheduler, Resource Tagger or automated instance configuration to install required agents in your EC2 instances is removed.                                                                      | CloudWatch and SSM Agents on instances are left in place with existing configurations however, AMS no longer assists with these configurations.                                                                                                                                                  | You manage tagging and on-instance CloudWatch and SSM agent configurations.                                                                                                                                                                                                               |
| Patch and reporting infrastructure     | AMS no longer manages pre- and post- patching activities, and access and visibility to these services are removed.                                                                                                  | AMS no longer creates a snapshot of the instance prior to patching, no longer installs and monitors the patch installation, and no longer notifies you of the outcome. Reports and "audit" S3 buckets are left in your accounts at your request. AMS no longer generates service metric reports. | You retain the Patch baselines and snapshots created in the past. Additionally, the configuration of the patch maintenance windows remains but the patches are no longer installed or remediated by AMS. All reporting on infrastructure operational metrics are now your responsibility. |
| Process management                     | All accounts are offboarded from the service management provided for incidents, including service requests, problem, and change, management.                                                                        | All service disruption formerly remediated by AMS through incidents and service requests, and changes to the environment, as well as Root Cause investigations, are longer managed by AMS.                                                                                                       | You regain full ownership of all process management.                                                                                                                                                                                                                                      |
