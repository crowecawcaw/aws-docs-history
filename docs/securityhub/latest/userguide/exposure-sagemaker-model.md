

# Remediating exposures for Amazon SageMaker models
<a name="exposure-sagemaker-model"></a>

AWS Security Hub can generate exposure findings for Amazon SageMaker models. A model whose artifact runs malicious code when it loads can act with the permissions of the model's execution role. Remediate these findings before you deploy or continue to serve the model.

On the Security Hub console, the model involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other AWS resources. 

**Contents**
+ [Vulnerability traits for Amazon SageMaker models](#sagemaker-model-vulnerability)
  + [The Amazon SageMaker model has a potentially malicious artifact](#malicious-model-artifact)
+ [Impact traits for Amazon SageMaker models](#sagemaker-model-impact)
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
  + [Business criticality](#business-criticality)

## Vulnerability traits for Amazon SageMaker models
<a name="sagemaker-model-vulnerability"></a>

Here are the vulnerability traits for Amazon SageMaker models and suggested remediation steps.

### The Amazon SageMaker model has a potentially malicious artifact
<a name="malicious-model-artifact"></a>

 An integrated AI security product flags the artifact that backs the Amazon SageMaker model as potentially malicious. For example, the product found a serialized callable in the model artifact that runs code when the model is loaded, outside of an approved set of runtime libraries. Security Hub reports this trait consistently, regardless of which integrated product performed the inspection. 

 When SageMaker loads the artifact to serve the model, that code runs inside the inference container with the permissions of the model's execution role. A threat actor who controls the artifact can use those permissions to read or modify the data that the role can reach. The threat actor can also take the role's credentials, tamper with predictions, or open an outbound connection to a command-and-control server. The impact traits in this finding show which downstream resources the execution role can reach. 

 Replace or delete the flagged artifact to resolve this trait. Until you do, the following security best practices reduce the risk of the artifact running. 

To identify the model artifact, do the following:

1. To open the affected model, choose the resource hyperlink in the exposure finding.

1. Note the model name, the AWS account, and the AWS Region.

1. In the model details, note the location of the model artifact in Amazon S3 (`ModelDataUrl`) and the container image.

1. Review the finding from the AI security product to determine what it detected in the artifact.

 Based on how the model is used, implement the appropriate security controls: 
+  **Stop serving the model** – If any of your endpoint configurations reference the model, update the endpoint to use a verified model, or delete the endpoint. Then delete the model so that no one can deploy it again. For instructions on deleting endpoints and resources, see [Delete endpoints and resources](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-delete-resources.html) in the *Amazon SageMaker Developer Guide*. 
+  **Quarantine and replace the artifact** – Restrict access to the artifact in Amazon S3 so that it can't be loaded again, and keep a copy for investigation. Verify where the artifact came from, then rebuild the model from trusted code and dependencies. Where your framework supports it, save model weights in a format that doesn't run code when it's loaded. 
+  **Require approval before deployment** – Register model versions in the SageMaker Model Registry, and deploy only versions with an approval status of `Approved`. For instructions on updating the approval status of a model, see [Update the approval status of a model](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-approve.html) in the *Amazon SageMaker Developer Guide*. 
+  **Enable network isolation** – Create the model with `EnableNetworkIsolation` set to `True`. With network isolation, the inference container can't make outbound network calls and doesn't receive any AWS credentials. You set network isolation when you create a model, so to enable it, create a new model and update the endpoint to use it. For instructions on enabling network isolation, see [Run training and inference containers in internet-free mode](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html) in the *Amazon SageMaker Developer Guide*. 
+  **Scope the execution role** – Grant the model's execution role only the permissions that inference requires, such as read access to the artifact and the container image. For more information, see [How to use SageMaker execution roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) in the *Amazon SageMaker Developer Guide*. 
+  **Monitor model and endpoint changes** – Review AWS CloudTrail for `CreateModel`, `CreateEndpointConfig`, and `UpdateEndpoint` calls from unexpected identities, and for writes to the Amazon S3 location of your model artifacts. For more information, see [Logging Amazon SageMaker API calls using AWS CloudTrail](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-using-cloudtrail.html) in the *Amazon SageMaker Developer Guide*. 

## Impact traits for Amazon SageMaker models
<a name="sagemaker-model-impact"></a>

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the effective permissions of the execution role associated with the SageMaker model. From these permissions, it determines the downstream resources that an attacker could reach if the model artifact runs malicious code, and the business criticality of those resources. Each impact trait identifies a specific privilege escalation pattern. To reduce your blast radius, review the permission paths described in each trait and remove any unnecessary privileges.

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

### Business criticality
<a name="business-criticality"></a>

The business criticality of the primary resource, set either by automation rules or by inference from the name and tags.