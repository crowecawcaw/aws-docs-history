

# AWS managed policies
<a name="auth-AwsManagedPolicies"></a>

AWS Private CA includes a set of predefined AWS managed policies for AWS Private CA administrators, users, and auditors. Understanding these policies can help you implement [Customer managed policies](auth-CustManagedPolicies.md).

Choose any of the policies listed below to see details and sample policy code.

## AWSPrivateCAFullAccess
<a name="AWSPrivateCAFullAccess"></a>

Grants unrestricted administrative control.

For a JSON listing of the policy details, see [AWSPrivateCAFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateCAFullAccess.html).

## AWSPrivateCAReadOnly
<a name="AWSPrivateCAFullAccess"></a>

Grants access limited to read-only API operations.

For a JSON listing of the policy details, see [AWSPrivateCAReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateCAReadOnly.html).

## AWSPrivateCAPrivilegedUser
<a name="AWSPrivateCAFullAccess"></a>

Grants ability to issue and revoke CA certificates. This policy has no other administrative capabilities and no ability to issue end-entity certificates. Permissions are mutually exclusive with the **User** policy. 

For a JSON listing of the policy details, see [AWSPrivateCAPrivilegedUser](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateCAPrivilegedUser.html).

## AWSPrivateCAUser
<a name="AWSPrivateCAUser"></a>

Grant ability to issue and revoke end-entity certificates. This policy has no administrative capabilities and no ability to issue CA certificates. Permissions are mutually exclusive with the **PrivilegedUser** policy.

For a JSON listing of the policy details, see [AWSPrivateCAUser](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateCAUser.html).

## AWSPrivateCAAuditor
<a name="AWSPrivateCAAuditor"></a>

Grant access to read-only API operations and permission to generate a CA audit report. 

For a JSON listing of the policy details, see [AWSPrivateCAAuditor](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateCAAuditor.html).

## AWSPrivateCAConnectorForKubernetesPolicy
<a name="AWSPrivateCAConnectorForKubernetesPolicy"></a>

Grants essential permissions for the AWS Private CA Connector for Kubernetes. 

For a JSON listing of the policy details, see [AWSPrivateCAConnectorForKubernetesPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateCAConnectorForKubernetesPolicy.html).

## Updates to AWS managed policies for AWS Private CA
<a name="managed-policy-updates"></a>

In the following table, view details about updates to AWS managed policies for AWS Private CA since the service began tracking these changes. For automatic alerts about all changes to AWS Private CA, subscribe to the RSS feed on the [Document History](dochistory.md) page.


**Managed policy changes**  

| Change | Description  | Date | 
| --- | --- | --- | 
| New Policy: AWSPrivateCAConnectorForKubernetesPolicy | New managed policy introduced for use with AWS Private CA Connector for Kubernetes. | May 19, 2025 | 
| AWSPrivateCAPrivilegedUser and AWSPrivateCAUser - Updated policy | Replaced `StringLike` with `ArnLike`, and `StringNotLike` with `ArnNotLike`.<br />Updated template arn to include wild cards `arn:aws:acm-pca:::template` to `arn:aws:acm-pca:*:*:template`. | January 22, 2025 | 
| New policy names:+  `AWSPrivateCAFullAccess` <br />+  `AWSPrivateCAReadOnly` <br />+  `AWSPrivateCAPrivilegedUser` <br />+  `AWSPrivateCAAuditor` <br />+  `AWSPrivateCAUser`  | Policy name prefixes were changed from `AWSCertificateManagerPrivateCA` to `AWSPrivateCA`.<br />Functionality remains unchanged. | February 13, 2023 | 