**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Updating a Firewall Manager administrator account

The following procedure describes how to update a Firewall Manager administrator account using the Firewall Manager console.

###### Note

To update an administrator's scope to include a Region that's disabled by default,
you must enable the Region for both the AWS Organizations organization management account
and the default administration account. For information about enabling Regions for an account,
see [Enable a Region](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable")
in the _Amazon Web Services General Reference_.

Only an organization's managment account can update
Firewall Manager administrator accounts.

###### To update an administrator account (console)

1. Sign in to the Firewall Manager AWS Management Console using an existing AWS Organizations management account.
2. Open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2").
3. In the navigation pane, choose **Settings**.
4. in the **Firewall Manager administrators** table, choose the account that you'd like to update.
5. Select **Edit** to change details of administrator's account. You can't change the **account ID**.
6. Choose **Save** to save your changes.
