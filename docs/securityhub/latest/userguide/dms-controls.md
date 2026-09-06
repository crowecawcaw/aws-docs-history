

# Security Hub CSPM controls for AWS Database Migration Service
<a name="dms-controls"></a>

These AWS Security Hub CSPM controls evaluate the AWS Database Migration Service (AWS DMS) and AWS DMS resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [DMS.1] Database Migration Service replication instances should not be public
<a name="dms-1"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v3.2.1/1.2.1,PCI DSS v3.2.1/1.3.1,PCI DSS v3.2.1/1.3.4,PCI DSS v3.2.1/1.3.2,PCI DSS v3.2.1/1.3.6, PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration

**Severity:** Critical

**Resource type:** `AWS::DMS::ReplicationInstance`

**AWS Config rule:** [dms-replication-not-public](https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-not-public.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether AWS DMS replication instances are public. To do this, it examines the value of the `PubliclyAccessible` field.

A private replication instance has a private IP address that you cannot access outside of the replication network. A replication instance should have a private IP address when the source and target databases are in the same network. The network must also be connected to the replication instance's VPC using a VPN, Direct Connect, or VPC peering. To learn more about public and private replication instances, see [Public and private replication instances](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.PublicPrivate) in the *AWS Database Migration Service User Guide*.

You should also ensure that access to your AWS DMS instance configuration is limited to only authorized users. To do this, restrict users' IAM permissions to modify AWS DMS settings and resources.

### Remediation
<a name="dms-1-remediation"></a>

You can't change the public access setting for a DMS replication instance after creating it. To change the public access setting, [delete your current instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Deleting.html), and then [recreate it](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Creating.html). Don't select the **Publicly accessible** option.

## [DMS.2] DMS certificates should be tagged
<a name="dms-2"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::DMS::Certificate`

**AWS Config rule:** `tagged-dms-certificate` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an AWS DMS certificate has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the certificate doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the certificate isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="dms-2-remediation"></a>

To add tags to a DMS certificate, see [Tagging resources in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html) in the *AWS Database Migration Service User Guide*.

## [DMS.3] DMS event subscriptions should be tagged
<a name="dms-3"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::DMS::EventSubscription`

**AWS Config rule:** `tagged-dms-eventsubscription` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an AWS DMS event subscription has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the event subscription doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the event subscription isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="dms-3-remediation"></a>

To add tags to a DMS event subscription, see [Tagging resources in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html) in the *AWS Database Migration Service User Guide*.

## [DMS.4] DMS replication instances should be tagged
<a name="dms-4"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::DMS::ReplicationInstance`

**AWS Config rule:** `tagged-dms-replicationinstance` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an AWS DMS replication instance has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the replication instance doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the replication instance isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="dms-4-remediation"></a>

To add tags to a DMS replication instance, see [Tagging resources in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html) in the *AWS Database Migration Service User Guide*.

## [DMS.5] DMS replication subnet groups should be tagged
<a name="dms-5"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::DMS::ReplicationSubnetGroup`

**AWS Config rule:** `tagged-dms-replicationsubnetgroup` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an AWS DMS replication subnet group has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the replication subnet group doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the replication subnet group isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="dms-5-remediation"></a>

To add tags to a DMS replication subnet group, see [Tagging resources in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html) in the *AWS Database Migration Service User Guide*.

## [DMS.6] DMS replication instances should have automatic minor version upgrade enabled
<a name="dms-6"></a>

**Related requirements:** NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5 SI-2(4), NIST.800-53.r5 SI-2(5), PCI DSS v4.0.1/6.3.3

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** Medium

**Resource type:** `AWS::DMS::ReplicationInstance`

**AWS Config rule:** [dms-auto-minor-version-upgrade-check](https://docs.aws.amazon.com/config/latest/developerguide/dms-auto-minor-version-upgrade-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if automatic minor version upgrade is enabled for an AWS DMS replication instance. The control fails if automatic minor version upgrade isn't enabled for a DMS replication instance.

DMS provides automatic minor version upgrade to each supported replication engine so that you can keep your replication instance up-to-date. Minor versions can introduce new software features, bug fixes, security patches, and performance improvements. By enabling automatic minor version upgrade on DMS replication instances, minor upgrades are applied automatically during the maintenance window or immediately if the **Apply changes immediately option is chosen**.

### Remediation
<a name="dms-6-remediation"></a>

To enable automatic minor version upgrade on DMS replication instances, see [Modifying a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Modifying.html) in the *AWS Database Migration Service User Guide*.

## [DMS.7] DMS replication tasks for the target database should have logging enabled
<a name="dms-7"></a>

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::DMS::ReplicationTask`

**AWS Config rule:** [dms-replication-task-targetdb-logging](https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-task-targetdb-logging.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether logging is enabled with the minimum severity level of `LOGGER_SEVERITY_DEFAULT` for DMS replication tasks `TARGET_APPLY` and `TARGET_LOAD`. The control fails if logging isn't enabled for these tasks or if the minimum severity level is less than `LOGGER_SEVERITY_DEFAULT`.

DMS uses Amazon CloudWatch to log information during the migration process. Using logging task settings, you can specify which component activities are logged and how much information is logged. You should specify logging for the following tasks:
+ `TARGET_APPLY` – Data and data definition language (DDL) statements are applied to the target database.
+ `TARGET_LOAD` – Data is loaded into the target database.

Logging plays a critical role in DMS replication tasks by enabling monitoring, troubleshooting, auditing, performance analysis, error detection, and recovery, as well as historical analysis and reporting. It helps ensure the successful replication of data between databases while maintaining data integrity and compliance with regulatory requirements. Logging levels other than `DEFAULT` are rarely needed for these components during troubleshooting. We recommend keeping the logging level as `DEFAULT` for these components unless specifically requested to change it by Support. A minimal logging level of `DEFAULT` ensures that informational messages, warnings, and error messages are written to the logs. This control checks if the logging level is at least one of the following for the preceding replication tasks: `LOGGER_SEVERITY_DEFAULT`, `LOGGER_SEVERITY_DEBUG`, or `LOGGER_SEVERITY_DETAILED_DEBUG`.

### Remediation
<a name="dms-7-remediation"></a>

To enable logging for target database DMS replication tasks, see [Viewing and managing AWS DMS task logs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Monitoring.ManagingLogs) in the *AWS Database Migration Service User Guide*.

## [DMS.8] DMS replication tasks for the source database should have logging enabled
<a name="dms-8"></a>

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::DMS::ReplicationTask`

**AWS Config rule:** [dms-replication-task-sourcedb-logging](https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-task-sourcedb-logging.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether logging is enabled with the minimum severity level of `LOGGER_SEVERITY_DEFAULT` for DMS replication tasks `SOURCE_CAPTURE` and `SOURCE_UNLOAD`. The control fails if logging isn't enabled for these tasks or if the minimum severity level is less than `LOGGER_SEVERITY_DEFAULT`.

DMS uses Amazon CloudWatch to log information during the migration process. Using logging task settings, you can specify which component activities are logged and how much information is logged. You should specify logging for the following tasks:
+ `SOURCE_CAPTURE` – Ongoing replication or change data capture (CDC) data is captured from the source database or service, and passed to the `SORTER` service component.
+ `SOURCE_UNLOAD` – Data is unloaded from the source database or service during full load.

Logging plays a critical role in DMS replication tasks by enabling monitoring, troubleshooting, auditing, performance analysis, error detection, and recovery, as well as historical analysis and reporting. It helps ensure the successful replication of data between databases while maintaining data integrity and compliance with regulatory requirements. Logging levels other than `DEFAULT` are rarely needed for these components during troubleshooting. We recommend keeping the logging level as `DEFAULT` for these components unless specifically requested to change it by Support. A minimal logging level of `DEFAULT` ensures that informational messages, warnings, and error messages are written to the logs. This control checks if the logging level is at least one of the following for the preceding replication tasks: `LOGGER_SEVERITY_DEFAULT`, `LOGGER_SEVERITY_DEBUG`, or `LOGGER_SEVERITY_DETAILED_DEBUG`.

### Remediation
<a name="dms-8-remediation"></a>

To enable logging for source database DMS replication tasks, see [Viewing and managing AWS DMS task logs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Monitoring.ManagingLogs) in the *AWS Database Migration Service User Guide*.

## [DMS.9] DMS endpoints should use SSL
<a name="dms-9"></a>

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::DMS::Endpoint`

**AWS Config rule:** [dms-endpoint-ssl-configured](https://docs.aws.amazon.com/config/latest/developerguide/dms-endpoint-ssl-configured.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS DMS endpoint uses an SSL connection. The control fails if the endpoint doesn't use SSL.

SSL/TLS connections provide a layer of security by encrypting connections between DMS replication instances and your database. Using certificates provides an extra layer of security by validating that the connection is being made to the expected database. It does so by checking the server certificate that is automatically installed on all database instances that you provision. By enabling SSL connection on your DMS endpoints, you protect the confidentiality of the data during the migration.

### Remediation
<a name="dms-9-remediation"></a>

To add an SSL connection to a new or existing DMS endpoint, see [Using SSL with AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.SSL.html#CHAP_Security.SSL.Procedure) in the *AWS Database Migration Service User Guide*.

## [DMS.10] DMS endpoints for Neptune databases should have IAM authorization enabled
<a name="dms-10"></a>

**Related requirements:** NIST.800-53.r5 AC-2, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-17, NIST.800-53.r5 IA-2, NIST.800-53.r5 IA-5, PCI DSS v4.0.1/7.3.1

**Category:** Protect > Secure access management > Passwordless authentication

**Severity:** Medium

**Resource type:** `AWS::DMS::Endpoint`

**AWS Config rule:** [dms-neptune-iam-authorization-enabled](https://docs.aws.amazon.com/config/latest/developerguide/dms-neptune-iam-authorization-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS DMS endpoint for an Amazon Neptune database is configured with IAM authorization. The control fails if the DMS endpoint doesn't have IAM authorization enabled.

AWS Identity and Access Management (IAM) provides fine-grained access control across AWS. With IAM, you can specify who can access which services and resources, and under which conditions. With IAM policies, you manage permissions to your workforce and systems to ensure least-privilege permissions. By enabling IAM authorization on AWS DMS endpoints for Neptune databases, you can grant authorization privileges to IAM users by using a service role specified by the `ServiceAccessRoleARN` parameter.

### Remediation
<a name="dms-10-remediation"></a>

To enable IAM authorization on DMS endpoints for Neptune databases, see [Using Amazon Neptune as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html) in the *AWS Database Migration Service User Guide*.

## [DMS.11] DMS endpoints for MongoDB should have an authentication mechanism enabled
<a name="dms-11"></a>

**Related requirements:** NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-6, NIST.800-53.r5 IA-2, NIST.800-53.r5 IA-5, PCI DSS v4.0.1/7.3.1

**Category:** Protect > Secure access management > Passwordless authentication

**Severity:** Medium

**Resource type:** `AWS::DMS::Endpoint`

**AWS Config rule:** [dms-mongo-db-authentication-enabled](https://docs.aws.amazon.com/config/latest/developerguide/dms-mongo-db-authentication-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS DMS endpoint for MongoDB is configured with an authentication mechanism. The control fails if an authentication type isn't set for the endpoint.

AWS Database Migration Service supports two authentications methods for MongoDB—**MONGODB-CR** for MongoDB version 2.x, and **SCRAM-SHA-1** for MongoDB version 3.x or later. These authentication methods are used to authenticate and encrypt MongoDB passwords if users want to use the passwords to access the databases. Authentication on AWS DMS endpoints ensures that only authorized users can access and modify the data being migrated between databases. Without proper authentication, unauthorized users may be able to gain access to sensitive data during the migration process. This can result in data breaches, data loss, or other security incidents.

### Remediation
<a name="dms-11-remediation"></a>

To enable an authentication mechanism on DMS endpoints for MongoDB, see [Using MongoDB as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html) in the *AWS Database Migration Service User Guide*.

## [DMS.12] DMS endpoints for Redis OSS should have TLS enabled
<a name="dms-12"></a>

**Related requirements:** NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-13, PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::DMS::Endpoint`

**AWS Config rule:** [dms-redis-tls-enabled](https://docs.aws.amazon.com/config/latest/developerguide/dms-redis-tls-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS DMS endpoint for Redis OSS is configured with a TLS connection. The control fails if the endpoint doesn't have TLS enabled.

TLS provides end-to-end security when data is sent between applications or databases over the internet. When you configure SSL encryption for your DMS endpoint, it enables encrypted communication between the source and target databases during the migration process. This helps prevent eavesdropping and interception of sensitive data by malicious actors. Without SSL encryption, sensitive data may be accessed, resulting in data breaches, data loss, or other security incidents.

### Remediation
<a name="dms-12-remediation"></a>

To enable a TLS connection on DMS endpoints for Redis, see [Using Redis as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html) in the *AWS Database Migration Service User Guide*.

## [DMS.13] DMS replication instances should be configured to use multiple Availability Zones
<a name="dms-13"></a>

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::DMS::ReplicationInstance`

**AWS Config rule:** [dms-replication-instance-multi-az-enabled](https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-instance-multi-az-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS Database Migration Service (AWS DMS) replication instance is configured to use multiple Availability Zones (Multi-AZ deployment). The control fails if the AWS DMS replication instance isn't configured to use a Multi-AZ deployment.

In a Multi-AZ deployment, AWS DMS automatically provisions and maintains a standby replica of a replication instance in a different Availability Zone (AZ). The primary replication instance is then synchronously replicated to the standby replica. If the primary replication instance fails or becomes unresponsive, the standby resumes any running tasks with minimal interruption. For more information, see [Working with a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the *AWS Database Migration Service User Guide*.

### Remediation
<a name="dms-13-remediation"></a>

After you create an AWS DMS replication instance, you can change the Multi-AZ deployment setting for it. For information about changing this and other settings for an existing replication instance, see [Modifying a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Modifying.html) in the *AWS Database Migration Service User Guide*.