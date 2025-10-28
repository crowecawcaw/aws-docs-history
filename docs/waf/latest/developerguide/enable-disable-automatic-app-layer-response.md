**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Enabling and disabling

automatic application layer DDoS mitigation

The following procedure shows how to enable or disable automatic response for a protected
resource.

###### To enable or disable automatic application layer DDoS mitigation for a single resource

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").
2. In the AWS Shield navigation pane, choose **Protected resources**.
3. In the **Protections** tab, select the application layer resource that
   you want to enable automatic mitigation for. The protections page opens
   for the resource.
4. In the resource's protections page, choose
   **Edit**.
5. In the page **Configure layer 7 DDoS mitigation for global resources - _optional_**, for
   **Automatic application layer DDoS mitigation**, choose the
   option that you want to use for automatic mitigations. The options in
   the console are the following:
   - **Keep current settings** – Make no changes to the automatic
     mitigation settings of the protected resource.
   - **Enable** – Enable automatic mitigation for the protected
     resource. When you choose this, also select the rule action that
     you want the automatic mitigations to use in the web ACL rules.
     For information about rule action settings, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

   If your protected resource doesn’t yet have a history of normal application traffic,
   enable automatic mitigation in Count mode until Shield Advanced can establish a baseline.
   Shield Advanced begins to collect
   information for its baseline when you associate a web ACL with your protected resource,
   and it can take 24 hour to 30 days to establish a good baseline of normal traffic.
   - **Disable** – Disable automatic mitigation for the protected
     resource.

6. Walk through the rest of the pages until you finish and save the configuration.
   In the **Protections** page, the automatic mitigation settings are updated
   for the resource.
