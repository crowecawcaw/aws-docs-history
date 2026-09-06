

# Quotas and service limits for AWS Organizations
<a name="orgs_reference_limits"></a>

This topic describes quotas and service limits for AWS Organizations.

## Naming guidelines
<a name="name-limits"></a>

The following are guidelines for names that you create in AWS Organizations, including names of accounts, organizational units (OUs), roots, and policies:
+ Names must be composed of Unicode characters.
+ Maximum string length for names vary by the object. For information about the actual limit for each object, see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/) and find the API operation that creates the object, and look at the details for that operation's `Name` parameter. For example: [Account name](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html#organizations-CreateAccount-request-AccountName), or [OU name](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateOrganizationalUnit.html#organizations-CreateOrganizationalUnit-request-Name).

## Considerations
<a name="orgs_reference_limits-considerations"></a>

Service quota codes might change over time due to updates. This does not impact the quota values or names. To find the quota code for a specific quota, use the [ListServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html) operation, and look for the `QuotaCode` response in the output for the quota you want.

## Maximum and minimum values
<a name="min-max-values"></a>

The following are the ***default*** maximums for entities in AWS Organizations. 

**Note**  
Consider the following information about AWS Organizations quotas:  
You can request increases for some of these values by using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/organizations/quotas). 
AWS Organizations limits apply at the organization level, unless otherwise specified. Many quotas apply only to actions performed from the AWS Organizations management account.
AWS Organizations is a global service that is physically hosted in the US East (N. Virginia) Region (`us-east-1`). Therefore, you must use `us-east-1` to access these quotas when using the Service Quotas console, the AWS CLI, or an AWS SDK.



| Description | Limit | 
| --- | --- | 
| <a name="default-maximum-number-of-accounts"></a>Maximum number of accounts | 10 — The maximum number of accounts allowed in an organization. This quota is adjustable, and can be increased by using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/organizations/quotas).<br />**Note:** Only the Management account of an organization can submit this quota increase request. Limit increases can be granted up to 50,000 accounts based on customer qualifications and requirements. Newly created accounts and organizations might experience a quota below the default of 10 accounts.<br />An invitation sent to an account counts against this quota. The count is returned if the invited account declines, the management account cancels the invitation, or the invitation expires.<br />When an account is closed it does not stop counting against this quota until it is permanently closed. For more information on when an account is permanently closed, see [Post-closure period](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-closing.html#post-closure-period) in the *AWS Account Management Reference Guide*.<br />Some services have account limits separate from the maximum number of accounts allowed in an organization. For more information, see [Limits by AWS service](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html#min-max-service-limits). | 
| Minimum age for removal of created accounts | Each supported Region: 4 — The minimum number of days a created account must exist before you can remove it from the organization. | 
| Number of roots in an organization | 1 | 
| Number of OUs in an organization | 2000 | 
| Number of policies of each type in an organization | Service control policies: 10,000<br />Resource control policies: 2000<br />Declarative policies: 1000<br />Backup policies: 1000<br />Tag policies: 1000<br />Chat applications policies: 1000<br />AI services opt-out policies: 1000<br />Security Hub policies: 1000 | 
| Maximum size of a policy document | Service control policies: 10,240 characters<br />Resource control policies: 5120 characters<br />Declarative policies: 10,000 characters<br />Backup policies: 10,000 characters<br />Chat applications policies: 10,000 characters<br />AI services opt-out policies: 2500 characters<br />Tag policies: 10,000 characters<br />Security Hub policies: 10,000 characters<br />**Note:** If you save the policy by using the AWS Management Console, extra white space (such as spaces and line breaks) between JSON elements and outside of quotation marks, is removed and not counted. If you save the policy using an SDK operation or the AWS CLI, then the policy is saved exactly as you provided and no automatic removal of characters occurs.  | 
| OU maximum nesting in a root | Five levels of OUs deep under a root. | 
| Maximum number of invitation attempts you can perform in a 24-hour period | Either 20 or the maximum number of accounts allowed in your organization, whichever is greater. Accepted invitations don't count against this quota. As soon as one invitation is accepted, you can send another invitation that same day.<br />If the maximum number of accounts allowed in your organization is less than 20, then you get an "account limit exceeded" exception if you attempt to invite more accounts than your organization can contain. However, you can cancel invitations and send new ones up to the maximum of 20 attempts in one day. | 
| Number of member accounts you can create concurrently | 5 — As soon as one finishes, you can start another, but only five can be in progress at a time. | 
| <a name="number-of-accounts-you-can-close"></a>Number of accounts you can close within a 30-day period | 20% of member accounts in organizations or 250, whichever is higher, with a maximum of 1,000. This quota is not adjustable.+  ** < 1,250 accounts** – You can close up to 250 member accounts <br />+  ** 1,250 - 5,000 accounts** – You can close up to 20% of your member accounts <br />+  ** > 5,000 accounts** – You can close up to 1,000 member accounts <br />After you reach this quota, you can't close additional accounts until your quota resets. For more information, see [Close an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-closing.html) in the *AWS Account Management Guide*. | 
| Number of member accounts you can close concurrently | 3 — Only three account closures can be in progress at the same time. As soon as one finishes, you can close another account.  | 
| Number of targets a policy can be attached to | Unlimited | 
| Number of tags that you can attach to a root, OU, or account | 50 | 
| Maximum size of the resource-based delegation policy |  40,000 characters | 

### Limits by AWS service
<a name="min-max-service-limits"></a>

Most AWS services support the stated maximum number of accounts that you can have in an organization. However, some services have account limits separate from the maximum number of accounts allowed in an organization.

The following table shows services with separate account limits.



| AWS service | Limit | Can be increased | Service documentation | 
| --- | --- | --- | --- | 
| AWS Directory Service (Directory sharing is available for AWS Managed Microsoft AD) | Directory sharing account capacity varies by edition. | Yes | [Directory Service Quotas](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_limits.html) | 
| AWS Audit Manager | 250 | Yes | [AWS Audit Manager Quotas](https://docs.aws.amazon.com/general/latest/gr/audit-manager.html) | 
| Amazon Detective | 1200 | Yes | [Amazon Detective Quotas](https://docs.aws.amazon.com/detective/latest/userguide/regions-limitations.html) | 
| AWS IAM Identity Center | 7000 | Yes | [AWS IAM Identity Center Quotas](https://docs.aws.amazon.com/singlesignon/latest/userguide/limits.html) | 
| AWS Transform MGN | 5000 | No | [AWS Quotas](https://docs.aws.amazon.com/mgn/latest/ug/MGN-service-limits.html) | 
| AWS Security Hub | 10000 | No | [AWS Security Hub Quotas](https://docs.aws.amazon.com/general/latest/gr/sechub.html) | 
| Amazon Macie | 10000 | No | [Amazon Macie Quotas](https://docs.aws.amazon.com/macie/latest/user/macie-quotas.html) | 
| AWS Control Tower | 10000 | No | [AWS Control Tower Quotas](https://docs.aws.amazon.com/controltower/latest/userguide/limits.html) | 
| Amazon Inspector | 10000 | No | [Amazon Inspector Quotas](https://docs.aws.amazon.com/inspector/latest/user/quotas.html) | 
| AWS Firewall Manager | 10000 | Yes | [AWS Firewall Manager Quotas](https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html) | 
| Amazon DevOps Guru | 10000 | Yes | [Amazon DevOps Guru Quotas](https://docs.aws.amazon.com/devops-guru/latest/userguide/quotas.html) | 
| AWS Service Catalog | 15000 | No |  | 

## Expiration times for handshakes
<a name="min-max-handshakes"></a>

The following are the timeouts for handshakes in AWS Organizations.



| Description | Limit | 
| --- | --- | 
| Invitation to join an organization | 15 days | 
| Request to enable all features in an organization | 90 days | 
| Handshake is deleted and no longer appears in lists | 30 days after the handshake is completed | 

## Number of policies that you can attach to an entity
<a name="min-max-policies"></a>

The minimum and maximum depend on the policy type and the entity that you're attaching the policy to. The following table shows each policy type and the number of entities that you can attach each type to.

**Note**  
These numbers apply to only those policies that are directly attached to an OU or an account. Policies that affect an OU or account by inheritance do ***not*** count against these limits. All policy limits are hard limits.



| Policy type | Minimum attached to an entity | Maximum attached to root | Maximum attached per OU | Maximum attached per account | 
| --- | --- | --- | --- | --- | 
| Service control policy | 1 — Every entity must have at least one SCP attached at all times when you enable SCPs. You can't remove the last SCP from an entity. | 10 | 10 | 10 | 
| Resource control policy | 1 — The RCPFullAWSAccess policy is automatically attached to the root, every OU, and every account in your organization when you enable RCPs. You cannot detach this policy and it counts towards the 5 policies quota. | 5 | 5 | 5 | 
| Declarative policy | 0 | 10 | 10 | 10 | 
| Backup policy | 0 | 10 | 10 | 10 | 
| Tag policy | 0 | 10 | 10 | 10 | 
| Chat applications policy | 0 | 5 | 5 | 5 | 
| AI services opt-out policy | 0 | 5 | 5 | 5 | 
| Security Hub policy | 0 | 10 | 10 | 10 | 

**Note**  
You can have only one root in an organization.

## Throttling limits
<a name="throttling-limits"></a>

The following tables lists the AWS Organizations APIs by management category, and shows their respective throttle rates at the account and organizational level.

AWS Organizations uses the [token bucket algorithm](https://en.wikipedia.org/wiki/Token_bucket) to implement API throttling. With this algorithm, your account has a *bucket* that holds a specific number of *tokens*. The number of tokens in the bucket represents your throttling quota at any given second.

*Rate* is the fixed pace that tokens are added to the token bucket per second.

*Burst* is the maximum number of tokens that can be added and the maximum number of tokens that can be used per second.

For example, the `DescribeAccount` API is limited for a single AWS account to 20 requests per second as the baseline rate and to 30 requests per second as the burst rate. The burst rate of 30 requests per second allows you to temporarily exceed the baseline rate of 20 requests per second.

You can makes 20 requests in the first second, which is the baseline rate. In the next second, you can make 30 requests, exceeding the baseline but staying within the burst rate of 30. However, in the third second, if your try to make more than 20 requests, you will be throttled since you have exceeded the baseline rate and the burst capacity has been used.

The burst rate allows you to handle temporary spikes in traffic without getting throttled, as long as the average requests per second stay within the baseline limit over time.

### Account management limits
<a name="throttling-limits-account-management"></a>

The following table lists the AWS Organizations APIs for account management.



| AWS Organizations API | Per account limit (rate, burst) | Per organization limit (rate, burst) | 
| --- | --- | --- | 
| CloseAccount | .05, 1 |  | 
| CreateAccount, CreateGovCloudAccount | 0.1, 3 |  | 
| DescribeAccount | 20, 30 | 24, 36 | 
| DescribeCreateAccountStatus | 2, 2 | 2, 3 | 
| LeaveOrganization | 1, 1 |  | 
| ListCreateAccountStatus | 5, 8 | 6, 10 | 

### Handshake management limits
<a name="throttling-limits-handshake-management"></a>

The following table lists the AWS Organizations APIs for account handshake.



| AWS Organizations API | Per account limit (rate, burst) | Per organization limit (rate, burst) | 
| --- | --- | --- | 
| AcceptHandshake | 1, 2 | 5, 5 | 
| DescribeHandshake | 1, 2 | 6, 10 | 
| CancelHandshake | 2, 3 |  | 
| DeclineHandshake | 1, 1 | 5, 5 | 
| InviteAccountToOrganization | 3, 5 |  | 
| ListHandshakesForAccount, ListHandshakesForOrganization | 5, 8 | 6, 10 | 

### Organization management limits
<a name="throttling-limits-organization-management"></a>

The following table lists the AWS Organizations APIs for organization management.



| AWS Organizations API | Per account limit (rate, burst) | Per organization limit (rate, burst) | 
| --- | --- | --- | 
| CreateOrganization, DeleteOrganization, EnableFullControl | 1, 1 |  | 
| CreateOrganizationalUnit, DescribeOrganization | 1, 2 |  | 
| MoveAccount, UpdateOrganizationalUnit, DeleteOrganizationalUnit | 2, 3 |  | 
| DescribeOrganizationalUnit | 2, 2 | 2, 3 | 
| ListAccounts | 8, 12 | 9, 15 | 
| ListChildren | 6, 10 | 7, 12 | 
| ListParents, ListAccountsForParent, ListOrganizationalUnitsForParent | 5, 8 | 6, 10 | 
| ListRoots | 1, 2 | 1, 3 | 
| ListTagsForResource | 10, 15 | 12, 18 | 
| RemoveAccountFromOrganization | 2, 2 |  | 
| TagResource, UntagResource | 4, 6 |  | 

### Policy management limits
<a name="throttling-limits-policy-management"></a>

The following table lists the AWS Organizations APIs for policy management.



| AWS Organizations API | Per account limit (rate, burst) | Per organization limit (rate, burst) | 
| --- | --- | --- | 
| CreatePolicy, DeletePolicy, AttachPolicy, DetachPolicy | 2, 3 |  | 
| DescribePolicy | 2, 2 | 2, 3 | 
| DisablePolicyType, EnablePolicyType | 1, 1 |  | 
| ListPolicies, ListPoliciesForTarget, ListTargetsForPolicy | 5, 8 | 6, 10 | 
| UpdatePolicy | 2, 3 |  | 

### Service management limits
<a name="throttling-limits-serivce-management"></a>

The following table lists the AWS Organizations APIs for service management.



| AWS Organizations API | Per account limit (rate, burst) | Per organization limit (rate, burst) | 
| --- | --- | --- | 
| EnableAWSServiceAccess, DisableAWSServiceAccess | 1, 2 |  | 
| ListAWSServiceAccessForOrganization, ListDelegatedServicesForAccount | 1, 3 | 1, 4 | 
| ListDelegatedAdministrators | 5, 8 | 6, 10 | 
| RegisterDelegatedAdministrator, DeregisterDelegatedAdministrator | 1, 2 |  | 