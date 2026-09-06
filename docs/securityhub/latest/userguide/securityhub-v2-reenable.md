

# Re-enabling Security Hub
<a name="securityhub-v2-reenable"></a>

 Before re-enabling Security Hub on accounts that were previously disabled using a Security Hub policy, you must first detach the disable policy. If you attempt to re-enable Security Hub while a disable policy is still attached to the account or organizational unit, the disable policy overrides the enablement and Security Hub remains disabled. 

**To remove the Security Hub disable policy for an organization or an account**

1.  Sign in using your AWS account with your organization management account credentials. Open the AWS Organizations console at [https://console.aws.amazon.com/organizations/v2/home](https://console.aws.amazon.com/organizations/v2/home). 

1.  From the navigation panel choose **AWS accounts**. 

1.  If the current Security Hub disable policy was for your entire organization, choose **Root** under the **Organizational structure**. If the current Security Hub disable policy is for specific accounts, choose the specific account under the **Organizational structure** and then follow the remaining steps for each account. 

1.  In the **Policies** tab, find the section titled **Security Hub policies**. 

1.  Choose the radio button next to the policy that disables Security Hub. Choose **Detach**. 

 After you detach the policy from your organization or accounts, you can re-enable Security Hub. See [Managing configuration of member accounts in an AWS Organization](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-da-policy.html) for details on re-enabling Security Hub. 