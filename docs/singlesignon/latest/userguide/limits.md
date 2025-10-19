# Quotas and limits in IAM Identity Center

The following tables describe quotas within IAM Identity Center. Quota increase requests must come from
 a management or delegated administrator account. To increase a quota, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html "https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html").

###### Note

We recommend using the AWS
 CLI and APIs to administer IAM Identity Center if you have more than 50,000 users, 10,000 groups, or
 500 permission sets. For more information about the CLI, see [Integrating AWS CLI with IAM Identity Center](integrating-aws-cli.md "integrating-aws-cli.md"). For more
 information about APIs, see [Welcome to
 the IAM Identity Center API Reference](../APIReference/welcome.md "../APIReference/welcome.md").


## Application quotas




| Resource | Default quota | Can be increased |
| --- | --- | --- |
| File size of service provider SAML certificates (in PEM format) | 2 KB | No |
| SAML assertion limit | 50,000 characters | No |
| File size limit of the IdP certificate uploaded to IAM Identity Center | 2500 (UTF-8) characters | No |
| Access scopes per application | 25 | No | ## AWS account quotas
| Resource | Default quota | Can be increased |
| --- | --- | --- |
| Number of permission sets allowed in IAM Identity Center | 3500 | Yes |
| Number of provisioned permission sets allowed per AWS account  | 500 | Yes |
| Number of inline policies per permission set | 1 | No |
| Number of AWS managed and customer managed policies per permission set | 201 | No |
| Maximum size of inline policy per permission set | 32,768 bytes. Maximum size of non-whitespace characters in the inline policy per permission set is 10,240 bytes. | No |
| Number of IAM roles (permission sets) in the AWS account that can be updated at a time | 1 | No | 1AWS Identity and Access Management (IAM) sets a quota of 10 managed policies per role. To take advantage of this quota, request an increase to the IAM quota *Managed policies attached to an IAM role* in the Service Quotas console for each AWS account where you want to deploy the permission set. ###### Note [Manage AWS accounts with permission sets](permissionsetsconcept.md "permissionsetsconcept.md") are provisioned in AWS accounts as IAM roles, or use existing IAM roles in AWS accounts, and therefore follow IAM quotas. For more information about quotas that are associated with IAM roles, see [IAM and STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html"). ## Active Directory quotas
| Resource | Default quota | Can be increased |
| --- | --- | --- |
| Number of connected directories that you can have at a time | 1 | No | ## IAM Identity Center identity store quotas
| Resource | Default quota | Can be increased |
| --- | --- | --- |
| Number of users supported in IAM Identity Center | 100000 | Yes |
| Number of groups supported in IAM Identity Center | 100000 | No |
| Number of unique groups that can be used to evaluate the permissions for a user | 1000 | No | ## IAM Identity Center throttle limits
| Resource | Default quota | | --- | --- |
| IAM Identity Center APIs | [IAM Identity Center APIs](../APIReference/API_Operations.md "../APIReference/API_Operations.md") have a collective throttle maximum of 20 transactions per second (TPS). You can open a support case to request an increase. The [CreateAccountAssignment](../APIReference/API_CreateAccountAssignment.md "../APIReference/API_CreateAccountAssignment.md") has a maximum rate of 15 outstanding async calls and this limit cannot be increased. | | Identity Store APIs | [Identity Store APIs](../IdentityStoreAPIReference/welcome.md "../IdentityStoreAPIReference/welcome.md") have a collective throttle maximum of 20 transactions per second (TPS). You can open a support case to request an increase. |
| SCIM APIs | [SCIM APIs](../developerguide/what-is-scim.md "../developerguide/what-is-scim.md") have a collective throttle maximum of 20 transactions per second (TPS). You can open a support case to request an increase. | ## OIDC service request quotas
| Resource | Default value (requests per second) | Can be increased |
| --- | --- | --- |
| Request rate from a remote address to register a public OAuth client Applies to: [RegisterClient](../OIDCAPIReference/API_RegisterClient.md "../OIDCAPIReference/API_RegisterClient.md")  | 20 | Yes |
| Request rate from a public client registered with the OIDC service Applies to: [CreateToken](../OIDCAPIReference/API_CreateToken.md "../OIDCAPIReference/API_CreateToken.md"), [StartDeviceAuthorization](../OIDCAPIReference/API_StartDeviceAuthorization.md "../OIDCAPIReference/API_StartDeviceAuthorization.md")  | 80 | Yes |
| Request rate from all public clients registered with the same IAM Identity Center instance Applies to: [CreateToken](../OIDCAPIReference/API_CreateToken.md "../OIDCAPIReference/API_CreateToken.md")  | 250 | Yes |
| Request rate from an IAM Identity Center application registered with the IAM Identity Center instance Applies to: [CreateTokenWithIAM](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md")  | 80 | Yes |
| Token generation rate from all IAM Identity Center applications registered with the same IAM Identity Center instance with JWT Bearer grant Applies to: [CreateTokenWithIAM](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md")  | 10 | Contact AWS Support | ## Additional quotas
| Resource | Default quota | Can be increased |
| --- | --- | --- |
| Total number of AWS accounts or applications that can be configured \* \*\* | 3000 | Yes |
| Total number of instances of IAM Identity Center per account | 1 | No |
| Total number of trusted token issuers | 10 | No | \* For example, you might configure 2750 accounts and 250 applications, resulting in a total of 3000 accounts and applications. \*\* The[`ProvisionPermissionSet`](../APIReference/API_ProvisionPermissionSet.md "../APIReference/API_ProvisionPermissionSet.md") API operation can provision a permission set using the option `ALL_PROVISIONED_ACCOUNTS` to, at most, 3500 AWS accounts. If you need to provision a permission set to more than 3500 AWS accounts, you can use the `ProvisionPermissionSet` API operation with the `AWS_ACCOUNT` option, which provisions the permission set in a single AWS account. You can make up to three concurrent calls to `ProvisionPermissionSet`.
