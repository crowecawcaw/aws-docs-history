

# Deleting configuration policies
<a name="delete-policy"></a>

After creating a configuration policy, the delegated AWS Security Hub CSPM administrator can delete it. Alternatively, the delegated administrator can retain the policy, but disassociate it from specific accounts or organizational units (OUs), or from the root. For instructions on disassociating a policy, see [Disassociating a configuration from its targets](disassociate-policy.md).

For background information about the benefits of central configuration and how it works, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md).

This section explains how to delete configuration policies.

When you delete a configuration policy, it no longer exists for your organization. Target accounts, OUs, and the organization root can no longer use the configuration policy. Targets that were associated with a deleted configuration policy inherit the configuration policy of the closest parent, or become self-managed if the closest parent is self-managed. If you want a target to use a different configuration, you can associate the target with a new configuration policy. For more information, see [Creating and associating configuration policies](create-associate-policy.md).

We recommend creating and associating at least one configuration policy with your organization to provide adequate security coverage.

Before you can delete a configuration policy, you must disassociate the policy from any accounts, OUs, or the root to which it currently applies.

Choose your preferred method, and follow the steps to delete a configuration policy.

------
#### [ Console ]

**To delete a configuration policy**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

   Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region.

1. In the navigation pane, choose **Settings** and **Configuration**.

1. Choose the **Policies** tab. Select the configuration policy that you want to delete, and choose **Delete**. If the configuration policy is still associated with any accounts or OUs, you're prompted to first disassociate the policy from those targets before you can delete it.

1. Review the confirmation message. Enter **confirm**, and choose **Delete**.

------
#### [ API ]

**To delete a configuration policy**

Invoke the [DeleteConfigurationPolicy](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteConfigurationPolicy.html) API from the Security Hub CSPM delegated administrator account in the home Region.

Provide the Amazon Resource Name (ARN) or ID of the configuration policy that you want to delete. If you receive a `ConflictException` error, the configuration policy still applies to accounts or OUs in your organization. To resolve the error, disassociate the configuration policy from these accounts or OUs before trying to delete it.

**Example API request to delete a configuration policy:**

```
{
    "Identifier": "arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

------
#### [ AWS CLI ]

**To delete a configuration policy**

Run the [delete-configuration-policy](https://docs.aws.amazon.com/cli/latest/reference/securityhub/delete-configuration-policy.html) command from the Security Hub CSPM delegated administrator account in the home Region.

 Provide the Amazon Resource Name (ARN) or ID of the configuration policy that you want to delete. If you receive a `ConflictException` error, the configuration policy still applies to accounts or OUs in your organization. To resolve the error, disassociate the configuration policy from these accounts or OUs before trying to delete it.

```
aws securityhub --region us-east-1 delete-configuration-policy \
--identifier "arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```

------