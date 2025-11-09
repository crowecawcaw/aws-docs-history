# Why and when AMS accesses your account

AMS Accelerate (Accelerate) operators can access your account console and instances, in certain circumstances, for managing your resources.
These access events are documented in your AWS CloudTrail (CloudTrail) logs. For details on how to review activity in your account by the AMS Accelerate Operations team and AMS Accelerate automation,
see [Tracking changes in your AMS Accelerate accounts](acc-change-record.md "acc-change-record.md").

Why, when, and how AMS accesses your account is explained in the following topics.

## AMS customer account access triggers

AMS customer account access activity is driven by triggers. The triggers
today are the AWS tickets created in our issues management system in response
to Amazon CloudWatch (CloudWatch) alarms and events, and incident reports or service requests that you submit. Multiple
service calls and host-level activities might be performed for each access.

Access justification, the triggers, and the initiator of the trigger are listed in the following table.

| Access Triggers                        | Access | Initiator                                                        | Trigger |
| -------------------------------------- | ------ | ---------------------------------------------------------------- | ------- |
| Patching                               | AMS    | Patch issue                                                      |
| Internal problem investigation         | AMS    | Problem issue (an issue that has been identified as systemic)    |
| Alert investigation and remediation    | AMS    | AWS Systems Manager operational work items (SSM OpsItems)        |
| Incident investigation and remediation | You    | Inbound support case (an incident or service request you submit) |
| Inbound service request fulfillment    | You    |

## AMS customer account access IAM roles

AMS operators require the following roles to service your account.

###### Note

AMS access roles allow AMS operators to access your resources to provide AMS capabilities (see
[Service description](acc-sd.md "acc-sd.md")). Altering these roles can inhibit
our ability to provide these capabilities. If you need to alter AMS access roles, consult your Cloud Architect.

| IAM roles for AMS access to customer accounts | Role Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| ams-access-admin                              | This role has full administrative access to your account without restrictions.<br>AMS services use this role with restrictive session policies that limit access to deploy AMS infrastructure and operate your account.                                                                                                                                                                                                                                                                                                                                                                                                     |
| ams-access-admin-operations                   | This role grants AMS operators administrative permissions to operate your account. This role does not grant read, write, or delete permissions to customer content in AWS services commonly used as data stores, such as Amazon Simple Storage Service, Amazon Relational Database Service, Amazon DynamoDB, Amazon Redshift, and Amazon ElastiCache. Only qualified AMS operators who have a strong understanding and background in access management can assume this role. These operators serve as an escalation point for access management issues and access your accounts to troubleshoot AMS operator access issues. |
| ams-access-management                         | Deployed manually during onboarding. The AMS Access system requires this role to manage `ams-access-roles` and `ams-access-managed-policies` stacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ams-access-operations                         | This role has permissions to perform administrative tasks in your accounts. This role does not have read, write, or delete permissions to customer content in AWS services commonly used as data stores, such as Amazon Simple Storage Service, Amazon Relational Database Service, Amazon DynamoDB, Amazon Redshift, and Amazon ElastiCache. Permissions to perform AWS Identity and Access Management write operations are also excluded from this role. AMS Accelerate operations staff and cloud architects (CAs) can assume this role.                                                                                 |
| ams-access-read-only                          | This role has read-only access to your account. AMS Accelerate operations staff and cloud architects (CAs)<br>can assume this role. Read permissions to customer content in AWS services commonly used as data stores, such as Amazon S3, Amazon RDS, DynamoDB, Amazon Redshift, and ElastiCache, are not granted this role.                                                                                                                                                                                                                                                                                                |
| ams-access-security-analyst                   | This AMS security role has permissions in your AMS<br>account to perform dedicated security alert monitoring and security incident handling. Only a very few select AMS Security individuals<br>can assume this role.                                                                                                                                                                                                                                                                                                                                                                                                       |
| ams-access-security-analyst-read-only         | This AMS security role is limited to read-only permissions in your AMS<br>account to perform dedicated security alert monitoring and security incident handling.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

###### Note

This is the template for the ams-access-management role. It is the stack that cloud architects (CAs) manually deploy in your account at onboarding time:
[management-role.yaml](https://ams-account-access-templates.s3.amazonaws.com/management-role.yaml "https://ams-account-access-templates.s3.amazonaws.com/management-role.yaml").

This is the template for the different access roles for the different access levels: ams-access-read-only, ams-access-operations, ams-access-admin-operations, ams-access-admin:
[accelerate-roles.yaml](https://ams-account-access-templates.s3.amazonaws.com/accelerate-roles.yaml "https://ams-account-access-templates.s3.amazonaws.com/accelerate-roles.yaml").
