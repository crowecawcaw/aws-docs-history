**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Disassociating a health check from your

resource protected by Shield Advanced

The following procedure shows how to disassociate an Amazon Route 53 health check from a
protected resource.

###### To disassociate a health check

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").
2. In the AWS Shield navigation pane, choose **Protected
   resources**.
3. On the **Protections** tab, select the resource that you want to
   disassociate from a health check.
4. Choose **Configure protections**.
5. Choose **Next** until you get to the page
   **Configure health check based DDoS detection - _optional_**.
6. Under **Associated Health Check**, choose the empty option, listed as
   **-**.
7. Walk through the rest of the pages until you finish the configuration.
   On the **Protections** page, the health check field for your resource is
   set to **-**, indicating no health check association.
