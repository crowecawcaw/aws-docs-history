

# Quotas and limits in IAM Identity Center
<a name="limits"></a>

The following tables describe quotas within IAM Identity Center. Quota increase requests must come from a management or delegated administrator account. To increase a quota, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).

**Note**  
We recommend using the AWS CLI and APIs to centrally administer IAM Identity Center if you have more than 50,000 users, 10,000 groups, 500 permission sets, or 3,000 applications. For more information about the CLI, see [Integrating AWS CLI with IAM Identity Center](integrating-aws-cli.md). For more information about APIs, see [Welcome to the IAM Identity Center API Reference](https://docs.aws.amazon.com/singlesignon/latest/APIReference/welcome.html).

## Application quotas
<a name="applicationlimits"></a>


| Resource | Default quota | Can be increased | 
| --- | --- | --- | 
| File size of service provider SAML certificates (in PEM format) | 2 KB | No | 
| SAML assertion limit | 50,000 characters | No | 
| File size limit of the IdP certificate uploaded to IAM Identity Center | 2500 (UTF-8) characters | No | 
| Access scopes per application | 25 | No | 

## AWS account quotas
<a name="awsaccountlimits"></a>


| Resource | Default quota | Can be increased | 
| --- | --- | --- | 
| Number of permission sets allowed in IAM Identity Center | 3500 | Yes | 
| Number of provisioned permission sets allowed per AWS account  | 500 | Yes | 
| Number of inline policies per permission set | 1 | No | 
| Number of AWS managed and customer managed policies per permission set | 251 | No | 
| Maximum size of inline policy per permission set | 32,768 bytes.<br />Maximum size of non-whitespace characters in the inline policy per permission set is 10,240 bytes. | No | 
| Number of IAM roles (permission sets) in the AWS account that can be updated at a time | 1 | No | 

1AWS Identity and Access Management (IAM) sets a quota of 10 managed policies per role. To take advantage of this quota, request an increase to the IAM quota *Managed policies attached to an IAM role* in the Service Quotas console for each AWS account where you want to deploy the permission set. 

**Note**  
[Manage AWS accounts with permission sets](permissionsetsconcept.md) are provisioned in AWS accounts as IAM roles, or use existing IAM roles in AWS accounts, and therefore follow IAM quotas. For more information about quotas that are associated with IAM roles, see [IAM and STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html). 

## Active Directory quotas
<a name="connecteddirectorylimits"></a>


| Resource | Default quota | Can be increased | 
| --- | --- | --- | 
| Number of connected directories that you can have at a time | 1 | No | 

## IAM Identity Center identity store quotas
<a name="ssodirectorylimits"></a>


| Resource | Default quota | Can be increased | 
| --- | --- | --- | 
| Number of users supported in IAM Identity Center | 200000 | Yes | 
| Number of groups supported in IAM Identity Center | 100000 | Yes | 

## IAM Identity Center throttle limits
<a name="ssothrottlelimits"></a>


| Resource | Default quota | 
| --- | --- | 
| IAM Identity Center APIs | [IAM Identity Center APIs](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Operations.html) have a collective throttle limit of 20 transactions per second (TPS). For read APIs, you can open a support case to request a limit increase. The [CreateAccountAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateAccountAssignment.html) write API has a limit of 15 outstanding asynchronous calls. This limit cannot be increased. | 
| Identity Store APIs |  [Identity Store APIs ](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html) have a throttle limit of 20 transactions per second (TPS) per API. This limit applies per Identity Store instance. You can open a support case to request a limit increase.  | 
| SCIM APIs | [SCIM APIs](https://docs.aws.amazon.com/singlesignon/latest/developerguide/what-is-scim.html) have per-API throttle limits of 25 transactions per second (TPS) for write APIs and 40 TPS for read APIs. These limits apply per Identity Store instance. You can open a support case to request a limit increase.<br />Each individual membership operation in `CreateGroup` or `PatchGroup` calls counts as a transaction toward a separate membership operation throttle limit per Identity Store. | 

If your IAM Identity Center instance is enabled in multiple AWS Regions, the throttle limits apply equally to each enabled Region. For example, you would have the 20 TPS throttle limit on the Identity Store APIs in each enabled Region. For more information about which API operations are available in additional Regions, see the corresponding [table](api-support-in-additional-regions.md).

## OIDC service request quotas
<a name="oidcthrottlelimits"></a>


| Resource | Default value (requests per second) | Can be increased | 
| --- | --- | --- | 
| Request rate from a remote address to register a public OAuth client<br />Applies to: [ RegisterClient ](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_RegisterClient.html) | 20 | Yes | 
| Request rate from a public client registered with the OIDC service<br />Applies to: [ CreateToken](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html), [ StartDeviceAuthorization ](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_StartDeviceAuthorization.html) | 80 | Yes | 
| Request rate from all public clients registered with the same IAM Identity Center instance<br />Applies to: [ CreateToken ](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html) | 250 | Yes | 
| Request rate from an IAM Identity Center application registered with the IAM Identity Center instance with Token Exchange and Refresh Token grants.<br />Applies to: [ CreateTokenWithIAM ](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.html) | 80 | Yes | 
| Token generation rate from all IAM Identity Center applications registered with the same IAM Identity Center instance with JWT Bearer grant<br />Applies to: [ CreateTokenWithIAM ](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.html) | 10 | Contact AWS Support | 

If your IAM Identity Center instance is enabled in multiple AWS Regions, the request rates above apply equally to each enabled Region. For example, if your allowed request rate to register a public OAuth client from a remote address is 20 requests per second, this throughput is available in each enabled Region. For more information about which API operations are available in additional Regions, see the corresponding [table](api-support-in-additional-regions.md).

## Additional quotas
<a name="additionallimits"></a>


| Resource | Default quota | Can be increased | 
| --- | --- | --- | 
| Total number of AWS accounts or applications that can be configured \* \*\* | 7000 | Yes | 
| Total number of instances of IAM Identity Center per account | 1 | No | 
| Total number of trusted token issuers | 10 | No | 
| Total number of groups that can be assigned to a permission set per AWS account, or to an application | 100 | No | 
| Total number of AWS Regions enabled for a single IAM Identity Center instance | 6 | Yes | 

\* This quota applies separately to AWS accounts and to applications. You can configure up to 7000 accounts and up to 7000 applications.

\*\* The[`ProvisionPermissionSet`](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ProvisionPermissionSet.html) API operation can provision a permission set using the option `ALL_PROVISIONED_ACCOUNTS` to, at most, 3500 AWS accounts. If you need to provision a permission set to more than 3500 AWS accounts, you can use the `ProvisionPermissionSet` API operation with the `AWS_ACCOUNT` option, which provisions the permission set in a single AWS account. You can make up to three concurrent calls to `ProvisionPermissionSet`.