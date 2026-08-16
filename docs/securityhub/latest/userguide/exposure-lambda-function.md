# Remediating exposures for AWS Lambda functions

AWS Security Hub can generate exposure findings for AWS Lambda functions.

On the Security Hub console, the Lambda function involved in an exposure finding and its identifying information are listed in
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

- [Misconfiguration traits for Lambda functions](exposure-lambda-function.md#lambda-function-misconfiguration "exposure-lambda-function.md#lambda-function-misconfiguration")

  - [Lambda function is deployed outside of an Amazon VPC](exposure-lambda-function.md#deployed-outside-vpc "exposure-lambda-function.md#deployed-outside-vpc")
  - [The Lambda function is accessible through API Gateway without authorization](exposure-lambda-function.md#api-gateway-no-authorization "exposure-lambda-function.md#api-gateway-no-authorization")

- [Reachability traits for Lambda functions](exposure-lambda-function.md#lambda-function-reachability "exposure-lambda-function.md#lambda-function-reachability")

  - [The Lambda function can be publicly invoked](exposure-lambda-function.md#publicly-invocable "exposure-lambda-function.md#publicly-invocable")

- [Vulnerability traits for Lambda functions](exposure-lambda-function.md#lambda-function-vulnerability "exposure-lambda-function.md#lambda-function-vulnerability")

  - [The Lambda function has network-exploitable software vulnerabilities](exposure-lambda-function.md#high-priority-vulnerability "exposure-lambda-function.md#high-priority-vulnerability")
  - [The Lambda function has software vulnerabilities](exposure-lambda-function.md#low-priority-vulnerability "exposure-lambda-function.md#low-priority-vulnerability")
  - [The Lambda function has malicious software packages](exposure-lambda-function.md#malicious-package "exposure-lambda-function.md#malicious-package")
  - [The Lambda function has code vulnerabilities](exposure-lambda-function.md#code-vulnerability "exposure-lambda-function.md#code-vulnerability")

- [Impact traits for Lambda functions](exposure-lambda-function.md#lambda-impact "exposure-lambda-function.md#lambda-impact")

  - [Full control privileged executor](exposure-lambda-function.md#full-control-privileged-executor "exposure-lambda-function.md#full-control-privileged-executor")
  - [Direct policy escalation](exposure-lambda-function.md#direct-policy-escalation "exposure-lambda-function.md#direct-policy-escalation")
  - [Trust policy hijack](exposure-lambda-function.md#trust-policy-hijack "exposure-lambda-function.md#trust-policy-hijack")
  - [Data ransomware](exposure-lambda-function.md#data-ransomware "exposure-lambda-function.md#data-ransomware")
  - [Remove restriction](exposure-lambda-function.md#remove-restriction "exposure-lambda-function.md#remove-restriction")
  - [Pass role create executor](exposure-lambda-function.md#pass-role-create-executor "exposure-lambda-function.md#pass-role-create-executor")
  - [Swap role existing executor](exposure-lambda-function.md#swap-role-existing-executor "exposure-lambda-function.md#swap-role-existing-executor")
  - [Role chain escalation](exposure-lambda-function.md#role-chain-escalation "exposure-lambda-function.md#role-chain-escalation")
  - [Inject code privileged executor](exposure-lambda-function.md#inject-code-privileged-executor "exposure-lambda-function.md#inject-code-privileged-executor")
  - [Disable audit trail](exposure-lambda-function.md#disable-audit-trail "exposure-lambda-function.md#disable-audit-trail")
  - [Access existing executor](exposure-lambda-function.md#access-existing-executor "exposure-lambda-function.md#access-existing-executor")
  - [Credential minting](exposure-lambda-function.md#credential-minting "exposure-lambda-function.md#credential-minting")
  - [Pass role data access](exposure-lambda-function.md#pass-role-data-access "exposure-lambda-function.md#pass-role-data-access")
  - [Pass role task hijack](exposure-lambda-function.md#pass-role-task-hijack "exposure-lambda-function.md#pass-role-task-hijack")
  - [Single hop data access](exposure-lambda-function.md#single-hop-data-access "exposure-lambda-function.md#single-hop-data-access")
  - [Capability advancing](exposure-lambda-function.md#capability-advancing "exposure-lambda-function.md#capability-advancing")

## Misconfiguration traits for Lambda functions

Here are misconfiguration traits for Lambda functions and suggested remediation steps.

### Lambda function is deployed outside of an Amazon VPC

Lambda functions by default are deployed with access to the public internet.
This default configuration gives Lambda functions the ability to reach AWS service endpoints and external APIs, but it also exposes them to potential security risks.
Functions with internet access could be used to exfiltrate data, communicate with unauthorized servers, or become entry points for external actors if compromised.
Amazon VPC provides network isolation by restricting your Lambda functions to communicate only with resources within your defined private network.
Following standard security principles, deploy Lambda functions within a VPC to improve security through network isolation.

###### Remediation: Attach function to VPC

In the exposure finding, choose the resource link.
This opens the Lambda function in the Lambda console.
To secure your Lambda function by restricting its network access, attach it to a VPC that has the appropriate network controls in place.

Before attaching your function to a VPC, plan for any AWS service access it may need, as functions in private subnets without NAT gateways or VPC endpoints cannot reach AWS service APIs.
For information about how to attach a Lambda function to an Amazon VPC in your account, see [Attaching Lambda functions to an Amazon VPC in your AWS account](../../../lambda/latest/dg/configuration-vpc.md#configuration-vpc-attaching "../../../lambda/latest/dg/configuration-vpc.md#configuration-vpc-attaching").
Consider using VPC endpoints for service connectivity without internet access if your function requires to access AWS services from within a private subnet.
Configure a NAT Gateway if you require outbound internet connectivity from private subnets.

### The Lambda function is accessible through API Gateway without authorization

API Gateway methods without authorization allow any caller with access to the API Gateway to invoke the integrated Lambda function without identity verification.
This configuration creates security risks, as callers can invoke the Lambda function without proper authorization, potentially leading to abuse of function capabilities, resource consumption, access to sensitive data, or unauthorized operations.
While API Gateway may have network-level access controls, the lack of method-level authorization could allow free invocation of the function by any caller with network access to the API Gateway.
Following security best practices, implement appropriate authorization mechanisms for API Gateway methods that integrate with Lambda functions.

###### Remediation: Configure API Gateway authentication

In the **Resources** tab of the exposure, choose the resource link to access the API Gateway method.
Review the current authorization configuration and implement appropriate authentication mechanisms.

API Gateway supports several authentication options including AWS IAM, Amazon Cognito User Pools, Lambda authorizers, and API keys.
Choose the authentication method that best fits your security requirements and use case.
For detailed instructions on configuring authentication, see [Controlling and managing access to a REST API in API Gateway](../../../apigateway/latest/developerguide/apigateway-control-access-to-api.md "../../../apigateway/latest/developerguide/apigateway-control-access-to-api.md") in the _API Gateway Developer Guide_.

## Reachability traits for Lambda functions

Here are reachability traits for Lambda functions and suggested remediation steps.

### The Lambda function can be publicly invoked

Lambda resource-based policies determine who can invoke your functions.
A function with a resource policy that includes "\*" as the principal (or no principal at all) allows any authenticated AWS users to invoke it.
This creates significant risk, especially for functions that process sensitive data, modify resources, or have elevated permissions.
Unauthorized users could exploit this configuration to perform unwanted operations, potentially exposing data, manipulating resources, or abusing function capabilities.
Following security best practices, restrict Lambda function access to only authorized principals.

###### Remediation: Modify the function's resource-based policy

In the **Resources** tab of the exposure, open the resource with the hyperlink.
This opens the Lambda function in the Lambda console.
Restrict access to your Lambda function by specifying only authorized AWS account IDs or specific IAM principals (users, roles, or services) in the resource-based policy.
You can only modify resource-based policies programmatically.

## Vulnerability traits for Lambda functions

Here are vulnerability traits for Lambda functions and suggested remediation steps.

### The Lambda function has network-exploitable software vulnerabilities

Software packages used in Lambda function code can contain Common Vulnerabilities and Exposures (CVEs) that have a high chance of being exploited.
Critical CVEs pose significant security risks to your AWS environment.
Attackers can exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Critical vulnerabilities with high exploitation likelihood represent immediate security threats, as exploit code may already be publicly available and actively used by attackers or automated scanning tools.
Following security best practices, patch these vulnerabilities to protect your function from attack.

###### Remediation: Update affected functions

Review the **References** section in the **Vulnerability** tab for the trait.
Vendor documentation might include specific remediation guidance.
Update the vulnerable libraries to their latest secure versions following the vendor recommended procedures.

Typically, the remediation workflow depends on whether you deployed the Lambda package by uploading a zip file or by creating a Lambda function with a container image.
After updating the libraries, update the Lambda function code to use the fixed version.
Afterwards, deploy the updated version.

### The Lambda function has software vulnerabilities

Lambda functions often use third-party libraries and dependencies that may contain security vulnerabilities with lower severity or exploitability compared to critical CVEs.
While these non-critical vulnerabilities might not be as immediately exploitable, they still represent security weaknesses that could be chained together with other vulnerabilities to compromise your function.
Over time, new exploit techniques might also emerge that elevate the risk of these vulnerabilities.
Following standard security principles, patch these vulnerabilities to maintain a secure environment.

###### Remediation: Update affected functions

Review the **References** section in the **Vulnerability** tab for the trait.
Vendor documentation might include specific remediation guidance.
Update the vulnerable libraries to their latest secure versions following the vendor recommended procedures.

Typically, the remediation workflow depends on whether you deployed the Lambda package by uploading a zip file or by creating a Lambda function with a container image.
After updating the libraries, update the Lambda function code to use the fixed version.
Afterwards, deploy the updated version.

### The Lambda function has malicious software packages

Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious packages pose an active and critical threat to your Lambda function, as attackers can execute malicious code automatically without exploiting a vulnerability.
Following security best practices, remove malicious packages to protect your Lambda function from potential attacks.

###### Remediation: Remove malicious packages

Review the malicious package details in the **References** section of the **Vulnerability** tab of the trait to understand the threat.
Remove the identified malicious packages from your function code and dependencies.
For functions using layers, check if the malicious packages are installed in any layers and remove them.

Update your deployment package or container image to exclude the malicious packages, then deploy the updated version.
For instructions, see [Deploying Lambda functions as .zip file archives](../../../lambda/latest/dg/configuration-function-zip.md "../../../lambda/latest/dg/configuration-function-zip.md") for .zip file archives or [Create a Lambda function using a container image](../../../lambda/latest/dg/images-create.md "../../../lambda/latest/dg/images-create.md") for container images.

### The Lambda function has code vulnerabilities

Lambda function application code contains security vulnerabilities that could be exploited by threat actors.
Code vulnerabilities include data leaks, injection flaws, missing encryption, and weak cryptography that are identified through automated code analysis.
These vulnerabilities pose security risks to your AWS environment, as attackers can exploit them to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Code vulnerabilities represent security weaknesses that could be chained together with other attack vectors to compromise your function.
Following security best practices, address these code vulnerabilities to protect your function from attack.

###### Remediation: Update affected functions

Review the **References** section in the **Vulnerability** tab of the trait.
Amazon Inspector findings may include specific remediation guidance and code snippets showing the vulnerable code locations.
Address the identified security issues in your function code using the provided plug-and-play code blocks or by implementing secure coding practices.

Always review code remediation suggestions before adopting them, as you might need to edit them to ensure your code performs as intended.
After fixing the vulnerabilities, update the Lambda function code to use the corrected version.
For instructions, see [Updating function code](../../../lambda/latest/dg/configuration-function-zip.md#configuration-function-update "../../../lambda/latest/dg/configuration-function-zip.md#configuration-function-update") in the _AWS Lambda Developer Guide_.

Afterwards, deploy the updated version.
For instructions, see [Deploying Lambda functions as .zip file archives](../../../lambda/latest/dg/configuration-function-zip.md "../../../lambda/latest/dg/configuration-function-zip.md") for .zip file archives or [Create a Lambda function using a container image](../../../lambda/latest/dg/images-create.md "../../../lambda/latest/dg/images-create.md") for container images.
For more information about Amazon Inspector code scanning, see [Amazon Inspector Lambda code scanning](../../../inspector/latest/user/scanning_resources_lambda_code.md "../../../inspector/latest/user/scanning_resources_lambda_code.md") in the _Amazon Inspector User Guide_.

## Impact traits for Lambda functions

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the
effective permissions of the AWS Identity and Access Management principal associated with the Lambda function
to determine the downstream resources an attacker could reach if the function
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
