# Creating a policy as the delegated administrator to manage member accounts

The delegated administrator for an organization can create a policy allowing it to enable and disable member accounts in your organization.
All configured policies can be accessed on the **Configurations** screen in the Security Hub console.
The following procedure describes how to create the policy.

###### To create a policy that enables and disables member accounts

1. Sign in using your delegated administrator credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home? "https://console.aws.amazon.com/securityhub/v2/home?").
2. From the navigation pane, choose **Settings**, and then choose **Configurations**.
3. Choose **Create policy**.
4. For **Details**, enter a name for the policy, and determine whether to enter an optional description for the policy.
5. For **Regions**, choose **Enable all Regions**, **Disable all Regions**, or **Specify Regions**.
   If you choose **Enable all Regions**, you can determine whether to automatically enable new Regions.
   If you choose **Disable all Regions**, you can determine whether to automatically disable new Regions.
   If you choose **Specify Regions**, you must choose which Regions you want to enable and disable.
6. (Optional) For **Advanced settings**, please refer to the [guidance](../../../organizations/latest/userguide/policy-operators.md "../../../organizations/latest/userguide/policy-operators.md") from AWS Organizations.
7. For **Account selection**, select one of the following options.
   Choose **All organizational units and accounts** if you want to apply the policy to all organizational units and accounts.
   Choose **Specific organizational units and accounts** if you want to apply the policy to specific organizational units and accounts.
   If you choose this option, use the search bar or organizational structure tree to specify the organizational units and accounts where the policy will be applied.
   Choose **No organizational units or accounts** if you do not want to apply the policy to any organizational unit or account.
8. (Optional) For **Resource tags**, determine whether to add a key-value pair to the policy.
   You can add up to 50 tags.
9. Choose **Next**.
10. Review your changes, and then choose **Apply**.
    Your target accounts are configured based on the policy.
    To view the effective policy at the account level, you can review the **Organization** tab on the **Configurations** page where you can choose an account.
