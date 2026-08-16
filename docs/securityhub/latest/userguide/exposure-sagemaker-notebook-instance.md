# Remediating exposures for Amazon SageMaker notebook instances

AWS Security Hub can generate exposure findings for Amazon SageMaker notebook instances.

On the Security Hub console, the notebook instance involved in an exposure finding and its identifying information are listed in
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

- [Misconfiguration traits for Amazon SageMaker notebook instances](exposure-sagemaker-notebook-instance.md#sagemaker-misconfiguration "exposure-sagemaker-notebook-instance.md#sagemaker-misconfiguration")

  - [The Amazon SageMaker notebook instance has direct internet access enabled](exposure-sagemaker-notebook-instance.md#outbound-internet-enabled "exposure-sagemaker-notebook-instance.md#outbound-internet-enabled")
  - [The Amazon SageMaker notebook instance has root access enabled](exposure-sagemaker-notebook-instance.md#notebook-root-access-enabled "exposure-sagemaker-notebook-instance.md#notebook-root-access-enabled")

- [Impact traits for Amazon SageMaker notebook instances](exposure-sagemaker-notebook-instance.md#sagemaker-impact "exposure-sagemaker-notebook-instance.md#sagemaker-impact")

  - [Full control privileged executor](exposure-sagemaker-notebook-instance.md#full-control-privileged-executor "exposure-sagemaker-notebook-instance.md#full-control-privileged-executor")
  - [Direct policy escalation](exposure-sagemaker-notebook-instance.md#direct-policy-escalation "exposure-sagemaker-notebook-instance.md#direct-policy-escalation")
  - [Trust policy hijack](exposure-sagemaker-notebook-instance.md#trust-policy-hijack "exposure-sagemaker-notebook-instance.md#trust-policy-hijack")
  - [Data ransomware](exposure-sagemaker-notebook-instance.md#data-ransomware "exposure-sagemaker-notebook-instance.md#data-ransomware")
  - [Remove restriction](exposure-sagemaker-notebook-instance.md#remove-restriction "exposure-sagemaker-notebook-instance.md#remove-restriction")
  - [Pass role create executor](exposure-sagemaker-notebook-instance.md#pass-role-create-executor "exposure-sagemaker-notebook-instance.md#pass-role-create-executor")
  - [Swap role existing executor](exposure-sagemaker-notebook-instance.md#swap-role-existing-executor "exposure-sagemaker-notebook-instance.md#swap-role-existing-executor")
  - [Role chain escalation](exposure-sagemaker-notebook-instance.md#role-chain-escalation "exposure-sagemaker-notebook-instance.md#role-chain-escalation")
  - [Inject code privileged executor](exposure-sagemaker-notebook-instance.md#inject-code-privileged-executor "exposure-sagemaker-notebook-instance.md#inject-code-privileged-executor")
  - [Disable audit trail](exposure-sagemaker-notebook-instance.md#disable-audit-trail "exposure-sagemaker-notebook-instance.md#disable-audit-trail")
  - [Access existing executor](exposure-sagemaker-notebook-instance.md#access-existing-executor "exposure-sagemaker-notebook-instance.md#access-existing-executor")
  - [Credential minting](exposure-sagemaker-notebook-instance.md#credential-minting "exposure-sagemaker-notebook-instance.md#credential-minting")
  - [Pass role data access](exposure-sagemaker-notebook-instance.md#pass-role-data-access "exposure-sagemaker-notebook-instance.md#pass-role-data-access")
  - [Pass role task hijack](exposure-sagemaker-notebook-instance.md#pass-role-task-hijack "exposure-sagemaker-notebook-instance.md#pass-role-task-hijack")
  - [Single hop data access](exposure-sagemaker-notebook-instance.md#single-hop-data-access "exposure-sagemaker-notebook-instance.md#single-hop-data-access")
  - [Capability advancing](exposure-sagemaker-notebook-instance.md#capability-advancing "exposure-sagemaker-notebook-instance.md#capability-advancing")

## Misconfiguration traits for Amazon SageMaker notebook instances

Here are misconfiguration traits for Amazon SageMaker notebook instances and suggested remediation steps.

### The Amazon SageMaker notebook instance has direct internet access enabled

When `DirectInternetAccess` is enabled on an Amazon SageMaker notebook instance, outbound traffic is routed through a SageMaker-managed network address translation (NAT) gateway to the internet.
This provides an egress path that can be used for data exfiltration or as a command-and-control channel if the notebook is compromised.
Following security best practices, disable direct internet access and place notebook instances in a VPC with VPC endpoints for required AWS services.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Disable direct internet access

The `DirectInternetAccess` setting cannot be changed after a notebook instance is created. To disable it, create a new notebook instance with `DirectInternetAccess` set to `Disabled` in a private subnet within a VPC, then migrate your notebooks and data from the existing instance.
For instructions, see [Connect a notebook instance in a VPC to external resources](../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md "../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md") in the _Amazon SageMaker Developer Guide_.

###### Configure VPC endpoints

When direct internet access is disabled, the notebook instance requires VPC endpoints to access AWS services such as Amazon S3 and the Amazon SageMaker API.
Create interface VPC endpoints for the services your notebook needs.
For information on VPC endpoints, see [What is AWS PrivateLink?](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") in the _AWS PrivateLink Guide_.

### The Amazon SageMaker notebook instance has root access enabled

When `RootAccess` is enabled on an Amazon SageMaker notebook instance, users have full OS-level root privileges.
Root access allows arbitrary system modifications, persistent backdoors, and unrestricted package installation.
Following security best practices, disable root access for notebook instances unless it is explicitly required for your workflow.

###### Remediation: Disable root access

You cannot change the `RootAccess` setting on a running notebook instance. To disable it, stop the instance, then update the instance configuration to set `RootAccess` to `Disabled`.
Most notebook workflows, including installing packages with `pip` and running lifecycle configurations, continue to work without root access.
For instructions, see [Control root access to a Amazon SageMaker notebook instance](../../../sagemaker/latest/dg/nbi-root-access.md "../../../sagemaker/latest/dg/nbi-root-access.md") in the _Amazon SageMaker Developer Guide_.

###### Additional considerations

If root access is required for specific tasks, consider using Amazon SageMaker Studio notebooks instead, which provide isolated container-based environments with more granular access controls.
You can also use lifecycle configurations to pre-install required packages at instance creation time, reducing the need for root access during normal use.

## Impact traits for Amazon SageMaker notebook instances

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the
effective permissions of the AWS Identity and Access Management principal associated with the SageMaker notebook instance
to determine the downstream resources an attacker could reach if the notebook instance
is compromised. Each impact trait identifies a specific privilege escalation pattern.
To reduce your blast radius, review the permission paths described in each trait and
remove any unnecessary privileges.

Following standard security principles, grant least
privilege by providing only the permissions required to perform a task. Replace broad
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
