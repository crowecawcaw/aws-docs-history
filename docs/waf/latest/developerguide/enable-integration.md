**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Creating an AWS Firewall Manager default administrator

account

This page provides instructions for creating an AWS Firewall Manager default administrator
account.

###### Note

This procedure uses the account and organization that
you chose and configured in the preceding step.

Only the organization's management account can create Firewall Manager default administrator accounts.
The first administrator account that you create is the _default
admininstrator_ account. The default administrator account can manage
third-party firewalls and has full administrative scope. When you set the default
administrator account, Firewall Manager automatically sets it as an AWS Organizations delegated
administrator for Firewall Manager. This allows Firewall Manager to access information about the
organizational units (OUs) in the organization. You can use OUs to specify the scope of
your Firewall Manager policies. For more information about setting policy scope, see the guidance
for the individual policy types under [Creating an AWS Firewall Manager policy](create-policy.md "create-policy.md"). For more information about Organizations and
management accounts, see [Managing the AWS Accounts in Your Organization](../../../organizations/latest/userguide/orgs_manage_accounts.md "../../../organizations/latest/userguide/orgs_manage_accounts.md").

###### Required settings for the organization's management account

The organization's management account must have the following settings in order to onboard
the organization to Firewall Manager and create a default administrator:

- It must be a member of the organization in AWS Organizations where you want to apply your Firewall Manager policies.

###### To set the default administrator account

1. Sign in to the Firewall Manager AWS Management Console using an existing AWS Organizations management account.
2. Open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2").
3. In the navigation pane, choose **Settings**.
4. Type the AWS account ID of the account that you've chosen to use as the Firewall Manager administrator.

###### Note

The default administrator has full administrative scope. Full administrative scope means that
this account can apply policies to all accounts and organizational units
(OUs) within the organization, take actions in all Regions, and manage all
Firewall Manager policy types. 5. Choose **Create administrator account** to create the account.
For more information about managing the Firewall Manager administrator account, see [Using AWS Firewall Manager administrators](fms-administrators.md "fms-administrators.md").
