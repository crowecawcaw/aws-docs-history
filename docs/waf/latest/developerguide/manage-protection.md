**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Editing AWS Shield Advanced protections

You can change the settings for your AWS Shield Advanced protections at any time. To do this, walk
through the options for your selected protections and modify the settings that you need to
change.

###### To manage protected resources

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").
2. In the AWS Shield navigation pane, choose **Protected resources**.
3. In the **Protections** tab, select the resources that you want to protect.
4. Choose **Configure protections** and the resource specification option
   that you want.
5. Walk through each of the resource protection options, making changes as needed.

## Configure application layer DDoS protections

For protection against attacks on Amazon CloudFront and Application Load Balancer resources, you can add AWS WAF web
ACLs and add rate-based rules. For information about this, see [Protecting the application layer with AWS WAF web ACLs and Shield Advanced](ddos-app-layer-web-ACL-and-rbr.md "ddos-app-layer-web-ACL-and-rbr.md").

You can also enable the Shield Advanced automatic application layer DDoS mitigation. For
information about how AWS WAF works, see [AWS WAF](waf-chapter.md "waf-chapter.md"). For information about the
automatic mitigation feature, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

###### Important

If you manage your Shield Advanced protections through AWS Firewall Manager using a Shield Advanced policy,
you can't manage the application layer protections here. For all other resources, we
recommend that, at a minimum, you attach a web ACL to each resource, even if web ACL
doesn't contain any rules.

###### Note

When you enable automatic application layer DDoS mitigation for a resource, if needed, the operation
automatically adds a service-linked role to your account to give Shield Advanced the
permissions it needs to manage your web ACL protections. For information, see
[Using service-linked roles for
Shield Advanced](shd-using-service-linked-roles.md "shd-using-service-linked-roles.md").

###### To configure application layer DDoS protections

1. In the **Configure layer 7 DDoS protections** page, if the
   resource isn't already associated with a web ACL, you can choose an existing web
   ACL or create your own.

To create a web ACL, follow these steps:

    1. Choose **Create web ACL**.
    2. Enter a name. You can't change the name after you create the web
     ACL.
    3. Choose **Create**.###### Note

If a resource is already associated with a web ACL, you can't change to a
different web ACL. If you want to change the web ACL, you must first remove
the associated web ACLs from the resource. For more information, see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md"). 2. If the web ACL doesn't have a rate-based rule defined, you can add one by choosing
**Add rate limit rule** and then performing the following
steps:

    1. Enter a name.
    2. Enter a rate limit. This is the maximum number of requests allowed in any five minute
     period from any single IP address before the rate-based rule action is applied to the IP address. When the
     requests from the IP address fall below the limit, the action is discontinued.
    3. Set the rule action to count or block requests from IP addresses while their
     request counts are over the limit. The application
     and removal of the rule action might take effect a minute or two after the IP address request rate
     changes.
    4. Choose **Add rule**.

3.  For **Automatic application layer DDoS mitigation**, choose whether you
    want Shield Advanced to automatically mitigate DDoS attacks on your behalf, as follows:

        * To enable automatic mitigation, choose **Enable** and then
         select the AWS WAF rule action that you want Shield Advanced to use in its
         custom rules. Your choices are Count and Block. For
         information about these AWS WAF rule actions, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md"). For information about how
         Shield Advanced manages this action setting, see [How Shield Advanced manages the rule
         action setting](ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-rule-action "ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-rule-action").
        * To disable automatic mitigation, choose **Disable**.
        * To leave the automatic mitigation settings unchanged for the resources that
         you're managing, leave the default choice **Keep current settings**.

    For information about Shield Advanced automatic application layer DDoS mitigation, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

4.  Choose **Next**.
