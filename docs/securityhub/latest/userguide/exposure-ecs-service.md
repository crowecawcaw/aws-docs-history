

# Remediating exposures for Amazon ECS services
<a name="exposure-ecs-service"></a>

AWS Security Hub can generate exposure findings for Amazon Elastic Container Service (Amazon ECS) services.

The Amazon ECS service involved in an exposure finding and its identifying information are listed in the **Resource** section of the finding details. You can retrieve these resource details on the Security Hub console or programmatically with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other AWS resources. 

**Contents**
+ [Misconfiguration traits for Amazon ECS services](#ecs-service-misconfiguration)
  + [The Amazon ECS service uses a task definition that allows containers to access the root file systems](#root-access-to-filesystem)
  + [The Amazon ECS service uses a task definition configured to share a host's process namespace](#exposed-namespace)
  + [The Amazon ECS service uses a task definition configured with cleartext credentials in the environment variables](#cleartext-credentials-present)
  + [The Amazon ECS service has an open security group](#open-security-group)
  + [The Amazon ECS service has public IP addresses](#public-ip-assigned)
  + [The Amazon ECS service uses a task definition that is configured with host networking mode enabled](#host-networking-mode-enabled)
+ [Reachability traits for Amazon ECS services](#ecs-service-reachability)
  + [The Amazon ECS service is reachable over the internet](#internet-reachable)
+ [Vulnerability traits for Amazon ECS services](#vulnerability)
  + [The Amazon ECS service has a container with network-exploitable software vulnerabilities with a high likelihood of exploitation](#high-priority-vulnerability)
  + [The Amazon ECS service has a container with software vulnerabilities](#low-priority-vulnerability)
  + [The Amazon ECS service has a container with an End-Of-Life operating system](#end-of-life-operating-system-detected)
  + [The Amazon ECS service has a container with malicious software packages](#malicious-package)
+ [Impact traits for Amazon ECS services](#ecs-impact)
  + [Has full control privileged executor path](#has-full-control-privileged-executor-path)
  + [Has direct policy escalation path](#has-direct-policy-escalation-path)
  + [Has trust policy hijack path](#has-trust-policy-hijack-path)
  + [Has data ransomware path](#has-data-ransomware-path)
  + [Has remove restriction path](#has-remove-restriction-path)
  + [Has pass role create executor path](#has-pass-role-create-executor-path)
  + [Has swap role existing executor path](#has-swap-role-existing-executor-path)
  + [Has role chain escalation path](#has-role-chain-escalation-path)
  + [Has inject code privileged executor path](#has-inject-code-privileged-executor-path)
  + [Has disable audit trail path](#has-disable-audit-trail-path)
  + [Has access existing executor path](#has-access-existing-executor-path)
  + [Has credential minting path](#has-credential-minting-path)
  + [Has pass role data access path](#has-pass-role-data-access-path)
  + [Has pass role task hijack path](#has-pass-role-task-hijack-path)
  + [Has single hop data access path](#has-single-hop-data-access-path)
  + [Has capability advancing path](#has-capability-advancing-path)

## Misconfiguration traits for Amazon ECS services
<a name="ecs-service-misconfiguration"></a>

Here are misconfiguration traits for Amazon ECS services and suggested remediation steps.

### The Amazon ECS service uses a task definition that allows containers to access the root file systems
<a name="root-access-to-filesystem"></a>

Amazon ECS containers with access to the host root filesystem can potentially read, modify, or execute critical files on the host system. This configuration increases the risk that a compromised container could be used to access or modify resources outside its intended scope, potentially exposing sensitive data on the host filesystem. Following standard security principles, grant least privileges, which means that you grant only the permissions required to perform a task. 

**Remediation: Review and modify containers with host filesystem access**  
 In the exposure finding, identify the task definition ARN. Open the task definition in the Amazon ECS console. Look for the volumes section in the task definition that defines host path mappings. 

 Review the task definition to determine if the host filesystem access is required for container functionality. If host filesystem access is not required, create a new task definition revision and remove any volume definitions that use host paths. If host filesystem access is required, consider configuring the container to use a read-only file system to prevent unauthorized modifications. 

### The Amazon ECS service uses a task definition configured to share a host's process namespace
<a name="exposed-namespace"></a>

Amazon ECS containers running with exposed namespaces can potentially access host system resources and other container namespaces. This configuration could allow a compromised container to escape its isolation boundary, accessing processes, network interfaces, or other resources outside of its intended scope.

A process ID (PID) namespace provides separation between processes. It prevents system processes from being visible, and allows PIDs to be reused, including PID 1. If the host PID namespace is shared with containers, containers can see all processes on the host system, reducing process-level isolation. This could lead to unauthorized access to host processes, including the ability to manipulate and terminate them. Following standard security principles, maintain proper namespace isolation for containers.

**Remediation: Update task definitions with exposed namespaces**  
Open the **Resources** tab of the exposure, identify the task definition with the exposed namespace. Open the task definition in the Amazon ECS console. Look for the pidMode settings with a value of host, which would share the process ID namespaces with the host. Remove the pidMode: host settings from your task definitions to ensure containers run with proper namespace isolation. 

### The Amazon ECS service uses a task definition configured with cleartext credentials in the environment variables
<a name="cleartext-credentials-present"></a>

Amazon ECS containers with cleartext credentials in environment variables expose sensitive authentication information that could be compromised if an attacker gains access to the task definition, container environment, or container logs. This creates a significant security risk, as leaked credentials could be used to access other AWS services or resources. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Replace cleartext credentials**  
In the exposure finding, identify the task definition with cleartext credentials. Open the task definition in the Amazon ECS console. Look for environment variables in the container definition that contain sensitive values such as AWS access keys, database passwords, or API tokens. 

 Consider the following alternatives to pass credentials: 
+ Instead of using AWS access keys, use IAM task execution roles and task roles to grant permissions to your containers. 
+ Store credentials as secrets in AWS Secrets Manager and reference them in your task definition. 

**Update task definitions**  
Create a new revision of your task definition that securely handles credentials. Then update your Amazon ECS service to use the new task definition revision. 

### The Amazon ECS service has an open security group
<a name="open-security-group"></a>

Security groups act as virtual firewalls for your Amazon ECS tasks to control inbound and outbound traffic. Open security groups, which allow unrestricted access from any IP address, may expose your containers to unauthorized access, increasing the risk of exposure to automated scanning tools and targeted attacks. Following standard security principles, restrict security group access to specific IP addresses and ports. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Review security group rules and assess current configuration**  
Open the resource for the Amazon ECS Security Group. Evaluate which ports are open and accessible from broad IP ranges, such as `(0.0.0.0/0 or ::/0)`. 

**Modify security group rules**  
Modify your security group rules to restrict access to specific trusted IP addresses or ranges. When updating your security group rules, consider separating access requirements for different network segments by creating rules for each required source IP range or restricting access to specific ports. 

**Modify security group rules**  
 Consider the following options for alternative access methods: 
+ Session Manager provides secure shell access to your Amazon EC2 instances without the need for inbound ports, managing SSH keys, or maintaining bastion hosts. 
+ NACLs provide an additional layer of security at the subnet level. Unlike security groups, NACLs are stateless and require both inbound and outbound rules to be explicitly defined. 

### The Amazon ECS service has public IP addresses
<a name="public-ip-assigned"></a>

Amazon ECS services with public IP addresses assigned to their tasks are directly accessible from the internet. While this may be necessary for services that need to be publicly available, it increases the attack surface and potential for unauthorized access. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Identify services with public IP addresses**  
In the exposure finding, identify the Amazon ECS service that has public IP addresses assigned to its tasks. Look for the `assignPublicIp` setting with a value of `ENABLED` in the service configuration. 

**Update task definitions**  
Create a new revision of your task definition that disables public IP addresses. Then update your Amazon ECS service to use the new task definition revision. 

**Implement private network access patterns**  
For instances that are running web applications, consider using a Load Balancer (LB). LBs can be configured to allow your instances to run in private subnets while the LB runs in a public subnet and handles internet traffic. 

### The Amazon ECS service uses a task definition that is configured with host networking mode enabled
<a name="host-networking-mode-enabled"></a>

Amazon ECS containers running with host networking mode share the network namespace with the host, allowing direct access to the host's network interfaces, ports, and routing tables. This configuration bypasses the network isolation provided by containers, potentially exposing services running on the container directly to external networks and allowing containers to modify host network settings. Following standard security principles, maintain proper network isolation for containers. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Disable host networking mode**  
In the exposure finding, identify the task definition with host networking mode. Open the task definition in the Amazon ECS console. Look for the networkMode setting with a value of host in the task definition. 

 Consider the following options to disable host networking mode: 
+  The `awsvpc` network mode provides the strongest level of network isolation by giving each task its own elastic network interface. 
+  The `bridge` network mode provides isolation while allowing port mappings to expose specific container ports to the host. 

**Update task definitions**  
Create a new revision of your task definition with the updated network mode configuration. Then update your Amazon ECS service to use the new task definition revision. 

## Reachability traits for Amazon ECS services
<a name="ecs-service-reachability"></a>

Here are reachability traits for Amazon ECS services and suggested remediation steps.

### The Amazon ECS service is reachable over the internet
<a name="internet-reachable"></a><a name="potentially-internet-reachable"></a>

An Amazon ECS service that runs tasks on a public subnet is directly accessible from the internet. This increases the attack surface and the risk of unauthorized access. Following standard security principles, run tasks on private subnets and allow only the internet access that your service requires. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Run tasks on a private subnet**  
To move your tasks off a public subnet, update the network configuration for your launch type: 
+ For Fargate, specify private subnets in the network configuration of your Amazon ECS service and set `assignPublicIp` to `DISABLED`. Amazon ECS hosts each task on a private subnet and routes its outbound traffic through a NAT gateway that you associate with the subnet. 
+ For EC2, launch the container instances that provide your cluster capacity on private subnets. Tasks use the private networking of the host and route outbound traffic through a NAT gateway. 

**Use a NAT gateway for outbound access**  
For tasks on a private subnet that require outbound internet access, use a NAT gateway. You can use a NAT gateway to let tasks start outbound connections to the internet and prevent inbound connections from the internet. For more information, see [Connect Amazon ECS applications to the internet](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-outbound.html) in the Amazon ECS Developer Guide. 

**Use a load balancer for inbound access**  
For services that need to accept internet traffic, run your tasks on private subnets behind a load balancer that runs on a public subnet. To add protection against web exploits and bots, associate AWS Web Application Firewall (WAF) with your load balancer. For more information, see [Use load balancing to distribute Amazon ECS service traffic](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the Amazon ECS Developer Guide. 

## Vulnerability traits for Amazon ECS services
<a name="vulnerability"></a>

Here are vulnerability traits for Amazon ECS and suggested remediation steps.

### The Amazon ECS service has a container with network-exploitable software vulnerabilities with a high likelihood of exploitation
<a name="high-priority-vulnerability"></a>

1. **Understand the exposure**

   Package vulnerability findings identify software packages in your AWS environment that are exposed to Common Vulnerabilities and Exposures (CVEs). Attackers can exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems. ECR container images can have package vulnerability findings.

1. **Remediate the exposure**

   1. **Update package version**

      Review the package vulnerability finding for your ECR container image. Update the package version as suggested by Amazon Inspector. For more information, see [Viewing details for your Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-details.html) in the *Amazon Inspector User Guide*. The **Remediation** section of the finding details in the Amazon Inspector console tells you which commands you can run to update the package.

   1. **Update base container images**

      Rebuild and update base container images regularly to keep your containers up to date. When rebuilding an image, do not include unnecessary components to reduce the attack surface. For instructions on rebuilding a container image, see [Rebuild your images often](https://docs.docker.com/build/building/best-practices/#rebuild-your-images-often).

### The Amazon ECS service has a container with software vulnerabilities
<a name="low-priority-vulnerability"></a>

Software packages that are installed on Amazon ECS containers can be exposed to Common Vulnerabilities and Exposures (CVEs). Low priority vulnerabilities represent security weaknesses with lower severity or exploitability compared to high priority vulnerabilities. Although these vulnerabilities pose less immediate risk, attackers can still exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Update affected container images**  
Review the **References** section in the **Vulnerability** tab of the trait. Vendor documentation may include specific remediation guidance. 

Apply the appropriate remediation by following these general guidelines: 
+  Update your container images to use patched versions of the affected packages. 
+  Update the affected dependencies in your application to their latest secure versions. 

After updating your container image, push it to your container registry and update your Amazon ECS task definition to use the new image. 

**Future considerations**  
To further strengthen the security posture of your container images, consider following Amazon ECS task and container security best practices. Amazon Inspector can be configured to automatically scan for CVEs on your containers. Amazon Inspector can also be integrated with Security Hub for automatic remediations. Consider implementing a regular patching schedule using Systems Manager Maintenance Windows to minimize disruption to your containers. 

### The Amazon ECS service has a container with an End-Of-Life operating system
<a name="end-of-life-operating-system-detected"></a>

 The Amazon ECS container relies on an end-of-life operating system that is no longer supported or maintained by the original developer. This exposes the container to security vulnerabilities and potential attacks. When operating systems reach end-of-life, vendors typically stop releasing new security advisories. Existing security advisories may also be removed from vendor feeds. As a result, Amazon Inspector could potentially stop generating findings for known CVEs, creating further gaps in security coverage. 

 See [Discontinued operating systems](https://docs.aws.amazon.com/inspector/latest/user/supported.html#formerly-supported-os) in the *Amazon Inspector User Guide* for information about operating systems that have reached end of life that can be detected by Amazon Inspector. 

**Remediation: Update to a supported operating system version**  
 Update to a supported version of the operating system. In the exposure finding, open the resource to access the affected resource. Before updating the operating system version in your container image, review available versions in [Supported Operating Systems](https://docs.aws.amazon.com/inspector/latest/user/supported.html#supported-os) in the *Amazon Inspector User Guide* for a list of currently supported OS versions. After updating your container image, push it to your container registry and update your Amazon ECS task definition to use the new image. 

### The Amazon ECS service has a container with malicious software packages
<a name="malicious-package"></a>

 Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data. Malicious packages pose an active and critical threat to your Amazon ECS container images, as attackers can execute malicious code automatically without exploiting a vulnerability. Following security best practices, remove malicious packages to protect your containers from potential attacks. 

**Remediation: Remove malicious packages**  
 Review the malicious package details in the **References** section of the **Vulnerability** tab of the trait to understand the threat. Remove the identified malicious packages from your container images then rebuild them. For more information, see [ContainerDependency](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDependency.html) in the *AWS Amazon ECS API Reference*. 

 After updating your container image, push it to your container registry and update your Amazon ECS task definition to use the new image. For more information, see [Updating an Amazon ECS task definition using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html) in the *AWS Amazon ECS Developer Guide*. 

## Impact traits for Amazon ECS services
<a name="ecs-impact"></a>

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the effective permissions of the AWS Identity and Access Management principal associated with the Amazon ECS service to determine the downstream resources an attacker could reach if the service is compromised. Each impact trait identifies a specific privilege escalation pattern. To reduce your blast radius, review the permission paths described in each trait and remove any unnecessary privileges.

Following standard security principles, grant least privilege by providing only the permissions required to perform a task. Replace broad policies with scoped-down policies that grant only the specific actions and resources needed. To identify unused permissions to remove, use IAM Access Analyzer to generate recommendations based on access history. For more information, see [Findings for external and unused access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) and [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *IAM User Guide*.

### Has full control privileged executor path
<a name="has-full-control-privileged-executor-path"></a>

The associated principal can pass a role to and inject code into a compute resource that already has elevated permissions. This allows the principal to gain full control over the executor and perform any action that the executor's role permits.

### Has direct policy escalation path
<a name="has-direct-policy-escalation-path"></a>

The associated principal can directly modify IAM policies to grant itself additional permissions, escalating its own privileges without intermediate resources.

### Has trust policy hijack path
<a name="has-trust-policy-hijack-path"></a>

The associated principal can modify the trust policy of an IAM role to allow itself to assume that role, gaining the role's permissions.

### Has data ransomware path
<a name="has-data-ransomware-path"></a>

The associated principal can encrypt or delete data in a way that could be used for ransomware, such as encrypting Amazon S3 objects with a customer-managed AWS KMS key and then modifying the key policy.

### Has remove restriction path
<a name="has-remove-restriction-path"></a>

The associated principal can remove security restrictions such as permission boundaries, service control policies, or resource-based policy deny statements, expanding what other principals or the resource itself can do.

### Has pass role create executor path
<a name="has-pass-role-create-executor-path"></a>

The associated principal can create a new compute resource (such as a Lambda function or Amazon EC2 instance) and pass it a privileged role, effectively laundering its own permissions through the new resource.

### Has swap role existing executor path
<a name="has-swap-role-existing-executor-path"></a>

The associated principal can change the IAM role attached to an existing compute resource, replacing it with a more privileged role to escalate access.

### Has role chain escalation path
<a name="has-role-chain-escalation-path"></a>

The associated principal can assume a sequence of roles, where each role in the chain has progressively broader permissions, ultimately reaching a highly privileged role.

### Has inject code privileged executor path
<a name="has-inject-code-privileged-executor-path"></a>

The associated principal can inject code into a running compute resource that has elevated permissions, executing arbitrary operations under that resource's privileged role.

### Has disable audit trail path
<a name="has-disable-audit-trail-path"></a>

The associated principal can disable logging or monitoring services such as CloudTrail, effectively covering its tracks during or after an escalation.

### Has access existing executor path
<a name="has-access-existing-executor-path"></a>

The associated principal can invoke or connect to an existing compute resource and use its attached role to perform privileged actions.

### Has credential minting path
<a name="has-credential-minting-path"></a>

The associated principal can create new long-term credentials (such as access keys or login profiles) for other principals, establishing persistent access paths that survive password rotations or session expirations.

### Has pass role data access path
<a name="has-pass-role-data-access-path"></a>

The associated principal can create a service resource and pass it a role that has access to sensitive data, gaining indirect access to that data through the new resource.

### Has pass role task hijack path
<a name="has-pass-role-task-hijack-path"></a>

The associated principal can pass a role to a scheduled or event-driven task (such as a Lambda function triggered by an event), allowing it to execute arbitrary code with that role's permissions.

### Has single hop data access path
<a name="has-single-hop-data-access-path"></a>

The associated principal can directly access sensitive data resources (such as Amazon S3 buckets or DynamoDB tables) through its existing permissions, without needing intermediate escalation steps.

### Has capability advancing path
<a name="has-capability-advancing-path"></a>

The associated principal has a privilege escalation path that advances its overall capabilities beyond what its directly assigned permissions would suggest. This is a general classification for paths that do not match a more specific pattern.