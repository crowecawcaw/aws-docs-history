# AWS managed policies

AWS Private CA includes a set of predefined AWS managed policies for AWS Private CA
administrators, users, and auditors. Understanding these policies can help you
implement [Customer managed policies](auth-CustManagedPolicies.md "auth-CustManagedPolicies.md").

Choose any of the policies listed below to see details and sample policy
code.

Grants unrestricted administrative control.

For a JSON listing of the policy details, see [AWSPrivateCAFullAccess](../../../aws-managed-policy/latest/reference/AWSPrivateCAFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPrivateCAFullAccess.md").

Grants access limited to read-only API operations.

For a JSON listing of the policy details, see [AWSPrivateCAReadOnly](../../../aws-managed-policy/latest/reference/AWSPrivateCAReadOnly.md "../../../aws-managed-policy/latest/reference/AWSPrivateCAReadOnly.md").

Grants ability to issue and revoke CA certificates. This policy has no
other administrative capabilities and no ability to issue end-entity
certificates. Permissions are mutually exclusive with the **User** policy.

For a JSON listing of the policy details, see [AWSPrivateCAPrivilegedUser](../../../aws-managed-policy/latest/reference/AWSPrivateCAPrivilegedUser.md "../../../aws-managed-policy/latest/reference/AWSPrivateCAPrivilegedUser.md").

Grant ability to issue and revoke end-entity certificates. This policy has
no administrative capabilities and no ability to issue CA certificates.
Permissions are mutually exclusive with the **PrivilegedUser** policy.

For a JSON listing of the policy details, see [AWSPrivateCAUser](../../../aws-managed-policy/latest/reference/AWSPrivateCAUser.md "../../../aws-managed-policy/latest/reference/AWSPrivateCAUser.md").

Grant access to read-only API operations and permission to generate a CA
audit report.

For a JSON listing of the policy details, see [AWSPrivateCAAuditor](../../../aws-managed-policy/latest/reference/AWSPrivateCAAuditor.md "../../../aws-managed-policy/latest/reference/AWSPrivateCAAuditor.md").

Grants essential permissions for the AWS Private CA Connector for Kubernetes.

For a JSON listing of the policy details, see [AWSPrivateCAConnectorForKubernetesPolicy](../../../aws-managed-policy/latest/reference/AWSPrivateCAConnectorForKubernetesPolicy.md "../../../aws-managed-policy/latest/reference/AWSPrivateCAConnectorForKubernetesPolicy.md").

## Updates to AWS managed policies for

AWS Private CA

In the following table, view details about updates to AWS managed policies
for AWS Private CA since the service began tracking these changes. For automatic
alerts about all changes to AWS Private CA, subscribe to the RSS feed on the [Document History](dochistory.md "dochistory.md") page.

| Managed policy changes                                                                                                                                           | Change                                                                                                                                                                                                 | Description       | Date |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- | ---- |
| New Policy: AWSPrivateCAConnectorForKubernetesPolicy                                                                                                             | New managed policy introduced for use with AWS Private CA Connector for Kubernetes.                                                                                                                    | May 19, 2025      |
| AWSPrivateCAPrivilegedUser and AWSPrivateCAUser<br>• Updated<br>policy                                                                                           | Replaced `StringLike` with `ArnLike`,<br>and `StringNotLike` with<br>`ArnNotLike`.<br>Updated template arn to include wild cards<br>`arn:aws:acm-pca:::template` to<br>`arn:aws:acm-pca:*:*:template`. | January 22, 2025  |
| New policy names:<br>• `AWSPrivateCAFullAccess`<br>• `AWSPrivateCAReadOnly`<br>• `AWSPrivateCAPrivilegedUser`<br>• `AWSPrivateCAAuditor`<br>• `AWSPrivateCAUser` | Policy name prefixes were changed from<br>`AWSCertificateManagerPrivateCA` to<br>`AWSPrivateCA`.<br>Functionality remains unchanged.                                                                   | February 13, 2023 |
