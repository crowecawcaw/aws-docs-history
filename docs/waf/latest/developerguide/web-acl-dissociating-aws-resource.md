**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Disassociating a

protection from an AWS resource

Using the new console

1. Choose the protection pack (web ACL) that you want to edit. The
   console makes the main protection pack (web ACL) card editable, and also
   opens a side panel with details you can edit.
2. In the protection pack (web ACL) card, choose the
   **Edit** link next to
   **Resources** to open the **Manage
   resources** panel.
3. In the **Manage resources** section for the
   rule group, choose the resource you want to disassociate, and
   then choose **Disassociate**.

###### Note

You must disassociate one resource at a time. Do not
choose multiple resources. 4. In the confirmation page, type "disassociate", and then choose
**Disassociate**.

Using the standard console
To dissociate a web ACL from an AWS resource, perform the following procedure.

###### To disassociate a

web ACL from an AWS resource

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **web ACLs**.
3. Choose the name of the web ACL that you want to disassociate from your resource. The console takes you to the web
   ACL's description, where you can edit it.
4. On the **Associated AWS resources** tab,
   select
   the resource that you want to disassociate this web ACL from.

###### Note

You must disassociate one resource at a time. Do not choose multiple resources.

###### Note

When you choose to associate an Application Load Balancer with your webACL, **Resource-level DDoS protection** is enabled. For more information,
see [AWS WAF Distributed Denial of Service (DDoS) prevention](waf-anti-ddos.md "waf-anti-ddos.md"). 5. Choose **Disassociate**.
The console opens a confirmation dialogue. Confirm your choice to
disassociate the web ACL from the AWS resource.
