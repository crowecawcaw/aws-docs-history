**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Revoking a Firewall Manager administrator account

The following procedure describes how to revoke a Firewall Manager
administrator
account. If you are the default administrator, before you can revoke your account
all of the Firewall Manager administrator accounts within your organization must first revoke
their own accounts.

###### Note

Only an individual Firewall Manager administrator can revoke their
own administrator account.

###### To revoke an administrator account (console)

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").
2. In the navigation pane, choose **Settings**.
3. In the **Administrator account** pane, select **Revoke administrator account** to revoke your account.

###### Important

When you revoke administrator privileges from an administrator account, all Firewall Manager policies
created by that account are deleted.
