

# Security Hub CSPM controls for Amazon ECS
<a name="ecs-controls"></a>

These Security Hub CSPM controls evaluate the Amazon Elastic Container Service (Amazon ECS) service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [ECS.2] ECS services should not have public IP addresses assigned to them automatically
<a name="ecs-2"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:** `AWS::ECS::Service`

**AWS Config rule:** `ecs-service-assign-public-ip-disabled` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon ECS services are configured to automatically assign public IP addresses. This control fails if `AssignPublicIP` is `ENABLED`. This control passes if `AssignPublicIP` is `DISABLED`.

A public IP address is an IP address that is reachable from the internet. If you launch your Amazon ECS instances with a public IP address, then your Amazon ECS instances are reachable from the internet. Amazon ECS services should not be publicly accessible, as this may allow unintended access to your container application servers.

### Remediation
<a name="ecs-2-remediation"></a>

First, you must create a task definition for your cluster that uses the `awsvpc` network mode and specifies **FARGATE** for `requiresCompatibilities`. Then, for **Compute configuration**, choose **Launch type** and **FARGATE**. Finally, for the **Networking** field, turn off **Public IP** to disable automatic public IP assignment for your service.

## [ECS.3] ECS task definitions should not share the host's process namespace
<a name="ecs-3"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Identify > Resource configuration

**Severity:** High

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-task-definition-pid-mode-check](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-pid-mode-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon ECS task definitions are configured to share a host's process namespace with its containers. The control fails if the task definition shares the host's process namespace with the containers running on it. This control only evaluates the latest active revision of an Amazon ECS task definition.

A process ID (PID) namespace provides separation between processes. It prevents system processes from being visible, and allows PIDs to be reused, including PID 1. If the host's PID namespace is shared with containers, it would allow containers to see all of the processes on the host system. This reduces the benefit of process level isolation between the host and the containers. These circumstances could lead to unauthorized access to processes on the host itself, including the ability to manipulate and terminate them. Customers shouldn't share the host's process namespace with containers running on it.

### Remediation
<a name="ecs-3-remediation"></a>

To configure the `pidMode` on a task definition, see [Task definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_definition_pidmode) in the Amazon Elastic Container Service Developer Guide.

## [ECS.4] ECS containers should run as non-privileged
<a name="ecs-4"></a>

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6

**Category:** Protect > Secure access management > Root user access restrictions

**Severity:** High

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-containers-nonprivileged](https://docs.aws.amazon.com/config/latest/developerguide/ecs-containers-nonprivileged.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if the `privileged` parameter in the container definition of Amazon ECS Task Definitions is set to `true`. The control fails if this parameter is equal to `true`. This control only evaluates the latest active revision of an Amazon ECS task definition.

We recommend that you remove elevated privileges from your ECS task definitions. When the privilege parameter is `true`, the container is given elevated privileges on the host container instance (similar to the root user).

### Remediation
<a name="ecs-4-remediation"></a>

To configure the `privileged` parameter on a task definition, see [Advanced container definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definition_security) in the Amazon Elastic Container Service Developer Guide.

## [ECS.5] ECS task definitions should configure containers to be limited to read-only access to root filesystems
<a name="ecs-5"></a>

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6

**Category:** Protect > Secure access management

**Severity:** High

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-containers-readonly-access](https://docs.aws.amazon.com/config/latest/developerguide/ecs-containers-readonly-access.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether ECS task definitions configure containers to be limited to read-only access to mounted root file systems. The control fails if the `readonlyRootFilesystem` parameter in the container definitions of ECS task definition is set to `false`, or the parameter doesn't exist in the container definition within the task definition. This control evaluates only the latest active revision of an Amazon ECS task definition.

If the `readonlyRootFilesystem` parameter is set to `true` in an Amazon ECS task definition, the ECS container is given read-only access to its root file system. This reduces security attack vectors because the container instance's root file system can't be tampered with or written to without explicit volume mounts that have read-write permissions for file system folders and directories. Enabling this option also adheres to the principle of least privilege.

**Note**  
The `readonlyRootFilesystem` parameter is not supported for Windows containers. Task definitions with `runtimePlatform` configured to specify a `WINDOWS_SERVER` OS family are marked as `NOT_APPLICABLE` and will not generate findings for this control. 

### Remediation
<a name="ecs-5-remediation"></a>

To give an Amazon ECS container read-only access to its root file system, add the `readonlyRootFilesystem` parameter to the task definition for the container, and set the value for the parameter to `true`. For information about task definition parameters and how to add them to a task definition, see [Amazon ECS task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) and [Updating a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.8] Secrets should not be passed as container environment variables
<a name="ecs-8"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, PCI DSS v4.0.1/8.6.2

**Category:** Protect > Secure development > Credentials not hard-coded

**Severity:** High

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-no-environment-secrets](https://docs.aws.amazon.com/config/latest/developerguide/ecs-no-environment-secrets.html) 

**Schedule type:** Change triggered

**Parameters:** `secretKeys`: `AWS_ACCESS_KEY_ID`,`AWS_SECRET_ACCESS_KEY`,`ECS_ENGINE_AUTH_DATA` (not customizable) 

This control checks if the key value of any variables in the `environment` parameter of container definitions includes `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `ECS_ENGINE_AUTH_DATA`. This control fails if a single environment variable in any container definition equals `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `ECS_ENGINE_AUTH_DATA`. This control does not cover environmental variables passed in from other locations such as Amazon S3. This control only evaluates the latest active revision of an Amazon ECS task definition.

AWS Systems Manager Parameter Store can help you improve the security posture of your organization. We recommend using the Parameter Store to store secrets and credentials instead of directly passing them into your container instances or hard coding them into your code.

### Remediation
<a name="ecs-8-remediation"></a>

To create parameters using SSM, see [Creating Systems Manager parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html) in the *AWS Systems Manager User Guide*. For more information about creating a task definition that specifies a secret, see [Specifying sensitive data using Secrets Manager](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-secrets.html#secrets-create-taskdefinition) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.9] ECS task definitions should have a logging configuration
<a name="ecs-9"></a>

**Related requirements:** NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** High

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-task-definition-log-configuration](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-log-configuration.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if the latest active Amazon ECS task definition has a logging configuration specified. The control fails if the task definition doesn't have the `logConfiguration` property defined or if the value for `logDriver` is null in at least one container definition.

Logging helps you maintain the reliability, availability, and performance of Amazon ECS. Collecting data from task definitions provides visibility, which can help you debug processes and find the root cause of errors. If you are using a logging solution that does not have to be defined in the ECS task definition (such as a third party logging solution), you can disable this control after ensuring that your logs are properly captured and delivered.

### Remediation
<a name="ecs-9-remediation"></a>

To define a log configuration for your Amazon ECS task definitions, see [Specifying a log configuration in your task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html#specify-log-config) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.10] ECS Fargate services should run on the latest Fargate platform version
<a name="ecs-10"></a>

**Related requirements:** NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5 SI-2(4), NIST.800-53.r5 SI-2(5), PCI DSS v4.0.1/6.3.3

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** Medium

**Resource type:** `AWS::ECS::Service`

**AWS Config rule:** [ecs-fargate-latest-platform-version](https://docs.aws.amazon.com/config/latest/developerguide/ecs-fargate-latest-platform-version.html)

**Schedule type:** Change triggered

**Parameters:**
+ `latestLinuxVersion: 1.4.0` (not customizable)
+ `latestWindowsVersion: 1.0.0` (not customizable)

This control checks if Amazon ECS Fargate services are running the latest Fargate platform version. This control fails if the platform version is not the latest.

AWS Fargate platform versions refer to a specific runtime environment for Fargate task infrastructure, which is a combination of kernel and container runtime versions. New platform versions are released as the runtime environment evolves. For example, a new version may be released for kernel or operating system updates, new features, bug fixes, or security updates. Security updates and patches are deployed automatically for your Fargate tasks. If a security issue is found that affects a platform version, AWS patches the platform version. 

### Remediation
<a name="ecs-10-remediation"></a>

To update an existing service, including its platform version, see [Updating a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service.html) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.12] ECS clusters should use Container Insights
<a name="ecs-12"></a>

**Related requirements:** NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::ECS::Cluster`

**AWS Config rule:** [ecs-container-insights-enabled](https://docs.aws.amazon.com/config/latest/developerguide/ecs-container-insights-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if ECS clusters use Container Insights. This control fails if Container Insights are not set up for a cluster.

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon ECS clusters. Use CloudWatch Container Insights to collect, aggregate, and summarize metrics and logs from your containerized applications and microservices. CloudWatch automatically collects metrics for many resources, such as CPU, memory, disk, and network. Container Insights also provides diagnostic information, such as container restart failures, to help you isolate issues and resolve them quickly. You can also set CloudWatch alarms on metrics that Container Insights collects.

### Remediation
<a name="ecs-12-remediation"></a>

To use Container Insights, see [Updating a service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS.html) in the *Amazon CloudWatch User Guide*.

## [ECS.13] ECS services should be tagged
<a name="ecs-13"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::ECS::Service`

**AWS Config rule:** `tagged-ecs-service` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon ECS service has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the service doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the service isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ecs-13-remediation"></a>

To add tags to an ECS service, see [Tagging your Amazon ECS resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.14] ECS clusters should be tagged
<a name="ecs-14"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::ECS::Cluster`

**AWS Config rule:** `tagged-ecs-cluster` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon ECS cluster has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the cluster doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the cluster isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ecs-14-remediation"></a>

To add tags to an ECS cluster, see [Tagging your Amazon ECS resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.15] ECS task definitions should be tagged
<a name="ecs-15"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** `tagged-ecs-taskdefinition` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an Amazon ECS task definition has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the task definition doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the task definition isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="ecs-15-remediation"></a>

To add tags to an ECS task definition, see [Tagging your Amazon ECS resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.16] ECS task sets should not automatically assign public IP addresses
<a name="ecs-16"></a>

**Related requirements:** PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:** `AWS::ECS::TaskSet`

**AWS Config rule:** `ecs-taskset-assign-public-ip-disabled` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon ECS task set is configured to automatically assign public IP addresses. The control fails if `AssignPublicIP` is set to `ENABLED`.

A public IP address is reachable from the internet. If you configure your task set with a public IP address, the resources associated with the task set can be reached from the internet. ECS task sets shouldn't be publicly accessible, as this may allow unintended access to your container application servers.

### Remediation
<a name="ecs-16-remediation"></a>

To update an ECS task set so that it doesn't use a public IP address, see [Updating an Amazon ECS task definition using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.17] ECS task definitions should not use host network mode
<a name="ecs-17"></a>

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-task-definition-network-mode-not-host](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-network-mode-not-host.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the latest active revision of an Amazon ECS task definition uses `host` network mode. The control fails if the latest active revision of the ECS task definition uses `host` network mode.

When using `host` network mode, the networking of an Amazon ECS container is tied directly to the underlying host that's running the container. Consequently, this mode allows containers to connect to private loopback network services on the host and to impersonate the host. Other significant drawbacks are that there's no way to remap a container port when using `host` network mode, and you can't run more than a single instantiation of a task on each host.

### Remediation
<a name="ecs-17-remediation"></a>

For information about networking modes and options for Amazon ECS tasks that are hosted on Amazon EC2 instances, see [Amazon ECS task networking options for the EC2 launch type](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*. For information about creating a new revision of a task definition and specifying a different network mode, see [Updating an Amazon ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html) in that guide.

If the Amazon ECS task definition was created by AWS Batch, see [Networking modes for AWS Batch jobs](https://docs.aws.amazon.com/batch/latest/userguide/networking-modes-jobs.html) to learn about networking modes and typical usage for AWS Batch job types and to choose a secure option.

## [ECS.18] ECS Task Definitions should use in-transit encryption for EFS volumes
<a name="ecs-18"></a>

**Category:** Protect > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-task-definition-efs-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-efs-encryption-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the latest active revision of an Amazon ECS task definition uses in-transit encryption for EFS volumes. The control fails if the latest active revision of the ECS task definition has in-transit encryption disabled for EFS volumes.

Amazon EFS volumes provide simple, scalable, and persistent shared file storage for use with your Amazon ECS tasks. Amazon EFS supports encryption of data in transit with Transport Layer Security (TLS). When encryption of data in transit is declared as a mount option for your EFS file system, Amazon EFS establishes a secure TLS connection with your EFS file system upon mounting your file system.

### Remediation
<a name="ecs-18-remediation"></a>

For information about enabling in-transit encryption for Amazon ECS Task Definition with EFS volumes, see [Step 5: Create a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-efs-volumes.html#efs-task-def) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.19] ECS capacity providers should have managed termination protection enabled
<a name="ecs-19"></a>

**Category:** Protect > Data Protection

**Severity:** Medium

**Resource type:** `AWS::ECS::CapacityProvider`

**AWS Config rule:** [ecs-capacity-provider-termination-check](https://docs.aws.amazon.com/config/latest/developerguide/ecs-capacity-provider-termination-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon ECS capacity provider has managed termination protection enabled. The control fails if managed termination protection is not enabled on an ECS capacity provider.

Amazon ECS capacity providers manage the scaling of infrastructure for tasks in your clusters. When you use EC2 instances for your capacity, you use Auto Scaling group to manage the EC2 instances. Managed termination protection allows cluster auto scaling to control which instances are terminated. When you used managed termination protection, Amazon ECS only terminates EC2 instances that don't have any running Amazon ECS tasks.

**Note**  
When using managed termination protection, managed scaling must also be used otherwise managed termination protection doesn't work.

### Remediation
<a name="ecs-19-remediation"></a>

To enable managed termination protection for an Amazon ECS capacity provider, see [Updating managed termination protection for Amazon ECS capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-managed-termination-protection.html) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.20] ECS Task Definitions should configure non-root users in Linux container definitions
<a name="ecs-20"></a>

**Category:** Protect > Secure access management > Root user access restrictions

**Severity:** Medium

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-task-definition-linux-user-non-root](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-linux-user-non-root.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the latest active revision of an Amazon ECS task definition configures Linux containers to run as non-root users. The control fails if a default root user is configured or user configuration is absent for any container.

When Linux containers run with root privileges, they pose several significant security risks. Root users have unrestricted access within the container. This elevated access increases the risk of container escape attacks, where an attacker could potentially break out of container isolation and access the underlying host system. If a container running as root is compromised, attackers may exploit this to access or modify host system resources, affecting other containers or the host itself. Furthermore, root access could enable privilege escalation attacks, allowing attackers to gain additional permissions beyond the container's intended scope. The user parameter in ECS task definitions can specify users in several formats, including username, user ID, username with group, or UID with group ID. It's important to be aware of these various formats when configuring task definitions to ensure no root access is inadvertently granted. Following the principle of least privilege, containers should run with the minimum required permissions using non-root users. This approach significantly reduces the potential attack surface and mitigates the impact of potential security breaches. 

**Note**  
This control only evaluates the container definitions in a task definition if the `operatingSystemFamily` is configured as `LINUX` or `operatingSystemFamily` is not configured in the task definition. The control will generate a `FAILED` finding for an evaluated task definition if any container definition in the task definition has `user` not configured or `user` configured as default root user. The default root users for `LINUX` containers are `"root"` and `"0"`.

### Remediation
<a name="ecs-20-remediation"></a>

For information about creating a new revision of an Amazon ECS Task Definition and updating the `user` parameter in the container definition, see [Updating an Amazon ECS task defintion](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.

## [ECS.21] ECS Task Definitions should configure non-administrator users in Windows container definitions
<a name="ecs-21"></a>

**Category:** Protect > Secure access management > Root user access restrictions

**Severity:** Medium

**Resource type:** `AWS::ECS::TaskDefinition`

**AWS Config rule:** [ecs-task-definition-windows-user-non-admin](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-windows-user-non-admin.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the latest active revision of an Amazon ECS task definition configures Windows containers to run as users that are not default administrators. The control fails if a default administrator is configured as user or user configuration is absent for any container.

When Windows containers run with administrator privileges, they pose several significant security risks. Administrators have unrestricted access within the container. This elevated access increases the risk of container escape attacks, where an attacker could potentially break out of container isolation and access the underlying host system.

**Note**  
This control only evaluates the container definitions in a task definition if the `operatingSystemFamily` is configured as `WINDOWS_SERVER` or `operatingSystemFamily` is not configured in the task definition. The control will generate a `FAILED` finding for an evaluated task definition if any container definition in the task definition has `user` not configured or `user` configured as default administrator for `WINDOWS_SERVER` containers which is `"containeradministrator"`.

### Remediation
<a name="ecs-21-remediation"></a>

For information about creating a new revision of an Amazon ECS Task Definition and updating the `user` parameter in the container definition, see [Updating an Amazon ECS task defintion](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.