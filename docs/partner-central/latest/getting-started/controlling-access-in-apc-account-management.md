# Controlling access in

AWS Partner Central account management

[AWS Identity and
Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") is an AWS service you can use at no additional charge that
helps you control access to AWS resources. AWS Partner Central account management uses IAM for
AWS Partner Central authentication and authorization. Administrators can use IAM roles to control who
can sign in to AWS Partner Central and what AWS Partner Central permissions they have.

###### Important

AWS Partner Central users that you create authenticate using their credentials. However, they must use the same AWS account. Any change a user makes can impact the entire account.

For more information about available actions, resources, and condition keys, refer to [Actions, resources, and condition keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md").

###### Topics

- [Permissions for AWS Partner Central account
  management](#account-management-permissions "#account-management-permissions")
- [Condition keys for AWS Partner Central account management](#condition-keys "#condition-keys")
- [Additional resources](#additional-resources "#additional-resources")

## Permissions for AWS Partner Central account

management

You can use the following permissions in IAM policies for AWS Partner Central account
management. You can combine permissions into a single IAM policy to grant the permissions you
want.

### AssociatePartnerAccount

`AssociatePartnerAccount` provides access to associate AWS Partner Central and
AWS accounts.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### AssociatePartnerUser

`AssociatePartnerUser` provides access to associate AWS Partner Central users and
IAM roles.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### DisassociatePartnerUser

`DisassociatePartnerUser` provides access to associate AWS Partner Central users and
IAM roles.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### AccessLegacyPartnerCentral

`AccessLegacyPartnerCentral` provides access to Single Sign-On from AWS Partner Central into Legacy Partner Central.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.
- **Condition keys:** `partnercentral-account-management:LegacyPartnerCentralRole`

### AccessMarketingCentral

`AccessMarketingCentral` provides access to Single Sign-On from AWS Partner Central into Marketing Central.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.
- **Condition keys:** `partnercentral-account-management:MarketingCentralRole`

## Condition keys for AWS Partner Central account management

AWS Partner Central account management defines the following condition keys that you can use in the `Condition` element of an IAM policy.

### partnercentral-account-management:LegacyPartnerCentralRole

Filters access by the Legacy Partner Central role. Accepted values: [AceManager, TechnicalStaff, ChannelUser, MarketingStaff].

- **Type:** `ArrayOfString`

### partnercentral-account-management:MarketingCentralRole

Filters access by Marketing Central role. Accepted values: [portal-manager, marketing-staff, sales-representative].

- **Type:** `ArrayOfString`

## Additional resources

Refer to the following sections of the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md") for more information:

- [Security best
  practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [Managing
  IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md#create-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_manage.md#create-managed-policy-console")
- [Attaching a policy to an IAM user group](../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md "../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md")
- [IAM identities (users, user
  groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md")
- [Controlling
  access to AWS resources using policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md")
