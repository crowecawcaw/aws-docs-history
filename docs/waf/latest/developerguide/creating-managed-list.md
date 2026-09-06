

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Creating a custom managed list in Firewall Manager
<a name="creating-managed-list"></a>

Follow these procedures to create a custom managed application list or custom managed protocol list.

**Topics**
+ [Creating a custom managed application list](#creating-custom-managed-application-list)
+ [Creating a custom managed protocol list](#creating-custom-managed-protocol-list)

## Creating a custom managed application list
<a name="creating-custom-managed-application-list"></a>

**To create a custom managed application list**

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2). For information about setting up a Firewall Manager administrator account, see [AWS Firewall Manager prerequisites](fms-prereq.md).
**Note**  
For information about setting up a Firewall Manager administrator account, see [AWS Firewall Manager prerequisites](fms-prereq.md).

1. In the navigation pane, choose **Application lists**.

1. In the **Application lists** page, choose **Create application list**. 

1. In the **Create application list** page, give your list a name. Don't use the prefix `fms-` as this is reserved for Firewall Manager. 

1. Specify an application either by providing the protocol and port number or by selecting an application from the **Type** drop down. Give your application specification a name. 

1. Choose **Add another** as needed and fill in the application information until you have completed your list. 

1. (Optional) Apply tags to your list. 

1. Choose **Save** to save your list and return to the **Application lists** page. 

## Creating a custom managed protocol list
<a name="creating-custom-managed-protocol-list"></a>

**To create a custom managed protocol list**

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2). For information about setting up a Firewall Manager administrator account, see [AWS Firewall Manager prerequisites](fms-prereq.md).
**Note**  
For information about setting up a Firewall Manager administrator account, see [AWS Firewall Manager prerequisites](fms-prereq.md).

1. In the navigation pane, choose **Protocol lists**.

1. In the **Protocol lists** page, choose **Create protocol list**. 

1. In the protocol list creation page, give your list a name. Don't use the prefix `fms-` as this is reserved for Firewall Manager. 

1. Specify a protocol. 

1. Choose **Add another** as needed and fill in the protocol information until you have completed your list. 

1. (Optional) Apply tags to your list. 

1. Choose **Save** to save your list and return to the **Protocol lists** page. 