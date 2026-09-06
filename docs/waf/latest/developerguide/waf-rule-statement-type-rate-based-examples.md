

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Rate-based rule examples in AWS WAF
<a name="waf-rule-statement-type-rate-based-examples"></a>

This section describes example configurations for a variety of common rate-based rules use cases. 

Each example provides a description of the use case and then shows the solution in JSON listings for the custom configured rules. 

**Note**  
The JSON listings shown in these examples were created in the console by configuring the rule and then editing it using the **Rule JSON editor**. 

**Topics**
+ [Rate limit the requests to a login page](waf-rate-based-example-limit-login-page.md)
+ [Rate limit the requests to a login page from any IP address, user agent pair](waf-rate-based-example-limit-login-page-keys.md)
+ [Rate limit the requests that are missing a specific header](waf-rate-based-example-limit-missing-header.md)
+ [Rate limit the requests with specific labels](waf-rate-based-example-limit-labels.md)
+ [Rate limit the requests for labels that have a specified label namespace](waf-rate-based-example-limit-label-aggregation.md)
+ [Rate limit the requests with specific ASNs](waf-rate-based-example-limit-asn.md)