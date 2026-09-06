

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Changing the default Firewall Manager administrator account
<a name="fms-change-administrator"></a>

The following procedure describes how to change the default Firewall Manager administrator account. 

You can designate only one account in an organization as the default Firewall Manager administrator account. The default administrator account follows the principle of first in, last out. To designate a different default administrator account, each individual administrator account must first revoke their own account. Then, the existing default administrator can revoke their own account, which also will offboard the organization from Firewall Manager. When an administrator revokes their account, all Firewall Manager policies created by that account are deleted. To designate a new default administrator account, you then must sign into Firewall Manager with the AWS Organizations management account to designate a new administrator account. To change the default administrator account for an organization, perform the following procedure.

**To change the default administrator account**

1. Sign in to the Firewall Manager AWS Management Console using an existing AWS Organizations management account. 

1. Open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2). 

1. In the navigation pane, choose **Settings**.

1. Type the ID of the account that you've chosen to use as the Firewall Manager administrator. 
**Note**  
This account is given permission to create and manage Firewall Manager policies across all accounts within your organization.

1. Choose **Create administrator account**.

1. Type the AWS ID of the account that you've chosen to use as the Firewall Manager administrator. 
**Note**  
This account is given full administrative scope. Full administrative scope means that this account can apply policies to all accounts and organizational units (OUs) within the organization, take actions in all Regions, and manage all Firewall Manager policy types.

1. Choose **Create administrator account** to create the default administrator account.