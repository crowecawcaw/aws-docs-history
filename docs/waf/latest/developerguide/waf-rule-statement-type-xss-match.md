**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Cross-site scripting attack

rule statement

This section explains what an XSS (cross-site scripting) attack statement is and how it works.

An XSS attack statement inspects for malicious scripts in a web request component.
In an XSS attack, the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious
client-site scripts into other legitimate web browsers.

## Rule statement characteristics

**Nestable** – You can nest this statement
type.

**WCUs** – 40 WCUs, as a base cost.
If you use the request component **All query parameters**, add 10 WCUs.
If you use the request component **JSON body**, double the base cost WCUs. For each **Text transformation** that you apply, add 10 WCUs.

This statement type operates on a web request component, and requires the following request component settings:

- **Request component** – The part of the web request
  to inspect, for example, a query string or the body.

###### Warning

If you inspect the request components **Body**, **JSON body**, **Headers**, or **Cookies**, read about the limitations on how much content AWS WAF can inspect at
[Oversize web request components
in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

For information about web request components, see [Adjusting rule statement settings in AWS WAF](waf-rule-statement-fields.md "waf-rule-statement-fields.md").

- **Optional text transformations** –
  Transformations that you want AWS WAF to perform on the request component before
  inspecting it. For example, you could transform to lowercase or normalize
  white space. If you specify more than one transformation, AWS WAF processes them
  in the order listed. For information, see [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").

## Where to find this rule statement

- **Rule builder** on the console –
  For **Match type**, choose **Attack match
  condition** > **Contains XSS injection
  attacks**.
- **API** –
  [XssMatchStatement](../APIReference/API_XssMatchStatement.md "../APIReference/API_XssMatchStatement.md")
