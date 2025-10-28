# Disassociating a configuration from its targets

From the delegated AWS Security Hub CSPM administrator account, you can disassociate a configuration policy or self-managed configuration from
an account, OU, or root. Disassociation retains the policy for future use, but removes existing associations from
specific accounts, OUs, or the root.You can disassociate only a directly applied configuration, not an inherited configuration.
To change an inherited configuration, you can apply a configuration policy or self-managed behavior to the affected account or OU. You can also apply a
new configuration policy, which includes your desired modifications, to the closest parent.

Disassociation _doesn't_ delete a configuration policy. The policy is retained in your account, so
you can associate it with other targets in your organization. For instructions on deleting a configuration policy,
see [Deleting configuration policies](delete-policy.md "delete-policy.md"). When
disassociation is complete, an affected target inherits the configuration policy or self-managed behavior of the closest
parent. If there's no inheritable configuration, a target retains the settings it had prior to disassociation but becomes
self-managed.

Choose your preferred method, and follow the steps to disassociate
an account, OU, or root from its current configuration.

Console

###### To disassociate an account or OU from its current configuration

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region. 2. In the navigation pane, choose **Settings**
and **Configuration**. 3. On the **Organizations** tab, select the
account, OU, or the root that you want to disassociate from its current configuration. Choose
**Edit**. 4. On the **Define configuration** page, for **Management**,
choose **Policy applied** if you want the delegated administrator to be able to apply policies directly to the target. Choose
**Inherited** if you want the target to inherit the configuration of its closest parent. In either of these cases, the delegated administrator controls settings for the target. Choose
**Self-managed** if you want the account or OU to control its own settings. 5. After reviewing your changes, choose **Next** and **Apply**.
This action overrides existing configurations of
any accounts or OUs that are in scope, if those configurations conflict
with your current selections.

API

###### To disassociate an account or OU from its current configuration

1. Invoke the [StartConfigurationPolicyDisassociation](../../1.0/APIReference/API_StartConfigurationPolicyDisassociation.md "../../1.0/APIReference/API_StartConfigurationPolicyDisassociation.md") API
   from the Security Hub CSPM delegated administrator account in the home Region.
2. For `ConfigurationPolicyIdentifier`, provide the Amazon
   Resource Name (ARN) or ID of the configuration policy that you want to disassociate.
   Provide `SELF_MANAGED_SECURITY_HUB` for this field to disassociate self-managed behavior.
3. For `Target`, provide the accounts, OUs, or the root that you
   want to dissociate from this configuration policy.

**Example API request to disassociate a configuration policy:**

```
{
    "ConfigurationPolicyIdentifier": "arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Target": {"RootId": "r-f6g7h8i9j0example"}
}

```

AWS CLI

###### To disassociate an account or OU from its current configuration

1. Run the [start-configuration-policy-disassociation](../../../cli/latest/reference/securityhub/start-configuration-policy-disassociation.md "../../../cli/latest/reference/securityhub/start-configuration-policy-disassociation.md")
   command from the Security Hub CSPM delegated administrator account in the home Region.
2. For `configuration-policy-identifier`, provide the Amazon
   Resource Name (ARN) or ID of the configuration policy that you want to disassociate.
   Provide `SELF_MANAGED_SECURITY_HUB` for this field to disassociate self-managed behavior.
3. For `target`, provide the accounts, OUs, or the root that you
   want to dissociate from this configuration policy.

**Example command to disassociate a configuration policy:**

```
aws securityhub --region us-east-1 start-configuration-policy-disassociation \
--configuration-policy-identifier "arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" \
--target '{"RootId": "r-f6g7h8i9j0example"}'

```
