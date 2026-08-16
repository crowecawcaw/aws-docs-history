# Re-enabling Security Hub

Before re-enabling Security Hub on accounts that were previously disabled using a Security Hub policy, you must first detach the disable policy.
If you attempt to re-enable Security Hub while a disable policy is still attached to the account or organizational unit, the disable policy overrides the enablement and Security Hub remains disabled.

###### To remove the Security Hub disable policy for an organization or an account

1. Sign in using your AWS account with your organization management account credentials.
   Open the AWS Organizations console at [https://console.aws.amazon.com/organizations/v2/home](https://console.aws.amazon.com/organizations/v2/home "https://console.aws.amazon.com/organizations/v2/home").
2. From the navigation panel choose **AWS accounts**.
3. If the current Security Hub disable policy was for your entire organization, choose **Root** under the **Organizational structure**.
   If the current Security Hub disable policy is for specific accounts, choose the specific account under the **Organizational structure** and then follow the remaining steps for each account.
4. In the **Policies** tab, find the section titled **Security Hub policies**.
5. Choose the radio button next to the policy that disables Security Hub.
   Choose **Detach**.

After you detach the policy from your organization or accounts, you can re-enable Security Hub.
See [Managing configuration of member accounts in an AWS Organization](securityhub-v2-da-policy.md "securityhub-v2-da-policy.md") for details on re-enabling Security Hub.
