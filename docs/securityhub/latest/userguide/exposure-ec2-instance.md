

# Remediating exposures for EC2 instances
<a name="exposure-ec2-instance"></a>

AWS Security Hub can generate exposure findings for Amazon Elastic Compute Cloud (EC2) instances.

On the Security Hub console, the EC2 instance involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other AWS resources. 

**Contents**
+ [Misconfiguration traits for EC2 instances](#ec2-misconfiguration)
  + [The EC2 instance allows access to IMDS using version 1](#metadata-misconfiguration)
  + [The Amazon EC2 instance has a security group or network ACL that allows SSH or RDP access](#remote-access-allowed)
  + [The Amazon EC2 instance has an open security group](#open-security-group)
+ [Reachability traits for EC2 instances](#reachability)
  + [The EC2 instance is reachable over the internet](#internet-reachable)
+ [Vulnerability traits for EC2 instances](#vulnerability)
  + [EC2 instance has network-exploitable software vulnerabilities with a high likelihood of exploitation](#high-priority-vulnerability)
  + [The Amazon EC2 instance has software vulnerabilities](#low-priority-vulnerability)
  + [The EC2 instance has an End-Of-Life operating system](#end-of-life-operating-system-detected)
  + [The EC2 instance has malicious software packages](#malicious-package)
  + [The EC2 instance has malicious files](#malicious-file)
+ [Impact traits for EC2 instances](#ec2-impact)
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

## Misconfiguration traits for EC2 instances
<a name="ec2-misconfiguration"></a>

Here are misconfiguration traits for EC2 instances and suggested remediation steps.

### The EC2 instance allows access to IMDS using version 1
<a name="metadata-misconfiguration"></a>

 Instance metadata is data about your Amazon EC2 instance that applications can use to configure or manage the running instance. The instance metadata service (IMDS) is an on-instance component that code on the instance uses to securely access instance metadata. If IMDS is not properly secured, it can become a potential attack vector, as it provides access to temporary credentials and other sensitive configuration data. IMDSv2 provides stronger protection against exploitation through session-oriented authentication, requiring a session token for metadata requests and limiting session duration. Following standard security principles, configure Amazon EC2 instances to use IMDSv2 and disable IMDSv1. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Test application compatibility**  
 Before implementing IMDSv2, test your instance to ensure its compatibility with IMDSv2. Some applications or scripts may require IMDSv1 for core functionality and require additional configuration. For more information about tools and recommended paths for testing application compatibility, [Transition to using Instance Metadata Service Version 2 ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.html) in the *Amazon Elastic Compute Cloud User Guide*. 

**Update instance to use IMDSv2**  
 Modify existing instances to use IMDSv2. For more information, see [Modify instance metadata options for existing instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.html) in the *Amazon Elastic Compute Cloud User Guide*. 

**Apply updates to instances in an Auto Scaling group**  
 If your instance is part of an Auto Scaling group, update your launch template or launch configuration with a new configuration, and perform an instance refresh. 

### The Amazon EC2 instance has a security group or network ACL that allows SSH or RDP access
<a name="remote-access-allowed"></a>

 Remote access protocols like SSH and RDP allow users to connect to and manage Amazon EC2 instances from external locations. When security groups permit unrestricted access to these protocols from the internet, they increase the attack surface of your Amazon EC2 instances by allowing internet access to your instance. Following standard security principles, limit remote access to specific, trusted IP addresses or ranges. 

**Remediation: Modify security group rules**  
 Restrict access to your Amazon EC2 instances to specific trusted IP addresses. Limit SSH and RDP access to specific trusted IP addresses, or use CIDR notation to specify IP ranges (for example, 192.168.1.0/24). To modify security group rules, see [Configure security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html#add-remove-security-group-rules) in the *Amazon Elastic Compute Cloud User Guide*. 

### The Amazon EC2 instance has an open security group
<a name="open-security-group"></a>

 Security groups act as virtual firewalls for your Amazon EC2 instances to control inbound and outbound traffic. Open security groups, which allow unrestricted access from any IP address, may expose your instances to unauthorized access. Following standard security principles, restrict security group access to specific IP addresses and ports. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Review security group rules and assess current configuration**  
 Evaluate which ports are open and accessible from broad IP ranges, such as `(0.0.0.0/0 or ::/0)`. For instructions on viewing security group details, see [DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html) in the *Porting Assistant for .NET API Reference*. 

**Modify security group rules**  
 Modify your security group rules to restrict access to specific trusted IP addresses or ranges. When updating your security group rules, consider separating access requirements for different network segments by creating rules for each required source IP range or restricting access to specific ports. To modify security group rules, see [Configure security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html#add-remove-security-group-rules) in the *Amazon EC2 User Guide*. 

## Reachability traits for EC2 instances
<a name="reachability"></a>

Here are reachability traits for EC2 instances and suggested remediation steps.

### The EC2 instance is reachable over the internet
<a name="internet-reachable"></a><a name="potentially-internet-reachable"></a>

 Amazon EC2 instances with ports that are reachable from the internet may expose your instance. Reachability can occur through an internet gateway (including instances behind Application Load Balancers or Classic Load Balancers), a VPC peering connection, or a VPN virtual gateway. Following standard security principles, implement least-privilege network access controls by restricting inbound traffic to only necessary sources and ports. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Modify or remove security group rules**  
 In the **Resources** tab, open the resource for the Amazon EC2 Security Group. Review whether internet access is required for the instance to function. Modify or remove inbound security group rules that allow unrestricted access (`0.0.0.0/0` or `::/0`). Implement more restrictive rules based on specific IP ranges or security groups. If limited public access is necessary, restrict access to specific ports and protocols required for the instance's function. For instructions on managing security group rules, see [Configure security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html#add-remove-security-group-rules) in the *Amazon EC2 User Guide*. 

**Update network ACLs**  
 Review and modify network access control lists (ACLs) associated with the instance's subnet. Verify that the ACL settings align with the security group changes and do not unintentionally allow public access. For instructions on modifying network ACLs, see [Work with network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/nacl-tasks.html) in the *Amazon VPC User Guide*. 

**Alternative access methods**  
 Consider the following options for alternative access methods: 
+  **Use NAT Gateway for outbound internet connectivity** – For instances in private subnets that require access to the internet (for example, to download updates), consider using a NAT Gateway instead of assigning a public IP address. A NAT Gateway allows instances in private subnets to initiate outbound connections to the internet while preventing inbound connections from the internet. 
+  **Use Systems Manager Session Manager** – Session Manager provides secure shell access to your Amazon EC2 instances without the need for inbound ports, managing SSH keys, or maintaining bastion hosts. 
+  **Use WAF and Elastic Load Balancing or Application Load Balancer** – For instances that are running web applications, consider using an LB combined with AWS Web Application Firewall (WAF). LBs can be configured to allow your instances to run in private subnets while the LB runs in a public subnet and handles internet traffic. Adding a WAF to your load balancer provides additional protection against web exploits and bots. 

## Vulnerability traits for EC2 instances
<a name="vulnerability"></a>

Here are vulnerability traits for EC2 instances and suggested remediation steps.

### EC2 instance has network-exploitable software vulnerabilities with a high likelihood of exploitation
<a name="high-priority-vulnerability"></a>

 Software packages that are installed on EC2 instances can be exposed to Common Vulnerabilities and Exposures (CVEs). Critical CVEs pose significant security risks to your AWS environment. Unauthorized principals can exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems. Critical vulnerabilities with high exploitation likelihood represent immediate security threats, as exploit code may already be publicly available and actively used by attackers or automated scanning tools. Patch these vulnerabilities to protect your instance. 

**Remediation: Update affected instances**  
 Review the **References** section in the **Vulnerability** tab of the trait. Vendor documentation may include specific remediation guidance. Follow the appropriate remediation using these general guidelines: 

 Use Systems Manager Patch Manager to apply patches for both operating systems and applications. Patch Manager helps you select and deploy operating system and software patches automatically on large groups of instances. If you do not have Patch Manager configured, manually update the operating system on each affected instance. 

 Update the affected applications to their latest secure versions following the vendor’s recommended procedures. To manage application updates across multiple instances, consider using Systems Manager State Manager to keep your software in a consistent state. If updates are not available, consider removing or disabling the vulnerable application until a patch is released or other mitigations, such as restricting network access to the application or disabling vulnerable features. 

 Follow the specific remediation advice provided in the Amazon Inspector finding. This could involve changing security group rules, modifying instance configurations, or adjusting application settings. 

 Check if the instance is part of Auto Scaling Group. AMI-replacement patching is done on immutable infrastructures by updating the AMI ID that is configured to deploy new Amazon EC2 instances in an Auto Scaling group. If you are using a custom/golden AMI, create an instance with the new AMI, and then customize the instance and create a new golden AMI For more information, see [AMI updates patching (using patched AMIs for Auto Scaling groups)](https://docs.aws.amazon.com/managedservices/latest/userguide/patching-method-immutable.html). 

**Future considerations**  
 To prevent future occurrences, consider implementing a vulnerability management program. Amazon Inspector can be configured to automatically scan for CVEs on your instances. Amazon Inspector can also be integrated with Security Hub for automatic remediations. Consider implementing a regular patching schedule using Systems Manager Maintenance Windows to minimize disruption to your instances. 

### The Amazon EC2 instance has software vulnerabilities
<a name="low-priority-vulnerability"></a>

 Software packages that are installed on Amazon EC2 instances can be exposed to Common Vulnerabilities and Exposures (CVEs). Noncritical CVEs represent security weaknesses with lower severity or exploitability compared to critical CVEs. While these vulnerabilities pose less immediate risk, attackers can still exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems. Following security best practices, patch these vulnerabilities to protect your instance from attack. 

**Remediation: Update affected instances**  
 Use AWS Systems Manager Patch Manager to apply patches for operating systems. Patch Manager helps you select and deploy operating system and software patches automatically on large groups of instances. If you do not have Patch Manager configured, manually update the operating system on each affected instance. 

 Update the affected applications to their latest secure versions following the vendor’s recommended procedures. To manage application updates across multiple instances, consider using AWS Systems Manager State Manager to keep your software in a consistent state. If updates are not available, consider removing or disabling the vulnerable application until a patch is released or other mitigations, such as restricting network access to the application or disabling vulnerable features. 

 Follow the specific remediation advice provided in the Amazon Inspector finding. This could involve changing security group rules, modifying instance configurations, or adjusting application setting. 

 Check if the instance is part of Auto Scaling Group. AMI-replacement patching is done on immutable infrastructures by updating the AMI ID that is configured to deploy new Amazon EC2 instances in an Auto Scaling group. If you are using a custom/golden AMI, create an instance with the new AMI, and then customize the instance and create a new golden AMI For more information, see [AMI updates patching (using patched AMIs for Auto Scaling groups)](https://docs.aws.amazon.com/managedservices/latest/userguide/patching-method-immutable.html). 

**Future considerations**  
 To prevent future occurrences, consider implementing a vulnerability management program. Amazon Inspector can be configured to automatically scan for CVEs on your instances. Amazon Inspector can also be integrated with Security Hub for automatic remediations. Consider implementing a regular patching schedule using Systems Manager Maintenance Windows to minimize disruption to your instances. 

### The EC2 instance has an End-Of-Life operating system
<a name="end-of-life-operating-system-detected"></a>

 The EC2 instance runs an end-of-life operating system that is no longer supported or maintained by the original developer. This exposes the instance to security vulnerabilities and potential attacks. When operating systems reach end-of-life, vendors typically stop releasing new security advisories. Existing security advisories may also be removed from vendor feeds. As a result, Amazon Inspector could potentially stop generating findings for known CVEs, creating further gaps in security coverage. 

 See [Discontinued operating systems](https://docs.aws.amazon.com/inspector/latest/user/supported.html#formerly-supported-os) in the *Amazon Inspector User Guide* for information about operating systems that have reached end of life that can be detected by Amazon Inspector. 

**Remediation: Update to a supported operating system version**  
 Update to a supported version of the operating system. In the exposure finding, open the resource to access the affected resource. Before updating the operating system version on your instance, create a snapshot or AMI backup in case you need to roll back. Then, review available versions in [Supported Operating Systems](https://docs.aws.amazon.com/inspector/latest/user/supported.html#supported-os) in the *Amazon Inspector User Guide* for a list of currently supported OS versions. 

### The EC2 instance has malicious software packages
<a name="malicious-package"></a>

 Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data. Malicious packages pose an active and critical threat to your instance, as attackers can execute malicious code automatically without exploiting a vulnerability. Following security best practices, remove malicious packages to protect your instance from potential attacks. 

**Remediation: Remove malicious packages**  
 Review the malicious package details in the **References** section of the **Vulnerability** tab of the trait to understand the threat. Remove the identified malicious packages using the appropriate package manager. See [Package management tool](https://docs.aws.amazon.com/linux/al2023/ug/package-management.html) in the *Amazon Linux 2023 User Guide* for an example. After removing the malicious packages, consider performing a scan to ensure that all packages that may have been installed by the malicious code have been removed. For more information, see [Starting On-demand malware scan in GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.html) in the **. 

### The EC2 instance has malicious files
<a name="malicious-file"></a>

 Malicious files contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data. Malicious files pose an active and critical threat to your instance, as attackers can execute malicious code automatically without exploiting a vulnerability. Following security best practices, remove malicious files to protect your instance from potential attacks. 

**Remediation: Remove malicious files**  
 To identify the specific Amazon Elastic Block Store (Amazon EBS) volume that has malicious files, review the **Resources** section of the trait's finding details. After you have identified the volume with the malicious file, create a snapshot of the volume before making changes, then remove the identified malicious files. After removing the malicious files, consider performing a scan to ensure that all files that may have been installed by the malicious file have been removed. For more information, see [Starting On-demand malware scan in GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.html) in the **. 

## Impact traits for EC2 instances
<a name="ec2-impact"></a>

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the effective permissions of the AWS Identity and Access Management principal associated with the EC2 instance to determine the downstream resources an attacker could reach if the instance is compromised. Each impact trait identifies a specific privilege escalation pattern. To reduce your blast radius, review the permission paths described in each trait and remove any unnecessary privileges.

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