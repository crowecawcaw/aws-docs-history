

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Disabling logging for an AWS WAF policy in Firewall Manager
<a name="waf-policies-disabling-logging"></a>

The following procedure describes how to disable logging for an AWS WAF policy in the Firewall Manager console.

**To disable logging for an AWS WAF policy**

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2). For information about setting up a Firewall Manager administrator account, see [AWS Firewall Manager prerequisites](fms-prereq.md).
**Note**  
For information about setting up a Firewall Manager administrator account, see [AWS Firewall Manager prerequisites](fms-prereq.md).

1. In the navigation pane, choose **Security Policies**.

1. Choose the AWS WAF policy that you want to disable logging for.

1. On the **Policy details** tab, in the **Policy rules** section, choose **Edit**. 

1. For **Logging configuration status**, choose **Disabled**.

1. Choose **Next**.

1. Review your settings, then choose **Save** to save your changes to the policy.

**Note**  
Only modify or disable logging for Firewall Manager policies through the Firewall Manager interface. If you use AWS WAF to update or delete the logging configuration of a web ACL that's managed by Firewall Manager, Firewall Manager won't detect the change automatically. If you have used AWS WAF, you can manually prompt an update to the Firewall Manager AWS WAF policy by re-evaluating the policy's rule in AWS Config. To do this, in the AWS Config console, locate the AWS Config rule for the Firewall Manager policy and select the re-evaluate action. 