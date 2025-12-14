**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Creating a custom managed list in Firewall Manager

Follow these procedures to create a custom managed application list or custom managed protocol list.

###### Topics

- [Creating a custom managed application list](#creating-custom-managed-application-list "#creating-custom-managed-application-list")
- [Creating a custom managed protocol list](#creating-custom-managed-protocol-list "#creating-custom-managed-protocol-list")

## Creating a custom managed application list

###### To create a custom managed application list

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, choose **Application lists**. 3. In the **Application lists** page, choose
**Create application list**. 4. In the **Create application list** page, give your list a name. Don't
use the prefix `fms-` as this is reserved for Firewall Manager. 5. Specify an application either by providing the protocol and port number or
by selecting an application from the **Type** drop down.
Give your application specification a name. 6. Choose **Add another** as needed and fill in the application information until you have completed your list. 7. (Optional) Apply tags to your list. 8. Choose **Save** to save your list and return to the **Application
lists** page.

## Creating a custom managed protocol list

###### To create a custom managed protocol list

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, choose **Protocol lists**. 3. In the **Protocol lists** page, choose **Create
protocol list**. 4. In the protocol list creation page, give your list a name. Don't use the prefix
`fms-` as this is reserved for Firewall Manager. 5. Specify a protocol. 6. Choose **Add another** as needed and fill in the protocol information until you have completed your list. 7. (Optional) Apply tags to your list. 8. Choose **Save** to save your list and return to the **Protocol
lists** page.
