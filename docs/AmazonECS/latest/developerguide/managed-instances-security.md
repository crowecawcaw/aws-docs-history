

# Security considerations for Amazon ECS Managed Instances
<a name="managed-instances-security"></a>

 Amazon ECS Managed Instances provides a fully managed container compute experience that enables you to run workloads on specific Amazon EC2 instance types while offloading security responsibilities to AWS. This topic describes the security model, features, and considerations when using Amazon ECS Managed Instances. 

For information about AWS and customer responsibilities for Amazon ECS Managed Instances security, see [Shared responsibility model for Amazon ECS Managed Instances](security-shared-model-managed-instances.md).

## Security model
<a name="managed-instances-security-model"></a>

 Amazon ECS Managed Instances implements a comprehensive security model that balances flexibility with protection: 
+ **AWS-managed infrastructure** - AWS controls the lifecycle of managed instances and handles security patching, eliminating the possibility of human error and tampering.
+ **No administrative access** - The security model is locked down and prohibits administrative access to managed instances.
+ **Multi-task placement** - By default, Amazon ECS Managed Instances places multiple tasks on a single instance to optimize cost and utilization, which relaxes the workload-isolation constraint compared to Fargate.
+ **Data isolation** - Although AWS controls instance lifecycle and task placement, AWS cannot login to managed instances or access customer data.

## Understanding managed instances
<a name="managed-instances-understanding"></a>

Amazon ECS Managed Instances provisions EC2 managed instances in your account. As the designated operator, Amazon ECS manages the full lifecycle of these instances on your behalf, including provisioning, scaling, patching, and termination. You do not have permissions to directly terminate these instances or modify instance settings. For more information, see [Amazon EC2 managed instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html).

### Identifying managed instances
<a name="managed-instances-identifying"></a>

You can identify Amazon ECS Managed Instances in your account by using the following indicators:
+ The `Operator` field in the Amazon EC2 `DescribeInstances` response, with a value of `ecs.amazonaws.com`.
+ The `aws:ec2:managed-launch` tag on the instance, with a value of `ecs-managed-instances`.

### Managed resource visibility
<a name="managed-instances-resource-visibility"></a>

Beginning April 22, 2026, Amazon EC2 hides new managed instances from your Amazon EC2 console views and API list operations by default. Visibility settings do not affect billing or resource operation, and managed instances remain fully operational and billable regardless of visibility configuration. You can adjust this behavior at any time. For more information, see [Managed resource visibility settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html#managed-resource-visibility-settings).

## Security features
<a name="managed-instances-security-features"></a>

 Amazon ECS Managed Instances includes several built-in security features designed to protect your workloads and maintain a strong security posture. These features range from automated security patching to support for privileged Linux capabilities when needed. 

### Security best practices
<a name="managed-instances-security-best-practices"></a>

 Managed instances are configured according to AWS security best practices, including: 
+ **No SSH access** - Remote shell access is disabled to prevent unauthorized access.
+ **Immutable root filesystem** - The root filesystem cannot be modified, ensuring system integrity.
+ **Kernel-level mandatory access controls** - SELinux provides additional security enforcement at the kernel level.

### Automatic security patching
<a name="managed-instances-security-patching"></a>

 Amazon ECS Managed Instances helps improve the security posture of your workloads through automated patching: 
+ **Regular security updates** - Instances are regularly updated with the latest security patches by AWS, with respect to the maintenance windows that you configure.
+ **Limited instance lifetime** - The maximum lifetime of a running instance is limited to 14 days to ensure applications run on appropriately configured instances with up-to-date security patches.
+ **Maintenance window control** - You can use Amazon EC2 event windows capability to specify when Amazon ECS should replace your instances with patched ones.

### Privileged Linux capabilities
<a name="managed-instances-privileged-capabilities"></a>

 Amazon ECS Managed Instances supports software that requires elevated Linux privileges, enabling advanced monitoring and security solutions: 
+ **Supported capabilities** - You can opt-in to all privileged Linux capabilities, including `CAP_NET_ADMIN`, `CAP_SYS_ADMIN`, `CAP_BPF`, and `CAP_PERFMON`.
+ **Popular solutions** - This enables you to run popular network monitoring and observability solutions such as Wireshark and Datadog.
+ **Explicit configuration required** - You must explicitly configure your Amazon ECS Managed Instances capacity provider to enable privileged Linux capabilities, as it may pose additional security risks to your applications.

**Important**  
 Enabling privileged Linux capabilities may expose your tasks to additional security risks. Only enable these capabilities when required by your applications and ensure you understand the security implications. 

## Compliance and regulatory support
<a name="managed-instances-compliance"></a>

 Amazon ECS Managed Instances maintains the same compliance posture as Amazon ECS: 
+ **Compliance programs** - Amazon ECS Managed Instances is in scope of the same AWS Assurance Programs as Amazon ECS, including PCI-DSS, HIPAA, and FedRAMP.
+ **FIPS endpoints** - Amazon ECS Managed Instances supports FIPS endpoint configuration at the capacity provider level. Unlike Fargate, which uses an account-level setting, Amazon ECS Managed Instances uses a per-capacity-provider setting because FIPS is a per-instance configuration. You configure FIPS when creating or updating a capacity provider.
+ **Customer Managed Keys** - It supports security features required for achieving compliance, such as Customer Managed Keys for encryption.

## Amazon ECS Managed Instances FIPS-140 Considerations
<a name="managed-instances-fips-considerations"></a>

Consider the following when using FIPS-140 compliance on Amazon ECS Managed Instances:
+ FIPS-140-compliant Managed Instances AMIs are available in the AWS GovCloud (US) Regions only.
+ Amazon ECS Managed Instances supports FIPS-140-3
+ FIPS-140 compliance is enabled by default in the AWS GovCloud (US) Regions. If you need to run workloads without FIPS compliance, turn off FIPS compliance in the Managed Instances Capacity Provider configuration.
+ The `cpuArchitecture` for your tasks must be `X86_64` for FIPS-140 compliance.

## Disable FIPS on Amazon ECS Managed Instances
<a name="managed-instances-use-fips"></a>

By default, Amazon ECS Managed Instances Capacity Providers in AWS GovCloud (US) Regions launch FIPS-compliant AMIs. You choose to disable FIPS-140 compliance when creating a new Amazon ECS Managed Instances Capacity Provider. Follow these steps to create a new Capacity Provider without FIPS compliance.

1. Disable FIPS-140 compliance on Capacity Provider.

   ```
   aws ecs create-capacity-provider \
       --cluster {{cluster-name}} \
       --name {{capacity-provider-name}} \
       --managed-instances-provider '{
           "infrastructureRoleArn": "{{infrastructure-role-arn}}",
           "instanceLaunchTemplate": {
               "ec2InstanceProfileArn": "{{instance-profile-arn}}",
               "fipsEnabled": false,
               "networkConfiguration": {
                   "subnets": ["{{subnet-id}}"],
                   "securityGroups": ["{{security-group-id}}"]
               }
           }
       }'
   ```

1. You can optionally use ECS Exec to run the following command to verify the FIPS-140 compliance status for a capacity provider.

   Replace {{cluster-name}} with the name of your cluster, {{task-id}} with the ID or ARN of your task, and {{container-name}} with the name of the container in your task you want to run the command against.

   A return value of "1" indicates that you are using FIPS.

   ```
   aws ecs execute-command \
       --cluster {{cluster-name}} \
       --task {{task-id}} \
       --container {{container-name}} \
       --interactive \
       --command "cat /proc/sys/crypto/fips_enabled"
   ```

## Security considerations
<a name="managed-instances-security-considerations"></a>

 When using Amazon ECS Managed Instances, there are several important security considerations to understand and plan for. These considerations help you make informed decisions about your workload architecture and security requirements. 

### Multi-task security model
<a name="managed-instances-multi-task-security"></a>

 The default multi-task placement model in Amazon ECS Managed Instances differs from Fargate's single-task isolation: 
+ **Shared instance resources** - Multiple tasks may run on the same instance, potentially exposing a task to vulnerabilities from other tasks running on the same instance or in the same ECS cluster.
+ **Single-task option** - You can configure Amazon ECS Managed Instances to use single-task mode for customers requiring the default Fargate security model with VM-level security isolation boundary.
+ **Cost vs. security trade-off** - Multi-task mode provides cost optimization and faster task startup times, while single-task mode provides stronger isolation.

### Handling instance interruptions
<a name="managed-instances-interruption-handling"></a>

 It's important to design your applications to tolerate interruptions when using Amazon ECS Managed Instances: 
+ **Interruption tolerance** - Use Amazon ECS Managed Instances with applications that tolerate interruption to underlying services or tasks.
+ **Service-based workloads** - Use Amazon ECS services for automatic task replacement, or run workloads with controlled and limited duration not exceeding 14 days on standalone tasks.
+ **Graceful shutdown** - Configure task shutdown grace period to control the impact of interruptions.

### Data access and privacy
<a name="managed-instances-data-access"></a>

 Amazon ECS Managed Instances maintains strict data access controls: 
+ **No customer data access** - Although AWS controls the lifecycle of managed instances and the placement of tasks on the instances, AWS cannot login to managed instances or access customer data.
+ **Metrics and logs only** - AWS captures only metrics and related logs required to provide the Amazon ECS Managed Instances capabilities.
+ **Locked-down security model** - The security model prohibits administrative access, eliminating the possibility of human error and tampering.

## Security best practices
<a name="managed-instances-security-best-practices-recommendations"></a>

 Follow these best practices when using Amazon ECS Managed Instances: 
+ **Evaluate security model** - Make a conscious decision about adopting Amazon ECS Managed Instances based on your security requirements, particularly regarding the multi-task placement model.
+ **Use single-task mode when needed** - If your workloads require stronger isolation, configure Amazon ECS Managed Instances to use single-task mode.
+ **Minimize privileged capabilities** - Only enable privileged Linux capabilities when absolutely necessary and understand the associated security risks.
+ **Plan for interruptions** - Design applications to handle instance replacements gracefully, especially considering the 14-day maximum instance lifetime.
+ **Configure maintenance windows** - Use EC2 event windows to control when instance replacements occur to minimize impact on your workloads.
+ **Monitor and audit** - Regularly review your Amazon ECS Managed Instances configuration and monitor for any security-related events or changes.