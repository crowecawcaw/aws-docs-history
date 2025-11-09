# AWS Identity and Access Management in AMS Accelerate

AWS Identity and Access Management is a web service that helps you securely control access to AWS resources.
You use IAM to control who is authenticated (signed in) and authorized (has permissions) to
use resources. During AMS Accelerate onboarding, you are responsible for creating cross-account
IAM administrator roles within each of your managed accounts.

In AMS Accelerate, you're responsible for managing access to your AWS accounts and their underlying resources, such as access management solutions,
access policies, and related processes. This means that you manage your user lifecycle, permissions in directory services, and
federated authentication system, to access the AWS console or AWS APIs. To help you manage
your access solution, AMS Accelerate deploys AWS Config rules that detect common IAM misconfigurations, and
delivers remediation notifications. For more information, see
[AWS Config Managed Rules](../../../config/latest/developerguide/evaluate-config_use-managed-rules.md "../../../config/latest/developerguide/evaluate-config_use-managed-rules.md").

## Authenticating with identities in AMS Accelerate

AMS uses IAM roles, which are a type of IAM identity. An IAM role is similar to a user, in that it is an identity with permissions policies that determine what
the identity can and can't do in AWS. However, a role doesn't have credentials associated
with it and, instead of being uniquely associated with one person, is assumable by anyone who needs it. An IAM user can assume a role to temporarily take on
different permissions for a specific task.

Access roles are controlled by internal group membership, which is administered and
periodically reviewed by Operations Management. AMS uses the following IAM roles.

###### Note

AMS access roles allow AMS operators to access your resources to provide AMS capabilities (see
[Service description](acc-sd.md "acc-sd.md")). Altering these roles can inhibit
our ability to provide these capabilities. If you need to alter AMS access roles, consult your Cloud Architect.

| **Role name**                                                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Used by (entity): **AMS Access Service only**                     |
| ams-access-management                                             | Deployed manually by you during onboarding. Assumed only by AMS access to deploy or update access<br>roles. Remains in your account after onboarding for any future updates to the access roles.                                                                                                                                                                                                                                                                          |
| Used by (entity): **AMS Operations**                              |
| ams-access-admin-operations                                       | This role has administrative permissions to operate in accounts, but does not have permissions to read, write, or delete customer content in AWS services commonly used as data stores, such as Amazon Simple Storage Service, Amazon Relational Database Service, Amazon DynamoDB, Amazon Redshift, and Amazon ElastiCache. Only a very few select AMS individuals can assume this role.                                                                                 |
| ams-access-operations                                             | This AMS Operations role has permissions to perform administrative tasks in your accounts. This role does not have read, write, or delete permissions to customer content in AWS services commonly used as data stores, such as Amazon Simple Storage Service, Amazon Relational Database Service, Amazon DynamoDB, Amazon Redshift, and Amazon ElastiCache. Permissions to perform AWS Identity and Access Management write operations are also excluded from this role. |
| ams-access-read-only                                              | This AMS read-only role is limited to read-only permissions in your AMS<br>account. Read permissions to customer content in AWS services commonly used as data stores, such as Amazon S3, Amazon RDS, DynamoDB, Amazon Redshift, and ElastiCache, are not granted by this role.                                                                                                                                                                                           |
| Used by (entity): **AMS Operations and AMS Services**             |
| ams_ssm_automation_role                                           | Assumed by AWS Systems Manager to execute SSM Automation documents within<br>your account.                                                                                                                                                                                                                                                                                                                                                                                |
| ams_ssm_automation_role                                           |
| Used by (entity): **AMS Security**                                |
| ams-access-security-analyst                                       | This AMS security role has permissions in your AMS<br>account to perform dedicated security alert monitoring and security incident handling. Only a very few select AMS Security individuals<br>can assume this role. Read permissions to customer content in AWS services that are commonly used as data stores, such as Amazon S3;, Amazon RDS;, Amazon DynamoDB, Amazon Redshift, and ElastiCache, aren't granted by this role.                                        |
| ams-access-security-analyst-read-only                             | This AMS security role is limited to read-only permissions in your AMS<br>account to perform dedicated security alert monitoring and security incident handling. Read permissions to customer content in AWS services that are commonly used as data stores, such as Amazon S3;, Amazon RDS;, Amazon DynamoDB, Amazon Redshift, and ElastiCache, aren't granted by this role.                                                                                             |
| Used by (entity): **AWS Services**                                |
| ams-access-admin                                                  | This AMS admin role has full permissions to operate in accounts without restrictions. Only<br>AMS internal services (with a scoped-down session policy)<br>can assume the admin role.                                                                                                                                                                                                                                                                                     |
| ams-opscenter-eventbridge-role                                    | Assumed by Amazon EventBridge to create AWS Systems Manager OpsItems as a part of AMS-specific<br>AWS Config Rules remediation workflow.                                                                                                                                                                                                                                                                                                                                  |
| AMSOSConfigurationCustomerInstanceRole                            | This IAM role is applied to your Amazon EC2 instances when AMS OS-Configuration service<br>discovers that the required IAM policies are missing. It allows your Amazon EC2<br>instances to interact with AWS Systems Manager, Amazon CloudWatch, and Amazon EventBridge services. It also has<br>attached the AMS custom-managed policy to enable RDP access to your Windows<br>instances.                                                                                |
| mc-patch-glue-service-role                                        | Assumed by AWS Glue ETL workflow to perform data transformation and prepare it for AMS Patch<br>report generator.                                                                                                                                                                                                                                                                                                                                                         |
| Used by (entity): **AMS Service**                                 |
| ams-alarm-manager-AWSManagedServicesAlarmManagerDe-<8-digit hash> | Assumed by AMS alarm manager infrastructure within your AMS account to perform AWS Config Rules<br>evaluation for a new AWS AppConfig deployment.                                                                                                                                                                                                                                                                                                                         |
| ams-alarm-manager-AWSManagedServicesAlarmManagerRe-<8-digit hash> | Assumed by AMS alarm manager remediation infrastructure within your AMS account to<br>allow the creation or deletion of alarms for remediation.                                                                                                                                                                                                                                                                                                                           |
| ams-alarm-manager-AWSManagedServicesAlarmManagerSS-<8-digit hash> | Assumed by AWS Systems Manager to invoke the AMS alarm manager remediation service within<br>your AMS account.                                                                                                                                                                                                                                                                                                                                                            |
| ams-alarm-manager-AWSManagedServicesAlarmManagerTr-<8-digit hash> | Assumed by AMS alarm manager infrastructure within your AWS account to conduct periodic<br>AMS AWS Config Rules evaluation.                                                                                                                                                                                                                                                                                                                                               |
| ams-alarm-manager-AWSManagedServicesAlarmManagerVa-<8-digit hash> | Assumed by AMS alarm manager infrastructure within your AMS account to ensure<br>that the required alarms exists in the AWS account.                                                                                                                                                                                                                                                                                                                                      |
| ams-backup-iam-role                                               | This role is used to run AWS Backup within your accounts.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ams-monitoring-AWSManagedServicesLogGroupLimitLamb-<8-digit hash> | Assumed by AMS Logging & Monitoring infrastructure in your AMS account to evaluate<br>Amazon CloudWatch Logs groups limit and compare with the service quotas.                                                                                                                                                                                                                                                                                                            |
| ams-monitoring-AWSManagedServicesRDSMonitoringRDSE-<8-digit hash> | Assumed by AMS Logging & Monitoring infrastructure in your AMS account to forward<br>Amazon RDS events to Amazon CloudWatch Events.                                                                                                                                                                                                                                                                                                                                       |
| ams-monitoring-AWSManagedServicesRedshiftMonitorin-<8-digit hash> | Assumed by AMS Logging & Monitoring infrastructure in your AMS account to forward<br>Amazon Redshift events (CreateCluster and DeleteCuster) to Amazon CloudWatch Events.                                                                                                                                                                                                                                                                                                 |
| ams-monitoring-infrastruc-AWSManagedServicesMonito-<8-digit hash> | Assumed by AMS Logging & Monitoring infrastructure in your AMS account to publish<br>messages to Amazon Simple Notification Service to validate that the account is reporting all necessary data.                                                                                                                                                                                                                                                                         |
| ams-opscenter-role                                                | Assumed by AMS Notification Management system in your AMS account to manage<br>AWS Systems Manager OpsItems related to alerts in your account.                                                                                                                                                                                                                                                                                                                            |
| ams-opsitem-autoexecution-role                                    | Assumed by AMS Notification Management system to handle automated remediation using SSM<br>documents for monitoring alerts related to resources in your account.                                                                                                                                                                                                                                                                                                          |
| ams-patch-infrastructure-amspatchconfigruleroleC1-<8-digit hash>  | Assumed by AWS Config to evaluate AMS patch resources and detect drift in its AWS CloudFormation<br>stacks.                                                                                                                                                                                                                                                                                                                                                               |
| ams-patch-infrastructure-amspatchcwruleopsitemams-<8-digit hash>  | Assumed by Amazon EventBridge to create AWS Systems Manager OpsItems for patching failures.                                                                                                                                                                                                                                                                                                                                                                               |
| ams-patch-infrastructure-amspatchservicebusamspat-<8-digit hash>  | Assumed by Amazon EventBridge to send an event to the AMS Patch orchestrator event bus for<br>AWS Systems Manager Maintenance Windows state change notifications.                                                                                                                                                                                                                                                                                                         |
| ams-patch-reporting-infra-amspatchreportingconfigr-<8-digit hash> | Assumed by AWS Config to evaluate AMS Patch reporting resources and detect drift in its<br>AWS CloudFormation stacks.                                                                                                                                                                                                                                                                                                                                                     |
| ams-resource-tagger-AWSManagedServicesResourceTagg-<8-digit hash> | Assumed by AMS Resource Tagger infrastructure within your AMS account to perform<br>AWS Config Rules evaluation upon new AWS AppConfig deployment.                                                                                                                                                                                                                                                                                                                        |
| ams-resource-tagger-AWSManagedServicesResourceTagg-<8-digit hash> | Assumed by AMS Resource Tagger infrastructure within your AMS account to validate that<br>required AWS tags exist for the managed resources.                                                                                                                                                                                                                                                                                                                              |
| ams-resource-tagger-AWSManagedServicesResourceTagg-<8-digit hash> | Assumed by AWS Systems Manager to invoke AMS Resource Tagger remediation workflow in your AMS<br>account.                                                                                                                                                                                                                                                                                                                                                                 |
| ams-resource-tagger-AWSManagedServicesResourceTagg-<8-digit hash> | Assumed by AMS Resource Tagger remediation infrastructure within your AMS account to<br>create or delete AWS tags for the managed resources.                                                                                                                                                                                                                                                                                                                              |
| ams-resource-tagger-AWSManagedServicesResourceTagg-<8-digit hash> | Assumed by AMS Resource Tagger infrastructure within your AWS account to conduct periodic<br>AMS Config Rule evaluation.                                                                                                                                                                                                                                                                                                                                                  |
| ams_os_configuration_event_rule_role-<AWS Region>                 | Assumed by Amazon EventBridge to forward events from your account to AMS OS-Configuration service<br>EventBus in the correct Region.                                                                                                                                                                                                                                                                                                                                      |
| mc-patch-reporting-service                                        | Assumed by AMS patch data aggregator and report generator.                                                                                                                                                                                                                                                                                                                                                                                                                |

###### Note

This is the template for the ams-access-management role. It's the stack that cloud architects (CAs) manually deploy in your account at onboarding:
[management-role.yaml](https://ams-account-access-templates.s3.amazonaws.com/management-role.yaml "https://ams-account-access-templates.s3.amazonaws.com/management-role.yaml").

This is the template for the different access roles and access levels: ams-access-read-only, ams-access-operations, ams-access-admin-operations, ams-access-admin:
[accelerate-roles.yaml](https://ams-account-access-templates.s3.amazonaws.com/accelerate-roles.yaml "https://ams-account-access-templates.s3.amazonaws.com/accelerate-roles.yaml").

To learn more about AWS Cloud Development Kit (AWS CDK) (AWS CDK) identifiers, including hashes, see
[UniqueIDs](../../../cdk/latest/guide/identifiers.md#identifiers_unique_ids "../../../cdk/latest/guide/identifiers.md#identifiers_unique_ids").

AMS Accelerate feature services assume the **ams-access-admin**
role for programmatic access to the account, but with a session policy scoped down for the
respective feature service (for example, patch, backup, monitoring, and so forth).

AMS Accelerate follows industry best practices to meet and maintain compliance eligibility.
AMS Accelerate access to your account is recorded in CloudTrail and also available for your review
through change tracking. For information about queries that you can use to get this information,
see [Tracking changes in your AMS Accelerate accounts](acc-change-record.md "acc-change-record.md").

## Managing access using policies

Various AMS Accelerate support teams such as Operations Engineers, Cloud
Architects, and Cloud Service Delivery Managers (CSDMs), sometimes require access to your accounts in order
to respond to service requests and incidents. Their access is governed by an internal AMS access
service that enforces controls, such as business justification, service requests, operations items, and
support cases. The default access is read-only, and all access is tracked and recorded; see also
[Tracking changes in your AMS Accelerate accounts](acc-change-record.md "acc-change-record.md").

### Validation of IAM resources

The AMS Accelerate access system periodically assumes roles in your accounts (at
least every 24 hours) and validates that all of our IAM resources are as expected.

In order to protect your accounts, AMS Accelerate has a
"canary" that monitors and alarms on the presence and status of the IAM roles, as well
as their attached policies, mentioned above. Periodically, the canary assumes the
**ams-access-read-only** role and initiates CloudFormation and IAM
API calls against your accounts. The canary evaluates the status of the AMS Accelerate
access roles to make sure they are always unmodified and up-to-date. This activity creates CloudTrail logs in the account.

The AWS Security Token Service (AWS STS) session name of the canary is
**AMS-Access-Roles-Auditor-{uuid4()}** as seen in CloudTrail and the following API calls occur:

- Cloud Formation API Calls: `describe_stacks()`
- IAM API Calls:
  - `get_role()`
  - `list_attached_role_policies()`
  - `list_role_policies()`
  - `get_policy()`
  - `get_policy_version()`
  - `get_role_policy()`
