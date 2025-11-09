# Why and when AMS accesses your account

AWS Managed Services (AMS) manages your AWS infrastructure and sometimes, for specific reasons, AMS operators and administrators access
your account. These access events are documented in your AWS CloudTrail (CloudTrail) logs.

Why, when, and how AMS accesses your account is explained in the following topics.

## AMS customer account access triggers

AMS customer account access activity is driven by triggers. The triggers
today are the AWS tickets created in our issues management system in response
to Amazon CloudWatch (CloudWatch) alarms and events, and incident reports or service requests that you submit. Multiple
service calls and host-level activities might be performed for each access.

Access justification, the triggers, and the initiator of the trigger are listed in the following table.

| Access Triggers                        | Access | Initiator                                                                                     | Trigger |
| -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- | ------- |
| Patching                               | AMS    | Patch issue                                                                                   |
| Infrastructure deployments             | AMS    | Deployment issue                                                                              |
| Internal problem investigation         | AMS    | Problem issue (an issue that has been identified as systemic)                                 |
| Alert investigation and remediation    | AMS    | AWS Systems Manager operational work items (SSM OpsItems)                                     |
| Manual RFC execution                   | You    | Request for Change (RFC) issue. (Non-automated RFCs may require AMS access to your resources) |
| Incident investigation and remediation | You    | Inbound support case (an incident or service request you submit)                              |
| Inbound service request fulfillment    | You    |

## AMS customer account access IAM roles

When triggered, AMS accesses customer accounts using AWS Identity and Access Management (IAM) roles. Like all
activity in your account, the roles and their usage are logged in CloudTrail.

###### Important

Do not modify or delete these roles.

| IAM roles for AMS access to customer accounts      | Role Name                                                                                 | Account Type (SALZ, MALZ Management, MALZ Application, etc.)                                                     | Description |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| ams-service-admin                                  | SALZ, MALZ                                                                                | AMS Service automation access and automated infrastructure deployments e.g Patch, Backup, Automated Remediation. |
| ams-application-infra-read-only                    | SALZ, MALZ Application, MALZ Tools-Application                                            | Operator read only access                                                                                        |
| ams-application-infra-operations                   | Operator access for incidents/service requests                                            |
| ams-application-infra-admin                        | AD Admin access                                                                           |
| ams-primary-read-only                              | MALZ Management                                                                           | Operator read only access                                                                                        |
| ams-primary-operations                             | Operator access for incidents/service requests                                            |
| ams-primary-admin                                  | AD Admin access                                                                           |
| ams-logging-read-only                              | MALZ Logging                                                                              | Operator read only access                                                                                        |
| ams-logging-operations                             | Operator access for incidents/service requests                                            |
| ams-logging-admin                                  | AD Admin access                                                                           |
| ams-networking-read-only                           | MALZ Networking                                                                           | Operator read only access                                                                                        |
| ams-networking-operations                          | Operator access for incidents/service requests                                            |
| ams-networking-admin                               | AD Admin access                                                                           |
| ams-shared-services-read-only                      | MALZ Shared Services                                                                      | Operator read only access                                                                                        |
| ams-shared-services-operations                     | Operator access for incidents/service requests                                            |
| ams-shared-services-admin                          | AD Admin access                                                                           |
| ams-security-read-only                             | MALZ Security                                                                             | Operator read only access                                                                                        |
| ams-security-operations                            | Operator access for incidents/service requests                                            |
| ams-security-admin                                 | AD Admin access                                                                           |
| ams-access-security-analyst                        | SALZ, MALZ Application, MALZ Tools-Application, MALZ Core                                 | AMS Security access                                                                                              |
| ams-access-security-analyst-read-only              | AMS Security, read only access                                                            |
| Sentinel_AdminUser_Role_PXHazRQadu0PVcCDcMbHE      | SALZ                                                                                      | [BreakGlassRole]Used to breakGlass into the customer accounts                                                    |
| Sentinel_PowerUser_Role_wZuPuS0ROOl0IazDbRI9       | SALZ, MALZ                                                                                | Poweruser access to customer accounts for RFC execution                                                          |
| Sentinel_ReadOnlyUser_Role_Pd4L6Rw9RD0lnLkD5JOo    | ReadOnly access to customer accounts for RFC execution                                    |
| ams_admin_role                                     | Admin access to customer accounts for RFC execution                                       |
| AWSManagedServices_Provisioning_CustomerStacksRole | Used to launch and update CFN stacks on behalf of customers through CloudFormation Ingest |
| customer_ssm_automation_role                       | Role passed by CT executions to SSM Automation for runbook execution                      |
| ams_ssm_automation_role                            | SALZ, MALZ Application, MALZ Core                                                         | Role passed by AMS services to SSM Automation for runbook execution                                              |
| ams_ssm_iam_deployment_role                        | MALZ Application                                                                          | Role used by IAM catalog                                                                                         |
| ams_ssm_shared_svcs_intermediary_role              | MALZ Shared Services                                                                      | Role used by application ams_ssm_automation_role to execute specific SSM Documents in Shared Services account    |
| AmsOpsCenterRole                                   | SALZ, MALZ                                                                                | Used to create and update OpsItems in customer accounts                                                          |
| AMSOpsItemAutoExecutionRole                        | Used to get SSM Documents, describe resource tags, update OpsItems, and start automation  |
| customer-mc-ec2-instance-profile                   | Default customer EC2 instance profile (role)                                              |

## Requesting instance access

To access a resource, you must first submit a request for change (RFC) for that access. There
are two types of access that you can request: admin (read/write permissions) and
read-only (standard user access). Access lasts for eight
hours, by default. This information is required:

- Stack ID, or set of stack IDs, for the instance or instances you want to access.
- The fully qualified domain name of your AMS-trusted domain.
- The Active Directory username of the person who wants access.
- The ID of the VPC where the stacks are that you want access to.

Once you've been granted access, you can update the request as needed.

For examples of how to request access, see
[Stack Admin Access | Grant](../ctref/management-access-stack-admin-access-grant.md "../ctref/management-access-stack-admin-access-grant.md") or
[Stack Read-only Access | Grant](../ctref/management-access-stack-read-only-access-grant.md "../ctref/management-access-stack-read-only-access-grant.md").
