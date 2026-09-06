

# Remediating exposures for Amazon SageMaker notebook instances
<a name="exposure-sagemaker-notebook-instance"></a>

AWS Security Hub can generate exposure findings for Amazon SageMaker notebook instances.

On the Security Hub console, the notebook instance involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other AWS resources. 

**Contents**
+ [Misconfiguration traits for Amazon SageMaker notebook instances](#sagemaker-misconfiguration)
  + [The Amazon SageMaker notebook instance has direct internet access enabled](#outbound-internet-enabled)
  + [The Amazon SageMaker notebook instance has root access enabled](#notebook-root-access-enabled)
+ [Sensitive data traits for Amazon SageMaker notebook instances](#sensitive-data)
  + [The Amazon SageMaker notebook instance contains sensitive data](#sensitive-data-present)
+ [Impact traits for Amazon SageMaker notebook instances](#sagemaker-impact)
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

## Misconfiguration traits for Amazon SageMaker notebook instances
<a name="sagemaker-misconfiguration"></a>

Here are misconfiguration traits for Amazon SageMaker notebook instances and suggested remediation steps.

### The Amazon SageMaker notebook instance has direct internet access enabled
<a name="outbound-internet-enabled"></a>

 When `DirectInternetAccess` is enabled on an Amazon SageMaker notebook instance, outbound traffic is routed through a SageMaker-managed network address translation (NAT) gateway to the internet. This provides an egress path that can be used for data exfiltration or as a command-and-control channel if the notebook is compromised. Following security best practices, disable direct internet access and place notebook instances in a VPC with VPC endpoints for required AWS services. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Disable direct internet access**  
 The `DirectInternetAccess` setting cannot be changed after a notebook instance is created. To disable it, create a new notebook instance with `DirectInternetAccess` set to `Disabled` in a private subnet within a VPC, then migrate your notebooks and data from the existing instance. For instructions, see [Connect a notebook instance in a VPC to external resources](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-notebook-and-internet-access.html) in the *Amazon SageMaker Developer Guide*. 

**Configure VPC endpoints**  
 When direct internet access is disabled, the notebook instance requires VPC endpoints to access AWS services such as Amazon S3 and the Amazon SageMaker API. Create interface VPC endpoints for the services your notebook needs. For information on VPC endpoints, see [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) in the *AWS PrivateLink Guide*. 

### The Amazon SageMaker notebook instance has root access enabled
<a name="notebook-root-access-enabled"></a>

 When `RootAccess` is enabled on an Amazon SageMaker notebook instance, users have full OS-level root privileges. Root access allows arbitrary system modifications, persistent backdoors, and unrestricted package installation. Following security best practices, disable root access for notebook instances unless it is explicitly required for your workflow. 

**Remediation: Disable root access**  
 You cannot change the `RootAccess` setting on a running notebook instance. To disable it, stop the instance, then update the instance configuration to set `RootAccess` to `Disabled`. Most notebook workflows, including installing packages with `pip` and running lifecycle configurations, continue to work without root access. For instructions, see [Control root access to a Amazon SageMaker notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html) in the *Amazon SageMaker Developer Guide*. 

**Additional considerations**  
 If root access is required for specific tasks, consider using Amazon SageMaker Studio notebooks instead, which provide isolated container-based environments with more granular access controls. You can also use lifecycle configurations to pre-install required packages at instance creation time, reducing the need for root access during normal use. 

## Sensitive data traits for Amazon SageMaker notebook instances
<a name="sensitive-data"></a>

Here are the sensitive data traits for Amazon SageMaker notebook instances and suggested remediation steps.

### The Amazon SageMaker notebook instance contains sensitive data
<a name="sensitive-data-present"></a>

 A data security scan has confirmed that sensitive data is present on the Amazon SageMaker notebook instance. An integrated data security product sets this trait. The product inspects the notebook files, outputs, and attached storage, and identifies content that requires protection. We report this trait in Security Hub consistently, regardless of which integrated product performed the inspection. 

 Sensitive data raises the impact of every other weakness on the same notebook instance. A permissive execution role, a direct internet egress path, or overly broad access exposes regulated or confidential content. A threat actor who reaches the notebook can read and copy those records from the notebook files, output cells, and saved checkpoints. The threat actor can then retain those records outside your environment. They can also use any credentials found in the notebook to authenticate to other systems. 

 Following security best practices, we recommend restricting access to notebook instances that hold sensitive data, and encrypting the attached storage at rest. 

Sensitive data can include:
+ Credentials – such as passwords, access keys, and connection strings
+ Personally identifiable information
+ Financial information – such as account numbers and payment card data
+ Confidential content requiring protection

 Removing the sensitive data from the notebook is the only way to clear this trait. If the notebook must reference sensitive data, the following security best practices reduce the risk of exposure. 

**Review the sensitive data on the notebook instance**  
 In the exposure finding, open the resource with the hyperlink. This opens the affected notebook instance. Note the notebook instance name, the AWS account, and the AWS Region. Review the data security finding that reported the sensitive data to determine which notebook files, output cells, or checkpoints contain it. 

 Based on the type of sensitive data discovered, implement the appropriate security controls: 
+  **Remove the sensitive values from the notebook** – Delete sensitive values from the notebook code and clear the output cells that contain them. Delete any saved checkpoints and exported copies that retain the values. Where a value must remain referenced, replace it with a tokenized or masked placeholder. For more information, see [Use Amazon SageMaker notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) in the *Amazon SageMaker Developer Guide*. 
+  **Rotate any exposed credentials** – If the notebook contained credentials, treat them as compromised. Disable and rotate the credentials, then review the audit logs of the affected system for use of the exposed values. Retrieve secrets at run time from AWS Secrets Manager through a narrowly scoped execution role instead of embedding them in notebook content. For more information, see [Rotate AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. 
+  **Restrict who can open the notebook instance** – Grant access only to the IAM identities that need it. Scope the execution role to the specific actions and resources that the notebook uses. Control who can open the notebook by restricting the `sagemaker:CreatePresignedNotebookInstanceUrl` permission. For more information, see [Amazon SageMaker identity-based policy examples](https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_id-based-policy-examples.html#api-ip-filter) in the *Amazon SageMaker Developer Guide*. 
+  **Encrypt the notebook storage at rest** – Attach an AWS KMS key to the notebook instance so that the storage volume holding the notebook files and checkpoints is encrypted at rest. Use a customer managed key so that you control the key policy. Grant `kms:Decrypt` on that key only to the identities that need to read the notebook. For more information, see [Protect data at rest using encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest.html) in the *Amazon SageMaker Developer Guide*. 
+  **Monitor access to the notebook instance** – Review AWS CloudTrail for `sagemaker:CreatePresignedNotebookInstanceUrl` calls and for access from unexpected identities or sources. For more information, see [Log Amazon SageMaker API calls with AWS CloudTrail](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-using-cloudtrail.html) in the *Amazon SageMaker Developer Guide*. 

## Impact traits for Amazon SageMaker notebook instances
<a name="sagemaker-impact"></a>

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the effective permissions of the AWS Identity and Access Management principal associated with the SageMaker notebook instance to determine the downstream resources an attacker could reach if the notebook instance is compromised. Each impact trait identifies a specific privilege escalation pattern. To reduce your blast radius, review the permission paths described in each trait and remove any unnecessary privileges.

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