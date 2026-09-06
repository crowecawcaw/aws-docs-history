

# Centrally managed versus self-managed targets
<a name="central-configuration-management-type"></a>

When you enable central configuration, the delegated AWS Security Hub CSPM administrator can designate each organization account, organizational unit (OU), and the root as *centrally managed* or *self-managed*. The management type of a target determines how you can specify its Security Hub CSPM settings.

For background information about the benefits of central configuration and how it works, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md).

This section explains the differences between a centrally managed and self-managed designation and how to choose the management type of an account, OU, or the root.

**Self-managed**  
The owner of a self-managed account, OU, or root must configure its settings separately in each AWS Region. The delegated administrator can't create configuration policies for self-managed targets.

**Centrally managed**  
Only the delegated Security Hub CSPM administrator can configure settings for centrally managed accounts, OUs, or the root across the home Region and linked Regions. Configuration policies can be associated with centrally managed accounts and OUs.

The delegated administrator can switch the status of a target between self-managed and centrally managed. By default, all accounts and OU are self-managed when you start central configuration through the Security Hub CSPM API. In the console, management type depends on your first configuration policy. Accounts and OUs that you associate with your first policy are centrally managed. Other accounts and OUs are self-managed by default.

If you associate a configuration policy with a previously self-managed account, the policy settings override the self-managed designation. The account becomes centrally managed and adopts the settings reflected in the configuration policy.

If you change a centrally managed account to a self-managed account, the settings that were previously applied to the account through a configuration policy remain in place. For example, a centrally managed account could initially be associated with a policy that enabled Security Hub CSPM, enabled AWS Foundational Security Best Practices, and disabled CloudTrail.1. If you then designate the account as self-managed, all of the settings remain unchanged. However, the account owner can independently change the settings for the account going forward.

Child accounts and OUs can inherit self-managed behavior from a self-managed parent, in the same way that child accounts and OUs can inherit configuration policies from a centrally managed parent. For more information, see [Policy association through application and inheritance](configuration-policies-overview.md#policy-association).

A self-managed account or OU can't inherit a configuration policy from a parent node or from the root. For example, if you want all accounts and OUs in your organization to inherit a configuration policy from the root, you must change the management type of self-managed nodes to centrally managed.

## Options to configure settings in self-managed accounts
<a name="self-managed-settings"></a>

Self-managed accounts must configure their own settings separately in each Region.

Owners of self-managed accounts can invoke the following operations of the Security Hub CSPM API in each Region to configure their settings:
+ `EnableSecurityHub` and `DisableSecurityHub` to enable or disable the Security Hub CSPM service (if a self-managed account has a delegated Security Hub CSPM administrator, the administrator must [disassociate the account](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisassociateMembers.html) before the account owner can disable Security Hub CSPM).
+ `BatchEnableStandards` and `BatchDisableStandards` to enable or disable standards
+ `BatchUpdateStandardsControlAssociations` or `UpdateStandardsControl` to enable or disable controls

Self-managed accounts can also use `*Invitations` and `*Members` operations. However, we recommend that self-managed accounts don't use these operations. Policy associations can fail if a member account has its own members that are part of a different organization than the delegated administrator's.

For descriptions of Security Hub CSPM API actions, see the [*AWS Security Hub CSPM API Reference*](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html).

Self-managed accounts can also use the Security Hub CSPM console or AWS CLI to configure their settings in each Region.

Self-managed accounts can't invoke any APIs related to Security Hub CSPM configuration policies and policy associations. Only the delegated administrator can invoke central configuration APIs and use configuration policies to configure centrally managed accounts.

## Choosing the management type of a target
<a name="choose-management-type"></a>

Choose your preferred method, and follow the steps to designate an account or OU as centrally managed or self-managed in AWS Security Hub CSPM.

------
#### [ Security Hub CSPM console ]

**To choose the management type of an account or OU**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

   Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region.

1. Choose **Configuration**.

1. On the **Organization** tab, select the target account or OU. Choose **Edit**.

1. On the **Define configuration** page, for **Management type**, choose **Centrally managed** if you want the delegated administrator to configure the target account or OU. Then, choose **Apply a specific policy** if you want to associate an existing configuration policy with the target. Choose **Inherit from my organization** if you want the target to inherit the configuration of its closest parent. Choose **Self-managed** if you want the account or OU to configure its own settings.

1. Choose **Next**. Review your changes, and choose **Save**.

------
#### [ Security Hub CSPM API ]

**To choose the management type of an account or OU**

1. Invoke the [StartConfigurationPolicyAssociation](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StartConfigurationPolicyAssociation.html) API from the Security Hub CSPM delegated administrator account in the home Region.

1. For the `ConfigurationPolicyIdentifier` field, provide `SELF_MANAGED_SECURITY_HUB` if you want the account or OU to control its own settings. Provide the Amazon Resource Name (ARN) or ID of the relevant configuration policy if you want the delegated administrator to control settings for the account or OU.

1. For the `Target` field, provide the AWS account ID, OU ID, or root ID of the target whose management type you want to change. This associates the self-managed behavior or specified configuration policy with the target. Child accounts of the target may inherit the self-managed behavior or configuration policy.

**Example API request to designate a self-managed account:**

```
{
    "ConfigurationPolicyIdentifier": "SELF_MANAGED_SECURITY_HUB",
    "Target": {"AccountId": "123456789012"}
}
```

------
#### [ AWS CLI ]

**To choose the management type of an account or OU**

1. Run the [start-configuration-policy-association](https://docs.aws.amazon.com/cli/latest/reference/securityhub/start-configuration-policy-association.html) command from the Security Hub CSPM delegated administrator account in the home Region.

1. For `configuration-policy-identifier` field, provide `SELF_MANAGED_SECURITY_HUB` if you want the account or OU to control its own settings. Provide the Amazon Resource Name (ARN) or ID of the relevant configuration policy if you want the delegated administrator to control settings for the account or OU..

1. For the `target` field, provide the AWS account ID, OU ID, or root ID of the target whose management type you want to change. This associates the self-managed behavior or specified configuration policy with the target. Child accounts of the target may inherit the self-managed behavior or configuration policy.

**Example command to designate a self-managed account:**

```
aws securityhub --region us-east-1 start-configuration-policy-association \
--configuration-policy-identifier "SELF_MANAGED_SECURITY_HUB" \
--target '{"AccountId": "123456789012"}'
```

------