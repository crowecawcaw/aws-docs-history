# Remediating exposures for EC2 instances

AWS Security Hub can generate exposure findings for Amazon Elastic Compute Cloud (EC2) instances.

On the Security Hub console, the EC2 instance involved in an exposure finding and its identifying information are listed in
the **Resources** section of the finding details. Programmatically, you can retrieve resource
details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub CSPM API.

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

- [Misconfiguration traits for EC2 instances](exposure-ec2-instance.md#misconfiguration "exposure-ec2-instance.md#misconfiguration")

  - [The EC2 instance allows access to IMDS using version 1](exposure-ec2-instance.md#metadata-misconfiguration "exposure-ec2-instance.md#metadata-misconfiguration")
  - [The Amazon EC2 instance has a security group or network ACL that allows SSH or RDP access](exposure-ec2-instance.md#remote-access-allowed "exposure-ec2-instance.md#remote-access-allowed")
  - [The Amazon EC2 instance has an open security group](exposure-ec2-instance.md#open-security-group "exposure-ec2-instance.md#open-security-group")

- [Reachability traits for EC2 instances](exposure-ec2-instance.md#reachability "exposure-ec2-instance.md#reachability")

  - [The EC2 instance is reachable over the internet](exposure-ec2-instance.md#internet-reachable "exposure-ec2-instance.md#internet-reachable")

- [Vulnerability traits for EC2 instances](exposure-ec2-instance.md#vulnerability "exposure-ec2-instance.md#vulnerability")

  - [EC2 instance has network-exploitable software vulnerabilities with a high likelihood of exploitation](exposure-ec2-instance.md#high-priority-vulnerability "exposure-ec2-instance.md#high-priority-vulnerability")
  - [The Amazon EC2 instance has software vulnerabilities](exposure-ec2-instance.md#low-priority-vulnerability "exposure-ec2-instance.md#low-priority-vulnerability")
  - [The EC2 instance has an End-Of-Life operating system](exposure-ec2-instance.md#end-of-life-operating-system-detected "exposure-ec2-instance.md#end-of-life-operating-system-detected")
  - [The EC2 instance has malicious software packages](exposure-ec2-instance.md#malicious-package "exposure-ec2-instance.md#malicious-package")
  - [The EC2 instance has malicious files](exposure-ec2-instance.md#malicious-file "exposure-ec2-instance.md#malicious-file")

- [Impact traits for EC2 instances](exposure-ec2-instance.md#ec2-impact "exposure-ec2-instance.md#ec2-impact")

  - [Full control privileged executor](exposure-ec2-instance.md#full-control-privileged-executor "exposure-ec2-instance.md#full-control-privileged-executor")
  - [Direct policy escalation](exposure-ec2-instance.md#direct-policy-escalation "exposure-ec2-instance.md#direct-policy-escalation")
  - [Trust policy hijack](exposure-ec2-instance.md#trust-policy-hijack "exposure-ec2-instance.md#trust-policy-hijack")
  - [Data ransomware](exposure-ec2-instance.md#data-ransomware "exposure-ec2-instance.md#data-ransomware")
  - [Remove restriction](exposure-ec2-instance.md#remove-restriction "exposure-ec2-instance.md#remove-restriction")
  - [Pass role create executor](exposure-ec2-instance.md#pass-role-create-executor "exposure-ec2-instance.md#pass-role-create-executor")
  - [Swap role existing executor](exposure-ec2-instance.md#swap-role-existing-executor "exposure-ec2-instance.md#swap-role-existing-executor")
  - [Role chain escalation](exposure-ec2-instance.md#role-chain-escalation "exposure-ec2-instance.md#role-chain-escalation")
  - [Inject code privileged executor](exposure-ec2-instance.md#inject-code-privileged-executor "exposure-ec2-instance.md#inject-code-privileged-executor")
  - [Disable audit trail](exposure-ec2-instance.md#disable-audit-trail "exposure-ec2-instance.md#disable-audit-trail")
  - [Access existing executor](exposure-ec2-instance.md#access-existing-executor "exposure-ec2-instance.md#access-existing-executor")
  - [Credential minting](exposure-ec2-instance.md#credential-minting "exposure-ec2-instance.md#credential-minting")
  - [Pass role data access](exposure-ec2-instance.md#pass-role-data-access "exposure-ec2-instance.md#pass-role-data-access")
  - [Pass role task hijack](exposure-ec2-instance.md#pass-role-task-hijack "exposure-ec2-instance.md#pass-role-task-hijack")
  - [Single hop data access](exposure-ec2-instance.md#single-hop-data-access "exposure-ec2-instance.md#single-hop-data-access")
  - [Capability advancing](exposure-ec2-instance.md#capability-advancing "exposure-ec2-instance.md#capability-advancing")

## Misconfiguration traits for EC2 instances

Here are misconfiguration traits for EC2 instances and suggested remediation steps.

### The EC2 instance allows access to IMDS using version 1

Instance metadata is data about your Amazon EC2 instance that applications can use to configure or manage the running instance.
The instance metadata service (IMDS) is an on-instance component that code on the instance uses to securely access instance metadata.
If IMDS is not properly secured, it can become a potential attack vector, as it provides access to temporary credentials and other sensitive configuration data.
IMDSv2 provides stronger protection against exploitation through session-oriented authentication, requiring a session token for metadata requests and limiting session duration.
Following standard security principles, AWS recommends that you configure Amazon EC2 instances to use IMDSv2 and disable IMDSv1.

###### Test application compatibility

Before implementing IMDSv2, test your instance to ensure its compatibility with IMDSv2.
Some applications or scripts may require IMDSv1 for core functionality and require additional configuration.
For more information about tools and recommended paths for testing application compatibility, [Transition to using Instance Metadata Service Version 2](../../../AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.md "../../../AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.md") in the _Amazon Elastic Compute Cloud User Guide_.

###### Update instance to use IMDSv2

Modify existing instances to use IMDSv2.
For more information, see [Modify instance metadata options for existing instances](../../../AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.md "../../../AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.md") in the _Amazon Elastic Compute Cloud User Guide_.

###### Apply updates to instances in an Auto Scaling group

If your instance is part of an Auto Scaling group, update your launch template or launch configuration with a new configuration, and perform an instance refresh.

### The Amazon EC2 instance has a security group or network ACL that allows SSH or RDP access

Remote access protocols like SSH and RDP allow users to connect to and manage Amazon EC2 instances from external locations.
When security groups permit unrestricted access to these protocols from the internet, they increase the attack surface of your Amazon EC2 instances by allowing internet access to your instance.
Following standard security principles, AWS recommends you limit remote access to specific, trusted IP addresses or ranges.

1. **Modify security group rules**

Restrict access to your Amazon EC2 instances to specific trusted IP addresses.
Limit SSH and RDP access to specific trusted IP addresses, or use CIDR notation to specify IP ranges (e.g., 198.168.1.0/24).
To modify security group rules, see [Configure security group rules](../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules "../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules") in the _Amazon Elastic Compute Cloud User Guide_.

### The Amazon EC2 instance has an open security group

Security groups act as virtual firewalls for your Amazon EC2 instances to control inbound and outbound traffic.
Open security groups, which allow unrestricted access from any IP address, may expose your instances to unauthorized access.
Following standard security principles, AWS recommends restricting security group access to specific IP addresses and ports.

###### Review security group rules and assess current configuration

Evaluate which ports are open and accessible from broad IP ranges, such as `(0.0.0.0/0 or ::/0)`.
For instructions on viewing security group details, see [DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md") in the _Porting Assistant for .NET API Reference_.

###### Modify security group rules

Modify your security group rules to restrict access to specific trusted IP addresses or ranges.
When updating your security group rules, consider separating access requirements for different network segments by creating rules for each required source IP range or restricting access to specific ports.
To modify security group rules, see [Configure security group rules](../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules "../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules") in the _Amazon EC2 User Guide_.

## Reachability traits for EC2 instances

Here are reachability traits for EC2 instances and suggested remediation steps.

### The EC2 instance is reachable over the internet

Amazon EC2 instances with ports that are reachable from the internet may expose your instance. Reachability can occur through an internet gateway (including instances behind Application Load Balancers or Classic Load Balancers), a VPC peering connection, or a VPN virtual gateway.
Following standard security principles, we recommend implementing least-privilege network access controls by restricting inbound traffic to only necessary sources and ports.

###### Modify or remove security group rules

In the **Resources** tab, open the resource for the Amazon EC2 Security Group.
Review whether internet access is required for the instance to function.
Modify or remove inbound security group rules that allow unrestricted access (`0.0.0.0/0` or `::/0`). Implement more restrictive rules based on specific IP ranges or security groups.
If limited public access is necessary, restrict access to specific ports and protocols required for the instance's function.
For instructions on managing security group rules, see [Configure security group rules](../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules "../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules") in the _Amazon EC2 User Guide_.

###### Update network ACLs

Review and modify network access control lists (ACLs) associated with the instance's subnet.
Verify that the ACL settings align with the security group changes and don't unintentionally allow public access.
For instructions on modifying network ACLs, see [Work with network ACLs](../../../vpc/latest/userguide/nacl-tasks.md "../../../vpc/latest/userguide/nacl-tasks.md") in the _Amazon VPC User Guide_.

###### Alternative access methods

Consider the following options for alternative access methods:

- **Use NAT Gateway for outbound internet connectivity** –
  For instances in private subnets that require access to the internet (e.g., to download updates), consider using a NAT Gateway instead of assigning a public IP address.
  A NAT Gateway allows instances in private subnets to initiate outbound connections to the internet while preventing inbound connections from the internet.
- **Use Systems Manager Session Manager** –
  Session Manager provides secure shell access to your Amazon EC2 instances without the need for inbound ports, managing SSH keys, or maintaining bastion hosts.
- **Use WAF and Elastic Load Balancing or Application Load Balancer** –
  For instances that are running web applications, consider using an LB combined with AWS Web Application Firewall (WAF).
  LBs can be configured to allow your instances to run in private subnets while the LB runs in a public subnet and handles internet traffic.
  Adding a WAF to your load balancer provides additional protection against web exploits and bots.

## Vulnerability traits for EC2 instances

Here are vulnerability traits for EC2 instances and suggested remediation steps.

### EC2 instance has network-exploitable software vulnerabilities with a high likelihood of exploitation

Software packages that are installed on EC2 instances can be exposed to Common Vulnerabilities and Exposures (CVEs).
Critical CVEs pose significant security risks to your AWS environment.
Unauthorized principals can exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Critical vulnerabilities with high exploitation likelihood represent immediate security threats, as exploit code may already be publicly available and actively used by attackers or automated scanning tools.
We recommend patching these vulnerabilities to protect your instance.

###### Update affected instances

Review the **References** section in the **Vulnerability** tab of the trait.
Vendor documentation may include specific remediation guidance.
Follow the appropriate remediation using these general guidelines:

Use Systems Manager Patch Manager to apply patches for both operating systems and applications.
Patch Manager helps you select and deploy operating system and software patches automatically on large groups of instances.
If you don't have Patch Manager configured, manually update the operating system on each affected instance.

Update the affected applications to their latest secure versions following the vendor’s recommended procedures.
To manage application updates across multiple instances, consider using Systems Manager State Manager to keep your software in a consistent state.
If updates aren't available, consider removing or disabling the vulnerable application until a patch is released or other mitigations, such as restricting network access to the application or disabling vulnerable features.

Follow the specific remediation advice provided in the Amazon Inspector finding.
This could involve changing security group rules, modifying instance configurations, or adjusting application settings.

Check if the instance is part of Auto Scaling Group.
AMI-replacement patching is done on immutable infrastructures by updating the AMI ID that is configured to deploy new Amazon EC2 instances in an Auto Scaling group.
If you are using a custom/golden AMI, create an instance with the new AMI, and then customize the instance and create a new golden AMI
For more information, see [AMI updates patching (using patched AMIs for Auto Scaling groups)](../../../managedservices/latest/userguide/patching-method-immutable.md "../../../managedservices/latest/userguide/patching-method-immutable.md").

###### Future considerations

To prevent future occurrences, consider implementing a vulnerability management program.
Amazon Inspector can be configured to automatically scan for CVEs on your instances.
Amazon Inspector can also be integrated with Security Hub for automatic remediations.
Consider implementing a regular patching schedule using Systems Manager Maintenance Windows to minimize disruption to your instances.

### The Amazon EC2 instance has software vulnerabilities

Software packages that are installed on Amazon EC2 instances can be exposed to Common Vulnerabilities and Exposures (CVEs).
Noncritical CVEs represent security weaknesses with lower severity or exploitability compared to critical CVEs.
While these vulnerabilities pose less immediate risk, attackers can still exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Following security best practices, AWS recommends patching these vulnerabilities to protect your instance from attack.

###### Update affected instances

Use AWS Systems Manager Patch Manager to apply patches for operating systems.
Patch Manager helps you select and deploy operating system and software patches automatically on large groups of instances.
If you don't have Patch Manager configured, manually update the operating system on each affected instance.

Update the affected applications to their latest secure versions following the vendor’s recommended procedures.
To manage application updates across multiple instances, consider using AWS Systems Manager State Manager to keep your software in a consistent state.
If updates aren't available, consider removing or disabling the vulnerable application until a patch is released or other mitigations, such as restricting network access to the application or disabling vulnerable features.

Follow the specific remediation advice provided in the Amazon Inspector finding.
This could involve changing security group rules, modifying instance configurations, or adjusting application setting.

Check if the instance is part of Auto Scaling Group.
AMI-replacement patching is done on immutable infrastructures by updating the AMI ID that is configured to deploy new Amazon EC2 instances in an Auto Scaling group.
If you are using a custom/golden AMI, create an instance with the new AMI, and then customize the instance and create a new golden AMI
For more information, see [AMI updates patching (using patched AMIs for Auto Scaling groups)](../../../managedservices/latest/userguide/patching-method-immutable.md "../../../managedservices/latest/userguide/patching-method-immutable.md").

###### Future considerations

To prevent future occurrences, consider implementing a vulnerability management program.
Amazon Inspector can be configured to automatically scan for CVEs on your instances.
Amazon Inspector can also be integrated with Security Hub for automatic remediations.
Consider implementing a regular patching schedule using Systems Manager Maintenance Windows to minimize disruption to your instances.

### The EC2 instance has an End-Of-Life operating system

The EC2 instance runs an end-of-life operating system that is no longer supported or maintained by the original developer.
This exposes the instance to security vulnerabilities and potential attacks.
When operating systems reach end-of-life, vendors typically stop releasing new security advisories.
Existing security advisories may also be removed from vendor feeds.
As a result, Amazon Inspector could potentially stop generating findings for known CVEs, creating further gaps in security coverage.

See [Discontinued operating systems](../../../inspector/latest/user/supported.md#formerly-supported-os "../../../inspector/latest/user/supported.md#formerly-supported-os") in the _Amazon Inspector User Guide_ for information about operating systems that have reached end of life that can be detected by Amazon Inspector.

###### Update to a supported operating system version

We recommend updating to a supported version of the operating system.
In the exposure finding, open the resource to access the affected resource.
Before updating the operating system version on your instance, create a snapshot or AMI backup in case you need to roll back. Then, review available versions in [Supported Operating Systems](../../../inspector/latest/user/supported.md#supported-os "../../../inspector/latest/user/supported.md#supported-os") in the _Amazon Inspector User Guide_ for a list of currently supported OS versions.

### The EC2 instance has malicious software packages

Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious packages pose an active and critical threat to your instance, as attackers can execute malicious code automatically without exploiting a vulnerability.
Following security best practices, AWS recommends removing malicious packages to protect your instance from potential attacks.

###### Remove malicious packages

Review the malicious package details in the **References** section of the **Vulnerability** tab of the trait to understand the threat.
Remove the identified malicious packages using the appropriate package manager.
See [Package management tool](../../../linux/al2023/ug/package-management.md "../../../linux/al2023/ug/package-management.md") in the _Amazon Linux 2023 User Guide_ for an example.
After removing the malicious packages, consider performing a scan to ensure that all packages that may have been installed by the malicious code have been removed.
For more information, see [Starting On-demand malware scan in GuardDuty](../../../guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.md "../../../guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.md") in the .

### The EC2 instance has malicious files

Malicious files contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious files pose an active and critical threat to your instance, as attackers can execute malicious code automatically without exploiting a vulnerability.
Following security best practices, AWS recommends removing malicious files to protect your instance from potential attacks.

###### Remove malicious files

To identify the specific Amazon Elastic Block Store (Amazon EBS) volume that has malicious files, review the **Resources** section of the trait's finding details.
Once you have identified the volume with the malicious file, create a snapshot of the volume before making changes, then remove the identified malicious files.
After removing the malicious files, consider performing a scan to ensure that all files that may have been installed by the malicious file have been removed.
For more information, see [Starting On-demand malware scan in GuardDuty](../../../guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.md "../../../guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.md") in the .

## Impact traits for EC2 instances

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the
effective permissions of the AWS Identity and Access Management principal associated with the EC2 instance
to determine the downstream resources an attacker could reach if the instance
is compromised. Each impact trait identifies a specific privilege escalation pattern.
To reduce your blast radius, review the permission paths described in each trait and
remove any unnecessary privileges.

Following standard security principles, AWS recommends that you grant least
privilege — only the permissions required to perform a task. Replace broad
policies with scoped-down policies that grant only the specific actions and
resources needed. To identify unused permissions to remove, use IAM Access Analyzer to
generate recommendations based on access history. For more information, see [Findings for external
and unused access](../../../IAM/latest/UserGuide/access-analyzer-findings.md "../../../IAM/latest/UserGuide/access-analyzer-findings.md") and [Apply
least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the
_IAM User Guide_.

### Full control privileged executor

The associated principal can pass a role to and inject code into a compute resource that already has elevated permissions. This allows the principal to gain full control over the executor and perform any action that the executor's role permits.

### Direct policy escalation

The associated principal can directly modify IAM policies to grant itself additional permissions, escalating its own privileges without intermediate resources.

### Trust policy hijack

The associated principal can modify the trust policy of an IAM role to allow itself to assume that role, gaining the role's permissions.

### Data ransomware

The associated principal can encrypt or delete data in a way that could be used for ransomware, such as encrypting Amazon S3 objects with a customer-managed AWS KMS key and then modifying the key policy.

### Remove restriction

The associated principal can remove security restrictions such as permission boundaries, service control policies, or resource-based policy deny statements, expanding what other principals or the resource itself can do.

### Pass role create executor

The associated principal can create a new compute resource (such as a Lambda function or Amazon EC2 instance) and pass it a privileged role, effectively laundering its own permissions through the new resource.

### Swap role existing executor

The associated principal can change the IAM role attached to an existing compute resource, replacing it with a more privileged role to escalate access.

### Role chain escalation

The associated principal can assume a sequence of roles, where each role in the chain has progressively broader permissions, ultimately reaching a highly privileged role.

### Inject code privileged executor

The associated principal can inject code into a running compute resource that has elevated permissions, executing arbitrary operations under that resource's privileged role.

### Disable audit trail

The associated principal can disable logging or monitoring services such as CloudTrail, effectively covering its tracks during or after an escalation.

### Access existing executor

The associated principal can invoke or connect to an existing compute resource and use its attached role to perform privileged actions.

### Credential minting

The associated principal can create new long-term credentials (such as access keys or login profiles) for other principals, establishing persistent access paths that survive password rotations or session expirations.

### Pass role data access

The associated principal can create a service resource and pass it a role that has access to sensitive data, gaining indirect access to that data through the new resource.

### Pass role task hijack

The associated principal can pass a role to a scheduled or event-driven task (such as a Lambda function triggered by an event), allowing it to execute arbitrary code with that role's permissions.

### Single hop data access

The associated principal can directly access sensitive data resources (such as Amazon S3 buckets or DynamoDB tables) through its existing permissions, without needing intermediate escalation steps.

### Capability advancing

The associated principal has a privilege escalation path that advances its overall capabilities beyond what its directly assigned permissions would suggest. This is a general classification for paths that do not match a more specific pattern.
