

# AWS Identity and Access Management in AMS Accelerate
<a name="acc-sec-iam"></a>

AWS Identity and Access Management is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources. During AMS Accelerate onboarding, you are responsible for creating cross-account IAM administrator roles within each of your managed accounts.

In AMS Accelerate, you're responsible for managing access to your AWS accounts and their underlying resources, such as access management solutions, access policies, and related processes. This means that you manage your user lifecycle, permissions in directory services, and federated authentication system, to access the AWS console or AWS APIs. To help you manage your access solution, AMS Accelerate deploys AWS Config rules that detect common IAM misconfigurations, and delivers remediation notifications. For more information, see [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).

## Authenticating with identities in AMS Accelerate
<a name="acc-sec-iam-auth"></a>

AMS uses IAM roles, which are a type of IAM identity. An IAM role is similar to a user, in that it is an identity with permissions policies that determine what the identity can and can't do in AWS. However, a role doesn't have credentials associated with it and, instead of being uniquely associated with one person, is assumable by anyone who needs it. An IAM user can assume a role to temporarily take on different permissions for a specific task.

Access roles are controlled by internal group membership, which is administered and periodically reviewed by Operations Management. AMS uses the following IAM roles.

**Note**  
AMS access roles allow AMS operators to access your resources to provide AMS capabilities (see [Service description](acc-sd.md)). Altering these roles can inhibit our ability to provide these capabilities. If you need to alter AMS access roles, consult your Cloud Architect.


<table>
<thead>
  <tr><th><b>Role name</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="2">Used by (entity): <b>AMS Access Service only</b></td></tr>
  <tr><td>ams-access-management</td><td>Deployed manually by you during onboarding. Assumed only by AMS access to deploy or update access roles. Remains in your account after onboarding for any future updates to the access roles.</td></tr>
  <tr><td colspan="2">Used by (entity): <b>AMS Operations</b></td></tr>
  <tr><td>ams-access-admin-operations</td><td>This role has administrative permissions to operate in accounts, but does not have permissions to read, write, or delete customer content in AWS services commonly used as data stores, such as Amazon Simple Storage Service, Amazon Relational Database Service, Amazon DynamoDB, Amazon Redshift, and Amazon ElastiCache. Only a very few select AMS individuals can assume this role.</td></tr>
  <tr><td>ams-access-operations</td><td>This AMS Operations role has permissions to perform administrative tasks in your accounts. This role does not have read, write, or delete permissions to customer content in AWS services commonly used as data stores, such as Amazon Simple Storage Service, Amazon Relational Database Service, Amazon DynamoDB, Amazon Redshift, and Amazon ElastiCache. Permissions to perform AWS Identity and Access Management write operations are also excluded from this role.</td></tr>
  <tr><td>ams-access-read-only</td><td>This AMS read-only role is limited to read-only permissions in your AMS account. Read permissions to customer content in AWS services commonly used as data stores, such as Amazon S3, Amazon RDS, DynamoDB, Amazon Redshift, and ElastiCache, are not granted by this role.</td></tr>
  <tr><td colspan="2">Used by (entity): <b>AMS Operations and AMS Services</b></td></tr>
  <tr><td>ams_ssm_automation_role</td><td rowspan="2">Assumed by AWS Systems Manager to execute SSM Automation documents within your account.</td></tr>
  <tr><td>ams_ssm_automation_role</td></tr>
  <tr><td colspan="2">Used by (entity): <b>AMS Security</b></td></tr>
  <tr><td>ams-access-security-analyst</td><td>This AMS security role has permissions in your AMS account to perform dedicated security alert monitoring and security incident handling. Only a very few select AMS Security individuals can assume this role. Read permissions to customer content in AWS services that are commonly used as data stores, such as Amazon S3;, Amazon RDS;, Amazon DynamoDB, Amazon Redshift, and ElastiCache, aren't granted by this role.</td></tr>
  <tr><td>ams-access-security-analyst-read-only</td><td>This AMS security role is limited to read-only permissions in your AMS account to perform dedicated security alert monitoring and security incident handling. Read permissions to customer content in AWS services that are commonly used as data stores, such as Amazon S3;, Amazon RDS;, Amazon DynamoDB, Amazon Redshift, and ElastiCache, aren't granted by this role.</td></tr>
  <tr><td colspan="2">Used by (entity): <b>AWS Services</b></td></tr>
  <tr><td>ams-access-admin</td><td>This AMS admin role has full permissions to operate in accounts without restrictions. Only AMS internal services (with a scoped-down session policy) can assume the admin role.</td></tr>
  <tr><td>ams-opscenter-eventbridge-role</td><td>Assumed by Amazon EventBridge to create AWS Systems Manager OpsItems as a part of AMS-specific AWS Config Rules remediation workflow.</td></tr>
  <tr><td>AMSOSConfigurationCustomerInstanceRole</td><td>This IAM role is applied to your Amazon EC2 instances when AMS OS-Configuration service discovers that the required IAM policies are missing. It allows your Amazon EC2 instances to interact with AWS Systems Manager, Amazon CloudWatch, and Amazon EventBridge services. It also has attached the AMS custom-managed policy to enable RDP access to your Windows instances.</td></tr>
  <tr><td>mc-patch-glue-service-role</td><td>Assumed by AWS Glue ETL workflow to perform data transformation and prepare it for AMS Patch report generator.</td></tr>
  <tr><td colspan="2">Used by (entity): <b>AMS Service</b></td></tr>
  <tr><td>ams-alarm-manager-AWSManagedServicesAlarmManagerDe-&lt;8-digit hash&gt;</td><td>Assumed by AMS alarm manager infrastructure within your AMS account to perform AWS Config Rules evaluation for a new AWS AppConfig deployment.</td></tr>
  <tr><td>ams-alarm-manager-AWSManagedServicesAlarmManagerRe-&lt;8-digit hash&gt;</td><td>Assumed by AMS alarm manager remediation infrastructure within your AMS account to allow the creation or deletion of alarms for remediation.</td></tr>
  <tr><td>ams-alarm-manager-AWSManagedServicesAlarmManagerSS-&lt;8-digit hash&gt;</td><td>Assumed by AWS Systems Manager to invoke the AMS alarm manager remediation service within your AMS account.</td></tr>
  <tr><td>ams-alarm-manager-AWSManagedServicesAlarmManagerTr-&lt;8-digit hash&gt;</td><td>Assumed by AMS alarm manager infrastructure within your AWS account to conduct periodic AMS AWS Config Rules evaluation.</td></tr>
  <tr><td>ams-alarm-manager-AWSManagedServicesAlarmManagerVa-&lt;8-digit hash&gt;</td><td>Assumed by AMS alarm manager infrastructure within your AMS account to ensure that the required alarms exists in the AWS account.</td></tr>
  <tr><td>ams-backup-iam-role</td><td>This role is used to run AWS Backup within your accounts.</td></tr>
  <tr><td>ams-monitoring-AWSManagedServicesLogGroupLimitLamb-&lt;8-digit hash&gt;</td><td>Assumed by AMS Logging &amp; Monitoring infrastructure in your AMS account to evaluate Amazon CloudWatch Logs groups limit and compare with the service quotas.</td></tr>
  <tr><td>ams-monitoring-AWSManagedServicesRDSMonitoringRDSE-&lt;8-digit hash&gt;</td><td>Assumed by AMS Logging &amp; Monitoring infrastructure in your AMS account to forward Amazon RDS events to Amazon CloudWatch Events.</td></tr>
  <tr><td>ams-monitoring-AWSManagedServicesRedshiftMonitorin-&lt;8-digit hash&gt;</td><td>Assumed by AMS Logging &amp; Monitoring infrastructure in your AMS account to forward Amazon Redshift events (CreateCluster and DeleteCuster) to Amazon CloudWatch Events.</td></tr>
  <tr><td>ams-monitoring-infrastruc-AWSManagedServicesMonito-&lt;8-digit hash&gt;</td><td>Assumed by AMS Logging &amp; Monitoring infrastructure in your AMS account to publish messages to Amazon Simple Notification Service to validate that the account is reporting all necessary data.</td></tr>
  <tr><td>ams-opscenter-role</td><td>Assumed by AMS Notification Management system in your AMS account to manage AWS Systems Manager OpsItems related to alerts in your account.</td></tr>
  <tr><td>ams-opsitem-autoexecution-role</td><td>Assumed by AMS Notification Management system to handle automated remediation using SSM documents for monitoring alerts related to resources in your account.</td></tr>
  <tr><td>ams-patch-infrastructure-amspatchconfigruleroleC1-&lt;8-digit hash&gt;</td><td>Assumed by AWS Config to evaluate AMS patch resources and detect drift in its CloudFormation stacks.</td></tr>
  <tr><td>ams-patch-infrastructure-amspatchcwruleopsitemams-&lt;8-digit hash&gt;</td><td>Assumed by Amazon EventBridge to create AWS Systems Manager OpsItems for patching failures.</td></tr>
  <tr><td>ams-patch-infrastructure-amspatchservicebusamspat-&lt;8-digit hash&gt;</td><td>Assumed by Amazon EventBridge to send an event to the AMS Patch orchestrator event bus for AWS Systems Manager Maintenance Windows state change notifications.</td></tr>
  <tr><td>ams-patch-reporting-infra-amspatchreportingconfigr-&lt;8-digit hash&gt;</td><td>Assumed by AWS Config to evaluate AMS Patch reporting resources and detect drift in its CloudFormation stacks.</td></tr>
  <tr><td>ams-resource-tagger-AWSManagedServicesResourceTagg-&lt;8-digit hash&gt;</td><td>Assumed by AMS Resource Tagger infrastructure within your AMS account to perform AWS Config Rules evaluation upon new AWS AppConfig deployment.</td></tr>
  <tr><td>ams-resource-tagger-AWSManagedServicesResourceTagg-&lt;8-digit hash&gt;</td><td>Assumed by AMS Resource Tagger infrastructure within your AMS account to validate that required AWS tags exist for the managed resources.</td></tr>
  <tr><td>ams-resource-tagger-AWSManagedServicesResourceTagg-&lt;8-digit hash&gt;</td><td>Assumed by AWS Systems Manager to invoke AMS Resource Tagger remediation workflow in your AMS account.</td></tr>
  <tr><td>ams-resource-tagger-AWSManagedServicesResourceTagg-&lt;8-digit hash&gt;</td><td>Assumed by AMS Resource Tagger remediation infrastructure within your AMS account to create or delete AWS tags for the managed resources.</td></tr>
  <tr><td>ams-resource-tagger-AWSManagedServicesResourceTagg-&lt;8-digit hash&gt;</td><td>Assumed by AMS Resource Tagger infrastructure within your AWS account to conduct periodic AMS Config Rule evaluation.</td></tr>
  <tr><td>ams_os_configuration_event_rule_role-&lt;AWS Region&gt;</td><td>Assumed by Amazon EventBridge to forward events from your account to AMS OS-Configuration service EventBus in the correct Region.</td></tr>
  <tr><td>mc-patch-reporting-service</td><td>Assumed by AMS patch data aggregator and report generator.</td></tr>
</tbody>
</table>


**Note**  
This is the template for the ams-access-management role. It's the stack that cloud architects (CAs) manually deploy in your account at onboarding: [management-role.yaml](https://ams-account-access-templates.s3.amazonaws.com/management-role.yaml).  
This is the template for the different access roles and access levels: ams-access-read-only, ams-access-operations, ams-access-admin-operations, ams-access-admin: [accelerate-roles.yaml](https://ams-account-access-templates.s3.amazonaws.com/accelerate-roles.yaml).

To learn more about AWS Cloud Development Kit (AWS CDK) (AWS CDK) identifiers, including hashes, see [UniqueIDs](https://docs.aws.amazon.com/cdk/latest/guide/identifiers.html#identifiers_unique_ids).

AMS Accelerate feature services assume the **ams-access-admin** role for programmatic access to the account, but with a session policy scoped down for the respective feature service (for example, patch, backup, monitoring, and so forth).

AMS Accelerate follows industry best practices to meet and maintain compliance eligibility. AMS Accelerate access to your account is recorded in CloudTrail and also available for your review through change tracking. For information about queries that you can use to get this information, see [Tracking changes in your AMS Accelerate accounts](acc-change-record.md).

## Managing access using policies
<a name="acc-sec-iam-policy"></a>

Various AMS Accelerate support teams such as Operations Engineers, Cloud Architects, and Cloud Service Delivery Managers (CSDMs), sometimes require access to your accounts in order to respond to service requests and incidents. Their access is governed by an internal AMS access service that enforces controls, such as business justification, service requests, operations items, and support cases. The default access is read-only, and all access is tracked and recorded; see also [Tracking changes in your AMS Accelerate accounts](acc-change-record.md).

### Validation of IAM resources
<a name="acc-sec-iam-policy-valid"></a>

The AMS Accelerate access system periodically assumes roles in your accounts (at least every 24 hours) and validates that all of our IAM resources are as expected.

In order to protect your accounts, AMS Accelerate has a "canary" that monitors and alarms on the presence and status of the IAM roles, as well as their attached policies, mentioned above. Periodically, the canary assumes the **ams-access-read-only** role and initiates CloudFormation and IAM API calls against your accounts. The canary evaluates the status of the AMS Accelerate access roles to make sure they are always unmodified and up-to-date. This activity creates CloudTrail logs in the account.

The AWS Security Token Service (AWS STS) session name of the canary is **AMS-Access-Roles-Auditor-{uuid4()}** as seen in CloudTrail and the following API calls occur:
+ Cloud Formation API Calls: `describe_stacks()`
+ IAM API Calls:
  + `get_role()`
  + `list_attached_role_policies()`
  + `list_role_policies()`
  + `get_policy()`
  + `get_policy_version()`
  + `get_role_policy()`