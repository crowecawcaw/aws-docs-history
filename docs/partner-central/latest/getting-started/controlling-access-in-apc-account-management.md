

# Controlling access in AWS Partner Central account management
<a name="controlling-access-in-apc-account-management"></a>

[AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) is an AWS service you can use at no additional charge that helps you control access to AWS resources. AWS Partner Central account management uses IAM for AWS Partner Central authentication and authorization. Administrators can use IAM roles to control who can sign in to AWS Partner Central and what AWS Partner Central permissions they have.

**Important**  
AWS Partner Central users that you create authenticate using their credentials. However, they must use the same AWS account. Any change a user makes can impact the entire account.

For more information about available actions, resources, and condition keys, refer to [Actions, resources, and condition keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html).

**Topics**
+ [Permissions for AWS Partner Central account management](#account-management-permissions)
+ [Condition keys for AWS Partner Central account management](#condition-keys)
+ [Additional resources](#additional-resources)

## Permissions for AWS Partner Central account management
<a name="account-management-permissions"></a>

You can use the following permissions in IAM policies for AWS Partner Central account management. You can combine permissions into a single IAM policy to grant the permissions you want.

### AssociatePartnerAccount
<a name="associatepartneraccount"></a>

`AssociatePartnerAccount` provides access to associate AWS Partner Central and AWS accounts.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### AssociatePartnerUser
<a name="associatepartneruser"></a>

`AssociatePartnerUser` provides access to associate AWS Partner Central users and IAM roles.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### DisassociatePartnerUser
<a name="disassociatepartneruser"></a>

`DisassociatePartnerUser` provides access to associate AWS Partner Central users and IAM roles.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### AccessLegacyPartnerCentral
<a name="accesslegacypartnercentral"></a>

`AccessLegacyPartnerCentral` provides access to Single Sign-On from AWS Partner Central into Legacy Partner Central.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.
+ **Condition keys:** `partnercentral-account-management:LegacyPartnerCentralRole`

### AccessMarketingCentral
<a name="accessmarketingcentral"></a>

`AccessMarketingCentral` provides access to Single Sign-On from AWS Partner Central into Marketing Central.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.
+ **Condition keys:** `partnercentral-account-management:MarketingCentralRole`

## Condition keys for AWS Partner Central account management
<a name="condition-keys"></a>

AWS Partner Central account management defines the following condition keys that you can use in the `Condition` element of an IAM policy.

### partnercentral-account-management:LegacyPartnerCentralRole
<a name="legacypartnercentralrole"></a>

Filters access by the Legacy Partner Central role. Accepted values: [AceManager, TechnicalStaff, ChannelUser, MarketingStaff].
+ **Type:** `ArrayOfString`

### partnercentral-account-management:MarketingCentralRole
<a name="marketingcentralrole"></a>

Filters access by Marketing Central role. Accepted values: [portal-manager, marketing-staff, sales-representative].
+ **Type:** `ArrayOfString`

## Additional resources
<a name="additional-resources"></a>

Refer to the following sections of the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/) for more information:
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+ [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html#create-managed-policy-console)
+ [Attaching a policy to an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html)
+ [IAM identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)
+ [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html)