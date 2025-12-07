# Remediating exposures for Lambda functions

AWS Security Hub can generate exposure findings for AWS Lambda (Lambda) functions.

On the Security Hub console, the Lambda function involved in an exposure finding and its identifying information are listed in
the **Resources** section of the finding details. Programmatically, you can retrieve resource
details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub API.

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
  - [Lambda function is running an unsupported runtime](exposure-lambda-function.md#function-runtimes "exposure-lambda-function.md#function-runtimes")
  - [Lambda function is deployed outside of an Amazon VPC](exposure-lambda-function.md#deployed-outside-vpc "exposure-lambda-function.md#deployed-outside-vpc")
  - [The Lambda function is able to assume an IAM role](exposure-lambda-function.md#aws-role-access-granted "exposure-lambda-function.md#aws-role-access-granted")
  - [The IAM Role associated with the Lambda function has an Administrative access policy](exposure-lambda-function.md#administrative-access-policy "exposure-lambda-function.md#administrative-access-policy")
  - [The IAM Role associated with the Lambda function has a policy with administrative access to an AWS Service](exposure-lambda-function.md#service-admin-policy "exposure-lambda-function.md#service-admin-policy")

- [Reachability traits for Lambda functions](exposure-lambda-function.md#lambda-function-reachability "exposure-lambda-function.md#lambda-function-reachability")
  - [The Lambda function can be publicly invoked](exposure-lambda-function.md#publicly-invocable "exposure-lambda-function.md#publicly-invocable")

- [Vulnerability traits for Lambda functions](exposure-lambda-function.md#lambda-function-vulnerability "exposure-lambda-function.md#lambda-function-vulnerability")
  - [The Lambda function has network-exploitable software vulnerabilities](exposure-lambda-function.md#high-priority-vulnerability "exposure-lambda-function.md#high-priority-vulnerability")
  - [The Lambda function has software vulnerabilities](exposure-lambda-function.md#low-priority-vulnerability "exposure-lambda-function.md#low-priority-vulnerability")

- [The Lambda function has malicious software packages](exposure-lambda-function.md#malicious-package "exposure-lambda-function.md#malicious-package")

## Misconfiguration traits for Lambda functions

Here are misconfiguration traits for Lambda functions and suggested remediation steps.

### Lambda function is running an unsupported runtime

Lambda allows developers to run code without provisioning or managing servers through runtimes that execute your code in a managed environment.
Lambda automatically applies patches and security updates to managed runtimes and their corresponding container base images.
When a runtime version is no longer supported, it no longer receives security updates, bug fixes, or technical support.
Functions running on deprecated runtimes can have security vulnerabilities and may eventually stop working due to issues like certificate expiration.
Additionally, unsupported runtimes may be vulnerable to newly discovered security exploits without available patches.
Following security best practices, we recommend using patched, supported runtimes for Lambda functions.

###### Upgrade function runtime

In the **Resources** tab of the exposure, open the resource with the hyperlink.
This will open the Lambda function window.
To upgrade your function to a supported runtime, configure the runtime management configuration.
You can choose to have your function automatically update to the latest runtime version, but before selecting this option, assess if automatic upgrades could impact your running applications.
For more information, see [Understanding how Lambda manages runtime version updates](../../../lambda/latest/dg/runtimes-update.md "../../../lambda/latest/dg/runtimes-update.md").

### Lambda function is deployed outside of an Amazon VPC

Lambda functions by default are deployed with access to the public internet.
This default configuration gives Lambda functions the ability to reach AWS service endpoints and external APIs, but it also exposes them to potential security risks.
Functions with internet access could be used to exfiltrate data, communicate with unauthorized servers, or become entry points for external actors if compromised.
Amazon VPC provides network isolation by restricting your Lambda functions to communicate only with resources within your defined private network.
Following standard security principles, we recommend deploying Lambda functions within a VPC to improve security through network isolation.

###### Attach function to VPC

In the exposure finding, open the resource with the hyperlink.
This will open the Lambda function window.
To secure your Lambda function by restricting its network access, attach it to a VPC that has the appropriate network controls in place.
Before attaching your function to a VPC, plan for any AWS service access it may need, as functions in private subnets without NAT gateways or VPC endpoints won't be able to reach AWS service APIs.
For information about how to attach a Lambda function to an Amazon VPC in your account, see [Attaching Lambda functions to an Amazon VPC in your AWS account](../../../lambda/latest/dg/configuration-vpc.md#configuration-vpc-attaching "../../../lambda/latest/dg/configuration-vpc.md#configuration-vpc-attaching").
Consider using VPC endpoints for service connectivity without internet access if your function requires to access AWS services from within a private subnet.
Configure a NAT Gateway if you require outbound internet connectivity from private subnets.

### The Lambda function is able to assume an IAM role

Lambda functions use IAM roles to interact with AWS services.
These roles grant permissions for the Lambda function to access AWS resources during execution.
While these roles are sometimes necessary for Lambda functions to perform their tasks, these roles should follow the principle of least privilege.
Following standard security principles, AWS recommends that you review whether the permissions attached to the role are appropriate based on the function's intended functionality.

1. **Determine if attached IAM Role is required**

Determine whether the Lambda function requires an IAM execution role to be configured.
Most Lambda functions need basic permissions to operate, such as writing logs to CloudWatch.
Review the permissions attached to the function's execution role and determine whether the IAM Role is required for the function.
For information on Lambda execution roles, see [Defining Lambda function permissions with an execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") in the _AWS Lambda Developer Guide_. 2. **Implement least privilege access**

Replace overly permissive policies with those that grant only the specific permissions required for the function to operate.
For information about security best practices for IAM roles, see [Apply least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _AWS Identity and Access Management User Guide_.
To identify unnecessary permissions, you can use the IAM Access Analyzer to understand how to modify your policy based on access history.
For more information, see [Findings for external and unused access](../../../IAM/latest/UserGuide/access-analyzer-findings.md "../../../IAM/latest/UserGuide/access-analyzer-findings.md") in the _AWS Identity and Access Management User Guide_.
Alternatively, you can create a new IAM role to avoid impacting other Lambda functions that are using the existing role.
In this scenario, create a new IAM role, then associate the new IAM role with the instance.
For instructions on replacing an IAM role for a function, see [Update a function’s execution role](../../../lambda/latest/dg/permissions-executionrole-update.md#update-execution-role "../../../lambda/latest/dg/permissions-executionrole-update.md#update-execution-role") in the _AWS Lambda Developer Guide_.

### The IAM Role associated with the Lambda function has an Administrative access policy

Administrative access policies provide Lambda functions with broad permissions to AWS services and resources.
These policies typically include permissions that are not required for functionality.
Providing an IAM identity with an administrative access policy on a Lambda function, instead of the minimum set of permissions that the execution role needs, can increase the scope of an attack if the function is compromised.
Following standard security principles, AWS recommends that you grant least privileges, which means that you grant only the permissions required to perform a task.

1. **Review and identify administrative policies**

In the exposure finding, identify the role name.
Go to the IAM dashboard and find the role with the role name identified previously.
Review the permissions policy attached to the IAM role.
If the policy is an AWS managed policy, look for `AdministratorAccess` or `IAMFullAccess`.
Otherwise, in the policy document, look for statements that have the statements `"Effect": "Allow", "Action": "*"` and `"Resource": "*"` together. 2. **Implement least privilege access**

Replace administrative policies with those that grant only the specific permissions required for the function to operate.
For more information on security best practices for IAM roles, see [Apply least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _AWS Identity and Access Management User Guide_.
To identify unnecessary permissions, you can use the IAM Access Analyzer to understand how to modify your policy based on access history.
For more information, see [Findings for external and unused access](../../../IAM/latest/UserGuide/access-analyzer-findings.md "../../../IAM/latest/UserGuide/access-analyzer-findings.md") in the _AWS Identity and Access Management User Guide_.
Alternatively, you can create a new IAM role to avoid impacting other Lambda functions using the existing role.
In this scenario, create a new IAM role.
Then associate the new role with the instance.
For information about replacing an IAM role for a function, see [Update a function’s execution role](../../../lambda/latest/dg/permissions-executionrole-update.md#update-execution-role "../../../lambda/latest/dg/permissions-executionrole-update.md#update-execution-role") in the _AWS Lambda Developer Guide_. 3. **Secure configuration considerations**

If administrative access permissions are necessary for the instance, consider implementing these additional security controls to mitigate risk:

    * **Multi-factor authentication (MFA)** –
     MFA adds an additional security layer by requiring an additional form of authentication.
     This helps prevent unauthorized access even if credentials are compromised.
     For more information, see [Require multi-factor authentication (MFA)](../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users "../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users") in the *AWS Identity and Access Management User Guide*.
    * **IAM conditions** –
     Setting up condition elements allows you to restrict when and how administrative permissions can be used based on factors like source IP or MFA age.
     For more information, see [Use conditions in IAM policies to further restrict access](../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions "../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions") in the *IAM User Guide*.
    * **Permission boundaries** –
     Permission boundaries establish the maximum permissions a role can have, providing guardrails for roles with administrative access.
     For more information, see [Use permissions boundaries to delegate permissions management within an account](../../../IAM/latest/UserGuide/best-practices.md#bp-permissions-boundaries "../../../IAM/latest/UserGuide/best-practices.md#bp-permissions-boundaries") in the *AWS Identity and Access Management User Guide*.

### The IAM Role associated with the Lambda function has a policy with administrative access to an AWS Service

Service admin policies allow Lambda functions to perform all actions within a specific AWS service.
These policies typically grant more permissions than necessary for a function's operation.
If a Lambda function with a service admin policy is compromised, an attacker could use those permissions to potentially access or modify sensitive data or services within your AWS environment.
Following standard security principles, we recommend that you grant least privileges, which means that you grant only the permissions required to perform a task.

1. **Review and identify administrative policies**

In the exposure finding, identify the role name in the ARN.
Go to the IAM dashboard, and find the role name.
Review the permissions policy attached to the role.
If the policy is an AWS managed policy, look for `AdministratorAccess` or `IAMFullAccess`.
Otherwise, in the policy document, look for statements that have the statements `"Effect": "Allow", "Action": "*"` and `"Resource": "*"` . 2. **Implement least privilege access**

Replace administrative policies with those that grant only the specific permissions required for the function to operate.
For more information, see [Apply least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _AWS Identity and Access Management User Guide_.
To identify unnecessary permissions, you can use the IAM Access Analyzer to understand how to modify your policy based on access history.
For more information, see [Findings for external and unused access](../../../IAM/latest/UserGuide/access-analyzer-findings.md "../../../IAM/latest/UserGuide/access-analyzer-findings.md") in the _AWS Identity and Access Management User Guide_.
Alternatively, you can create a new IAM role to avoid impacting other Lambda functions that are using the existing role.
In this scenario, create a new IAM role, then associate the new IAM role with the instance.
For instructions on replacing an IAM role for a function, see [Update a function’s execution role](../../../lambda/latest/dg/permissions-executionrole-update.md#update-execution-role "../../../lambda/latest/dg/permissions-executionrole-update.md#update-execution-role") in the _AWS Lambda Developer Guide_. 3. **Secure configuration considerations**

If service-level administrative permissions are necessary for the instance, consider implementing these additional security controls to mitigate risk:

    * **Multi-factor authentication (MFA)** –
     MFA adds an additional security layer by requiring an additional form of authentication.
     This helps prevent unauthorized access even if credentials are compromised.
     For more information, see [Require multi-factor authentication (MFA)](../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users "../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users") in the *AWS Identity and Access Management User Guide*.
    * **IAM conditions** –
     Setting up condition elements allows you to restrict when and how administrative permissions can be used based on factors like source IP or MFA age.
     For more information, see [Use conditions in IAM policies to further restrict access](../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions "../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions") in the *AWS Identity and Access Management User Guide*.
    * **Permissions boundaries** –
     Permission boundaries establish the maximum permissions a role can have, providing guardrails for roles with administrative access.
     For more information, see [Use permissions boundaries to delegate permissions management](../../../IAM/latest/UserGuide/best-practices.md#bp-permissions-boundaries "../../../IAM/latest/UserGuide/best-practices.md#bp-permissions-boundaries") in the *AWS Identity and Access Management User Guide*.

## Reachability traits for Lambda functions

Here are reachability traits for Lambda functions and suggested remediation steps.

### The Lambda function can be publicly invoked

Lambda resource-based policies determine who can invoke your functions.
A function with a resource policy that includes "\*" as the principal (or no principal at all) allows any authenticated AWS users to invoke it.
This creates significant risk, especially for functions that process sensitive data, modify resources, or have elevated permissions.
Unauthorized users could exploit this configuration to perform unwanted operations, potentially exposing data, manipulating resources, or abusing function capabilities.
Following security best practices, we recommend restricting Lambda function access to only authorized principals.

###### Modify the function's resource-based policy

In the **Resources** tab of the exposure, open the resource with the hyperlink.
This will open the Lambda function window.
Restrict access to your Lambda function by specifying only authorized AWS account IDs or specific IAM principals (users, roles, or services) in the resource-based policy.
You can only modify resource-based policies programmatically.

## Vulnerability traits for Lambda functions

Here are vulnerability traits for Lambda functions and suggested remediation steps.

### The Lambda function has network-exploitable software vulnerabilities

Software packages used in Lambda function code can contain Common Vulnerabilities and Exposures (CVEs) that have a high chance of being exploited.
Critical CVEs pose significant security risks to your AWS environment.
Attackers can exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Critical vulnerabilities with high exploitation likelihood represent immediate security threats, as exploit code may already be publicly available and actively used by attackers or automated scanning tools.
Following security best practices, we recommend patching these vulnerabilities to protect your function from attack.

###### Update affected functions

Review the **References** section in the **Vulnerability** tab for the trait.
Vendor documentation may include specific remediation guidance.
Update the vulnerable libraries to their latest secure versions following the vendor recommended procedures.
Typically, the remediation workflow depends on whether you deployed the Lambda package by uploading a zip file or by creating a Lambda function with a container image.
After updating the libraries, update the Lambda function code to use the fixed version.

Afterwards, deploy the updated version.

### The Lambda function has software vulnerabilities

Lambda functions often use third-party libraries and dependencies that may contain security vulnerabilities with lower severity or exploitability compared to critical CVEs.
While these non-critical vulnerabilities might not be as immediately exploitable, they still represent security weaknesses that could be chained together with other vulnerabilities to compromise your function.
Over time, new exploit techniques might also emerge that elevate the risk of these vulnerabilities.
Following standard security principles, we recommend patching these vulnerabilities to maintain a secure environment.

######

Review the **References** section in the **Vulnerability** tab for the trait.
Vendor documentation may include specific remediation guidance.
Update the vulnerable libraries to their latest secure versions following the vendor recommended procedures.
Typically, the remediation workflow depends on whether you deployed the Lambda package by uploading a zip file or by creating a Lambda function with a container image.
After updating the libraries, update the Lambda function code to use the fixed version.

Afterwards, deploy the updated version.

## The Lambda function has malicious software packages

Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious packages pose an active and critical threat to your Lambda function, as attackers can execute malicious code automatically without exploiting a vulnerability.
Following security best practices, AWS recommends removing malicious packages to protect your Lambda function from potential attacks.

###### Remove malicious packages

Review the malicious package details in the **References** section of the **Vulnerability** tab of the trait to understand the threat.
Remove the identified malicious packages from your function code and dependencies.
For functions using layers, check if the malicious packages are installed in any layers and remove them.
Update your deployment package or container image to exclude the malicious packages, then deploy the updated version.
For instructions, see [Deploying Lambda functions as .zip file archives](../../../lambda/latest/dg/configuration-function-zip.md "../../../lambda/latest/dg/configuration-function-zip.md") for .zip file archives or [Create a Lambda function using a container image](../../../lambda/latest/dg/images-create.md "../../../lambda/latest/dg/images-create.md") for container images.
