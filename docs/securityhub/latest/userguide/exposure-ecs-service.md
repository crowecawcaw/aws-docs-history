# Remediating exposures for Amazon ECS services

AWS Security Hub can generate exposure findings for Amazon Elastic Container Service (Amazon ECS) services.

The Amazon ECS service involved in an exposure finding and its identifying information are
listed in the **Resource** section of the finding details. You can retrieve
these resource details on the Security Hub console or programmatically with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other AWS resources.

###### Contents

- [Misconfiguration traits for Amazon ECS services](exposure-ecs-service.md#ecs-service-misconfiguration "exposure-ecs-service.md#ecs-service-misconfiguration")
  - [The Amazon ECS service uses a task definition configured with elevated privileges](exposure-ecs-service.md#task-definition-privileged "exposure-ecs-service.md#task-definition-privileged")
  - [The Amazon ECS service uses a task definition that allows containers to access the root file systems](exposure-ecs-service.md#root-access-to-filesystem "exposure-ecs-service.md#root-access-to-filesystem")
  - [The Amazon ECS service uses a task definition configured to share a host's process namespace](exposure-ecs-service.md#exposed-name-space "exposure-ecs-service.md#exposed-name-space")
  - [The Amazon ECS service uses a task definition configured with cleartext credentials in the environment variables](exposure-ecs-service.md#cleartext-credentials-present "exposure-ecs-service.md#cleartext-credentials-present")
  - [The Amazon ECS service has an open security group](exposure-ecs-service.md#open-security-group "exposure-ecs-service.md#open-security-group")
  - [The Amazon ECS service has public IP addresses](exposure-ecs-service.md#public-ip-assigned "exposure-ecs-service.md#public-ip-assigned")
  - [The Amazon ECS service uses a task definition that is configured with host networking mode enabled](exposure-ecs-service.md#host-networking-mode-enabled "exposure-ecs-service.md#host-networking-mode-enabled")
  - [The IAM role associated with the Amazon ECS service has an administrative access policy](exposure-ecs-service.md#administrative-access-policy "exposure-ecs-service.md#administrative-access-policy")
  - [The IAM Role associated with the ECS service has a Service Admin Policy](exposure-ecs-service.md#service-administrative-policy "exposure-ecs-service.md#service-administrative-policy")

- [Vulnerability traits for Amazon ECS services](exposure-ecs-service.md#vulnerability "exposure-ecs-service.md#vulnerability")
  - [The Amazon ECS service has a container with network-exploitable software vulnerabilities with a high likelihood of exploitation](exposure-ecs-service.md#high-priority-vulnerability "exposure-ecs-service.md#high-priority-vulnerability")
  - [The Amazon ECS service has a container with software vulnerabilities](exposure-ecs-service.md#low-priority-vulnerability "exposure-ecs-service.md#low-priority-vulnerability")
  - [The Amazon ECS service has a container with an End-Of-Life operating system](exposure-ecs-service.md#end-of-life-operating-system-detected "exposure-ecs-service.md#end-of-life-operating-system-detected")

- [The Amazon ECS service has a container with malicious software packages](exposure-ecs-service.md#malicious-package "exposure-ecs-service.md#malicious-package")

## Misconfiguration traits for Amazon ECS services

Here are misconfiguration traits for Amazon ECS services and suggested remediation steps.

### The Amazon ECS service uses a task definition configured with elevated privileges

Amazon ECS containers running with elevated privileges have similar capabilities to the
host system, potentially allowing access to host resources and other containers.
This configuration increases the risk that a compromised container could be used to
access or modify resources outside its intended scope, potentially leading to
container escape, unauthorized access to the underlying host, and breaches affecting
other containers on the same host. Following standard security principles, AWS
recommends that you grant least privileges, which means that you grant only the
permissions required to perform a task.

###### Review and modify task definition

In the exposure, identify the task definition ARN. Open the task definition in
the Amazon ECS console. In the task definition, look for the privileged flag set to
true in the container definitions.

If privileged mode is not required, create a new task definition revision
without the privileged flag.

If privileged mode is required, consider configuring the container to use a
read-only file system to prevent unauthorized modifications.

### The Amazon ECS service uses a task definition that allows containers to access the root file systems

Amazon ECS containers with access to the host root filesystem can potentially read,
modify, or execute critical files on the host system. This configuration increases
the risk that a compromised container could be used to access or modify resources
outside its intended scope, potentially exposing sensitive data on the host
filesystem. Following standard security principles, AWS recommends that you grant
least privileges, which means that you grant only the permissions required to
perform a task.

###### Review and modify containers with host filesystem access

In the exposure finding, identify the task definition ARN. Open the task
definition in the Amazon ECS console. Look for the volumes section in the task
definition that defines host path mappings. Review the task definition to
determine if the host filesystem access is required for container functionality.

If host filesystem access is not required, create a new task definition revision
and remove any volume definitions that use host paths.

If host filesystem access is required, consider configuring the container to use
a read-only file system to prevent unauthorized modifications.

### The Amazon ECS service uses a task definition configured to share a host's process namespace

Amazon ECS containers running with exposed namespaces can potentially access host
system resources and other container namespaces. This configuration could allow a
compromised container to escape its isolation boundary, which could lead to
accessing processes, network interfaces, or other resources outside of its intended
scope. A process ID (PID) namespace provides separation between processes. It
prevents system processes from being visible, and allows PIDs to be reused,
including PID 1. If the host's PID namespace is shared with containers, it would
allow containers to see all of the processes on the host system. This reduces the
benefit of process level isolation between the host and the containers. These
factors could lead to unauthorized access to processes on the host itself, including
the ability to manipulate and terminate them. Following standard security
principles, AWS recommends maintaining proper namespace isolation for containers.

###### Update task definitions with exposed namespaces

Open the **Resources** tab of the exposure, identify the task
definition with the exposed namespace. Open the task definition in the Amazon ECS
console. Look for the pidMode settings with a value of host, which would share
the process ID namespaces with the host. Remove the pidMode: host settings from
your task definitions to ensure containers run with proper namespace isolation.

### The Amazon ECS service uses a task definition configured with cleartext credentials in the environment variables

Amazon ECS containers with cleartext credentials in environment variables expose
sensitive authentication information that could be compromised if an attacker gains
access to the task definition, container environment, or container logs. This
creates a significant security risk, as leaked credentials could be used to access
other AWS services or resources.

###### Replace cleartext credentials

In the exposure finding, identify the task definition with cleartext
credentials. Open the task definition in the Amazon ECS console. Look for environment
variables in the container definition that contain sensitive values such as
AWS access keys, database passwords, or API tokens.

Consider the following alternatives to pass credentials:

- Instead of using AWS access keys, use IAM task execution roles and
  task roles to grant permissions to your containers.
- Store credentials as secrets in AWS Secrets Manager and reference them in your task
  definition.

###### Update task definitions

Create a new revision of your task definition that securely handles
credentials. Then update your Amazon ECS service to use the new task definition
revision.

### The Amazon ECS service has an open security group

Security groups act as virtual firewalls for your Amazon ECS tasks to control inbound
and outbound traffic. Open security groups, which allow unrestricted access from any
IP address, may expose your containers to unauthorized access, increasing the risk
of exposure to automated scanning tools and targeted attacks. Following standard
security principles, AWS recommends restricting security group access to specific
IP addresses and ports.

###### Review security group rules and assess current configuration

Open the resource for the Amazon ECS Security Group. Evaluate which ports are open
and accessible from broad IP ranges, such as `(0.0.0.0/0 or ::/0)`.

###### Modify security group rules

Modify your security group rules to restrict access to specific trusted IP
addresses or ranges. When updating your security group rules, consider
separating access requirements for different network segments by creating rules
for each required source IP range or restricting access to specific ports.

###### Modify security group rules

Consider the following options for alternative access methods:

- Session Manager provides secure shell access to your Amazon EC2 instances
  without the need for inbound ports, managing SSH keys, or maintaining
  bastion hosts.
- NACLs provide an additional layer of security at the subnet level. Unlike
  security groups, NACLs are stateless and require both inbound and outbound
  rules to be explicitly defined.

### The Amazon ECS service has public IP addresses

Amazon ECS services with public IP addresses assigned to their tasks are directly
accessible from the internet. While this may be necessary for services that need to
be publicly available, it increases the attack surface and potential for
unauthorized access.

###### Identify services with public IP addresses

In the exposure finding, identify the Amazon ECS service that has public IP
addresses assigned to its tasks. Look for the `assignPublicIp`
setting with a value of `ENABLED` in the service configuration.

###### Update task definitions

Create a new revision of your task definition that disables public IP
addresses. Then update your Amazon ECS service to use the new task definition
revision.

###### Implement private network access patterns

For instances that are running web applications, consider using a Load
Balancer (LB). LBs can be configured to allow your instances to run in private
subnets while the LB runs in a public subnet and handles internet traffic.

### The Amazon ECS service uses a task definition that is configured with host networking mode enabled

Amazon ECS containers running with host networking mode share the network namespace
with the host, allowing direct access to the host's network interfaces, ports, and
routing tables. This configuration bypasses the network isolation provided by
containers, potentially exposing services running on the container directly to
external networks and allowing containers to modify host network settings. Following
standard security principles, AWS recommends maintaining proper network isolation
for containers.

###### Disable host networking mode

In the exposure finding, identify the task definition with host networking
mode. Open the task definition in the Amazon ECS console. Look for the networkMode
setting with a value of host in the task definition.

Consider the following options to disable host networking mode:

- The `awsvpc` network mode provides the strongest level of network isolation by giving each task its own elastic network interface.
- The `bridge` network mode provides isolation while allowing port mappings to expose specific container ports to the host.

###### Update task definitions

Create a new revision of your task definition with the updated network mode
configuration. Then update your Amazon ECS service to use the new task definition
revision.

### The IAM role associated with the Amazon ECS service has an administrative access policy

IAM roles with administrative access policies attached to Amazon ECS tasks provide
broad permissions that exceed what is typically required for container operation.
This configuration increases the risk that a compromised container could be used to
access or modify resources throughout your AWS environment. Following standard
security principles, AWS recommends implementing least privilege access by
granting only the permissions required for a task to function.

###### Review and identify administrative policies

In the **Resource ID**, identify the IAM role name. Go to the
IAM dashboard and select the identified role. Review the permissions policy
attached to the IAM role. If the policy is an AWS managed policy, look for
`AdministratorAccess`. Otherwise, in the policy document, look
for statements that have the statements `"Effect": "Allow", "Action": "*",
 and "Resource": "*"` together.

###### Implement least privilege access

Replace administrative policies with those that grant only the specific
permissions required for the instance to function.

To identify unnecessary permissions, you can use IAM Access Analyzer to understand how
to modify your policy based on access history.

Alternatively, you can create a new IAM role to avoid impacting other
applications that are using the existing role. In this scenario, create a new
IAM role, then associate the new IAM role with the instance.

###### Secure configuration considerations

If service-level administrative permissions are necessary for the instance,
consider implementing these additional security controls to mitigate risk:

- MFA adds an additional security layer by requiring an additional form of authentication.
  This helps prevent unauthorized access even if credentials are compromised.
- Setting up condition elements allow you to restrict when and how administrative permissions can be used based on factors like source IP or MFA age.

###### Update task definitions

Create a new revision of your task definition that references the new or
updated IAM roles. Then update your Amazon ECS service to use the new task
definition revision.

### The IAM Role associated with the ECS service has a Service Admin Policy

Service admin policies provide Amazon ECS tasks and services with permissions to perform all actions within specific AWS services.
These policies typically include permissions that are required for Amazon ECS task functionality.
Providing an IAM role with a service admin policy for Amazon ECS tasks, instead of the minimum set of permissions needed, can increase the scope of an attack if a container is compromised.
Following standard security principles, AWS recommends that you grant least privileges, which means granting only the permissions required to perform a task.

###### Review and identify administrative policies

In the **Resource ID**, identify the Amazon ECS task role and execution role names.
Go to the [IAM dashboard](https://console.aws.amazon.com/iam/home/#roles "https://console.aws.amazon.com/iam/home/#roles") and select the identified roles.
Review the permissions policies attached to these IAM roles.
Look for policy statements that grant full access to services (e.g., `"s3": "*", "ecr": "*"`).
For instructions on editing IAM policies, see [Edit IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-policy-details "../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-policy-details") in the _IAM User Guide_.

###### Implement least privilege access

Replace service admin policies with those that grant only the specific permissions required for Amazon ECS tasks to function.
To identify unnecessary permissions, you can use IAM Access Analyzer to understand how to modify your policy based on access history.
Alternatively, you can create a new IAM role to avoid impacting other applications that are using the existing role.
In this scenario, create a new IAM role, then associate the new IAM role with the instance.

###### Secure configuration considerations

If service-level administrative permissions are necessary for Amazon ECS tasks, consider implementing these additional security controls:

- **IAM conditions** –
  Set up condition elements to restrict when and how administrative permissions can be used based on factors like VPC endpoints or specific Amazon ECS clusters.
  For more information, see [Use conditions in IAM policies to further restrict access](../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions "../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions") in the _IAM User Guide_.
- **Permission boundaries** –
  Establish maximum permissions a role can have, providing guardrails for roles with administrative access.
  For more information, see [Use permissions boundaries to delegate permissions management within an account](../../../IAM/latest/UserGuide/best-practices.md#bp-permissions-boundaries "../../../IAM/latest/UserGuide/best-practices.md#bp-permissions-boundaries") in the _IAM User Guide_.

###### Update task definitions

Create a new revision of your task definition that references the new or updated IAM roles.
Then update your Amazon ECS service to use the new task definition revision.

## Vulnerability traits for Amazon ECS services

Here are vulnerability traits for Amazon ECS and suggested remediation steps.

### The Amazon ECS service has a container with network-exploitable software vulnerabilities with a high likelihood of exploitation

1. **Understand the exposure**

Package vulnerability findings identify software packages in your AWS
environment that are exposed to Common Vulnerabilities and Exposures (CVEs).
Attackers can exploit these unpatched vulnerabilities to compromise the
confidentiality, integrity, or availability of data, or to access other
systems. ECR container images can have package vulnerability
findings. 2. **Remediate the exposure**

    1. **Update package version**


    Review the package vulnerability finding for your ECR
     container image. Update the package version as suggested by
     Amazon Inspector. For more information, see [Viewing details for your Amazon Inspector findings](../../../inspector/latest/user/findings-understanding-details.md "../../../inspector/latest/user/findings-understanding-details.md") in the
     *Amazon Inspector User Guide*. The
     **Remediation** section of the finding details
     in the Amazon Inspector console tells you which commands you can run to update
     the package.
    2. **Update base container images**


    Rebuild and update base container images regularly to keep your
     containers up to date. When rebuilding an image, don't include
     unnecessary components to reduce the attack surface. For
     instructions on rebuilding a container image, see [Rebuild your images often](https://docs.docker.com/build/building/best-practices/#rebuild-your-images-often "https://docs.docker.com/build/building/best-practices/#rebuild-your-images-often").

### The Amazon ECS service has a container with software vulnerabilities

Software packages that are installed on Amazon ECS containers can be exposed to Common
Vulnerabilities and Exposures (CVEs). Low priority vulnerabilities represent
security weaknesses with lower severity or exploitability compared to high priority
vulnerabilities. While these vulnerabilities pose less immediate risk, attackers can
still exploit these unpatched vulnerabilities to compromise the confidentiality,
integrity, or availability of data, or to access other systems.

###### Update affected container images

Review the **References** section in the
**Vulnerability** tab of the trait. Vendor documentation
may include specific remediation guidance.

Apply the appropriate remediation by following these general guidelines:

- Update your container images to use patched versions of the affected packages.
- Update the affected dependencies in your application to their latest secure versions.

After updating your container image, push it to your container registry and update
your Amazon ECS task definition to use the new image.

###### Future considerations

To further strengthen the security posture of your container images, consider
following Amazon ECS task and container security best
practices. Amazon Inspector can be configured to
automatically scan for CVEs on your containers.

Amazon Inspector can also be integrated with Security Hub for automatic remediations.

Consider implementing a regular patching schedule using Systems Manager Maintenance
Windows to minimize disruption to your containers.

### The Amazon ECS service has a container with an End-Of-Life operating system

The Amazon ECS container relies on an end-of-life operating system that is no longer supported or maintained by the original developer.
This exposes the container to security vulnerabilities and potential attacks.
When operating systems reach end-of-life, vendors typically stop releasing new security advisories.
Existing security advisories may also be removed from vendor feeds.
As a result, Amazon Inspector could potentially stop generating findings for known CVEs, creating further gaps in security coverage.

See [Discontinued operating systems](../../../inspector/latest/user/supported.md#formerly-supported-os "../../../inspector/latest/user/supported.md#formerly-supported-os") in the _Amazon Inspector User Guide_ for information about operating systems that have reached end of life that can be detected by Amazon Inspector.

###### Update to a supported operating system version

We recommend updating to a supported version of the operating system.
In the exposure finding, open the resource to access the affected resource.
Before updating the operating system version in your container image, review available versions in [Supported Operating Systems](../../../inspector/latest/user/supported.md#supported-os "../../../inspector/latest/user/supported.md#supported-os") in the _Amazon Inspector User Guide_ for a list of currently supported OS versions.
After updating your container image, push it to your container registry and update your Amazon ECS task definition to use the new image.

## The Amazon ECS service has a container with malicious software packages

Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious packages pose an active and critical threat to your Amazon ECS container images, as attackers can execute malicious code automatically without exploiting a vulnerability.
Following security best practices, AWS recommends removing malicious packages to protect your containers from potential attacks.

###### Remove malicious packages

Review the malicious package details in the **References** section of the **Vulnerability** tab of the trait to understand the threat.
Remove the identified malicious packages from your container images then rebuild them.
For more information, see [ContainerDependency](../../../AmazonECS/latest/APIReference/API_ContainerDependency.md "../../../AmazonECS/latest/APIReference/API_ContainerDependency.md") in the _AWS Amazon ECS API Reference_.
After updating your container image, push it to your container registry and update your Amazon ECS task definition to use the new image.
For more information, see [Updating an Amazon ECS task definition using the console](../../../AmazonECS/latest/developerguide/update-task-definition-console-v2.md "../../../AmazonECS/latest/developerguide/update-task-definition-console-v2.md") in the _AWS Amazon ECS Developer Guide_.
